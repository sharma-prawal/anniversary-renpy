# Premium Polish Roadmap

This document is the working checklist for moving the anniversary visual novel toward a premium, polished indie visual-novel presentation. Keep recommendations, implementation status, and validation notes here so each pass can be handled one by one.

## Target Bar

- Premium anime/visual-novel art direction across backgrounds, sprites, props, and UI.
- Cinematic scene staging with no character clipping, awkward overlays, or stretched imagery.
- UI that feels intentional: readable, elegant, animated where it helps, and never visually bland.
- Scene-specific interaction points, not generic repeated marker placement.
- Consistent quality across menu, gallery, preferences, dialogue, chapter cards, and story scenes.

## Current Baseline

- Premium AI replacements are active for all chapter backgrounds, props, and character sprites.
- Existing background, prop, and sprite asset references pass the local PNG reference check.
- Unused legacy runtime art is archived under `archive/unused_legacy_assets/2026-05-19/` with a manifest.
- The Ren'Py visual audit currently runs and captures 43 screenshots for the main menu, chapter card, gallery, gallery viewer, preferences, quit confirmation, representative hotspots, chapter moments, props, curated CG moments, and finale scenes.
- The latest visual audit contact sheet is at `tests/screenshots/visual_audit_contact_sheet.png`.

## Work Queue

| Priority | Area | Status | Recommendation | Notes |
| --- | --- | --- | --- | --- |
| P0 | Character staging | Complete | Pull side characters inward and reduce sprite scale slightly so faces and bodies frame cleanly without right-edge clipping. | Applied in `game/definitions.rpy`; verified in the 34-shot contact sheet. |
| P0 | Dialogue UI | Complete | Slim the dialogue panel, reduce text size slightly, and give the name label more breathing room. | Applied in `game/screens.rpy`; lower screen coverage is reduced. |
| P0 | Main menu state | Complete | Disable Continue when no chapter progress exists. | Applied in `game/screens.rpy`; prevents a confusing first-launch path. |
| P0 | Visual audit coverage | Complete | Include preferences, quit confirmation, gallery viewer, chapter card, representative hotspots, and curated CG moments in the contact sheet audit. | Contact sheet now has 43 screenshots. |
| P1 | Outfit variants | Complete | Generate scene-specific outfits for office, casual/date, family, wedding, party, finale, and storm scenes. | Office, date/casual, family, storm, and wedding/finale variants are integrated and verified in the visual audit. |
| P1 | Scene lighting/tints | Complete | Add subtle per-scene color grades and sprite rim-light/tint transforms so sprites sit inside each background. | Applied with reusable sprite tone transforms across story and visual audit scenes. |
| P1 | Prop integration | Complete | Replace floating prop overlays with composed moment images or add shadows, scale, and position per scene. | Added prop-specific focus transforms for book, framed photos, mug, and rings. |
| P1 | Hotspot markers | Complete | Move click markers to scene-relevant locations and add object-specific glow treatment. | Added typed cue colors, precise object placement, dialogue-window hiding during hotspot interaction, and four hotspot audit screenshots. |
| P2 | Main menu identity | Complete | Add a premium title/logo treatment, subtle animated particles, and more layered foreground depth. | Reworked main menu into a hero title lockup plus navigation deck; added restrained petal motion and foreground depth overlays. |
| P2 | Preferences and quit screens | Complete | Make these screens feel like part of the same premium UI system with richer panel hierarchy and state styling. | Preferences now has stronger layout and visible premium sliders; quit confirmation has clearer modal hierarchy. |
| P2 | Memory gallery | Complete | Improve photo presentation with preserved aspect ratios, hover/focus states, and a polished viewer modal. | Added curated memory cards, non-stretched thumbnails, numbered labels, modal viewer, Prev/Next/Close controls, and audit coverage. |
| P2 | Chapter cards | Complete | Give chapter cards chapter-specific blurred backgrounds, reveal motion, and stronger typography. | Added per-chapter art metadata, preview panels, accent colors, mood copy, and reveal motion. |
| P2 | CG moments | Complete | Add key full-screen CG illustrations for major emotional beats. | Added curated 1920x1080 CGs for first meeting, storm reconciliation, and wedding vows; verified in visual audit. |
| P2 | Audio and transitions | Complete | Add scene ambience, premium UI sounds, and smoother scene transitions. | Added deterministic ambience loops for city, digital, office, restaurant, garden, home, wedding, and ethereal arcs; story scenes now use named premium transitions. |
| P3 | Asset cleanup | Complete | Remove or archive unused generated legacy assets after confirming no references remain. | Archived 123 unused assets outside `game/`: old backgrounds, old sprites, procedural prop copies, unused UI artifacts, and AI source/cutout workfiles. |

