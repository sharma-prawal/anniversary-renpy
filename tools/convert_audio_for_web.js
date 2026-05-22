const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const GAME = path.join(ROOT, "game");
const AUDIO = path.join(GAME, "audio");
const AUDIO_RPY = path.join(GAME, "audio.rpy");

function walk(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...walk(full));
    } else if (entry.isFile()) {
      files.push(full);
    }
  }

  return files;
}

function hasFfmpeg() {
  const result = spawnSync("ffmpeg", ["-version"], { stdio: "ignore" });
  return result.status === 0;
}

if (!hasFfmpeg()) {
  console.error("ffmpeg is required. Install it with Homebrew: brew install ffmpeg");
  process.exit(1);
}

const wavFiles = walk(AUDIO).filter((file) => file.endsWith(".wav"));
let converted = 0;

for (const wav of wavFiles) {
  const mp3 = wav.replace(/\.wav$/, ".mp3");
  const wavStat = fs.statSync(wav);
  const needsConversion = !fs.existsSync(mp3) || fs.statSync(mp3).mtimeMs < wavStat.mtimeMs;

  if (!needsConversion) continue;

  const result = spawnSync(
    "ffmpeg",
    [
      "-y",
      "-hide_banner",
      "-loglevel",
      "error",
      "-i",
      wav,
      "-codec:a",
      "libmp3lame",
      "-b:a",
      "96k",
      "-ar",
      "44100",
      "-ac",
      "1",
      mp3,
    ],
    { stdio: "inherit" },
  );

  if (result.status !== 0) {
    console.error(`Failed to convert ${path.relative(ROOT, wav)}`);
    process.exit(result.status || 1);
  }

  converted += 1;
}

const audioText = fs.readFileSync(AUDIO_RPY, "utf8");
const updatedAudioText = audioText.replace(/(audio\/[^"]+)\.wav/g, "$1.mp3");
if (updatedAudioText !== audioText) {
  fs.writeFileSync(AUDIO_RPY, updatedAudioText);
}

console.log(`Converted ${converted} audio files to MP3.`);
console.log(`Updated ${path.relative(ROOT, AUDIO_RPY)} to reference MP3 runtime audio.`);
