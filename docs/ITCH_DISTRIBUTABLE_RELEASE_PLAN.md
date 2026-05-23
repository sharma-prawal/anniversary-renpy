# Itch.io Ren'Py Distributable Release Plan

Last updated: 2026-05-23

This is the active release plan after pausing HTML5. The goal is to ship a downloadable itch.io build that players install and play on laptops/desktops or larger displays, prioritizing high-resolution art quality over browser payload constraints.

## Release Target

| Target | Decision |
| --- | --- |
| Storefront | itch.io |
| Delivery | Downloadable Ren'Py distributables, not HTML5/browser |
| Primary experience | Installed desktop play on big screens |
| Resolution target | Native 1920x1080 game canvas |
| Asset priority | High-resolution PNG backgrounds/CGs where available |
| Browser/mobile parity | Not required for this release pass |

## Current State

- HTML5 release work is preserved but paused.
- The game already runs at `1920x1080` via `config.screen_width` / `config.screen_height`.
- Runtime image declarations now point to high-resolution desktop assets:
  - Backgrounds: `game/backgrounds_ai/*.png` (`139.7M` referenced)
  - CGs: `game/images_ai/cg/*.png` (`8.5M` referenced)
- Web-optimized assets are preserved in the project for future HTML5 work, but excluded from desktop distributables:
  - `game/backgrounds_web/**`
  - `game/images_web/**`
  - `game/web-presplash.jpg`
- Sprites and props already use AI/runtime PNG paths where needed.
- Runtime music/SFX use MP3 assets. Voiceover uses warmed OGG assets; WAVs and source voice MP3s are excluded from builds.
- Current referenced runtime payload is `177.9M` with `0` missing referenced files.

## Active Progress

| Pass | Status | Result |
| --- | --- | --- |
| High-resolution runtime art | Complete | `game/definitions.rpy` now references `backgrounds_ai/*.png` and `images_ai/cg/*.png`. |
| Desktop build exclusions | Complete | High-res art is included; web JPEGs, web presplash, testcases, docs/tools, images-output, package files, and WAV duplicates are excluded. |
| Automated validation | Complete | `npm test`, payload report, Ren'Py lint, and visual audit passed after the high-resolution switch. |
| Distributable build | Complete | Current Windows, macOS, and Linux archives with the voice update were generated in `/Users/prawalsharma/Documents/Projects/our_story_love_quest-1.0-dists`. |
| Packaged smoke test | Partial | Manual mac packaged playthrough was fine except the cold-open "Tap or click" prompt auto-advanced. That prompt now waits for input, and Downloads distributables/extracted smoke app were rebuilt. Retest only that prompt before closing. |

## Current Build Artifacts

| Artifact | Size | SHA-256 |
| --- | ---: | --- |
| `our_story_love_quest-1.0-win.zip` | `227M` | `2acfe69fce09987c4d83edfd57ef95b6e0d627b50717281fe8a282ed98d68f1a` |
| `our_story_love_quest-1.0-mac.zip` | `236M` | `5045de4e363393e9d5c356d7df14cee98b19d6442fe9c82dc0bac4c59ebe8836` |
| `our_story_love_quest-1.0-linux.tar.bz2` | `211M` | `f4b32f751979f6c2b0c8b5d239b429f57deec89937c7e1eb07731e383a23204e` |

Current output folder:

`/Users/prawalsharma/Documents/Projects/our_story_love_quest-1.0-dists`

For itch upload, use the separate `win`, `mac`, and `linux` builds.

Each current package was checked for the audio update:

- 266 voice OGG files included.
- 0 stale voice MP3 files included.

## P0 Plan

### 1. Switch desktop runtime to high-resolution art

Use the high-resolution assets for the downloadable release:

- [x] Change background image declarations from `backgrounds_web/*.jpg` to `backgrounds_ai/*.png`.
- [x] Change CG image declarations from `images_web/cg/*.jpg` to `images_ai/cg/*.png`.
- Keep sprites/props as-is unless a specific screenshot shows blur or scaling artifacts.
- Keep `backgrounds_web/` and `images_web/` available only for future HTML5/web builds.

Done when:

- Ren'Py lint passes with high-resolution image declarations.
- Visual audit uses high-resolution backgrounds/CGs.
- No referenced high-resolution asset is missing.

### 2. Update build exclusions for desktop release

Current exclusions remove high-resolution assets from builds. For itch desktop builds:

- [x] Stop excluding `game/backgrounds_ai/**`.
- [x] Stop excluding `game/images_ai/cg/**`.
- [x] Exclude web-only optimized assets for desktop packages:
  - `game/backgrounds_web/**`
  - `game/images_web/**`
  - `game/web-presplash.jpg`
- Continue excluding:
  - `game/testcases.*`
  - `tests/**`
  - `archive/**`
  - `images-output/**`
  - `docs/**`
  - `tools/**`
  - `node_modules/**`
  - package files
  - `game/audio/**/*.wav`

Done when:

- Build packages include high-resolution PNG art.
- Build packages do not include debug/test/docs/tools/web-smoke artifacts.

### 3. Validate big-screen quality

Run a visual pass on a large display or high-resolution desktop window:

