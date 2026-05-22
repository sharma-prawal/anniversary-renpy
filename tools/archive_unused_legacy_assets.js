const crypto = require("crypto");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const ARCHIVE_ROOT = path.join(ROOT, "archive", "unused_legacy_assets", "2026-05-19");

const candidates = [
  { path: "game/backgrounds", category: "legacy_backgrounds" },
  { path: "game/sprites", category: "legacy_sprites" },
  { path: "game/images/props", category: "legacy_procedural_props" },
  { path: "game/images/ui/nameplate.png", category: "unused_ui" },
  { path: "game/images/ui/ui_chat_bubbles.png", category: "unused_ui" },
  { path: "game/images/ui/watermark_mask.png", category: "unused_ui" },
  { path: "game/images_ai/_cutouts", category: "ai_prop_workfiles" },
  { path: "game/images_ai/_sources", category: "ai_prop_workfiles" },
  { path: "game/sprites_ai/prawal/_cutouts", category: "ai_sprite_workfiles" },
  { path: "game/sprites_ai/prawal/_sources", category: "ai_sprite_workfiles" },
  { path: "game/sprites_ai/aashna/_cutouts", category: "ai_sprite_workfiles" },
  { path: "game/sprites_ai/aashna/_sources", category: "ai_sprite_workfiles" },
];

function walkFiles(target) {
  if (!fs.existsSync(target)) return [];
  const stat = fs.statSync(target);
  if (stat.isFile()) return [target];
  if (!stat.isDirectory()) return [];

  const out = [];
  for (const entry of fs.readdirSync(target)) {
    out.push(...walkFiles(path.join(target, entry)));
  }
  return out;
}

function readRuntimeText() {
  const files = [
    ...walkFiles(path.join(ROOT, "game")).filter((file) => /\.(rpy|json)$/i.test(file)),
  ];
  return files.map((file) => fs.readFileSync(file, "utf8")).join("\n");
}

function sha256(file) {
  return crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function pruneEmptyDirs(dir, stopAt) {
  let current = dir;
  while (current.startsWith(stopAt) && current !== stopAt) {
    if (!fs.existsSync(current)) {
      current = path.dirname(current);
      continue;
    }
    if (fs.readdirSync(current).length > 0) return;
    fs.rmdirSync(current);
    current = path.dirname(current);
  }
}

function archiveFile(file, category, runtimeText) {
  const rel = path.relative(ROOT, file).replace(/\\/g, "/");
  if (runtimeText.includes(rel) || runtimeText.includes(rel.replace(/^game\//, ""))) {
    return { original: rel, category, skipped: true, reason: "runtime_reference" };
  }

  const destination = path.join(ARCHIVE_ROOT, rel);
  ensureDir(path.dirname(destination));

  const entry = {
    original: rel,
    archived: path.relative(ROOT, destination).replace(/\\/g, "/"),
    category,
    bytes: fs.statSync(file).size,
    sha256: sha256(file),
  };

  fs.renameSync(file, destination);
  pruneEmptyDirs(path.dirname(file), path.join(ROOT, "game"));
  return entry;
}

function main() {
  ensureDir(ARCHIVE_ROOT);
  const manifestPath = path.join(ARCHIVE_ROOT, "manifest.json");
  const runtimeText = readRuntimeText();
  const manifest = fs.existsSync(manifestPath)
    ? JSON.parse(fs.readFileSync(manifestPath, "utf8"))
    : {
        created_at: new Date().toISOString(),
        archive_root: path.relative(ROOT, ARCHIVE_ROOT).replace(/\\/g, "/"),
        entries: [],
        skipped: [],
      };
  manifest.updated_at = new Date().toISOString();

  for (const candidate of candidates) {
    const absolute = path.join(ROOT, candidate.path);
    for (const file of walkFiles(absolute)) {
      const result = archiveFile(file, candidate.category, runtimeText);
      if (result.skipped) manifest.skipped.push(result);
      else manifest.entries.push(result);
    }
  }

  fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);
  console.log(`Archived ${manifest.entries.length} unused legacy asset(s).`);
  console.log(`Skipped ${manifest.skipped.length} referenced asset(s).`);
  console.log(`Manifest: ${path.relative(ROOT, path.join(ARCHIVE_ROOT, "manifest.json"))}`);
}

main();
