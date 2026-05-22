const fs = require("fs");
const path = require("path");
const { PNG } = require("pngjs");

const inputDir = process.argv[2];
const outputFile = process.argv[3];

if (!inputDir || !outputFile) {
  console.error("Usage: node tools/make_contact_sheet.js <input-dir> <output.png>");
  process.exit(1);
}

const files = fs.readdirSync(inputDir)
  .filter((file) => {
    const lower = file.toLowerCase();
    return lower.endsWith(".png") && !lower.endsWith(".new.png") && !lower.endsWith(".diff.png");
  })
  .sort();

if (!files.length) {
  console.error(`No PNG files found in ${inputDir}`);
  process.exit(1);
}

const columns = 4;
const thumbWidth = 420;
const thumbHeight = 236;
const gap = 18;
const rows = Math.ceil(files.length / columns);
const width = columns * thumbWidth + (columns + 1) * gap;
const height = rows * thumbHeight + (rows + 1) * gap;
const sheet = new PNG({ width, height });

for (let i = 0; i < sheet.data.length; i += 4) {
  sheet.data[i] = 18;
  sheet.data[i + 1] = 16;
  sheet.data[i + 2] = 20;
  sheet.data[i + 3] = 255;
}

function blitScaled(source, target, x, y) {
  for (let ty = 0; ty < thumbHeight; ty += 1) {
    const sy = Math.min(source.height - 1, Math.floor((ty / thumbHeight) * source.height));
    for (let tx = 0; tx < thumbWidth; tx += 1) {
      const sx = Math.min(source.width - 1, Math.floor((tx / thumbWidth) * source.width));
      const s = (sy * source.width + sx) * 4;
      const d = ((y + ty) * target.width + (x + tx)) * 4;
      const alpha = source.data[s + 3] / 255;

      target.data[d] = Math.round(source.data[s] * alpha + target.data[d] * (1 - alpha));
      target.data[d + 1] = Math.round(source.data[s + 1] * alpha + target.data[d + 1] * (1 - alpha));
      target.data[d + 2] = Math.round(source.data[s + 2] * alpha + target.data[d + 2] * (1 - alpha));
      target.data[d + 3] = 255;
    }
  }
}

files.forEach((file, index) => {
  const source = PNG.sync.read(fs.readFileSync(path.join(inputDir, file)));
  const row = Math.floor(index / columns);
  const column = index % columns;
  const x = gap + column * (thumbWidth + gap);
  const y = gap + row * (thumbHeight + gap);
  blitScaled(source, sheet, x, y);
});

fs.mkdirSync(path.dirname(outputFile), { recursive: true });
fs.writeFileSync(outputFile, PNG.sync.write(sheet));
console.log(`Wrote ${outputFile} (${files.length} images)`);
