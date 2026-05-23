const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const {
  ROOT,
  CONFIG_PATH,
  SCRIPT_PATH,
  buildManifest,
  filesystemAudioPath,
  loadVoiceConfig,
  manifestPath,
  readJson,
  staleVoiceFiles,
  writeJsonIfChanged,
} = require("./voice_manifest_common");

function parseArgs(argv) {
  const args = {
    cleanStale: false,
    dryRun: false,
    force: false,
    listVoices: false,
    manifestOnly: false,
    chapter: null,
    limit: null,
    locale: null,
  };

  for (const arg of argv) {
    if (arg === "--clean-stale") args.cleanStale = true;
    else if (arg === "--dry-run") args.dryRun = true;
    else if (arg === "--force") args.force = true;
    else if (arg === "--list-voices") args.listVoices = true;
    else if (arg === "--manifest-only") args.manifestOnly = true;
    else if (arg.startsWith("--chapter=")) args.chapter = arg.slice("--chapter=".length);
    else if (arg.startsWith("--limit=")) args.limit = Number(arg.slice("--limit=".length));
    else if (arg.startsWith("--locale=")) args.locale = arg.slice("--locale=".length);
    else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (args.limit !== null && (!Number.isInteger(args.limit) || args.limit < 1)) {
    throw new Error("--limit must be a positive integer.");
  }

  return args;
}

function printable(file) {
  return path.relative(ROOT, file);
}

function hasGeneratedAudio(line) {
  const file = filesystemAudioPath(line.audioPath);
  return fs.existsSync(file) && fs.statSync(file).size > 0;
}

function sourceAudioPathForLine(line, config) {
  if (!config.sourceFormat || config.sourceFormat === config.format) return null;
  const sourcePath = line.audioPath.replace(new RegExp(`\\.${config.format}$`), `.${config.sourceFormat}`);
  return filesystemAudioPath(sourcePath);
}

function edgeTtsInstallMessage() {
  return [
    "Edge TTS CLI is unavailable.",
    "Install it outside the shipped game with `python3 -m pip install edge-tts` or `pipx install edge-tts`.",
    "You can also set EDGE_TTS_BIN to an edge-tts-compatible executable.",
  ].join(" ");
}

function resolveEdgeTtsCommand() {
  const helper = path.join(__dirname, "edge_tts_ssml.py");
  for (const python of ["python3", "python"]) {
    const result = spawnSync(python, [helper, "--help"], { stdio: "ignore" });
    if (result.status === 0) return { command: python, prefix: [helper] };
  }
  throw new Error(edgeTtsInstallMessage());
}

function runEdgeTts(commandInfo, args, options = {}) {
  const result = spawnSync(commandInfo.command, [...commandInfo.prefix, ...args], {
    encoding: options.encoding || "utf8",
    stdio: options.stdio || "inherit",
  });
  if (result.error) {
    throw new Error(`${edgeTtsInstallMessage()} (${result.error.message})`);
  }
  if (result.status !== 0) {
    throw new Error(`Edge TTS failed with exit code ${result.status}.`);
  }
  return result;
}

function runFfmpeg(args, description) {
  const result = spawnSync(
    "ffmpeg",
    ["-y", "-hide_banner", "-loglevel", "error", ...args],
    { stdio: "inherit" },
  );
  if (result.error) {
    throw new Error(`ffmpeg is required for voice audio processing. (${result.error.message})`);
  }
  if (result.status !== 0) {
    throw new Error(`ffmpeg failed while ${description} with exit code ${result.status}.`);
  }
}

function generateSilentAudio(outFile, duration = 0.55) {
  const ext = path.extname(outFile).toLowerCase();
  const codecArgs = ext === ".ogg" ? ["-ac", "2", "-codec:a", "vorbis", "-q:a", "4", "-strict", "-2"] : ["-codec:a", "libmp3lame", "-b:a", "48k"];
  runFfmpeg(
    [
      "-f",
      "lavfi",
      "-i",
      "anullsrc=r=24000:cl=mono",
      "-t",
      String(duration),
      ...codecArgs,
      outFile,
    ],
    "generating silent punctuation-only voice audio",
  );
}

function postProcessVoiceAudio(sourceFile, outFile, config) {
  const postProcess = config.postProcess || {};
  if (!postProcess.enabled || path.extname(outFile).toLowerCase() === ".mp3") {
    if (sourceFile !== outFile) fs.copyFileSync(sourceFile, outFile);
    return;
  }

  const filters = Array.isArray(postProcess.filters) ? postProcess.filters.join(",") : "aresample=44100";
  const codec = postProcess.codec || "libvorbis";
  const quality = postProcess.quality || "5";
  const strictArgs = codec === "vorbis" ? ["-strict", "-2"] : [];
  runFfmpeg(
    [
      "-i",
      sourceFile,
      "-af",
      filters,
      "-ac",
      "2",
      "-codec:a",
      codec,
      "-q:a",
      quality,
      ...strictArgs,
      outFile,
    ],
    "warming and converting voice audio",
  );
}

function synthesizeLine(commandInfo, line, outFile, config) {
  const speechText = line.speechText || line.text;
  if (!/[A-Za-z0-9]/.test(speechText)) {
    generateSilentAudio(outFile);
    return;
  }

  const reusableSource = sourceAudioPathForLine(line, config);
  if (reusableSource && fs.existsSync(reusableSource) && fs.statSync(reusableSource).size > 0) {
    postProcessVoiceAudio(reusableSource, outFile, config);
    return;
  }

  const tempSource = path.extname(outFile).toLowerCase() === ".mp3" ? outFile : `${outFile}.tmp.${config.sourceFormat || "mp3"}`;
  const args = [
    `--voice=${line.voice}`,
    `--text=${speechText}`,
    `--write-media=${tempSource}`,
  ];
  if (line.rate) args.push(`--rate=${line.rate}`);
  if (line.pitch) args.push(`--pitch=${line.pitch}`);
  if (line.volume) args.push(`--volume=${line.volume}`);
  runEdgeTts(commandInfo, args);
  if (tempSource !== outFile) {
    postProcessVoiceAudio(tempSource, outFile, config);
    fs.unlinkSync(tempSource);
  }
}

function listVoices(commandInfo, locale) {
  if (!locale) {
    runEdgeTts(commandInfo, ["--list-voices"]);
    return;
  }
  const result = runEdgeTts(commandInfo, ["--list-voices"], { encoding: "utf8", stdio: "pipe" });
  const output = `${result.stdout || ""}${result.stderr || ""}`;
  for (const line of output.split(/\r?\n/)) {
    if (line.includes(locale)) console.log(line);
  }
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const config = loadVoiceConfig();
  const manifestFile = manifestPath(config);

  if (args.listVoices) {
    listVoices(resolveEdgeTtsCommand(), args.locale);
    return;
  }

  const existingManifest = readJson(manifestFile, null);
  const scriptText = fs.readFileSync(SCRIPT_PATH, "utf8");
  const manifest = buildManifest(scriptText, config, existingManifest);
  const configStat = fs.statSync(CONFIG_PATH);
  const staleFiles = staleVoiceFiles(config, manifest);
  const missingLines = manifest.lines.filter((line) => !hasGeneratedAudio(line));
  let targetLines = manifest.lines.filter((line) => {
    if (args.force || !hasGeneratedAudio(line)) return true;
    return fs.statSync(filesystemAudioPath(line.audioPath)).mtimeMs < configStat.mtimeMs;
  });

  if (args.chapter) {
    targetLines = targetLines.filter((line) => line.label === args.chapter);
  }
  if (args.limit !== null) {
    targetLines = targetLines.slice(0, args.limit);
  }

  if (args.dryRun) {
    console.log(`Voice manifest would contain ${manifest.lineCount} line(s).`);
    console.log(`Missing voice asset(s): ${missingLines.length}`);
    console.log(`Target generation line(s): ${targetLines.length}`);
    console.log(`Stale voice asset(s): ${staleFiles.length}`);
    return;
  }

  const manifestChanged = writeJsonIfChanged(manifestFile, manifest);
  console.log(`${manifestChanged ? "Updated" : "Manifest already current"}: ${printable(manifestFile)}`);
  console.log(`Voice manifest contains ${manifest.lineCount} line(s).`);

  if (args.manifestOnly) {
    return;
  }

  if (targetLines.length) {
    const commandInfo = resolveEdgeTtsCommand();
    let generated = 0;
    for (const line of targetLines) {
      const outFile = filesystemAudioPath(line.audioPath);
      fs.mkdirSync(path.dirname(outFile), { recursive: true });
      console.log(`Generating ${line.id} (${line.speaker})`);
      synthesizeLine(commandInfo, line, outFile, config);
      generated += 1;
    }
    console.log(`Generated ${generated} voice asset(s).`);
  } else {
    console.log("No voice assets need generation.");
  }

  if (args.cleanStale) {
    for (const file of staleFiles) {
      fs.unlinkSync(file);
      console.log(`Deleted stale voice asset: ${printable(file)}`);
    }
    console.log(`Deleted ${staleFiles.length} stale voice asset(s).`);
  } else if (staleFiles.length) {
    console.log(`Stale voice asset(s) detected: ${staleFiles.length}. Re-run with --clean-stale to delete them.`);
  }
}

try {
  main();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
