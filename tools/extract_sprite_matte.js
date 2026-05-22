#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const [src, dst, thresholdArg = "6"] = process.argv.slice(2);
if (!src || !dst) {
    console.error("Usage: node tools/extract_sprite_matte.js <src.png> <dst.png> [threshold]");
    process.exit(1);
}

const threshold = Number(thresholdArg);
const canvasWidth = 402;
const canvasHeight = 1536;
const maxSpriteWidth = 392;
const maxSpriteHeight = 1510;

function makeCrc32Table() {
    const table = new Uint32Array(256);
    for (let n = 0; n < 256; n += 1) {
        let c = n;
        for (let k = 0; k < 8; k += 1) {
            c = (c & 1) ? (0xedb88320 ^ (c >>> 1)) : (c >>> 1);
        }
        table[n] = c >>> 0;
    }
    return table;
}

const crcTable = makeCrc32Table();

function crc32(buffer) {
    let c = 0xffffffff;
    for (let i = 0; i < buffer.length; i += 1) {
        c = crcTable[(c ^ buffer[i]) & 0xff] ^ (c >>> 8);
    }
    return (c ^ 0xffffffff) >>> 0;
}

function paeth(left, up, upLeft) {
    const p = left + up - upLeft;
    const pa = Math.abs(p - left);
    const pb = Math.abs(p - up);
    const pc = Math.abs(p - upLeft);
    if (pa <= pb && pa <= pc) return left;
    if (pb <= pc) return up;
    return upLeft;
}

function parsePng(filePath) {
    const buffer = fs.readFileSync(filePath);
    if (buffer.toString("hex", 0, 8) !== "89504e470d0a1a0a") {
        throw new Error("Input is not a PNG.");
    }

    let offset = 8;
    let width = 0;
    let height = 0;
    let colorType = 0;
    const idatChunks = [];

    while (offset < buffer.length) {
        const length = buffer.readUInt32BE(offset);
        offset += 4;
        const type = buffer.toString("ascii", offset, offset + 4);
        offset += 4;
        const data = buffer.subarray(offset, offset + length);
        offset += length + 4;

        if (type === "IHDR") {
            width = data.readUInt32BE(0);
            height = data.readUInt32BE(4);
            const bitDepth = data[8];
            colorType = data[9];
            if (bitDepth !== 8 || ![2, 6].includes(colorType)) {
                throw new Error(`Unsupported PNG format: bitDepth=${bitDepth}, colorType=${colorType}`);
            }
        } else if (type === "IDAT") {
            idatChunks.push(data);
        } else if (type === "IEND") {
            break;
        }
    }

    const bytesPerPixel = colorType === 6 ? 4 : 3;
    const raw = zlib.inflateSync(Buffer.concat(idatChunks));
    const stride = width * bytesPerPixel;
    const rgba = Buffer.alloc(width * height * 4);
    let rawOffset = 0;
    let previous = Buffer.alloc(stride);

    for (let y = 0; y < height; y += 1) {
        const filter = raw[rawOffset];
        rawOffset += 1;
        const line = Buffer.alloc(stride);

        for (let x = 0; x < stride; x += 1) {
            const value = raw[rawOffset];
            rawOffset += 1;
            const left = x >= bytesPerPixel ? line[x - bytesPerPixel] : 0;
            const up = previous[x] || 0;
            const upLeft = x >= bytesPerPixel ? previous[x - bytesPerPixel] : 0;

            if (filter === 0) line[x] = value;
            else if (filter === 1) line[x] = (value + left) & 255;
            else if (filter === 2) line[x] = (value + up) & 255;
            else if (filter === 3) line[x] = (value + Math.floor((left + up) / 2)) & 255;
            else if (filter === 4) line[x] = (value + paeth(left, up, upLeft)) & 255;
            else throw new Error(`Unsupported PNG filter: ${filter}`);
        }

        for (let x = 0; x < width; x += 1) {
            const sourceIndex = x * bytesPerPixel;
            const destIndex = (y * width + x) * 4;
            rgba[destIndex] = line[sourceIndex];
            rgba[destIndex + 1] = line[sourceIndex + 1];
            rgba[destIndex + 2] = line[sourceIndex + 2];
            rgba[destIndex + 3] = colorType === 6 ? line[sourceIndex + 3] : 255;
        }

        previous = line;
    }

    return { width, height, data: rgba };
}

function encodePng(width, height, rgba) {
    const signature = Buffer.from("89504e470d0a1a0a", "hex");

    function chunk(type, data) {
        const typeBuffer = Buffer.from(type, "ascii");
        const length = Buffer.alloc(4);
        const crc = Buffer.alloc(4);
        length.writeUInt32BE(data.length, 0);
        crc.writeUInt32BE(crc32(Buffer.concat([typeBuffer, data])), 0);
        return Buffer.concat([length, typeBuffer, data, crc]);
    }

    const ihdr = Buffer.alloc(13);
    ihdr.writeUInt32BE(width, 0);
    ihdr.writeUInt32BE(height, 4);
    ihdr[8] = 8;
    ihdr[9] = 6;

    const stride = width * 4;
    const raw = Buffer.alloc((stride + 1) * height);
    for (let y = 0; y < height; y += 1) {
        raw[y * (stride + 1)] = 0;
        rgba.copy(raw, y * (stride + 1) + 1, y * stride, y * stride + stride);
    }

    return Buffer.concat([
        signature,
        chunk("IHDR", ihdr),
        chunk("IDAT", zlib.deflateSync(raw, { level: 9 })),
        chunk("IEND", Buffer.alloc(0)),
    ]);
}

