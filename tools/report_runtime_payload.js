const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const GAME = path.join(ROOT, "game");

const referenced = new Set();
for (const file of ["definitions.rpy", "audio.rpy"]) {
  const full = path.join(GAME, file);
  const text = fs.readFileSync(full, "utf8");
  const re = /(?:image\s+[^=]+|define\s+audio\.[^=]+)\s*=\s*"([^"]+)"/gm;
  let match;
  while ((match = re.exec(text))) {
    referenced.add(match[1]);
  }

  const quotedRuntimeAssetRe = /"((?:photos)\/[^"]+)"/gm;
  while ((match = quotedRuntimeAssetRe.exec(text))) {
    referenced.add(match[1]);
  }
}

const categories = {
  backgrounds: /^backgrounds_(?:ai|web)\//,
  cgs: /^images_(?:ai|web)\/cg\//,
  sprites: /^sprites_ai\//,
  propsAndUi: /^(images_ai\/props\/|images\/)/,
  photos: /^photos\//,
  audio: /^audio\//,
};

const totals = Object.fromEntries(Object.keys(categories).map((key) => [key, 0]));
const missing = [];

for (const rel of referenced) {
  const full = path.join(GAME, rel);
  if (!fs.existsSync(full)) {
    missing.push(rel);
    continue;
  }

  const size = fs.statSync(full).size;
  const key = Object.entries(categories).find(([, re]) => re.test(rel))?.[0];
  if (key) totals[key] += size;
}

function format(bytes) {
  return `${(bytes / 1024 / 1024).toFixed(1)}M`;
}

let total = 0;
for (const [key, value] of Object.entries(totals)) {
  total += value;
  console.log(`${key}: ${format(value)}`);
}
console.log(`referenced total: ${format(total)}`);
console.log(`missing referenced files: ${missing.length}`);
for (const rel of missing) console.log(`- ${rel}`);
process.exit(missing.length ? 1 : 0);
