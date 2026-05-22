const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");
const { PNG } = require("pngjs");

const ROOT = path.resolve(__dirname, "..");
const QUALITY = "88";
const MAX_DIMENSION = "2048";

const groups = [
  {
    sourceDir: path.join(ROOT, "game", "backgrounds_ai"),
    outputDir: path.join(ROOT, "game", "backgrounds_web"),
  },
  {
    sourceDir: path.join(ROOT, "game", "images_ai", "cg"),
    outputDir: path.join(ROOT, "game", "images_web", "cg"),
  },
];

function walkPngs(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      out.push(...walkPngs(full));
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith(".png")) {
      out.push(full);
    }
  }
  return out.sort();
}

function isOpaquePng(file) {
  const png = PNG.sync.read(fs.readFileSync(file));
  for (let index = 3; index < png.data.length; index += 4) {
    if (png.data[index] !== 255) {
      return false;
    }
  }
  return true;
}

function sizeOf(file) {
  return fs.statSync(file).size;
}

function formatBytes(bytes) {
  if (bytes >= 1024 * 1024) {
    return `${(bytes / 1024 / 1024).toFixed(1)}M`;
  }
  if (bytes >= 1024) {
    return `${Math.round(bytes / 1024)}K`;
  }
  return `${bytes}B`;
}

let converted = 0;
let skipped = 0;
let before = 0;
let after = 0;

for (const group of groups) {
  if (!fs.existsSync(group.sourceDir)) continue;
  fs.mkdirSync(group.outputDir, { recursive: true });

  for (const source of walkPngs(group.sourceDir)) {
    const relative = path.relative(group.sourceDir, source);
    const output = path.join(group.outputDir, relative).replace(/\.png$/i, ".jpg");
    fs.mkdirSync(path.dirname(output), { recursive: true });

    if (!isOpaquePng(source)) {
      skipped += 1;
      continue;
    }

    execFileSync("sips", [
      "-Z",
      MAX_DIMENSION,
      "-s",
      "format",
      "jpeg",
      "-s",
      "formatOptions",
      QUALITY,
      source,
      "--out",
      output,
    ], { stdio: "ignore" });

    converted += 1;
    before += sizeOf(source);
    after += sizeOf(output);
  }
}

console.log(`Converted ${converted} opaque PNG assets to web JPEG.`);
console.log(`Skipped ${skipped} transparent PNG assets.`);
console.log(`Converted source size: ${formatBytes(before)} -> ${formatBytes(after)}.`);
console.log(`Estimated converted asset reduction: ${formatBytes(before - after)}.`);
