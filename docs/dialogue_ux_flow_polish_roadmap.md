# Dialogue and UX Flow Polish Roadmap

This document tracks story, dialogue, and UX-flow issues found from `images-output/` screenshots and the generated Ren'Py flow. Use it like `premium_polish_roadmap.md`: keep findings, fixes, and validation notes here as each pass is completed.

## Review Inputs

- Screenshot folder reviewed: `images-output/`
- Contact sheet created for review: `images-output/contact_sheet.png`
- Runtime script reviewed: `game/script.rpy`
- Generated story copy reviewed: `game/story.json`
- Source story manually verified by user and removed from the active work queue.

## Current Findings

| Priority | Area | Status | Finding | Recommended Fix |
| --- | --- | --- | --- | --- |
| P0 | Chapter cards | Complete | Chapter title screens sometimes showed an empty dialogue panel at the bottom. This made the screen look broken and created visual confusion before the chapter started. | `show_chapter_card` now hides the dialogue window before the card appears and restores normal dialogue afterward. |
| P0 | Chapter cards | Complete | Chapter cards repeated chapter labels too much: `CH 07`, `CHAPTER 07`, and large `Chapter 7` all appeared on one screen. The real emotional title was visually secondary. | Chapter cards now use a single chapter identifier and make the emotional subtitle the primary headline. |
| P0 | Save/load UI | Complete | Save/load screen screenshot showed black default Ren'Py UI with plain text and no premium styling. This broke the polished presentation. | Added custom `save`, `load`, `file_slots`, and `navigation` screens with premium panels, touch-friendly slot cards, screenshot previews, and page controls. |
| P1 | Chapter 6 gift scene | Complete | Screenshot/dialogue said `Find the gift in the park`, but the scene is an office gift scene and the earphones are given at the office. This was narratively wrong. | Replaced park copy with office-desk surprise copy and changed the hotspot to `Give her the earphones`; visual audit screenshot reviewed after the prop scale adjustment. |
| P1 | Chapter 6 gift continuity | Complete | The gift visual was a large wrapped box, while the dialogue was about wireless earphones. This could feel mismatched unless framed as a wrapped surprise. | Added the earphones prop reveal and revised dialogue to frame the gift as wrapped earphones; visual audit confirms the prop now reads as part of the desk surprise. |
| P1 | Chapter 7 friend mention | Complete | Dialogue says `Aashna, me, and a friend` and `just the two of them and a friend`, but no friend was shown in the restaurant scene. This read like a missing character or wrong line. | Kept the friend continuity and added a matching full-body friend sprite staged in the Chapter 7 restaurant scene. |
| P1 | Dialogue perspective | Complete | Several Prawal lines refer to `Prawal and Aashna` in third person, which feels odd when Prawal is speaking. Example: `Something was quietly... growing between Prawal and Aashna.` | Rewrote the spoken Chapter 8 and Chapter 10 lines into first person; visual audit now captures the actual rewritten lines for review. |
| P1 | Chapter 10 storm interior | Complete | The inside-apartment storm screenshot still had the full-screen rain overlay, making it look like rain was falling indoors. | Removed the rain overlay after the player enters the apartment; rain is now only visible through the background window and the storm ambience continues. |
| P1 | Chapter 14 intro continuity | Complete | Chapter 14 opens with engagement rings but the narration says the aisle stretches before you and she is waiting at the end. The text describes the wedding before the engagement moment resolves. | Split the scene: engagement ring narration first, then wedding aisle narration after hiding the rings and showing the wedding scene. |
| P1 | Chapter 4 outfit fidelity | Complete | The story detail is specifically a maroon hoodie, but the earlier office sprite read too much like a black jacket at gameplay size. | Restored the `maroon hoodie` wording and added `aashna office_maroon_hoodie`, a clearer premium sprite variant where the maroon hoodie is the dominant visible garment. |
| P1 | Chapter card composition | Complete | Latest `images-output/` screenshot showed the chapter-card thumbnail overlapping the left edge of the copy column, cutting off text like `CHAPTER 05`. | Removed the internal thumbnail column and converted chapter cards to a centered title plaque over full-screen scene art; visual audit now covers Chapter 1, Chapter 5, Chapter 8, and the long Chapter 14 title with no text overlap. |
| P2 | Memory gallery | Complete | Gallery is much better than before, but labels and controls still feel small in screenshots compared with the premium card treatment elsewhere. | Increased gallery label/control prominence while preserving `fit "contain"` thumbnails; visual audit confirms the cards and viewer controls read more clearly. |
| P2 | Final modal | Complete | Final message is readable but visually smaller than the emotional weight of the finale. It could feel more premium. | Added a stronger final-message treatment and direct visual audit screenshot with improved title, copy scale, and Play Again hierarchy. |
| P2 | Window aspect/capture | Complete | Screenshots show large black top/bottom bands when the game window is not 16:9. This may be from the desktop window capture, but it affects perceived polish. | Added 16:9 desktop launch sizing, changed the Ren'Py clear color to the premium shell background, and documented web hosting aspect guidance for centered 16:9 HTML5 deployment. |