- Main menu title and buttons feel balanced.
- Dialogue and choice panels do not overlap.
- High-resolution backgrounds look crisp at 1920x1080.
- CG signature peaks look crisp.
- Chapter cards do not flash previous frames.
- Save/load, chapter select, memory gallery, keepsake, and final recap screens remain readable.

Done when:

- Full visual audit passes.
- Manual big-screen review finds no blurry/cropped key screens.

### 4. Build Ren'Py distributables

Use the Ren'Py Launcher or SDK build flow:

```bash
rtk proxy npm test
rtk proxy npm run report:payload
rtk proxy /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.sh . lint
rtk proxy /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.sh . test --overwrite-screenshots visual_audit
rtk proxy /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.sh /Users/prawalsharma/Applications/renpy-8.5.2-sdk/launcher distribute --destination /path/to/itch-dist --no-update /Users/prawalsharma/Documents/Projects/anniversary-renpy
```

Then open Ren'Py Launcher and use **Build Distributions** for desktop targets:

- Windows
- macOS
- Linux

Done when:

- Distributable archives are generated.
- Each target archive has a clear filename, version, and platform label.

### 5. Run final packaged playthrough

Test from the generated distribution, not only from the project folder:

- [x] Launch from a clean extracted package.
- [x] Verify high-resolution art is present in the package.
- [x] Verify web/test/docs/tools/images-output/WAV duplicates are absent from the package.
- Start New Game and complete the story.
- Save and load mid-game.
- Use Chapter Select after unlocks.
- Use Memory Gallery and replay links.
- Confirm all five choice echoes show in annotations/gallery/finale recap.
- Confirm Play Again returns cleanly.
- Confirm audio works from first interaction.

Done when:

- The downloadable package works without requiring project/source files.

## Itch.io Upload Checklist

- Create itch project page as a downloadable game.
- Upload Windows, macOS, and Linux builds separately.
- Mark platform support correctly on itch.
- Use final screenshots from the latest high-resolution desktop pass.
- Page copy should emphasize:
  - premium personal anniversary visual novel
  - memory gallery
  - choices that echo emotionally
  - cinematic CG moments
  - accessible settings
- Add install notes:
  - Download the build for your platform.
  - Extract the compressed file.
  - Run the platform executable/app.
  - Recommended: headphones, fullscreen, 1920x1080 or larger display.

## Copy-Ready itch.io Install Instructions

Use this on the itch page under **Download & Install** or **How to play**.

### Windows

1. Download `our_story_love_quest-1.0-win.zip`.
2. Right-click the ZIP and choose **Extract All...**.
3. Open the extracted folder.
4. Double-click `our_story_love_quest.exe` to start the game.
5. If Windows SmartScreen appears, choose **More info** -> **Run anyway**. This can happen for small indie builds that are not code-signed yet.

### macOS

1. Download `our_story_love_quest-1.0-mac.zip`.
2. Double-click the ZIP to extract it.
3. Open the extracted `our_story_love_quest.app`.
4. If macOS blocks the app because it was downloaded from the internet, right-click the app, choose **Open**, then choose **Open** again.
5. You can also move the app to **Applications** if you want to keep it installed.

### Linux

1. Download `our_story_love_quest-1.0-linux.tar.bz2`.
2. Extract it using your file manager, or run:

   ```bash
   tar -xjf our_story_love_quest-1.0-linux.tar.bz2
   ```

3. Open the extracted folder.
4. Run `our_story_love_quest.sh`.
5. If it does not launch, make it executable and try again:

   ```bash
   chmod +x our_story_love_quest.sh
   ./our_story_love_quest.sh
   ```

### Recommended play setup

- Best experienced with headphones or speakers on.
- Fullscreen is recommended.
- Play on a laptop/desktop display at 1920x1080 or larger when possible.
- The game includes music, ambience, SFX, and voiced dialogue. Voice volume and per-character voice controls are available in **Preferences**.

### Troubleshooting

- If the game does not open, make sure you fully extracted the ZIP/TAR file before launching.
- Do not run the game directly from inside the compressed archive.
- On macOS, use right-click -> **Open** the first time if Gatekeeper blocks the app.
- On Windows, extract the ZIP first; running from the compressed folder can cause missing-file issues.

## Risks and Safeguards

| Risk | Safeguard |
| --- | --- |
| `game/script.rpy` is generated but locally polished | Do not regenerate unless necessary; if regeneration is required, preserve Pass 8 peak beats and Chapter 6 sadness correction. |
| Desktop build accidentally ships web/test artifacts | Re-check build package contents before upload. |
| High-res PNGs increase package size | Accept larger package for itch desktop release; trim only duplicate web assets. |
| Audio changed to MP3 during HTML5 work | Keep MP3 if playback is clean; WAVs remain available locally but excluded to avoid duplicate payload. |
| macOS app quarantine confusion for itch users | Add clear itch install/run note if needed. |

## Success Gate

The itch release is ready when:

- High-resolution assets are active in the desktop runtime.
- Desktop distributables build successfully.
- A clean extracted package completes the full story.
- Screenshots for itch come from the high-resolution desktop build.
- No docs, tools, testcases, images-output, web smoke builds, or WAV duplicates are shipped.
