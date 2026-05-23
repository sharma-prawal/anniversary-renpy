const crypto = require("crypto");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const GAME = path.join(ROOT, "game");
const SCRIPT_PATH = path.join(GAME, "script.rpy");
const CONFIG_PATH = path.join(__dirname, "voice_config.json");
const GENERATED_VOICE_RE = /^\s*voice\s+"audio\/voice\/[^"]+"\s*# auto-generated voice\s*$/;
const GENERATED_VOICE_HELPER_RE = /^\s*(?:voice sustain|\$\s*voice_line_pause\(\))\s*# auto-generated voice (?:sustain|pause)\s*$/;
const SAY_RE = /^(\s*)(p|a|n)\s+"((?:\\.|[^"\\])*)"\s*$/;
const LABEL_RE = /^label\s+([A-Za-z_][A-Za-z0-9_]*)\s*:/;

function readJson(file, fallback = null) {
  if (!fs.existsSync(file)) return fallback;
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

function writeJsonIfChanged(file, value) {
  const text = `${JSON.stringify(value, null, 2)}\n`;
  const current = fs.existsSync(file) ? fs.readFileSync(file, "utf8") : null;
  if (current === text) return false;
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, text);
  return true;
}

function loadVoiceConfig() {
  const config = readJson(CONFIG_PATH);
  if (!config || !config.outputRoot || !config.format || !config.speakers) {
    throw new Error(`Invalid voice config: ${path.relative(ROOT, CONFIG_PATH)}`);
  }
  return config;
}

function manifestPath(config) {
  return path.join(ROOT, config.outputRoot, "manifest.json");
}

function stripGeneratedVoiceStatements(scriptText) {
  return scriptText
    .split(/\r?\n/)
    .filter((line) => !GENERATED_VOICE_RE.test(line) && !GENERATED_VOICE_HELPER_RE.test(line))
    .join("\n");
}

function parseRenpyString(raw) {
  try {
    return JSON.parse(`"${raw}"`);
  } catch (error) {
    return raw.replace(/\\"/g, "\"").replace(/\\\\/g, "\\");
  }
}

function hashText(text) {
  return crypto.createHash("sha1").update(text).digest("hex").slice(0, 10);
}

function stableNumber(seed) {
  return parseInt(crypto.createHash("sha1").update(seed).digest("hex").slice(0, 8), 16);
}

function percentValue(value) {
  const match = String(value || "+0%").match(/^([+-]?\d+)%$/);
  return match ? Number(match[1]) : 0;
}

function hertzValue(value) {
  const match = String(value || "+0Hz").match(/^([+-]?\d+)Hz$/);
  return match ? Number(match[1]) : 0;
}

function formatPercent(value) {
  const rounded = Math.max(-50, Math.min(50, Math.round(value)));
  return `${rounded >= 0 ? "+" : ""}${rounded}%`;
}

function formatHertz(value) {
  const rounded = Math.max(-80, Math.min(80, Math.round(value)));
  return `${rounded >= 0 ? "+" : ""}${rounded}Hz`;
}

function speechTextForTts(text) {
  return text
    .replace(/✓\s*/g, "")
    .replace(/&/g, " and ")
    .replace(/[“”]/g, "\"")
    .replace(/[‘’]/g, "'")
    .replace(/—/g, ", ")
    .replace(/–/g, ", ")
    .replace(/…/g, ", ")
    .replace(/\.\.\./g, ", ")
    .replace(/\s+/g, " ")
    .replace(/\s+([,.!?])/g, "$1")
    .trim();
}

function deliveryForLine(speakerConfig, text, sourceKey) {
  const seed = stableNumber(sourceKey);
  const rateVariation = (seed % 5) - 2;
  const pitchVariation = ((Math.floor(seed / 7) % 5) - 2) * 2;
  let rate = percentValue(speakerConfig.rate) + rateVariation;
  let pitch = hertzValue(speakerConfig.pitch) + pitchVariation;

  if (/[?!]$/.test(text.trim())) rate += 1;
  if (/^(I love|I still|Because|Forever|Aashna|Prawal)/i.test(text.trim())) rate -= 1;
  if (text.length > 85) rate -= 2;
  if (text.length < 18) rate -= 1;

  return {
    rate: formatPercent(rate),
    pitch: formatHertz(pitch),
  };
}

function slug(value) {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9_]+/g, "_")
    .replace(/^_+|_+$/g, "")
    .slice(0, 80);
}

