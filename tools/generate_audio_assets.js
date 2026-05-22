const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "game", "audio");
const SAMPLE_RATE = 44100;

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function clamp(v) {
  return Math.max(-1, Math.min(1, v));
}

function midiToHz(midi) {
  return 440 * Math.pow(2, (midi - 69) / 12);
}

function envelope(t, duration, attack = 0.025, release = 0.18) {
  if (t < attack) return t / attack;
  if (duration - t < release) return Math.max(0, (duration - t) / release);
  return 1;
}

function writeWav(file, samples) {
  const bytesPerSample = 2;
  const blockAlign = bytesPerSample;
  const byteRate = SAMPLE_RATE * blockAlign;
  const dataSize = samples.length * bytesPerSample;
  const buffer = Buffer.alloc(44 + dataSize);

  buffer.write("RIFF", 0);
  buffer.writeUInt32LE(36 + dataSize, 4);
  buffer.write("WAVE", 8);
  buffer.write("fmt ", 12);
  buffer.writeUInt32LE(16, 16);
  buffer.writeUInt16LE(1, 20);
  buffer.writeUInt16LE(1, 22);
  buffer.writeUInt32LE(SAMPLE_RATE, 24);
  buffer.writeUInt32LE(byteRate, 28);
  buffer.writeUInt16LE(blockAlign, 32);
  buffer.writeUInt16LE(16, 34);
  buffer.write("data", 36);
  buffer.writeUInt32LE(dataSize, 40);

  for (let i = 0; i < samples.length; i++) {
    buffer.writeInt16LE(Math.round(clamp(samples[i]) * 32767), 44 + i * 2);
  }

  ensureDir(path.dirname(file));
  fs.writeFileSync(file, buffer);
}

function synthMusic({ file, duration, progression, melody = [], pad = 0.18, bell = 0.08, bass = 0.08 }) {
  const total = Math.floor(duration * SAMPLE_RATE);
  const samples = new Float32Array(total);
  const chordDuration = duration / progression.length;

  for (let i = 0; i < total; i++) {
    const t = i / SAMPLE_RATE;
    const chordIndex = Math.floor(t / chordDuration) % progression.length;
    const chord = progression[chordIndex];
    const local = t - chordIndex * chordDuration;
    const chordEnv = envelope(local, chordDuration, 0.6, 0.8);
    let value = 0;

    for (const note of chord) {
      const hz = midiToHz(note);
      value += Math.sin(2 * Math.PI * hz * t) * pad * chordEnv;
      value += Math.sin(2 * Math.PI * hz * 2 * t) * pad * 0.16 * chordEnv;
    }

    value += Math.sin(2 * Math.PI * midiToHz(chord[0] - 12) * t) * bass * chordEnv;

    if (melody.length) {
      const stepDuration = chordDuration / 4;
      const stepIndex = Math.floor(t / stepDuration) % melody.length;
      const note = melody[stepIndex];
      if (note) {
        const stepLocal = t - Math.floor(t / stepDuration) * stepDuration;
        const e = envelope(stepLocal, stepDuration, 0.01, 0.22);
        const hz = midiToHz(note);
        value += Math.sin(2 * Math.PI * hz * t) * bell * e;
        value += Math.sin(2 * Math.PI * hz * 2.01 * t) * bell * 0.22 * e;
      }
    }

    samples[i] = value / Math.max(1.6, chord.length);
  }

  writeWav(path.join(OUT, "music", file), samples);
}

function synthTone({ file, duration, notes, volume = 0.24, noise = 0 }) {
  const total = Math.floor(duration * SAMPLE_RATE);
  const samples = new Float32Array(total);

  for (let i = 0; i < total; i++) {
    const t = i / SAMPLE_RATE;
    const e = envelope(t, duration, 0.01, Math.min(0.5, duration / 2));
    let value = 0;
    for (const note of notes) {
      const hz = typeof note === "number" ? midiToHz(note) : note;
      value += Math.sin(2 * Math.PI * hz * t);
    }
    value = (value / notes.length) * volume * e;
    value += (Math.random() * 2 - 1) * noise * e;
    samples[i] = value;
  }

  writeWav(path.join(OUT, "sfx", file), samples);
}