## Dialogue Rewrite Targets

These are the highest-impact text edits to make first.

| Chapter | Current Issue | Proposed Direction |
| --- | --- | --- |
| Chapter 4 | `Notice the girl in the maroon hoodie` / `Standing there in that maroon hoodie.` | Complete: kept the real-story maroon hoodie wording and replaced the scene sprite with a clearer maroon-hoodie variant. |
| Chapter 6 | `Find the gift in the park.` | Complete: changed to `Open the surprise on her desk.` and `Give her the earphones.` |
| Chapter 6 | Earphones appear as a large gift box. | Complete: added the earphones prop reveal and the line `I wrapped them like it was the biggest gift in the world.` |
| Chapter 7 | `Aashna, me, and a friend.` | Keep the line; the new `friend date_happy` sprite is now visible in the restaurant scene. |
| Chapter 8 | `just the two of them and a friend` | Keep friend continuity if Chapter 7 staging is visible; optionally tighten wording later to `the three of them`. |
| Chapter 8 | Prawal says `between Prawal and Aashna` | Complete: changed to `between us`. |
| Chapter 10 | Prawal says `Prawal and Aashna came back` | Complete: changed to `we came back to each other`. |
| Chapter 10 | Rain overlay appears inside the apartment. | Complete: removed the full-screen rain overlay from the interior scene while keeping the storm ambience. |
| Chapter 14 | Wedding aisle text appears while rings are on screen. | Complete: engagement/rings text now appears first, then wedding aisle text after the scene changes. |

## Recommended Pass Order

1. Complete: Fix chapter-card UX: hide the dialogue window during chapter cards and simplify duplicate title hierarchy.
2. Removed: source story continuity was manually verified by the user and no longer needs an active pass.
3. Complete: Rewrite Chapter 6 continuity and validate Chapter 7/8 friend staging: office earphones, visible friend sprite, and no off-screen-only character references.
4. Complete: Sweep dialogue perspective: keep Prawal first-person, narrator third-person, and remove awkward mixed narration.
5. Complete: Add premium save/load screens so the default black Ren'Py UI no longer appears.
6. Complete: Polish final modal and gallery control hierarchy.
7. Complete: Re-run full visual audit and add screenshots specifically for chapter cards, save/load, rewritten story beats, gallery, final modal, and aspect-safe representative frames.

## Implementation Notes

- Prefer editing `../anniversary-game/src/data/story.json` for story/dialogue changes, then regenerate this Ren'Py project.
- Keep local UI polish in `game/screens.rpy`, `game/polish.rpy`, and supporting assets/scripts where it is already intentionally local.
- After regeneration, verify that local polish files are not overwritten or re-apply expected local changes if needed.
- Any new screenshots added to `images-output/` should be reviewed against this document and then reflected in the work queue.
- Chapter 7 friend resolution: generated `game/sprites_ai/friend/date_happy.png`, registered `image friend date_happy`, and staged it in the Chapter 7 restaurant scene behind the leads.
- Chapter 4 hoodie resolution: generated a clean maroon-hoodie Aashna sprite, extracted it to the standard Ren'Py transparent sprite canvas with `tools/extract_sprite_matte.js`, and staged it only in the Chapter 4 first-meeting scene.

## Implementation Log

