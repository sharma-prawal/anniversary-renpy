const fs = require("fs");
const path = require("path");

const [, , outputPath] = process.argv;

if (!outputPath) {
  console.error("Usage: node tools/copy_latest_generated_image.js <output-path>");
  process.exit(1);
}

const root = path.resolve(__dirname, "..");
const generatedDir = path.join(
  process.env.HOME,
  ".codex",
  "generated_images",
  "019e2aac-8a45-7492-9309-9554188ed7b4"
);
const dest = path.resolve(root, outputPath);

const files = fs.readdirSync(generatedDir)
  .filter((file) => file.toLowerCase().endsWith(".png"))
  .map((file) => {
    const full = path.join(generatedDir, file);
    return { full, mtime: fs.statSync(full).mtimeMs };
  })
  .sort((a, b) => b.mtime - a.mtime);

if (!files.length) {
  console.error(`No generated PNG files found in ${generatedDir}`);
  process.exit(1);
}

fs.mkdirSync(path.dirname(dest), { recursive: true });
fs.copyFileSync(files[0].full, dest);
console.log(`${files[0].full} -> ${path.relative(root, dest)}`);