function extractBackgroundMask(image) {
    const { width, height, data } = image;
    const mask = new Uint8Array(width * height);
    const queueX = new Int32Array(width * height);
    const queueY = new Int32Array(width * height);
    let head = 0;
    let tail = 0;

    function index(x, y) {
        return y * width + x;
    }

    function isBackground(x, y) {
        const pixel = index(x, y) * 4;
        return (
            data[pixel + 3] > 0
            && data[pixel] <= threshold
            && data[pixel + 1] <= threshold
            && data[pixel + 2] <= threshold
        );
    }

    function push(x, y) {
        const maskIndex = index(x, y);
        if (!mask[maskIndex] && isBackground(x, y)) {
            mask[maskIndex] = 1;
            queueX[tail] = x;
            queueY[tail] = y;
            tail += 1;
        }
    }

    for (let x = 0; x < width; x += 1) {
        push(x, 0);
        push(x, height - 1);
    }
    for (let y = 0; y < height; y += 1) {
        push(0, y);
        push(width - 1, y);
    }

    while (head < tail) {
        const x = queueX[head];
        const y = queueY[head];
        head += 1;
        if (x > 0) push(x - 1, y);
        if (x + 1 < width) push(x + 1, y);
        if (y > 0) push(x, y - 1);
        if (y + 1 < height) push(x, y + 1);
    }

    return mask;
}

function cropSubject(image, mask) {
    const { width, height, data } = image;
    let minX = width;
    let minY = height;
    let maxX = -1;
    let maxY = -1;
    const transparent = Buffer.alloc(width * height * 4);

    for (let y = 0; y < height; y += 1) {
        for (let x = 0; x < width; x += 1) {
            const sourceIndex = (y * width + x) * 4;
            transparent[sourceIndex] = data[sourceIndex];
            transparent[sourceIndex + 1] = data[sourceIndex + 1];
            transparent[sourceIndex + 2] = data[sourceIndex + 2];
            transparent[sourceIndex + 3] = mask[y * width + x] ? 0 : 255;

            if (!mask[y * width + x]) {
                minX = Math.min(minX, x);
                minY = Math.min(minY, y);
                maxX = Math.max(maxX, x);
                maxY = Math.max(maxY, y);
            }
        }
    }

    if (maxX < 0) throw new Error("Could not find a foreground subject.");

    const croppedWidth = maxX - minX + 1;
    const croppedHeight = maxY - minY + 1;
    const cropped = Buffer.alloc(croppedWidth * croppedHeight * 4);

    for (let y = 0; y < croppedHeight; y += 1) {
        for (let x = 0; x < croppedWidth; x += 1) {
            const sourceIndex = ((minY + y) * width + minX + x) * 4;
            const destIndex = (y * croppedWidth + x) * 4;
            transparent.copy(cropped, destIndex, sourceIndex, sourceIndex + 4);
        }
    }

    return {
        width: croppedWidth,
        height: croppedHeight,
        data: cropped,
        bbox: [minX, minY, maxX + 1, maxY + 1],
    };
}

function resizeBilinear(source, width, height) {
    const resized = Buffer.alloc(width * height * 4);

    for (let y = 0; y < height; y += 1) {
        const sourceY = (y + 0.5) * source.height / height - 0.5;
        const y0 = Math.max(0, Math.floor(sourceY));
        const y1 = Math.min(source.height - 1, y0 + 1);
        const fy = sourceY - y0;

        for (let x = 0; x < width; x += 1) {
            const sourceX = (x + 0.5) * source.width / width - 0.5;
            const x0 = Math.max(0, Math.floor(sourceX));
            const x1 = Math.min(source.width - 1, x0 + 1);
            const fx = sourceX - x0;
            const destIndex = (y * width + x) * 4;

            for (let channel = 0; channel < 4; channel += 1) {
                const p00 = source.data[(y0 * source.width + x0) * 4 + channel];
                const p10 = source.data[(y0 * source.width + x1) * 4 + channel];
                const p01 = source.data[(y1 * source.width + x0) * 4 + channel];
                const p11 = source.data[(y1 * source.width + x1) * 4 + channel];
                resized[destIndex + channel] = Math.round(
                    p00 * (1 - fx) * (1 - fy)
                    + p10 * fx * (1 - fy)
                    + p01 * (1 - fx) * fy
                    + p11 * fx * fy
                );
            }
        }
    }

    return { width, height, data: resized };
}

const image = parsePng(src);
const backgroundMask = extractBackgroundMask(image);
const cropped = cropSubject(image, backgroundMask);
const scale = Math.min(maxSpriteWidth / cropped.width, maxSpriteHeight / cropped.height);
const spriteWidth = Math.round(cropped.width * scale);
const spriteHeight = Math.round(cropped.height * scale);
const resized = resizeBilinear(cropped, spriteWidth, spriteHeight);
const canvas = Buffer.alloc(canvasWidth * canvasHeight * 4);
const offsetX = Math.floor((canvasWidth - spriteWidth) / 2);
const offsetY = canvasHeight - spriteHeight - 4;

for (let y = 0; y < spriteHeight; y += 1) {
    for (let x = 0; x < spriteWidth; x += 1) {
        const sourceIndex = (y * spriteWidth + x) * 4;
        const destIndex = ((offsetY + y) * canvasWidth + offsetX + x) * 4;
        resized.data.copy(canvas, destIndex, sourceIndex, sourceIndex + 4);
    }
}

fs.mkdirSync(path.dirname(dst), { recursive: true });
fs.writeFileSync(dst, encodePng(canvasWidth, canvasHeight, canvas));
console.log(
    `Wrote ${dst}: crop=${cropped.bbox.join(",")} resized=${spriteWidth}x${spriteHeight} threshold=${threshold}`,
);