function runtimeAudioPath(config, role, id) {
  const outputRoot = config.outputRoot.replace(/\\/g, "/").replace(/^game\//, "");
  return path.posix.join(outputRoot, role, `${id}.${config.format}`);
}

function filesystemAudioPath(audioPath) {
  return path.join(GAME, audioPath);
}

function previousLineBySourceKey(existingManifest) {
  const map = new Map();
  for (const line of existingManifest && Array.isArray(existingManifest.lines) ? existingManifest.lines : []) {
    if (line.sourceKey) map.set(line.sourceKey, line);
  }
  return map;
}

function extractVoiceLines(scriptText, config, existingManifest = null) {
  const cleanScriptText = stripGeneratedVoiceStatements(scriptText);
  const previous = previousLineBySourceKey(existingManifest);
  const lines = [];
  const occurrenceByKey = new Map();
  const usedIds = new Set();
  let label = "start";
  let labelSayIndex = 0;

  const sourceLines = cleanScriptText.split(/\r?\n/);
  for (let i = 0; i < sourceLines.length; i++) {
    const sourceLine = sourceLines[i];
    const labelMatch = sourceLine.match(LABEL_RE);
    if (labelMatch) {
      label = labelMatch[1];
      labelSayIndex = 0;
      occurrenceByKey.clear();
      continue;
    }

    const sayMatch = sourceLine.match(SAY_RE);
    if (!sayMatch) continue;

    const speakerCode = sayMatch[2];
    const speakerConfig = config.speakers[speakerCode];
    if (!speakerConfig) continue;

    labelSayIndex += 1;
    const text = parseRenpyString(sayMatch[3]);
    const textHash = hashText(text);
    const occurrenceBase = `${label}\0${speakerCode}\0${text}`;
    const occurrence = (occurrenceByKey.get(occurrenceBase) || 0) + 1;
    occurrenceByKey.set(occurrenceBase, occurrence);
    const sourceKey = `${occurrenceBase}\0${occurrence}`;
    const previousLine = previous.get(sourceKey);
    const canReusePrevious =
      previousLine &&
      previousLine.textHash === textHash &&
      previousLine.speakerCode === speakerCode &&
      previousLine.label === label &&
      previousLine.audioPath;
    let id = canReusePrevious ? previousLine.id : `${slug(label)}_${String(labelSayIndex).padStart(3, "0")}_${speakerConfig.role}_${textHash}`;

    while (usedIds.has(id)) {
      id = `${id}_dup`;
    }
    usedIds.add(id);

    const audioPath = runtimeAudioPath(config, speakerConfig.role, id);
    const delivery = deliveryForLine(speakerConfig, text, sourceKey);
    lines.push({
      id,
      label,
      lineNumber: i + 1,
      speakerCode,
      speaker: speakerConfig.name,
      role: speakerConfig.role,
      voice: speakerConfig.voice,
      rate: delivery.rate,
      pitch: delivery.pitch,
      volume: speakerConfig.volume || "+0%",
      text,
      speechText: speechTextForTts(text),
      textHash,
      sourceKey,
      audioPath,
    });
  }

  return { cleanScriptText, lines };
}

function buildManifest(scriptText, config, existingManifest = null) {
  const { lines } = extractVoiceLines(scriptText, config, existingManifest);
  return {
    schemaVersion: 1,
    source: "game/script.rpy",
    config: "tools/voice_config.json",
    lineCount: lines.length,
    lines,
  };
}

function staleVoiceFiles(config, manifest) {
  const outputRoot = path.join(ROOT, config.outputRoot);
  if (!fs.existsSync(outputRoot)) return [];
  const expected = new Set(manifest.lines.map((line) => filesystemAudioPath(line.audioPath)));
  const staleExtensions = new Set([config.format, config.sourceFormat, "mp3", "ogg"].filter(Boolean).map((ext) => `.${ext}`));
  const stale = [];

  function walk(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(full);
      } else if (entry.isFile() && staleExtensions.has(path.extname(entry.name)) && !expected.has(full)) {
        stale.push(full);
      }
    }
  }

  walk(outputRoot);
  return stale;
}

module.exports = {
  ROOT,
  GAME,
  SCRIPT_PATH,
  CONFIG_PATH,
  SAY_RE,
  buildManifest,
  extractVoiceLines,
  filesystemAudioPath,
  loadVoiceConfig,
  manifestPath,
  readJson,
  staleVoiceFiles,
  stripGeneratedVoiceStatements,
  writeJsonIfChanged,
};
