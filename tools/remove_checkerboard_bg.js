const fs = require("fs");
const path = require("path");
const { PNG } = require("pngjs");

const ROOT = path.resolve(__dirname, "..");
const SPRITES_DIR = path.join(ROOT, "game", "sprites");
const SOURCE_ASSET_ROOT = path.resolve(ROOT, "..", "anniversary-game", "Assets for Game", "sprites");

const SPRITE_SHEETS = [
  {
    sheet: path.join(SOURCE_ASSET_ROOT, "prawal", "sprite_prawal.png"),
    outputDir: path.join(SPRITES_DIR, "prawal"),
    names: ["happy", "neutral", "surprised", "thinking", "loving"],
  },
  {
    sheet: path.join(SOURCE_ASSET_ROOT, "aashna", "sprite_aashna.png"),
    outputDir: path.join(SPRITES_DIR, "aashna"),
    names: ["happy", "shy", "neutral", "laughing", "surprised", "emotional", "loving"],
  },
];

function isGrayChecker(r, g, b, a) {
  if (a === 0) return false;
  const maxDelta = Math.max(Math.abs(r - g), Math.abs(g - b), Math.abs(r - b));
  if (maxDelta > 14) return false;
  const v = (r + g + b) / 3;
  return v >= 145;
}

function restoreSpritesFromSheets() {
  for (const config of SPRITE_SHEETS) {
    if (!fs.existsSync(config.sheet)) continue;
    fs.mkdirSync(config.outputDir, { recursive: true });

    const sheet = PNG.sync.read(fs.readFileSync(config.sheet));
    const count = config.names.length;

    for (let index = 0; index < count; index++) {
      const startX = Math.round((sheet.width * index) / count);
      const endX = Math.round((sheet.width * (index + 1)) / count);
      const width = endX - startX;
      const out = new PNG({ width, height: sheet.height });

      for (let y = 0; y < sheet.height; y++) {
        for (let x = 0; x < width; x++) {
          const src = (y * sheet.width + startX + x) * 4;
          const dst = (y * width + x) * 4;
          out.data[dst] = sheet.data[src];
          out.data[dst + 1] = sheet.data[src + 1];
          out.data[dst + 2] = sheet.data[src + 2];
          out.data[dst + 3] = sheet.data[src + 3];
        }
      }

      const target = path.join(config.outputDir, `${config.names[index]}.png`);
      fs.writeFileSync(target, PNG.sync.write(out, { colorType: 6, inputColorType: 6 }));
    }
  }
}

function floodEraseChecker(png) {
  const { width, height, data } = png;
  const seen = new Uint8Array(width * height);
  const qx = new Int32Array(width * height);
  const qy = new Int32Array(width * height);
  let head = 0;
  let tail = 0;

  function enqueue(x, y) {
    const idx = y * width + x;
    if (seen[idx]) return;
    seen[idx] = 1;
    qx[tail] = x;
    qy[tail] = y;
    tail++;
  }

  function pixelIsChecker(x, y) {
    const i = (y * width + x) * 4;
    return isGrayChecker(data[i], data[i + 1], data[i + 2], data[i + 3]);
  }

  // Seed flood-fill from image borders only.
  for (let x = 0; x < width; x++) {
    if (pixelIsChecker(x, 0)) enqueue(x, 0);
    if (pixelIsChecker(x, height - 1)) enqueue(x, height - 1);
  }
  for (let y = 0; y < height; y++) {
    if (pixelIsChecker(0, y)) enqueue(0, y);
    if (pixelIsChecker(width - 1, y)) enqueue(width - 1, y);
  }

  let removed = 0;
  while (head < tail) {
    const x = qx[head];
    const y = qy[head];
    head++;

    const i = (y * width + x) * 4;
    if (!pixelIsChecker(x, y)) continue;
    data[i + 3] = 0;
    removed++;

    if (x > 0) enqueue(x - 1, y);
    if (x + 1 < width) enqueue(x + 1, y);
    if (y > 0) enqueue(x, y - 1);
    if (y + 1 < height) enqueue(x, y + 1);
  }

  return removed;
}

function keepLargestOpaqueComponent(png) {
  const { width, height, data } = png;
  const total = width * height;
  const seen = new Uint8Array(total);
  const comp = new Int32Array(total);
  const qx = new Int32Array(total);
  const qy = new Int32Array(total);

  let largestSize = 0;
  let largestId = -1;
  let nextId = 1;

  function alphaAt(x, y) {
    return data[(y * width + x) * 4 + 3];
  }

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const idx = y * width + x;
      if (seen[idx] || alphaAt(x, y) === 0) continue;

      let head = 0;
      let tail = 0;
      qx[tail] = x;
      qy[tail] = y;
      tail++;
      seen[idx] = 1;
      comp[idx] = nextId;
      let size = 0;

      while (head < tail) {
        const cx = qx[head];
        const cy = qy[head];
        head++;
        size++;

        const n = [
          [cx - 1, cy],
          [cx + 1, cy],
          [cx, cy - 1],
          [cx, cy + 1],
        ];
        for (const [nx, ny] of n) {
          if (nx < 0 || ny < 0 || nx >= width || ny >= height) continue;
          const nidx = ny * width + nx;
          if (seen[nidx] || alphaAt(nx, ny) === 0) continue;
          seen[nidx] = 1;
          comp[nidx] = nextId;
          qx[tail] = nx;
          qy[tail] = ny;
          tail++;
        }
      }

      if (size > largestSize) {
        largestSize = size;
        largestId = nextId;
      }
      nextId++;
    }
  }

  if (largestId < 0) return 0;

  let removed = 0;
  for (let i = 0; i < total; i++) {
    const alphaIndex = i * 4 + 3;
    if (data[alphaIndex] === 0) continue;
    if (comp[i] !== largestId) {
      data[alphaIndex] = 0;
      removed++;
    }
  }

  return removed;
}

