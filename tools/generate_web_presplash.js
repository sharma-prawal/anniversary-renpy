const fs = require("fs");
const os = require("os");
const path = require("path");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "game", "web-presplash.jpg");

if (spawnSync("swift", ["--version"], { stdio: "ignore" }).status !== 0) {
  console.error("swift is required to render the branded web presplash on macOS.");
  process.exit(1);
}

const swiftSource = String.raw`
import AppKit

let root = CommandLine.arguments[1]
let out = CommandLine.arguments[2]
let size = NSSize(width: 1920, height: 1920)
let rep = NSBitmapImageRep(
    bitmapDataPlanes: nil,
    pixelsWide: Int(size.width),
    pixelsHigh: Int(size.height),
    bitsPerSample: 8,
    samplesPerPixel: 4,
    hasAlpha: true,
    isPlanar: false,
    colorSpaceName: .deviceRGB,
    bytesPerRow: 0,
    bitsPerPixel: 0
)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)

func yFromTop(_ y: CGFloat, _ height: CGFloat) -> CGFloat {
    return size.height - y - height
}

func color(_ hex: Int, _ alpha: CGFloat = 1.0) -> NSColor {
    let r = CGFloat((hex >> 16) & 0xff) / 255.0
    let g = CGFloat((hex >> 8) & 0xff) / 255.0
    let b = CGFloat(hex & 0xff) / 255.0
    return NSColor(calibratedRed: r, green: g, blue: b, alpha: alpha)
}

func font(_ name: String, _ size: CGFloat, _ fallback: NSFont) -> NSFont {
    return NSFont(name: name, size: size) ?? fallback
}

func drawCentered(_ text: String, top: CGFloat, height: CGFloat, font: NSFont, color: NSColor, maxWidth: CGFloat, kern: CGFloat = 0) {
    let paragraph = NSMutableParagraphStyle()
    paragraph.alignment = .center
    let attrs: [NSAttributedString.Key: Any] = [
        .font: font,
        .foregroundColor: color,
        .paragraphStyle: paragraph,
        .kern: kern,
    ]
    let rect = NSRect(x: (size.width - maxWidth) / 2, y: yFromTop(top, height), width: maxWidth, height: height)
    NSString(string: text).draw(in: rect, withAttributes: attrs)
}

func aspectFillRect(imageSize: NSSize, target: NSRect) -> NSRect {
    let scale = max(target.width / imageSize.width, target.height / imageSize.height)
    let width = imageSize.width * scale
    let height = imageSize.height * scale
    return NSRect(x: target.midX - width / 2, y: target.midY - height / 2, width: width, height: height)
}

let full = NSRect(x: 0, y: 0, width: size.width, height: size.height)
color(0x050007).setFill()
full.fill()

let bgPath = root + "/game/backgrounds_web/bg_main_menu.jpg"
if let bg = NSImage(contentsOfFile: bgPath) {
    bg.draw(in: aspectFillRect(imageSize: bg.size, target: full), from: .zero, operation: .sourceOver, fraction: 0.72)
}

color(0x050007, 0.68).setFill()
full.fill()

if let glow = NSGradient(colors: [color(0x5A1226, 0.52), color(0x050007, 0.0)]) {
    glow.draw(fromCenter: NSPoint(x: 960, y: 860), radius: 0, toCenter: NSPoint(x: 960, y: 860), radius: 760, options: [])
}

let card = NSRect(x: 340, y: yFromTop(520, 700), width: 1240, height: 700)
let cardPath = NSBezierPath(roundedRect: card, xRadius: 34, yRadius: 34)
color(0x140810, 0.84).setFill()
cardPath.fill()
color(0xFFD7A6, 0.32).setStroke()
cardPath.lineWidth = 3
cardPath.stroke()

let line = NSRect(x: 650, y: yFromTop(805, 3), width: 620, height: 3)
color(0xFFD7A6, 0.70).setFill()
line.fill()

drawCentered(
    "ANNIVERSARY VISUAL NOVEL",
    top: 640,
    height: 54,
    font: font("AvenirNext-DemiBold", 38, NSFont.boldSystemFont(ofSize: 38)),
    color: color(0xFFE9B8, 0.88),
    maxWidth: 1040,
    kern: 2
)

drawCentered(
    "OUR STORY",
    top: 715,
    height: 150,
    font: font("AvenirNext-Heavy", 122, NSFont.boldSystemFont(ofSize: 122)),
    color: color(0xFFF8F2),
    maxWidth: 1120,
    kern: 1
)

drawCentered(
    "A LOVE QUEST",
    top: 872,
    height: 72,
    font: font("AvenirNext-Bold", 48, NSFont.boldSystemFont(ofSize: 48)),
    color: color(0xFFD8BB),
    maxWidth: 1040,
    kern: 3
)

drawCentered(
    "Loading Our Story...",
    top: 1008,
    height: 58,
    font: font("AvenirNext-Regular", 38, NSFont.systemFont(ofSize: 38)),
    color: color(0xFFEDE1, 0.94),
    maxWidth: 1040
)

NSGraphicsContext.restoreGraphicsState()

guard let jpg = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.86]) else {
    fatalError("Could not encode presplash JPG.")
}

try jpg.write(to: URL(fileURLWithPath: out))
`;

const temp = path.join(os.tmpdir(), `generate-web-presplash-${process.pid}.swift`);
fs.writeFileSync(temp, swiftSource);

const result = spawnSync("swift", [temp, ROOT, OUT], { stdio: "inherit" });
fs.unlinkSync(temp);

if (result.status !== 0) {
  console.error("Failed to generate web presplash.");
  process.exit(result.status || 1);
}

const oldPng = path.join(ROOT, "game", "web-presplash.png");
if (fs.existsSync(oldPng)) fs.unlinkSync(oldPng);

console.log(`Generated ${path.relative(ROOT, OUT)}`);
