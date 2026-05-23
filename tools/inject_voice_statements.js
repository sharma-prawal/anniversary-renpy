const fs = require("fs");
const path = require("path");

const {
  ROOT,
  SCRIPT_PATH,
  extractVoiceLines,
  filesystemAudioPath,
  loadVoiceConfig,
  manifestPath,
  readJson,
  stripGeneratedVoiceStatements,
} = require("./voice_manifest_common");

function parseArgs(argv) {
  const args = {
    dryRun: false,
    ifManifest: false,
    skipMissingAssets: false,
  };

  for (const arg of argv) {
    if (arg === "--dry-run") args.dryRun = true;
    else if (arg === "--if-manifest") args.ifManifest = true;
    else if (arg === "--skip-missing-assets") args.skipMissingAssets = true;
    else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return args;
}

function relative(file) {
  return path.relative(ROOT, file);
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const config = loadVoiceConfig();
  const manifestFile = manifestPath(config);

  if (!fs.existsSync(manifestFile)) {
    if (args.ifManifest) {
      console.log(`No voice manifest found at ${relative(manifestFile)}; skipping voice injection.`);
      return;
    }
    throw new Error(`Missing voice manifest: ${relative(manifestFile)}. Run npm run generate:voice-manifest or npm run generate:voice first.`);
  }

  const manifest = readJson(manifestFile);
  const missingAssets = manifest.lines.filter((line) => {
    const file = filesystemAudioPath(line.audioPath);
    return !fs.existsSync(file) || fs.statSync(file).size <= 0;
  });
  if (missingAssets.length && !args.dryRun) {
    const message = `Voice manifest references ${missingAssets.length} missing asset(s). Run npm run generate:voice before injecting.`;
    if (args.ifManifest || args.skipMissingAssets) {
      console.log(`${message} Skipping voice injection.`);
      return;
    }
    throw new Error(message);
  }

  const manifestBySourceKey = new Map(manifest.lines.map((line) => [line.sourceKey, line]));
  const original = fs.readFileSync(SCRIPT_PATH, "utf8");
  const cleanScriptText = stripGeneratedVoiceStatements(original);
  const current = extractVoiceLines(cleanScriptText, config, manifest);
  const currentByLineNumber = new Map();
  const missingManifestLines = [];

  for (const line of current.lines) {
    const manifestLine = manifestBySourceKey.get(line.sourceKey);
    if (!manifestLine || manifestLine.textHash !== line.textHash || manifestLine.speakerCode !== line.speakerCode) {
      missingManifestLines.push(line);
      continue;
    }
    currentByLineNumber.set(line.lineNumber, manifestLine);
  }

  if (missingManifestLines.length) {
    throw new Error(`Voice manifest is stale for ${missingManifestLines.length} script line(s). Run npm run generate:voice-manifest or npm run generate:voice.`);
  }

  const output = [];
  const sourceLines = cleanScriptText.split(/\r?\n/);
  for (let i = 0; i < sourceLines.length; i++) {
    const lineNumber = i + 1;
    const voiceLine = currentByLineNumber.get(lineNumber);
    if (voiceLine) {
      const indent = sourceLines[i].match(/^(\s*)/)[1];
      output.push(`${indent}voice "${voiceLine.audioPath}" # auto-generated voice`);
    }
    output.push(sourceLines[i]);
    if (voiceLine) {
      const indent = sourceLines[i].match(/^(\s*)/)[1];
      output.push(`${indent}voice sustain # auto-generated voice sustain`);
      output.push(`${indent}$ voice_line_pause() # auto-generated voice pause`);
    }
  }

  const updated = output.join("\n");
  if (args.dryRun) {
    if (missingAssets.length) {
      console.log(`Voice manifest references ${missingAssets.length} missing asset(s); dry-run is checking script coverage only.`);
    }
    console.log(`Would inject ${currentByLineNumber.size} voice statement(s) into ${relative(SCRIPT_PATH)}.`);
    return;
  }

  if (updated === original) {
    console.log(`${relative(SCRIPT_PATH)} already has current generated voice statements.`);
    return;
  }

  fs.writeFileSync(SCRIPT_PATH, updated);
  console.log(`Injected ${currentByLineNumber.size} voice statement(s) into ${relative(SCRIPT_PATH)}.`);
}

try {
  main();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
