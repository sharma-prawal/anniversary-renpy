# Copilot Instructions

## Project Overview

This is a Ren'Py visual novel generated from a sibling Phaser project (`../anniversary-game`). The Ren'Py project is a distribution target — it does not own the story data; the Phaser project does.

## Build & Development Commands

Prefix all shell commands with `rtk` in this repository.

```bash
rtk proxy npm install           # one-time setup
rtk proxy npm run check:source  # validate sibling source paths exist
rtk proxy npm run generate      # regenerate scripts and assets from Phaser story.json
```

`npm test` is an alias for `check:source` — it only validates sibling paths, not game logic.

**Run the game locally:**
```bash
# Option A: Ren'Py CLI
/Applications/renpy-8.5.2-sdk/renpy.sh /Users/prawalsharma/Documents/Projects/anniversary-renpy

# Option B: Open renpy.app in Launcher and add this project folder
open -a /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.app /Users/prawalsharma/Documents/Projects/anniversary-renpy
```

**Ren'Py lint (no automated test suite):**
Run from the Ren'Py launcher or SDK. The visual audit label `visual_audit_gallery` in `game/testcases.rpy` steps through all backgrounds and sprites for manual review.

## Architecture: Generated vs. Manual Files

The critical split to understand:

| File | Owned by |
|---|---|
| `game/script.rpy` | **Generated** — do not hand-edit. Regenerate via `npm run generate` |
| `game/audio.rpy` | **Generated** — produced by `tools/generate_audio_assets.js` |
| `game/definitions.rpy` | **Manual** — characters, transitions, Python helpers, persistent vars |
| `game/screens.rpy` | **Manual** — all custom UI screens |
| `game/polish.rpy` | **Manual** — intentional local polish layer, splashscreen, chapter card label |
| `game/options.rpy`, `game/gui.rpy` | **Manual** — Ren'Py config and styling |
| `game/story.json` | Copy of upstream source; refreshed on generate |

**Source of truth** for story data is `../anniversary-game/src/data/story.json`. After changing it, run `npm run generate` to propagate.

If you need to make a local-only story tweak that shouldn't be regenerated, put it in `game/polish.rpy` — never in `game/script.rpy`.

## Key Conventions

### Ren'Py naming
- Chapter labels: `chapter_1`, `chapter_2`, ... `chapter_15`
- Background images: `bg_ch{N}_{description}` (e.g., `bg_ch4_office_full`)
- CG (key art) images: `cg_ch{N}_{description}` (e.g., `cg_ch14_vows`)
- Sprite display: `show {character} {emotion}` (e.g., `show prawal happy`, `show aashna office_maroon_hoodie`)
- Props: `prop_{name}` (e.g., `prop_rings`)
- Audio channels: `music`, `ambience` (looping), `ui_sfx` (one-shot)

### Characters
```renpy
p = Character("Prawal")   # player character
a = Character("Aashna")   # love interest
n = Character(None)       # narrator (italic)
```

### Transitions
Always use `directed_transition(style)` for scene changes, not bare `with dissolve`. It respects the `access_reduced_motion` accessibility flag.

```renpy
scene bg_ch7_restaurant at bg_cinematic with directed_transition("date")
```

Named styles: `"lonely"`, `"digital"`, `"office"`, `"gift"`, `"date"`, `"starlit"`, `"page"`, `"storm"`, `"home"`, `"family"`, `"promise"`, `"vow"`, `"finale"`, `"soft"`, `"focus"`.

### Mobile layout
Screens must branch on `renpy.variant("small") or renpy.variant("touch")`. Assign this to a local `mobile` variable at the top of each screen block:

```renpy
screen my_screen():
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
```

### Accessibility
Three persistent flags to check in screens and transitions:
- `persistent.access_reduced_motion` — skip or shorten animations
- `persistent.access_large_text` — increase font sizes
- `persistent.access_high_contrast` — swap colour palette

### Audio scene mixing
Call `set_audio_scene("scene_key")` to apply the correct music/ambience volume mix for a scene. Keys are defined in `audio_scene_mix` in `game/audio.rpy`.

### Story choice flags
Five persistent choice variables track tone across chapters:
`story_choice_leap`, `story_choice_gift`, `story_choice_closeness`, `story_choice_repair`, `story_choice_promise`.
These are canon-safe — they add reflective lines but do not change plot events.

### JavaScript tools (`tools/`)
- CommonJS (`require`/`module.exports`), no ESM
- Semicolons required
- Small, synchronous utility functions preferred
- Use `pngjs` for image manipulation (the only devDependency)

## Deployment

Distributed as a Ren'Py build, not a web app:
1. Open project in Ren'Py Launcher → **Build Distributions**
2. Select target (Windows / macOS / Linux / market bundle)
3. Upload artifacts from the `*-dists` output folder to itch.io or Steam

HTML5/web export is currently blocked pending Ren'Py Web support in the local SDK (`WEB_PATH` must be set).
