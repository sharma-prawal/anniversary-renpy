const fs = require("fs");
const path = require("path");
const { PNG } = require("pngjs");

const [, , inputFile, outputFile, character] = process.argv;

if (!inputFile || !outputFile || !character) {
  console.error("Usage: node tools/normalize_ai_sprites.js <input.png> <output.png> <prawal|aashna|aashna_formal|friend>");
  process.exit(1);
}

const TARGETS = {
  prawal: { canvasWidth: 563, canvasHeight: 1536, boxWidth: 445, boxHeight: 1428, centerX: 281, bottomY: 1506 },
  aashna: { canvasWidth: 402, canvasHeight: 1536, boxWidth: 360, boxHeight: 1358, centerX: 201, bottomY: 1484 },
  aashna_formal: { canvasWidth: 700, canvasHeight: 1536, boxWidth: 660, boxHeight: 1358, centerX: 350, bottomY: 1484 },
  friend: { canvasWidth: 520, canvasHeight: 1536, boxWidth: 420, boxHeight: 1420, centerX: 260, bottomY: 1502 },
};

const target = TARGETS[character];
if (!target) {
  console.error(`Unknown character: ${character}`);
  process.exit(1);
}

const source = PNG.sync.read(fs.readFileSync(inputFile));

function getBounds(image) {
  let minX = image.width;
  let minY = image.height;
  let maxX = -1;
  let maxY = -1;

  for (let y = 0; y < image.height; y += 1) {
    for (let x = 0; x < image.width; x += 1) {
      if (image.data[(y * image.width + x) * 4 + 3] > 8) {
        if (x < minX) minX = x;
        if (y < minY) minY = y;
        if (x > maxX) maxX = x;
        if (y > maxY) maxY = y;
      }
    }
  }

  if (maxX < minX || maxY < minY) throw new Error("Input image has no visible pixels.");
  return { x: minX, y: minY, width: maxX - minX + 1, height: maxY - minY + 1 };
}

function sampleBilinear(image, x, y) {
  const x0 = Math.max(0, Math.min(image.width - 1, Math.floor(x)));
  const y0 = Math.max(0, Math.min(image.height - 1, Math.floor(y)));
  const x1 = Math.max(0, Math.min(image.width - 1, x0 + 1));
  const y1 = Math.max(0, Math.min(image.height - 1, y0 + 1));
  const tx = x - x0;
  const ty = y - y0;
  const out = [0, 0, 0, 0];
  const weights = [
    (1 - tx) * (1 - ty),
    tx * (1 - ty),
    (1 - tx) * ty,
    tx * ty,
  ];
  const points = [
    (y0 * image.width + x0) * 4,
    (y0 * image.width + x1) * 4,
    (y1 * image.width + x0) * 4,
    (y1 * image.width + x1) * 4,
  ];

  let alpha = 0;
  for (let p = 0; p < points.length; p += 1) {
    alpha += image.data[points[p] + 3] * weights[p];
  }

  out[3] = Math.round(alpha);
  if (alpha <= 0) return out;

  for (let c = 0; c < 3; c += 1) {
    let premultiplied = 0;
    for (let p = 0; p < points.length; p += 1) {
      premultiplied += image.data[points[p] + c] * image.data[points[p] + 3] * weights[p];
    }
    out[c] = Math.round(premultiplied / alpha);
  }

  return out;
}

function blend(canvas, index, pixel) {
  const a = pixel[3] / 255;
  if (a <= 0) return;
  canvas.data[index] = pixel[0];
  canvas.data[index + 1] = pixel[1];
  canvas.data[index + 2] = pixel[2];
  canvas.data[index + 3] = pixel[3];
}

const bounds = getBounds(source);
const scale = Math.min(target.boxWidth / bounds.width, target.boxHeight / bounds.height);
const drawW = Math.max(1, Math.round(bounds.width * scale));
const drawH = Math.max(1, Math.round(bounds.height * scale));
const left = Math.round(target.centerX - drawW / 2);
const top = Math.round(target.bottomY - drawH);
const canvas = new PNG({ width: target.canvasWidth, height: target.canvasHeight });

for (let y = 0; y < drawH; y += 1) {
  for (let x = 0; x < drawW; x += 1) {
    const sx = bounds.x + (x + 0.5) / scale;
    const sy = bounds.y + (y + 0.5) / scale;
    const dx = left + x;
    const dy = top + y;
    if (dx < 0 || dx >= target.canvasWidth || dy < 0 || dy >= target.canvasHeight) continue;
    blend(canvas, (dy * target.canvasWidth + dx) * 4, sampleBilinear(source, sx, sy));
  }
}

fs.mkdirSync(path.dirname(outputFile), { recursive: true });
fs.writeFileSync(outputFile, PNG.sync.write(canvas));
console.log(`${path.basename(outputFile)}: ${bounds.width}x${bounds.height} -> ${drawW}x${drawH}`);