function eraseLightCheckerComponents(png) {
  const { width, height, data } = png;
  const total = width * height;
  const seen = new Uint8Array(total);
  const qx = new Int32Array(total);
  const qy = new Int32Array(total);
  let removed = 0;

  function alphaAt(x, y) {
    return data[(y * width + x) * 4 + 3];
  }

  function pixelIsLightChecker(x, y) {
    const i = (y * width + x) * 4;
    const a = data[i + 3];
    if (a === 0) return false;
    const r = data[i];
    const g = data[i + 1];
    const b = data[i + 2];
    const maxDelta = Math.max(Math.abs(r - g), Math.abs(g - b), Math.abs(r - b));
    const v = (r + g + b) / 3;
    return maxDelta <= 14 && v >= 145;
  }

  function hasTransparentNeighbor(x, y) {
    for (const [nx, ny] of [
      [x - 1, y],
      [x + 1, y],
      [x, y - 1],
      [x, y + 1],
    ]) {
      if (nx < 0 || ny < 0 || nx >= width || ny >= height) return true;
      if (alphaAt(nx, ny) === 0) return true;
    }
    return false;
  }

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const idx = y * width + x;
      if (seen[idx] || !pixelIsLightChecker(x, y)) continue;

      let head = 0;
      let tail = 0;
      let size = 0;
      let minX = x;
      let maxX = x;
      let minY = y;
      let maxY = y;
      let touchesTransparent = false;
      qx[tail] = x;
      qy[tail] = y;
      tail++;
      seen[idx] = 1;

      while (head < tail) {
        const cx = qx[head];
        const cy = qy[head];
        head++;
        size++;
        minX = Math.min(minX, cx);
        maxX = Math.max(maxX, cx);
        minY = Math.min(minY, cy);
        maxY = Math.max(maxY, cy);
        if (hasTransparentNeighbor(cx, cy)) touchesTransparent = true;

        for (const [nx, ny] of [
          [cx - 1, cy],
          [cx + 1, cy],
          [cx, cy - 1],
          [cx, cy + 1],
        ]) {
          if (nx < 0 || ny < 0 || nx >= width || ny >= height) continue;
          const nidx = ny * width + nx;
          if (seen[nidx] || !pixelIsLightChecker(nx, ny)) continue;
          seen[nidx] = 1;
          qx[tail] = nx;
          qy[tail] = ny;
          tail++;
        }
      }

      const componentWidth = maxX - minX + 1;
      const componentHeight = maxY - minY + 1;
      const isEnclosedTallGap =
        !touchesTransparent && size >= 600 && componentHeight >= 80 && componentWidth <= 120;

      if (isEnclosedTallGap) {
        for (let i = 0; i < tail; i++) {
          const px = qx[i];
          const py = qy[i];
          const alphaIndex = (py * width + px) * 4 + 3;
          if (data[alphaIndex] !== 0) {
            data[alphaIndex] = 0;
            removed++;
          }
        }
      }
    }
  }

  return removed;
}

function processFile(file) {
  const buf = fs.readFileSync(file);
  const png = PNG.sync.read(buf);
  const removedBorder = floodEraseChecker(png);
  const removedLightComponents = eraseLightCheckerComponents(png);
  const removedIslands = keepLargestOpaqueComponent(png);
  fs.writeFileSync(file, PNG.sync.write(png, { colorType: 6, inputColorType: 6 }));
  return { removedBorder, removedLightComponents, removedIslands };
}

function walkPngs(dir, out = []) {
  const items = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of items) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) {
      walkPngs(full, out);
    } else if (item.isFile() && full.toLowerCase().endsWith(".png")) {
      out.push(full);
    }
  }
  return out;
}

function main() {
  restoreSpritesFromSheets();

  const files = walkPngs(SPRITES_DIR);
  let totalRemovedBorder = 0;
  let totalRemovedLightComponents = 0;
  let totalRemovedIslands = 0;
  for (const file of files) {
    const { removedBorder, removedLightComponents, removedIslands } = processFile(file);
    totalRemovedBorder += removedBorder;
    totalRemovedLightComponents += removedLightComponents;
    totalRemovedIslands += removedIslands;
    console.log(
      `${path.relative(
        ROOT,
        file
      )}: removed border=${removedBorder} light=${removedLightComponents} islands=${removedIslands}`
    );
  }
  console.log(
    `Done. Removed border=${totalRemovedBorder} light=${totalRemovedLightComponents} islands=${totalRemovedIslands} checkerboard pixels.`
  );
}

main();