## Validation Log

| Date | Check | Result | Notes |
| --- | --- | --- | --- |
| 2026-05-18 | Background contact sheet | Passed | `tests/screenshots/backgrounds_ai_contact_sheet.png`; no exact duplicate backgrounds. |
| 2026-05-18 | Prop and sprite normalization | Passed | Props normalized to 1920x1080; sprites normalized to 1536px height with alpha. |
| 2026-05-18 | PNG reference check | Passed | 49 image references checked, 0 missing. |
| 2026-05-18 | Ren'Py visual audit | Passed | 32 screenshots captured; contact sheet generated at `tests/screenshots/visual_audit_contact_sheet.png`. |
| 2026-05-18 | P0 polish pass | Passed | Character staging, dialogue panel, Continue disabled state, and expanded 34-shot visual audit completed. |
| 2026-05-18 | P1 integration pass | Passed | Scene sprite tints, prop focus transforms, preferences polish, and quit confirmation polish completed; 34-shot audit passed. |
| 2026-05-18 | Outfit pass 1 | Passed | Generated and integrated `prawal formal_loving` and `aashna formal_loving` for wedding/finale scenes; 51 PNG refs checked, 34-shot audit passed. |
| 2026-05-18 | Outfit pass 2 | Passed | Generated and integrated office variants for chapters 4-6: Prawal neutral/happy and Aashna neutral/happy/surprised; 56 PNG refs checked, 34-shot audit passed. |
| 2026-05-18 | Outfit pass 3 | Passed | Generated and integrated date/casual variants for restaurant, garden, and paths scenes; 63 PNG refs checked, 34-shot audit passed. |
| 2026-05-18 | Outfit pass 4 | Passed | Generated and integrated family and storm variants for chapters 10 and 12; 89 PNG refs checked, 34-shot audit passed. |
| 2026-05-18 | Hotspot marker pass | Passed | Repositioned every story hotspot to scene objects, added typed cue colors and a dialogue-hiding wrapper, expanded audit coverage to 38 screenshots; 89 PNG refs checked, audit passed. |
| 2026-05-19 | Memory gallery pass | Passed | Upgraded the gallery grid and focused photo viewer; 118 PNG/JPEG refs checked, expanded 39-shot audit passed. |
| 2026-05-19 | Chapter card and CG pass | Passed | Added per-chapter premium card treatment and three curated key CGs; 70 image refs checked, 43-shot visual audit passed. |
| 2026-05-19 | Audio and transition pass | Passed | Added deterministic ambience loops and named premium scene transitions; image/audio refs checked, Ren'Py lint passed with the existing testcase warning, 43-shot visual audit passed. |
| 2026-05-19 | Main menu identity pass | Passed | Added hero title lockup, navigation deck layout, menu foreground depth, and animated petal layers; refs checked, Ren'Py lint passed with the existing testcase warning, 43-shot visual audit passed. |
| 2026-05-19 | Asset cleanup pass | Passed | Archived 123 unused legacy/runtime/workfile artifacts with `archive/unused_legacy_assets/2026-05-19/manifest.json`; runtime refs checked, Ren'Py lint passed with the existing testcase warning, 43-shot visual audit passed. |

## Next Pass Order

1. Roadmap complete. Recommended next step: final release QA playthrough and packaging review.
2. Web/mobile deployment plan is documented in `docs/renpy_web_mobile_deployment_plan.md`.
3. Dialogue and UX-flow polish plan is documented in `docs/dialogue_ux_flow_polish_roadmap.md`.
