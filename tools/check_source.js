const fs = require("fs");
const path = require("path");

const sourceRoot = path.resolve(__dirname, "../../anniversary-game");
const requiredPaths = [
  path.join(sourceRoot, "src/data/story.json"),
  path.join(sourceRoot, "Assets for Game"),
  path.join(sourceRoot, "Anniversary - Wedding"),
];

const missing = requiredPaths.filter((target) => !fs.existsSync(target));

if (missing.length > 0) {
  console.error("Missing required upstream files/folders:");
  for (const target of missing) console.error(`- ${target}`);
  process.exit(1);
}

console.log("Source check passed.");
for (const target of requiredPaths) console.log(`- ${target}`);
