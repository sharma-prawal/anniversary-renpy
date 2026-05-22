# Local Testing Setup

## Purpose

This project runs on the Ren'Py engine. Node/npm is used only for local generation helpers in `tools/`.

## Installed Tools

- Ren'Py SDK: `/Applications/renpy-8.5.2-sdk`
- Node.js: `v25.9.0`
- npm: `11.12.1`

## One-Time Setup

1. Install Ren'Py SDK (already done on this machine):
   `brew install --cask renpy`
2. Install local Node dependencies from repository root:
   `npm install`

## Pre-Run Validation

From repo root:

```bash
npm run check:source
```

This verifies required sibling source paths:
- `../anniversary-game/src/data/story.json`
- `../anniversary-game/Assets for Game`
- `../anniversary-game/Anniversary - Wedding`

## Generate/Refresh Game Data

Run:

```bash
npm run generate
```

This runs the local generator workflow before testing.

## Run the Game Locally

### Option A: Ren'Py Launcher (recommended)

1. Open Ren'Py:
   `open /Applications/renpy-8.5.2-sdk/renpy.app`
2. In launcher, add/open project folder:
   `/Users/prawalsharma/Documents/Projects/anniversary-renpy`
3. Click `Launch Project`.

### Option B: Ren'Py CLI

Use:

```bash
/Applications/renpy-8.5.2-sdk/renpy.sh /Users/prawalsharma/Documents/Projects/anniversary-renpy
```

## Test Checklist

1. Main menu opens with no script errors.
2. `Begin Our Story` starts at Chapter 1.
3. `Continue` resumes from stored chapter.
4. Chapter transitions and hotspot prompts work.
5. Key backgrounds/sprites load without missing image errors.

## Build/Deployment Flow

This is a Ren'Py distribution flow (not CRA/web deploy):

1. Open project in Ren'Py Launcher.
2. Click `Build Distributions`.
3. Select target packages (Windows/macOS/Linux/market bundle).
4. Publish artifacts from the generated `*-dists` folder to your release channel (for example itch.io or Steam).

## Troubleshooting (macOS)

### Error: `"pythonw" Not Opened`

Cause: macOS quarantine/Gatekeeper blocked Ren'Py helper binaries.

Fix used on this machine:

1. Copy SDK to user-local Applications path:
   `ditto /Applications/renpy-8.5.2-sdk /Users/prawalsharma/Applications/renpy-8.5.2-sdk`
2. Remove quarantine from user-local app:
   `xattr -dr com.apple.quarantine /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.app`
3. Launch that app:
   `open -a /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.app /Users/prawalsharma/Documents/Projects/anniversary-renpy`
