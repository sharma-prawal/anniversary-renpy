const fs = require("fs");
const path = require("path");
const { PNG } = require("pngjs");

const root = path.resolve(__dirname, "..");
const dir = path.join(root, "game", "backgrounds_ai");
const targetWidth = 2752;
const targetHeight = 1536;

function sampleBilinear(src, x, y) {
  const x0 = Math.max(0, Math.min(src.width - 1, Math.floor(x)));
  const y0 = Math.max(0, Math.min(src.height - 1, Math.floor(y)));
  const x1 = Math.max(0, Math.min(src.width - 1, x0 + 1));
  const y1 = Math.max(0, Math.min(src.height - 1, y0 + 1));
  const tx = x - x0;
  const ty = y - y0;
  const out = [0, 0, 0, 0];

  for (let c = 0; c < 4; c += 1) {
    const i00 = (src.width * y0 + x0) * 4 + c;
    const i10 = (src.width * y0 + x1) * 4 + c;
    const i01 = (src.width * y1 + x0) * 4 + c;
    const i11 = (src.width * y1 + x1) * 4 + c;
    const top = src.data[i00] * (1 - tx) + src.data[i10] * tx;
    const bottom = src.data[i01] * (1 - tx) + src.data[i11] * tx;
    out[c] = Math.round(top * (1 - ty) + bottom * ty);
  }

  return out;
}

function normalize(file) {
  const full = path.join(dir, file);
  const src = PNG.sync.read(fs.readFileSync(full));

  if (src.width === targetWidth && src.height === targetHeight) {
    return false;
  }

  const srcRatio = src.width / src.height;
  const targetRatio = targetWidth / targetHeight;
  let cropX = 0;
  let cropY = 0;
  let cropWidth = src.width;
  let cropHeight = src.height;

  if (srcRatio > targetRatio) {
    cropWidth = Math.round(src.height * targetRatio);
    cropX = Math.floor((src.width - cropWidth) / 2);
  } else {
    cropHeight = Math.round(src.width / targetRatio);
    cropY = Math.floor((src.height - cropHeight) / 2);
  }

  const out = new PNG({ width: targetWidth, height: targetHeight });
  for (let y = 0; y < targetHeight; y += 1) {
    const sy = cropY + (y / Math.max(1, targetHeight - 1)) * Math.max(1, cropHeight - 1);
    for (let x = 0; x < targetWidth; x += 1) {
      const sx = cropX + (x / Math.max(1, targetWidth - 1)) * Math.max(1, cropWidth - 1);
      const rgba = sampleBilinear(src, sx, sy);
      const i = (targetWidth * y + x) * 4;
      out.data[i] = rgba[0];
      out.data[i + 1] = rgba[1];
      out.data[i + 2] = rgba[2];
      out.data[i + 3] = rgba[3];
    }
  }

  fs.writeFileSync(full, PNG.sync.write(out, { colorType: 6, inputColorType: 6 }));
  console.log(`${file}: ${src.width}x${src.height} -> ${targetWidth}x${targetHeight}`);
  return true;
}

const files = fs.readdirSync(dir).filter((file) => file.toLowerCase().endsWith(".png")).sort();
let changed = 0;
for (const file of files) {
  if (normalize(file)) changed += 1;
}

console.log(`normalized ${changed}/${files.length} staged background(s)`);