| Date | Pass | Completed Pointers | Files Updated | Validation Notes |
| --- | --- | --- | --- | --- |
| 2026-05-19 | Chapter-card UX pass | P0 chapter-card dialogue window; P0 duplicate chapter hierarchy | `game/polish.rpy`, `game/screens.rpy` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed and refreshed `tests/screenshots/visual_audit/00a_chapter_card.png`. |
| 2026-05-19 | Premium save/load pass | P0 save/load UI | `game/screens.rpy`, `game/testcases.rpy` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed after fixing the reusable `file_slots` audit render path, with `00e_save.png` and `00f_load.png` captured. |
| 2026-05-19 | Visual audit refresh | Validation artifact update | `game/testcases.rpy`, `tests/screenshots/visual_audit/`, `tests/screenshots/visual_audit_contact_sheet.png` | `renpy.sh ... test --overwrite-screenshots visual_audit` passed; regenerated 45 screenshots and refreshed the review contact sheet. |
| 2026-05-20 | Chapter 6 gift continuity pass | P1 Chapter 6 gift scene; P1 Chapter 6 gift continuity | `game/script.rpy`, `game/definitions.rpy`, `game/testcases.rpy`, `tests/screenshots/visual_audit/09_ch6_office_gift.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:146` warning; visual audit passed, the earphones prop scale was adjusted after screenshot review, and the contact sheet was refreshed. |
| 2026-05-20 | Dialogue perspective pass | P1 Dialogue perspective | `game/script.rpy`, `game/story.json`, `game/testcases.rpy`, `tests/screenshots/visual_audit/13_ch8_clearing_stars.png`, `tests/screenshots/visual_audit/17_ch10_storm_inside.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:146` warning; visual audit passed, refreshed 45 screenshots, and Chapter 8/10 dialogue screenshots were manually reviewed. |
| 2026-05-20 | Chapter 10 rain and Chapter 14 continuity pass | P1 Chapter 10 storm interior; P1 Chapter 14 intro continuity | `game/script.rpy`, `game/story.json`, `game/testcases.rpy`, `tests/screenshots/visual_audit/17_ch10_storm_inside.png`, `tests/screenshots/visual_audit/26_ch14_engagement_rings.png`, `tests/screenshots/visual_audit/27_ch14_wedding.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed, refreshed 45 screenshots, and Chapter 10/14 screenshots were manually reviewed. |
| 2026-05-20 | Gallery and final modal hierarchy pass | P2 Memory gallery; P2 Final modal | `game/screens.rpy`, `game/testcases.rpy`, `tests/screenshots/visual_audit/00b_memory_gallery.png`, `tests/screenshots/visual_audit/00bb_memory_viewer.png`, `tests/screenshots/visual_audit/00g_final_message.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed, refreshed 46 screenshots, and gallery/viewer/final-modal screenshots were manually reviewed. |
| 2026-05-20 | Window aspect/capture pass | P2 Window aspect/capture | `game/options.rpy`, `docs/renpy_web_mobile_deployment_plan.md`, `tests/screenshots/visual_audit/00_main_menu.png`, `tests/screenshots/visual_audit/00a_chapter_card.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; config verification confirmed `config.physical_width = 1280`, `config.physical_height = 720`, and `config.gl_clear_color = "#050007"`; visual audit passed, refreshed 46 screenshots, and representative full-screen frames were manually reviewed. |
| 2026-05-20 | Screenshot feedback pass | P1 Chapter 4 outfit fidelity; P1 Chapter card composition | `game/script.rpy`, `game/story.json`, `game/screens.rpy`, `game/testcases.rpy`, `game/definitions.rpy`, `game/sprites_ai/aashna/office_maroon_hoodie.png`, `tools/extract_sprite_matte.js`, `docs/dialogue_ux_flow_polish_roadmap.md`, `tests/screenshots/visual_audit/00aa_chapter_card_ch1.png`, `tests/screenshots/visual_audit/05b_hotspot_maroon_hoodie.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed, refreshed 48 screenshots, and `05b_hotspot_maroon_hoodie.png` plus the Chapter 4 first-meeting CG were manually reviewed. |
| 2026-05-20 | Chapter-card overlap fix | P1 Chapter card composition | `game/screens.rpy`, `game/testcases.rpy`, `docs/dialogue_ux_flow_polish_roadmap.md`, `tests/screenshots/visual_audit/00a_chapter_card.png`, `tests/screenshots/visual_audit/00ab_chapter_card_ch5.png`, `tests/screenshots/visual_audit/00ac_chapter_card_ch14.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed, refreshed 50 screenshots, and Chapter 5/14 cards were manually reviewed with no left-side text overlap. |

## Validation Checklist

- Runtime story reference scan has `0` missing assets.
- `rtk npm test` passes.
- Ren'Py lint passes, allowing only the existing known testcase warning if still present.
- Visual audit passes and contact sheet is regenerated.
- Manual playthrough confirms:
  - No empty dialogue panel appears on chapter cards.
  - Chapter cards do not duplicate chapter labels awkwardly.
  - Save/load screens match the premium UI system.
  - Chapter 6 gift copy matches the office/earphones scene.
  - Chapter 7/8 friend references are supported visually by the Chapter 7 friend sprite.
  - Prawal dialogue stays first-person unless intentionally narrated.
