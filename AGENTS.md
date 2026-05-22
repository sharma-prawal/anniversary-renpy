# Repository Guidelines

## Project Structure & Module Organization

This is a generated Ren'Py visual novel project. Game code and assets live under `game/`:

- `game/script.rpy` contains the generated chapter flow and dialogue labels.
- `game/definitions.rpy`, `game/screens.rpy`, `game/gui.rpy`, and `game/options.rpy` define characters, images, UI screens, styling, and Ren'Py configuration.
- `game/backgrounds/`, `game/sprites/`, `game/images/`, and `game/photos/` contain runtime art assets.
- `game/story.json` is the copied story data used by this generated project.
- `tools/build_from_story.js` is the regeneration helper. Its source of truth is the sibling Phaser project at `../anniversary-game/src/data/story.json`.

## Build, Test, and Development Commands

- `rtk proxy npm install` sets up the local Node tooling workspace (`package.json`, `node_modules`).
- `rtk proxy npm run check:source` validates the required sibling source directories before generation.
- `rtk proxy npm run generate` regenerates Ren'Py scripts and assets from the sibling Phaser project. Run it from the repository root after upstream story or asset changes.
- Open this folder in the Ren'Py launcher to run the game locally.
- If a local Ren'Py SDK is installed, use that SDK's launcher or CLI to start/check the project; no project-specific wrapper is currently provided.

## Coding Style & Naming Conventions

Use 4-space indentation in `.rpy` files, matching the existing Ren'Py labels, screens, and transforms. Keep generated labels in the `chapter_N` pattern and image names aligned with asset filenames, such as `bg_ch7_restaurant` or `prawal happy`. Prefer lowercase snake_case for new image, transform, and screen identifiers. JavaScript helper code in `tools/` uses CommonJS, semicolons, and small synchronous utility functions.

## Testing Guidelines

There is no automated test suite in this repository. Validate changes by launching the project in Ren'Py and walking through affected chapters. For regeneration changes, confirm that `game/script.rpy`, `game/definitions.rpy`, and expected assets are recreated correctly, then run the game from the main menu and continue flow.

## Commit & Pull Request Guidelines

This directory is not currently a Git repository, so no local commit convention can be inferred. Use concise imperative commit messages when versioning is added, for example `Update generated chapter backgrounds`. Pull requests should describe the story or asset changes, note whether `tools/build_from_story.js` was run, and include screenshots for visible UI or art changes.

## Agent-Specific Instructions

Follow `/Users/prawalsharma/.codex/RTK.md`: prefix shell commands with `rtk` when working in this repository. Do not hand-edit generated sections unless the change is intentionally local; prefer updating the source story or generator and regenerating.
