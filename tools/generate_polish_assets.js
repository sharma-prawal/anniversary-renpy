const fs = require("fs");
const path = require("path");
const { PNG } = require("pngjs");

const ROOT = path.resolve(__dirname, "..");
const UI_DIR = path.join(ROOT, "game", "images", "ui");
const PROPS_DIR = path.join(ROOT, "game", "images", "props");
const EFFECTS_DIR = path.join(ROOT, "game", "images", "effects");

function ensureDirs() {
  for (const dir of [UI_DIR, PROPS_DIR, EFFECTS_DIR]) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function png(width, height, rgba = [0, 0, 0, 0]) {
  const out = new PNG({ width, height });
  for (let i = 0; i < out.data.length; i += 4) {
    out.data[i] = rgba[0];
    out.data[i + 1] = rgba[1];
    out.data[i + 2] = rgba[2];
    out.data[i + 3] = rgba[3];
  }
  return out;
}

function save(file, image) {
  fs.writeFileSync(file, PNG.sync.write(image, { colorType: 6, inputColorType: 6 }));
}

function blendPixel(image, x, y, rgba) {
  if (x < 0 || y < 0 || x >= image.width || y >= image.height) return;
  const i = (y * image.width + x) * 4;
  const srcA = rgba[3] / 255;
  const dstA = image.data[i + 3] / 255;
  const outA = srcA + dstA * (1 - srcA);
  if (outA <= 0) return;

  image.data[i] = Math.round((rgba[0] * srcA + image.data[i] * dstA * (1 - srcA)) / outA);
  image.data[i + 1] = Math.round((rgba[1] * srcA + image.data[i + 1] * dstA * (1 - srcA)) / outA);
  image.data[i + 2] = Math.round((rgba[2] * srcA + image.data[i + 2] * dstA * (1 - srcA)) / outA);
  image.data[i + 3] = Math.round(outA * 255);
}

function fillRect(image, x, y, width, height, rgba) {
  for (let yy = y; yy < y + height; yy += 1) {
    for (let xx = x; xx < x + width; xx += 1) blendPixel(image, xx, yy, rgba);
  }
}

function strokeRect(image, x, y, width, height, rgba, thickness = 1) {
  fillRect(image, x, y, width, thickness, rgba);
  fillRect(image, x, y + height - thickness, width, thickness, rgba);
  fillRect(image, x, y, thickness, height, rgba);
  fillRect(image, x + width - thickness, y, thickness, height, rgba);
}

function fillRoundedRect(image, x, y, width, height, radius, rgba) {
  const r2 = radius * radius;
  for (let yy = y; yy < y + height; yy += 1) {
    for (let xx = x; xx < x + width; xx += 1) {
      const lx = xx < x + radius ? x + radius - xx : xx >= x + width - radius ? xx - (x + width - radius - 1) : 0;
      const ly = yy < y + radius ? y + radius - yy : yy >= y + height - radius ? yy - (y + height - radius - 1) : 0;
      if (lx * lx + ly * ly <= r2 || lx === 0 || ly === 0) blendPixel(image, xx, yy, rgba);
    }
  }
}

function strokeRoundedRect(image, x, y, width, height, radius, rgba, thickness = 2) {
  const outerR2 = radius * radius;
  const innerRadius = Math.max(0, radius - thickness);
  const innerR2 = innerRadius * innerRadius;

  function insideRounded(px, py, rx, ry, rw, rh, rr, rr2) {
    const lx = px < rx + rr ? rx + rr - px : px >= rx + rw - rr ? px - (rx + rw - rr - 1) : 0;
    const ly = py < ry + rr ? ry + rr - py : py >= ry + rh - rr ? py - (ry + rh - rr - 1) : 0;
    return lx * lx + ly * ly <= rr2 || lx === 0 || ly === 0;
  }

  for (let yy = y; yy < y + height; yy += 1) {
    for (let xx = x; xx < x + width; xx += 1) {
      const outer = insideRounded(xx, yy, x, y, width, height, radius, outerR2);
      const inner = insideRounded(
        xx,
        yy,
        x + thickness,
        y + thickness,
        width - thickness * 2,
        height - thickness * 2,
        innerRadius,
        innerR2
      );
      if (outer && !inner) blendPixel(image, xx, yy, rgba);
    }
  }
}

function fillEllipse(image, cx, cy, rx, ry, rgba) {
  for (let y = Math.floor(cy - ry); y <= Math.ceil(cy + ry); y += 1) {
    for (let x = Math.floor(cx - rx); x <= Math.ceil(cx + rx); x += 1) {
      const dx = (x - cx) / rx;
      const dy = (y - cy) / ry;
      if (dx * dx + dy * dy <= 1) blendPixel(image, x, y, rgba);
    }
  }
}

function fillRotatedEllipse(image, cx, cy, rx, ry, angle, rgba) {
  const cos = Math.cos(angle);
  const sin = Math.sin(angle);
  const radius = Math.ceil(Math.max(rx, ry) + 2);
  for (let y = Math.floor(cy - radius); y <= Math.ceil(cy + radius); y += 1) {
    for (let x = Math.floor(cx - radius); x <= Math.ceil(cx + radius); x += 1) {
      const dx = x - cx;
      const dy = y - cy;
      const px = dx * cos + dy * sin;
      const py = -dx * sin + dy * cos;
      if ((px / rx) ** 2 + (py / ry) ** 2 <= 1) blendPixel(image, x, y, rgba);
    }
  }
}

function strokeEllipse(image, cx, cy, rx, ry, rgba, thickness = 8) {
  const innerRx = Math.max(1, rx - thickness);
  const innerRy = Math.max(1, ry - thickness);
  for (let y = Math.floor(cy - ry); y <= Math.ceil(cy + ry); y += 1) {
    for (let x = Math.floor(cx - rx); x <= Math.ceil(cx + rx); x += 1) {
      const outer = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1;
      const inner = ((x - cx) / innerRx) ** 2 + ((y - cy) / innerRy) ** 2 <= 1;
      if (outer && !inner) blendPixel(image, x, y, rgba);
    }
  }
}

function line(image, x1, y1, x2, y2, rgba, thickness = 1) {
  const dx = x2 - x1;
  const dy = y2 - y1;
  const steps = Math.max(Math.abs(dx), Math.abs(dy));
  for (let i = 0; i <= steps; i += 1) {
    const x = Math.round(x1 + (dx * i) / steps);
    const y = Math.round(y1 + (dy * i) / steps);
    fillEllipse(image, x, y, thickness, thickness, rgba);
  }
}

function gradientPanel(file, width, height, radius, border) {
  const image = png(width, height);
  for (let y = 0; y < height; y += 1) {
    const t = y / Math.max(1, height - 1);
    for (let x = 0; x < width; x += 1) {
      const lx = x < radius ? radius - x : x >= width - radius ? x - (width - radius - 1) : 0;
      const ly = y < radius ? radius - y : y >= height - radius ? y - (height - radius - 1) : 0;
      if (lx * lx + ly * ly <= radius * radius || lx === 0 || ly === 0) {
        blendPixel(image, x, y, [
          Math.round(15 + 10 * t),
          Math.round(7 + 5 * t),
          Math.round(13 + 12 * t),
          Math.round(206 + 26 * t),
        ]);
      }
    }
  }
  fillRoundedRect(image, 0, 0, width, Math.floor(height * 0.42), radius, [255, 226, 190, 18]);
  strokeRoundedRect(image, 2, 2, width - 4, height - 4, radius, border, 3);
  save(path.join(UI_DIR, file), image);
}

function makeUi() {
  gradientPanel("dialogue_panel.png", 1700, 238, 28, [238, 186, 128, 110]);
  gradientPanel("nameplate.png", 420, 76, 20, [255, 200, 146, 135]);
  gradientPanel("chapter_panel.png", 980, 360, 34, [255, 209, 153, 130]);
  gradientPanel("prompt_panel.png", 1050, 160, 28, [255, 214, 171, 155]);
  gradientPanel("menu_panel.png", 760, 336, 34, [255, 210, 171, 120]);
  gradientPanel("button_idle.png", 560, 78, 22, [255, 214, 171, 105]);
  gradientPanel("button_hover.png", 560, 78, 22, [255, 232, 190, 190]);

  const overlay = png(1920, 1080);
  for (let y = 0; y < overlay.height; y += 1) {
    for (let x = 0; x < overlay.width; x += 1) {
      const nx = Math.abs(x / overlay.width - 0.5) * 2;
      const ny = Math.abs(y / overlay.height - 0.5) * 2;
      const edge = Math.pow(Math.max(nx, ny), 1.8);
      const bottom = Math.max(0, (y - 720) / 360);
      blendPixel(overlay, x, y, [7, 3, 9, Math.min(150, Math.round(edge * 118 + bottom * 92))]);
    }
  }
  save(path.join(UI_DIR, "cinematic_vignette.png"), overlay);

  const menuDepth = png(1920, 1080);
  for (let y = 0; y < menuDepth.height; y += 1) {
    for (let x = 0; x < menuDepth.width; x += 1) {
      const bottom = Math.max(0, (y - 690) / 390);
      const left = Math.max(0, (390 - x) / 390);
      const right = Math.max(0, (x - 1510) / 410);
      const top = Math.max(0, (220 - y) / 220);
      const alpha = Math.min(150, Math.round(bottom * bottom * 126 + Math.max(left, right) ** 2 * 54 + top * top * 28));
      if (alpha > 0) blendPixel(menuDepth, x, y, [5, 2, 7, alpha]);
    }
  }
  for (let i = 0; i < 10; i += 1) {
    const baseX = 20 + i * 42;
    const baseY = 970 + (i % 3) * 22;
    line(menuDepth, baseX, 1080, baseX + 126 + (i % 4) * 20, baseY - 94, [9, 5, 8, 44], 2);
    for (let j = 0; j < 3; j += 1) {
      const lx = baseX + 38 + j * 28 + (i % 3) * 5;
      const ly = baseY - 18 - j * 22;
      fillRotatedEllipse(menuDepth, lx, ly, 6, 18, -0.68 + j * 0.2, [10, 6, 9, 48]);
    }
  }
  for (let i = 0; i < 10; i += 1) {
    const baseX = 1890 - i * 39;
    const baseY = 100 + (i % 4) * 24;
    line(menuDepth, 1920, baseY - 60, baseX - 112 - (i % 3) * 14, baseY + 104, [9, 5, 8, 34], 2);
    for (let j = 0; j < 3; j += 1) {
      const lx = baseX - 36 - j * 24 - (i % 3) * 4;
      const ly = baseY + 16 + j * 22;
      fillRotatedEllipse(menuDepth, lx, ly, 5, 16, 0.72 - j * 0.18, [10, 6, 9, 40]);
    }
  }
  save(path.join(UI_DIR, "menu_foreground_depth.png"), menuDepth);

  const petals = png(1920, 1080);
  for (let i = 0; i < 72; i += 1) {
    const x = 80 + ((i * 347) % 1780);
    const y = 44 + ((i * 191) % 980);
    const rx = 4 + (i % 4);
    const ry = 10 + (i % 5) * 2;
    const angle = ((i * 29) % 180) * Math.PI / 180;
    const alpha = 34 + (i % 5) * 10;
    fillRotatedEllipse(petals, x, y, rx, ry, angle, [255, 189, 177, alpha]);
    fillRotatedEllipse(petals, x + 1, y - 1, Math.max(2, rx - 2), Math.max(5, ry - 4), angle, [255, 231, 203, Math.round(alpha * 0.35)]);
  }
  save(path.join(UI_DIR, "menu_petal_layer.png"), petals);

  const watermarkMask = png(1920, 1080);
  for (let y = 0; y < watermarkMask.height; y += 1) {
    for (let x = 0; x < watermarkMask.width; x += 1) {
      const tx = Math.max(0, (x - 1580) / 340);
      const ty = Math.max(0, (y - 780) / 300);
      const corner = Math.min(1, Math.max(tx, ty) * Math.min(1, tx + ty));
      if (corner > 0) {
        blendPixel(watermarkMask, x, y, [7, 3, 9, Math.round(210 * corner * corner)]);
      }
    }
  }
  save(path.join(UI_DIR, "watermark_mask.png"), watermarkMask);

  const marker = png(180, 180);
  for (let r = 80; r >= 14; r -= 3) fillEllipse(marker, 90, 90, r, r, [255, 218, 178, Math.max(4, 42 - r / 2)]);
  strokeEllipse(marker, 90, 90, 52, 52, [255, 225, 185, 230], 7);
  fillEllipse(marker, 90, 90, 13, 13, [255, 245, 224, 245]);
  save(path.join(UI_DIR, "hotspot_marker.png"), marker);

  const markerHover = png(180, 180);
  for (let r = 86; r >= 16; r -= 3) fillEllipse(markerHover, 90, 90, r, r, [255, 238, 196, Math.max(8, 62 - r / 2)]);
  strokeEllipse(markerHover, 90, 90, 58, 58, [255, 239, 206, 255], 8);
  fillEllipse(markerHover, 90, 90, 16, 16, [255, 255, 245, 255]);
  save(path.join(UI_DIR, "hotspot_marker_hover.png"), markerHover);
}

function makeRain() {
  const image = png(1920, 1080);
  for (let i = 0; i < 560; i += 1) {
    const x = (i * 137) % 2040 - 80;
    const y = (i * 251) % 1170 - 90;
    const len = 44 + (i % 6) * 18;
    const alpha = 42 + (i % 5) * 16;
    line(image, x, y, x - 18, y + len, [190, 223, 255, alpha], i % 4 === 0 ? 2 : 1);
  }
  for (let i = 0; i < 90; i += 1) {
    const x = (i * 331) % 1920;
    const y = 560 + ((i * 97) % 450);
    strokeEllipse(image, x, y, 18 + (i % 4) * 5, 5 + (i % 3), [200, 230, 255, 36], 2);
  }
  save(path.join(EFFECTS_DIR, "overlay_rain.png"), image);
}

function drawPropStage(drawFn, file) {
  const image = png(1920, 1080);
  drawFn(image);
  save(path.join(PROPS_DIR, file), image);
}

function makeProps() {
  drawPropStage((image) => {
    fillRoundedRect(image, 610, 265, 700, 480, 34, [33, 20, 27, 112]);
    fillRoundedRect(image, 665, 255, 270, 430, 20, [188, 118, 132, 245]);
    fillRoundedRect(image, 930, 255, 340, 430, 20, [252, 239, 221, 246]);
    fillRect(image, 925, 275, 14, 405, [125, 76, 88, 210]);
    strokeRoundedRect(image, 665, 255, 605, 430, 24, [246, 201, 157, 210], 5);
    for (let i = 0; i < 9; i += 1) line(image, 974, 330 + i * 28, 1195, 330 + i * 28, [121, 84, 78, 120], 2);
    fillRoundedRect(image, 728, 402, 150, 78, 12, [255, 231, 207, 60]);
    line(image, 720, 520, 875, 520, [255, 225, 190, 170], 3);
  }, "prop_book.png");

  drawPropStage((image) => {
    fillRoundedRect(image, 620, 250, 680, 410, 24, [35, 22, 22, 118]);
    const frames = [
      [675, 310, 185, 230],
      [895, 280, 250, 300],
      [1170, 330, 165, 205],
    ];
    for (const [x, y, w, h] of frames) {
      fillRoundedRect(image, x + 18, y + 18, w, h, 10, [0, 0, 0, 80]);
      fillRoundedRect(image, x, y, w, h, 10, [124, 82, 48, 255]);
      fillRoundedRect(image, x + 15, y + 15, w - 30, h - 30, 7, [253, 229, 196, 255]);
      fillRoundedRect(image, x + 30, y + 30, w - 60, h - 60, 4, [116, 150, 155, 235]);
      fillEllipse(image, x + w / 2 - 28, y + h / 2 - 10, 32, 44, [247, 190, 166, 220]);
      fillEllipse(image, x + w / 2 + 28, y + h / 2 - 8, 32, 44, [220, 160, 144, 220]);
    }
  }, "prop_framed_photos.png");

  drawPropStage((image) => {
    fillRoundedRect(image, 720, 280, 500, 390, 28, [20, 17, 15, 110]);
    fillRoundedRect(image, 785, 340, 280, 260, 40, [250, 236, 214, 255]);
    strokeEllipse(image, 1080, 455, 95, 85, [250, 236, 214, 245], 28);
    fillEllipse(image, 925, 456, 74, 50, [255, 217, 224, 115]);
    fillEllipse(image, 930, 448, 22, 16, [183, 83, 104, 145]);
    line(image, 850, 395, 998, 395, [180, 115, 120, 130], 4);
    line(image, 850, 525, 998, 525, [180, 115, 120, 90], 4);
  }, "prop_mug.png");

  drawPropStage((image) => {
    fillRoundedRect(image, 645, 230, 630, 500, 30, [26, 18, 16, 120]);
    fillRoundedRect(image, 715, 275, 220, 360, 18, [248, 229, 201, 245]);
    fillRoundedRect(image, 970, 275, 230, 360, 18, [248, 229, 201, 245]);
    for (let i = 0; i < 9; i += 1) {
      line(image, 755, 345 + i * 25, 892, 345 + i * 25, [119, 82, 70, 125], 2);
      line(image, 1010, 345 + i * 25, 1154, 345 + i * 25, [119, 82, 70, 125], 2);
    }
    fillEllipse(image, 822, 295, 25, 18, [216, 133, 132, 170]);
    fillEllipse(image, 1085, 295, 25, 18, [216, 133, 132, 170]);
  }, "prop_letters.png");

  drawPropStage((image) => {
    fillRoundedRect(image, 705, 280, 510, 380, 30, [23, 18, 16, 120]);
    strokeEllipse(image, 860, 470, 138, 88, [238, 180, 66, 255], 30);
    strokeEllipse(image, 1015, 470, 138, 88, [255, 213, 102, 255], 30);
    strokeEllipse(image, 860, 470, 94, 50, [255, 240, 172, 160], 8);
    strokeEllipse(image, 1015, 470, 94, 50, [255, 241, 178, 160], 8);
    fillEllipse(image, 932, 468, 22, 16, [255, 245, 200, 210]);
  }, "prop_rings.png");

  drawPropStage((image) => {
    fillRoundedRect(image, 720, 300, 480, 320, 28, [21, 18, 16, 118]);
    fillRoundedRect(image, 800, 375, 235, 120, 34, [232, 232, 236, 255]);
    strokeEllipse(image, 800, 435, 52, 40, [232, 232, 236, 255], 18);
    strokeEllipse(image, 1038, 435, 52, 40, [232, 232, 236, 255], 18);
    line(image, 824, 442, 1010, 442, [160, 166, 176, 200], 5);
    line(image, 918, 398, 918, 488, [160, 166, 176, 140], 4);
  }, "prop_earphones.png");
}

ensureDirs();
makeUi();
makeRain();
makeProps();
console.log("Generated polished UI, rain, and prop assets.");
