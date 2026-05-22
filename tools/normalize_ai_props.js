const fs = require("fs");
const path = require("path");
const { PNG } = require("pngjs");

const inputDir = process.argv[2] || "game/images_ai/_cutouts";
const outputDir = process.argv[3] || "game/images_ai/props";

const CANVAS_WIDTH = 1920;
const CANVAS_HEIGHT = 1080;

const TARGET_BOUNDS = {
  prop_book: { width: 760, height: 530, centerX: 960, centerY: 500 },
  prop_earphones: { width: 560, height: 370, centerX: 960, centerY: 500 },
  prop_framed_photos: { width: 780, height: 450, centerX: 960, centerY: 490 },
  prop_letters: { width: 700, height: 540, centerX: 960, centerY: 500 },
  prop_mug: { width: 560, height: 440, centerX: 960, centerY: 500 },
  prop_rings: { width: 560, height: 420, centerX: 960, centerY: 500 },
};

function getBounds(image) {
  let minX = image.width;
  let minY = image.height;
  let maxX = -1;
  let maxY = -1;

  for (let y = 0; y < image.height; y += 1) {
    for (let x = 0; x < image.width; x += 1) {
      const alpha = image.data[(y * image.width + x) * 4 + 3];
      if (alpha > 8) {
        if (x < minX) minX = x;
        if (y < minY) minY = y;
        if (x > maxX) maxX = x;
        if (y > maxY) maxY = y;
      }
    }
  }

  if (maxX < minX || maxY < minY) {
    throw new Error("Input image has no visible pixels.");
  }

  return {
    x: minX,
    y: minY,
    width: maxX - minX + 1,
    height: maxY - minY + 1,
  };
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

function alphaCompositePixel(target, index, source) {
  const srcAlpha = source[3] / 255;
  if (srcAlpha <= 0) return;

  const dstAlpha = target.data[index + 3] / 255;
  const outAlpha = srcAlpha + dstAlpha * (1 - srcAlpha);
  if (outAlpha <= 0) return;

  for (let c = 0; c < 3; c += 1) {
    const src = source[c] / 255;
    const dst = target.data[index + c] / 255;
    const out = (src * srcAlpha + dst * dstAlpha * (1 - srcAlpha)) / outAlpha;
    target.data[index + c] = Math.round(out * 255);
  }
  target.data[index + 3] = Math.round(outAlpha * 255);
}

function normalizeFile(file) {
  const key = path.basename(file, ".png");
  const target = TARGET_BOUNDS[key];
  if (!target) {
    console.warn(`Skipping ${file}: no target bounds configured.`);
    return;
  }

  const source = PNG.sync.read(fs.readFileSync(path.join(inputDir, file)));
  const bounds = getBounds(source);
  const scale = Math.min(target.width / bounds.width, target.height / bounds.height);
  const drawW = Math.max(1, Math.round(bounds.width * scale));
  const drawH = Math.max(1, Math.round(bounds.height * scale));
  const left = Math.round(target.centerX - drawW / 2);
  const top = Math.round(target.centerY - drawH / 2);
  const canvas = new PNG({ width: CANVAS_WIDTH, height: CANVAS_HEIGHT });

  for (let y = 0; y < drawH; y += 1) {
    for (let x = 0; x < drawW; x += 1) {
      const sx = bounds.x + (x + 0.5) / scale;
      const sy = bounds.y + (y + 0.5) / scale;
      const dx = left + x;
      const dy = top + y;
      if (dx < 0 || dx >= CANVAS_WIDTH || dy < 0 || dy >= CANVAS_HEIGHT) continue;
      alphaCompositePixel(canvas, (dy * CANVAS_WIDTH + dx) * 4, sampleBilinear(source, sx, sy));
    }
  }

  fs.mkdirSync(outputDir, { recursive: true });
  fs.writeFileSync(path.join(outputDir, file), PNG.sync.write(canvas));
  console.log(`${file}: ${bounds.width}x${bounds.height} -> ${drawW}x${drawH}`);
}

const files = fs.readdirSync(inputDir)
  .filter((file) => file.toLowerCase().endsWith(".png"))
  .sort();

if (!files.length) {
  console.error(`No PNG files found in ${inputDir}`);
  process.exit(1);
}

files.forEach(normalizeFile);
