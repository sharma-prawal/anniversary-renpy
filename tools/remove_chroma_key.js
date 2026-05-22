const fs = require("fs");
const path = require("path");
const { PNG } = require("pngjs");

const [, , inputFile, outputFile] = process.argv;

if (!inputFile || !outputFile) {
  console.error("Usage: node tools/remove_chroma_key.js <input.png> <output.png>");
  process.exit(1);
}

const image = PNG.sync.read(fs.readFileSync(inputFile));

function pixelAt(x, y) {
  const i = (y * image.width + x) * 4;
  return [image.data[i], image.data[i + 1], image.data[i + 2]];
}

function median(values) {
  const sorted = values.slice().sort((a, b) => a - b);
  return sorted[Math.floor(sorted.length / 2)];
}

function sampleBorderKey() {
  const samples = [];
  const step = Math.max(1, Math.floor(Math.min(image.width, image.height) / 80));

  for (let x = 0; x < image.width; x += step) {
    samples.push(pixelAt(x, 0), pixelAt(x, image.height - 1));
  }
  for (let y = 0; y < image.height; y += step) {
    samples.push(pixelAt(0, y), pixelAt(image.width - 1, y));
  }

  return [
    median(samples.map((sample) => sample[0])),
    median(samples.map((sample) => sample[1])),
    median(samples.map((sample) => sample[2])),
  ];
}

function distance(r, g, b, key) {
  const dr = r - key[0];
  const dg = g - key[1];
  const db = b - key[2];
  return Math.sqrt(dr * dr + dg * dg + db * db);
}

const key = sampleBorderKey();
const transparentDistance = 58;
const opaqueDistance = 125;
const output = new PNG({ width: image.width, height: image.height });

for (let y = 0; y < image.height; y += 1) {
  for (let x = 0; x < image.width; x += 1) {
    const i = (y * image.width + x) * 4;
    let r = image.data[i];
    let g = image.data[i + 1];
    let b = image.data[i + 2];
    const sourceAlpha = image.data[i + 3] || 255;
    const d = distance(r, g, b, key);
    let alpha;

    if (d <= transparentDistance) {
      alpha = 0;
    } else if (d >= opaqueDistance) {
      alpha = sourceAlpha;
    } else {
      const t = (d - transparentDistance) / (opaqueDistance - transparentDistance);
      alpha = Math.round(sourceAlpha * t * t * (3 - 2 * t));
    }

    if (alpha > 0 && key[1] > key[0] + 80 && key[1] > key[2] + 80) {
      const neutralMax = Math.max(r, b);
      const spill = Math.max(0, g - neutralMax - 8);
      g = Math.max(0, g - Math.round(spill * 1.4));
      if (alpha < 245 && g > neutralMax + 12) {
        g = neutralMax + 12;
      }
    }

    output.data[i] = r;
    output.data[i + 1] = g;
    output.data[i + 2] = b;
    output.data[i + 3] = alpha;
  }
}

fs.mkdirSync(path.dirname(outputFile), { recursive: true });
fs.writeFileSync(outputFile, PNG.sync.write(output));
console.log(`Removed key rgb(${key.join(", ")}) -> ${outputFile}`);