function synthRain() {
  const duration = 18;
  const total = Math.floor(duration * SAMPLE_RATE);
  const samples = new Float32Array(total);
  let last = 0;

  for (let i = 0; i < total; i++) {
    const t = i / SAMPLE_RATE;
    const white = Math.random() * 2 - 1;
    last = last * 0.93 + white * 0.07;
    const gust = 0.55 + 0.45 * Math.sin(2 * Math.PI * 0.11 * t);
    samples[i] = (white * 0.08 + last * 0.22) * gust;
  }

  writeWav(path.join(OUT, "ambience", "rain_loop.wav"), samples);
}

ensureDir(OUT);

synthMusic({
  file: "lonely_signal.wav",
  duration: 24,
  progression: [
    [57, 60, 64],
    [55, 59, 62],
    [52, 57, 60],
    [53, 57, 62],
  ],
  melody: [72, null, 71, null, 69, null, 67, null],
  pad: 0.16,
  bell: 0.04,
  bass: 0.055,
});

synthMusic({
  file: "digital_spark.wav",
  duration: 20,
  progression: [
    [60, 64, 67],
    [62, 65, 69],
    [57, 60, 64],
    [55, 59, 62],
  ],
  melody: [76, 79, null, 72, 74, null, 79, null],
  pad: 0.12,
  bell: 0.07,
  bass: 0.04,
});

synthMusic({
  file: "office_warmth.wav",
  duration: 24,
  progression: [
    [55, 59, 62],
    [60, 64, 67],
    [57, 60, 64],
    [53, 57, 60],
  ],
  melody: [67, null, 69, 71, null, 72, null, 71],
  pad: 0.15,
  bell: 0.045,
  bass: 0.06,
});

synthMusic({
  file: "date_night.wav",
  duration: 24,
  progression: [
    [53, 57, 60],
    [57, 60, 64],
    [60, 64, 67],
    [55, 59, 62],
  ],
  melody: [72, 74, null, 76, 74, null, 72, null],
  pad: 0.13,
  bell: 0.06,
  bass: 0.07,
});

synthMusic({
  file: "starlit_confession.wav",
  duration: 28,
  progression: [
    [52, 55, 59],
    [57, 60, 64],
    [55, 59, 62],
    [60, 64, 67],
  ],
  melody: [76, null, 79, null, 81, 79, null, 76],
  pad: 0.19,
  bell: 0.055,
  bass: 0.055,
});

synthMusic({
  file: "storm_pulse.wav",
  duration: 22,
  progression: [
    [50, 53, 57],
    [48, 52, 55],
    [45, 50, 53],
    [47, 50, 55],
  ],
  melody: [62, null, null, 60, null, 59, null, null],
  pad: 0.16,
  bell: 0.025,
  bass: 0.12,
});

synthMusic({
  file: "family_blessing.wav",
  duration: 30,
  progression: [
    [55, 59, 62],
    [59, 62, 66],
    [60, 64, 67],
    [57, 60, 64],
  ],
  melody: [71, null, 72, 74, null, 76, 74, null],
  pad: 0.17,
  bell: 0.05,
  bass: 0.06,
});

synthMusic({
  file: "forever_theme.wav",
  duration: 32,
  progression: [
    [60, 64, 67],
    [67, 71, 74],
    [65, 69, 72],
    [64, 67, 72],
  ],
  melody: [79, null, 81, 83, null, 84, 83, 81],
  pad: 0.2,
  bell: 0.065,
  bass: 0.07,
});

synthRain();

synthTone({ file: "chapter_reveal.wav", duration: 1.0, notes: [72, 79, 84], volume: 0.18 });
synthTone({ file: "dialogue_advance.wav", duration: 0.18, notes: [880, 1320], volume: 0.08 });
synthTone({ file: "ui_chime.wav", duration: 0.45, notes: [79, 83], volume: 0.22 });
synthTone({ file: "add_friend.wav", duration: 0.62, notes: [72, 76, 79], volume: 0.26 });
synthTone({ file: "message_ping.wav", duration: 0.32, notes: [88, 91], volume: 0.2 });
synthTone({ file: "gift_open.wav", duration: 0.8, notes: [67, 72, 79], volume: 0.23 });
synthTone({ file: "page_turn.wav", duration: 0.38, notes: [180, 240], volume: 0.06, noise: 0.12 });
synthTone({ file: "ring_shimmer.wav", duration: 1.2, notes: [84, 88, 91], volume: 0.18 });
synthTone({ file: "final_swell.wav", duration: 1.8, notes: [72, 76, 79, 84], volume: 0.2 });

console.log(`Generated audio assets in ${path.relative(ROOT, OUT)}`);
