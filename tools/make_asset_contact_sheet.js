const fs = require("fs");
const path = require("path");
const { PNG } = require("pngjs");

const inputDir = process.argv[2];
const outputFile = process.argv[3];

if (!inputDir || !outputFile) {
  console.error("Usage: node tools/make_asset_contact_sheet.js <input-dir> <output.png>");
  process.exit(1);
}

const files = fs.readdirSync(inputDir)
  .filter((file) => file.toLowerCase().endsWith(".png"))
  .sort();

if (!files.length) {
  console.error(`No PNG files found in ${inputDir}`);
  process.exit(1);
}

const columns = Math.min(4, files.length);
const cellWidth = 430;
const cellHeight = 520;
const gap = 22;
const rows = Math.ceil(files.length / columns);
const width = columns * cellWidth + (columns + 1) * gap;
const height = rows * cellHeight + (rows + 1) * gap;
const sheet = new PNG({ width, height });

for (let i = 0; i < sheet.data.length; i += 4) {
  sheet.data[i] = 18;
  sheet.data[i + 1] = 16;
  sheet.data[i + 2] = 20;
  sheet.data[i + 3] = 255;
}

function fillRect(image, x, y, w, h, rgba) {
  for (let yy = Math.max(0, y); yy < Math.min(image.height, y + h); yy += 1) {
    for (let xx = Math.max(0, x); xx < Math.min(image.width, x + w); xx += 1) {
      const i = (yy * image.width + xx) * 4;
      image.data[i] = rgba[0];
      image.data[i + 1] = rgba[1];
      image.data[i + 2] = rgba[2];
      image.data[i + 3] = rgba[3];
    }
  }
}

function checker(image, x, y, w, h) {
  const size = 24;
  for (let yy = y; yy < y + h; yy += size) {
    for (let xx = x; xx < x + w; xx += size) {
      const light = ((Math.floor((xx - x) / size) + Math.floor((yy - y) / size)) % 2) === 0;
      fillRect(image, xx, yy, size, size, light ? [42, 38, 44, 255] : [31, 28, 34, 255]);
    }
  }
}

function blitContain(source, target, x, y, w, h) {
  const scale = Math.min(w / source.width, h / source.height);
  const drawW = Math.max(1, Math.round(source.width * scale));
  const drawH = Math.max(1, Math.round(source.height * scale));
  const ox = x + Math.floor((w - drawW) / 2);
  const oy = y + Math.floor((h - drawH) / 2);

  for (let ty = 0; ty < drawH; ty += 1) {
    const sy = Math.min(source.height - 1, Math.floor((ty / drawH) * source.height));
    for (let tx = 0; tx < drawW; tx += 1) {
      const sx = Math.min(source.width - 1, Math.floor((tx / drawW) * source.width));
      const s = (sy * source.width + sx) * 4;
      const d = ((oy + ty) * target.width + (ox + tx)) * 4;
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
  const x = gap + column * (cellWidth + gap);
  const y = gap + row * (cellHeight + gap);
  checker(sheet, x, y, cellWidth, cellHeight);
  blitContain(source, sheet, x + 12, y + 12, cellWidth - 24, cellHeight - 24);
});

fs.mkdirSync(path.dirname(outputFile), { recursive: true });
fs.writeFileSync(outputFile, PNG.sync.write(sheet));
console.log(`Wrote ${outputFile} (${files.length} images)`);
