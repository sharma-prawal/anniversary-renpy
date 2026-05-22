const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "game", "audio", "ambience");
const SAMPLE_RATE = 44100;

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function clamp(v) {
  return Math.max(-1, Math.min(1, v));
}

function makeRng(seed) {
  let state = seed >>> 0;
  return function next() {
    state = (state * 1664525 + 1013904223) >>> 0;
    return state / 0xffffffff;
  };
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

function loopEnvelope(t, duration) {
  const edge = Math.min(1.2, duration / 8);
  if (t < edge) return t / edge;
  if (duration - t < edge) return Math.max(0, (duration - t) / edge);
  return 1;
}

function synthAmbience({ file, seed, duration = 18, bed = 0.06, hum = [], sparkle = [], pulses = [] }) {
  const rng = makeRng(seed);
  const total = Math.floor(duration * SAMPLE_RATE);
  const samples = new Float32Array(total);
  let low = 0;
  let mid = 0;

  for (let i = 0; i < total; i++) {
    const t = i / SAMPLE_RATE;
    const white = rng() * 2 - 1;
    low = low * 0.992 + white * 0.008;
    mid = mid * 0.965 + white * 0.035;
    const slow = 0.72 + Math.sin(2 * Math.PI * 0.043 * t + seed) * 0.16 + Math.sin(2 * Math.PI * 0.071 * t) * 0.12;
    let value = (low * 0.58 + mid * 0.2 + white * 0.035) * bed * slow;

    for (const tone of hum) {
      const wobble = Math.sin(2 * Math.PI * tone.drift * t + tone.phase) * tone.depth;
      value += Math.sin(2 * Math.PI * (tone.hz + wobble) * t + tone.phase) * tone.volume;
    }

    for (const tone of sparkle) {
      const phase = (t * tone.rate + tone.phase) % 1;
      if (phase < tone.width) {
        const e = Math.sin(Math.PI * phase / tone.width);
        value += Math.sin(2 * Math.PI * tone.hz * t) * tone.volume * e;
      }
    }

    for (const pulse of pulses) {
      const phase = (t * pulse.rate + pulse.phase) % 1;
      const e = Math.exp(-phase * pulse.decay);
      value += Math.sin(2 * Math.PI * pulse.hz * t) * pulse.volume * e;
    }

    samples[i] = value * loopEnvelope(t, duration);
  }

  writeWav(path.join(OUT, file), samples);
}

ensureDir(OUT);

synthAmbience({
  file: "city_night_loop.wav",
  seed: 1001,
  bed: 0.08,
  hum: [
    { hz: 62, volume: 0.012, drift: 0.08, depth: 1.2, phase: 0.2 },
    { hz: 124, volume: 0.006, drift: 0.05, depth: 0.8, phase: 1.6 },
  ],
  pulses: [{ hz: 210, rate: 0.18, phase: 0.35, decay: 10, volume: 0.006 }],
});

synthAmbience({
  file: "digital_room_loop.wav",
  seed: 1002,
  bed: 0.045,
  hum: [
    { hz: 98, volume: 0.012, drift: 0.12, depth: 0.6, phase: 0.9 },
    { hz: 196, volume: 0.006, drift: 0.08, depth: 0.5, phase: 1.9 },
  ],
  sparkle: [{ hz: 1320, rate: 0.21, phase: 0.2, width: 0.012, volume: 0.008 }],
});

synthAmbience({
  file: "office_air_loop.wav",
  seed: 1003,
  bed: 0.07,
  hum: [
    { hz: 72, volume: 0.015, drift: 0.04, depth: 0.5, phase: 0.4 },
    { hz: 144, volume: 0.007, drift: 0.05, depth: 0.3, phase: 1.1 },
  ],
  pulses: [{ hz: 310, rate: 0.32, phase: 0.12, decay: 14, volume: 0.004 }],
});

synthAmbience({
  file: "restaurant_warm_loop.wav",
  seed: 1004,
  bed: 0.075,
  hum: [{ hz: 88, volume: 0.01, drift: 0.06, depth: 0.6, phase: 1.1 }],
  sparkle: [
    { hz: 740, rate: 0.13, phase: 0.38, width: 0.018, volume: 0.006 },
    { hz: 990, rate: 0.09, phase: 0.77, width: 0.014, volume: 0.005 },
  ],
});

synthAmbience({
  file: "garden_night_loop.wav",
  seed: 1005,
  bed: 0.05,
  hum: [{ hz: 54, volume: 0.007, drift: 0.04, depth: 0.7, phase: 0.5 }],
  sparkle: [
    { hz: 1750, rate: 0.27, phase: 0.1, width: 0.01, volume: 0.007 },
    { hz: 2100, rate: 0.19, phase: 0.65, width: 0.008, volume: 0.005 },
  ],
});

synthAmbience({
  file: "home_warm_loop.wav",
  seed: 1006,
  bed: 0.055,
  hum: [
    { hz: 66, volume: 0.01, drift: 0.05, depth: 0.5, phase: 0.8 },
    { hz: 132, volume: 0.005, drift: 0.05, depth: 0.4, phase: 1.8 },
  ],
});

synthAmbience({
  file: "wedding_hall_loop.wav",
  seed: 1007,
  bed: 0.045,
  hum: [
    { hz: 110, volume: 0.01, drift: 0.03, depth: 0.3, phase: 0.2 },
    { hz: 220, volume: 0.004, drift: 0.04, depth: 0.4, phase: 1.4 },
  ],
  sparkle: [{ hz: 1480, rate: 0.11, phase: 0.42, width: 0.02, volume: 0.006 }],
});

synthAmbience({
  file: "ethereal_light_loop.wav",
  seed: 1008,
  bed: 0.035,
  hum: [
    { hz: 96, volume: 0.01, drift: 0.05, depth: 1.0, phase: 0.6 },
    { hz: 192, volume: 0.007, drift: 0.04, depth: 0.8, phase: 1.2 },
    { hz: 384, volume: 0.004, drift: 0.06, depth: 0.5, phase: 2.1 },
  ],
  sparkle: [{ hz: 1680, rate: 0.08, phase: 0.5, width: 0.03, volume: 0.004 }],
});

console.log(`Generated ambience assets in ${path.relative(ROOT, OUT)}`);
