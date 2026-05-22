const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const destination = process.argv[2];

if (!destination) {
  console.error("Usage: npm run patch:web-shell -- /path/to/web-output");
  process.exit(1);
}

const indexPath = path.resolve(ROOT, destination);
const htmlPath = fs.statSync(indexPath).isDirectory() ? path.join(indexPath, "index.html") : indexPath;

if (!fs.existsSync(htmlPath)) {
  console.error(`Missing index.html at ${htmlPath}`);
  process.exit(1);
}

let html = fs.readFileSync(htmlPath, "utf8");
html = html
  .replace('<meta name="theme-color" content="#000" />', '<meta name="theme-color" content="#050007" />')
  .replace("html {\n      background: #444;", "html {\n      background: #050007;")
  .replace("#canvas {\n      background: #000;", "#canvas {\n      background: #050007;");

if (!html.includes("display: none;\n      position: absolute;\n      left: 0px;")) {
  html = html.replace(
    "    #ContextContainer {\n",
    "    #ContextContainer {\n      display: none;\n",
  );
}

if (!html.includes("#rotateHint")) {
  html = html
    .replace(
      "    #presplash {\n",
      `    #rotateHint {
        display: none;
        position: fixed;
        left: 50%;
        bottom: max(26px, env(safe-area-inset-bottom));
        transform: translateX(-50%);
        z-index: 20;
        max-width: 84vw;
        padding: 14px 22px;
        border: 1px solid rgba(255, 216, 187, 0.36);
        border-radius: 999px;
        background: rgba(5, 0, 7, 0.82);
        color: #FFF8F2;
        font: 600 15px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        text-align: center;
        pointer-events: none;
      }

      @media (orientation: portrait) and (max-width: 600px) {
        #rotateHint {
          display: block;
        }
      }

    #presplash {
`,
    )
    .replace(
      '  <img id="presplash" src="web-presplash.jpg">',
      '  <img id="presplash" src="web-presplash.jpg">\n  <div id="rotateHint">Rotate your phone for the best experience.</div>',
    );
}

html = html.replace("        object-fit: contain;", "        object-fit: cover;");

fs.writeFileSync(htmlPath, html);
console.log(`Patched web shell colors in ${path.relative(ROOT, htmlPath)}`);
