# Ren'Py Web and Mobile Browser Deployment Plan

## Summary

This plan prepares the anniversary Ren'Py visual novel for **HTML5 web deployment first**, with browser play on iPhone, iPad, Android Chrome, and desktop browsers. The implementation should preserve the current premium visuals and gameplay while making custom UI screens touch-friendly, responsive, and safe for mobile browser constraints.

Chosen defaults:

- Deployment target: web-first Ren'Py HTML5 build.
- Primary devices: iPhone/iPad Safari, Android Chrome, desktop Chrome/Safari.
- Asset profile: maximum quality; preserve premium art by default.
- Android APK: compatibility-aware, but not the first delivery target.
- Desktop compatibility: preserved.
- Gameplay: unchanged.
- Aspect policy: preserve the 16:9 game frame, use a 16:9 desktop launch window, and make any unavoidable browser letterbox/pillarbox bars use the same deep premium background color as the game shell.

## Implementation Status

Status as of 2026-05-21: **partially implemented and validated locally; final web build is blocked until Ren'Py Web support is installed in the local SDK**.

Implemented:

- Core custom screens have mobile/touch-aware variants.
- Runtime backgrounds and CGs now use a dedicated JPEG web profile:
  - `game/backgrounds_web/`
  - `game/images_web/cg/`
- Original premium PNG backgrounds/CGs remain in the repo for source-quality editing, but are excluded from Ren'Py distribution archives through `build.classify`.
- A reusable asset preparation script exists:

  ```sh
  rtk npm run prepare:web-assets
  ```

- A runtime payload report exists:

  ```sh
  rtk npm run report:payload
  ```

Current measured payload:

- Converted opaque background/CG source size: `148.2M -> 18.3M`.
- Referenced runtime payload after this pass:
  - backgrounds: `16.5M`
  - CGs: `1.8M`
  - sprites: `18.0M`
  - props/UI: `2.6M`
  - photos: `4.9M`
  - audio: `31.4M`
  - total referenced runtime assets/audio: `75.0M`

Remaining blockers:

- Audio is still PCM WAV. A real encoder such as `ffmpeg`, `opusenc`, or `oggenc` is needed before converting to OGG/Opus safely.
- The local Ren'Py SDK currently reports missing Ren'Py Web support during `web_build`. An escalated build attempt reaches "All packages have been built", then fails while preparing progressive download because `WEB_PATH` is `None`. Install Ren'Py Web support through the Ren'Py launcher before final HTML5 export.
- Real iPhone/iPad/Android browser QA is still required after a successful web build.

## Reviewed Prompt

Use this as the implementation prompt for the web/mobile readiness pass:

> Optimize this Ren'Py visual novel for HTML5 web deployment and touch-first browser play on iPhone, iPad, Android Chrome, and desktop browsers. Preserve existing premium visuals and gameplay. Refactor custom screens for mobile-safe layout, touch input, readable text, responsive scaling, and browser performance. Keep desktop behavior intact. Validate with Ren'Py lint, visual audit screenshots, and a Ren'Py web build.

## Key Changes

- Add mobile/touch-aware UI helpers in `game/screens.rpy`:
  - Use `renpy.variant("small")` and `renpy.variant("touch")` for mobile layout values.
  - Keep the 1920x1080 base resolution in `game/options.rpy`.
  - Keep the physical desktop launch window at 1280x720 so screenshots and local QA start in a clean 16:9 frame.
  - Set Ren'Py's OpenGL clear color to the game shell background (`#050007`) so browser or desktop letterbox/pillarbox areas no longer read as accidental black bars.
  - Add reusable sizing helpers for button height, text size, panel width, spacing, and gallery columns.

- Refactor custom screens for mobile:
  - `main_menu`: stack title and navigation vertically on small/touch screens; keep the premium split layout on desktop.
  - `say`: increase mobile dialogue height, preserve name/text separation, and keep text readable.
  - `memory_gallery`: switch from 4 columns to 2 columns on mobile, with larger touch cards and draggable scrolling.
  - `memory_photo_viewer`: enlarge Prev/Next/Close controls and place them safely inside touch reach.
  - `chapter_card`: use a vertical card layout on mobile instead of side-by-side preview/copy.
  - `hotspot_prompt`: keep the tap marker large and ensure the prompt does not cover required interaction areas.
  - `preferences`, `confirm`, `game_menu`, and `final_message`: reduce fixed panel widths, increase touch spacing, and make buttons/sliders easier to tap.

- Remove hover-only dependency:
  - Keep hover backgrounds for desktop polish.
  - Ensure every hover affordance also has a clear idle state and tap action.
  - Keep keyboard/right-click shortcuts only as optional desktop conveniences.
  - Add explicit visible Close/Back/Prev/Next buttons wherever keyboard/right-click currently exists.

- Preserve maximum visual quality while protecting browser performance:
  - Keep original premium PNG assets in source folders.
  - Use web JPEG runtime copies for opaque backgrounds and CGs.
  - Keep sprites/props as PNG because they require alpha and precise edge quality.
  - Avoid adding new heavy animated overlays on mobile/web.
  - Disable or simplify continuous decorative transforms on touch/small variants where needed.
  - Convert WAV audio later with a real OGG/Opus-capable encoder and verify browser playback.

- Add web deployment documentation:
  - Build command:

    ```sh
    rtk /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.sh /Users/prawalsharma/Applications/renpy-8.5.2-sdk/launcher web_build /Users/prawalsharma/Documents/Projects/anniversary-renpy --destination /path/to/web-output
    ```

  - If this fails with `WEB_PATH` as `None`, install Ren'Py Web support in the Ren'Py launcher and rerun the command.
  - The Ren'Py web output should be deployable as static files on HTTPS hosting.
  - Host the generated canvas inside a centered 16:9 container when possible. On phones and tablets, prefer fitting the whole 16:9 game in the visible viewport over cropping UI; if letterboxing is unavoidable, set the page background to `#050007`.
  - Target manual QA browsers: iPhone Safari, iPad Safari, Android Chrome, desktop Chrome, and desktop Safari.

## Test Plan

- Static checks:
  - Runtime asset reference scan reports `0` missing files.
  - `rtk npm test`.
  - Ren'Py lint passes, accepting only the existing `game/testcases.rpy:144` unreachable testcase warning.

- Visual checks:
  - Existing `visual_audit` screenshot suite passes.
  - Confirm screenshots are generated from a 16:9 runtime configuration and that the configured clear color is not pure black.
  - Add mobile-layout audit coverage where feasible for:
    - main menu
    - dialogue
    - memory gallery
    - memory viewer
    - preferences
    - hotspot prompt
    - chapter card

- Build checks:
  - Run the Ren'Py `web_build` command.
  - Serve the generated web folder locally.
  - Verify loading, audio start behavior, tap-to-advance, gallery scrolling, modal controls, preference sliders, and hotspot taps.
  - Resize desktop/browser windows to non-16:9 shapes and confirm any bars use the deep premium background rather than black.
  - Perform manual device QA on iPhone/iPad Safari and Android Chrome.

## Assumptions

- This pass does not reduce visual quality by default.
- Android APK is not built unless explicitly requested later.
- No inventory system exists in the current project, so inventory-specific work is out of scope.
- Save/load/history screens are Ren'Py defaults unless custom screens are added later.
- Desktop hover polish remains, but no required gameplay path may depend on hover, keyboard, or right-click.
