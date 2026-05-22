# Game Director Review

## Executive Summary

The game has moved well past a hobby prototype in visual ambition. It now presents as an indie-polished romantic visual novel with strong personal sincerity, upgraded art, custom UI, curated CG moments, and a mostly stable Ren'Py implementation.

It is not premium-ready yet. The largest gap is not raw asset quality anymore; it is direction, systems depth, web readiness, and deeper emotional interactivity. The game has started moving beyond fixed desktop-only layouts, but it still has heavy web payloads, limited release-device QA, and uneven UI maturity across screens. For a paid premium visual novel, it needs sharper pacing, more intentional interaction, robust mobile/web testing, accessibility controls, and a stronger "I am playing this story" feeling rather than "I am clicking through a tribute video."

Current professional read: **indie-polished vertical slice, not yet premium release-ready**.

Current roadmap status:

- Local premium-polish implementation tickets are mostly complete: Tickets 1-5 and 7-16 are `Complete`.
- Ticket 6 remains `Blocked`, not complete, because final HTML5 export and browser/device validation require Ren'Py Web support in the local SDK.
- The Premium Polish Roadmap phases are not fully complete. They still include release-device QA, HTML5 build verification, audio/web compression, manual real-save testing, and deeper premium upgrades.
- Do not treat this game as release-ready until Ticket 6 is unblocked and the open Phase 1/2 browser, mobile, audio, and manual QA items are validated.

Technical validation snapshot from this review:

- `rtk npm test` passes.
- Runtime image/audio reference scan reports `0` missing files.
- Static label scan found `22` labels, `40` static jumps/calls, and `0` missing static jump/call targets.
- Ren'Py lint now passes with no warnings after the testcase cleanup pass.
- Visual audit passes and now refreshes `69` screenshots, including forced mobile previews for main menu, chapter select, gallery, choice, preferences, save/load, final modal, a filled-slot save metadata check, and accessibility high-contrast/large-text previews.
- Lint reports `292` dialogue blocks, `2,390` words, `74` images, `25` screens, and `5` story menus after the implementation passes.
- Runtime background/CG assets now use web JPEG copies instead of the original premium PNGs. Opaque background/CG source size was reduced from `148.2M` to `18.3M` for runtime web use.
- Current referenced runtime payload is `75.0M`: `16.5M` backgrounds, `1.8M` CGs, `18.0M` sprites, `2.6M` props/UI, `4.9M` photos, and `31.4M` audio.
- Final HTML5 export is blocked until Ren'Py Web support is installed in the local SDK; an escalated `web_build` attempt builds the packages, then fails while preparing progressive download because `WEB_PATH` is unset.

## Implementation Tracker

Use this tracker as the working status board for the director backlog. A ticket is only `Complete` after implementation, automated checks, Ren'Py lint, and refreshed visual audit screenshots pass.

| Ticket | Status | Current Pass Notes | Validation |
| --- | --- | --- | --- |
| Ticket 1: Add a Persistent Quick Menu | Complete | Added an in-story quick menu with Back, Save, Load, History, Auto, Skip, Settings, and Menu actions. Screenshot review confirms it clears the dialogue box on the audited story frame. | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed and refreshed `52` screenshots. Reviewed `00h_quick_menu_story.png`. |
| Ticket 2: Add Dialogue History Screen | Complete | Added a premium History screen linked from the quick menu and navigation. The screen shows recent lines in readable premium cards and uses touch-friendly Older/Newer paging for longer history sessions. | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed and refreshed `52` screenshots. Reviewed `00i_history.png`. |
| Ticket 3: Convert Decorative Hotspots Into Meaningful Memory Interactions | Complete | Added a reusable memory-interaction map and converted Chapters 2, 6, 9, 11, and 12 into optional reveal screens with numbered scene markers, found-state feedback, and Continue unlocked after one reveal. | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed and refreshed `57` screenshots. Reviewed `03c_memory_map_ch2.png`, `09b_memory_map_ch6.png`, `15b_memory_map_ch9.png`, `19c_memory_map_ch11.png`, and `23b_memory_map_ch12.png`. |
| Ticket 4: Add Low-Risk Emotional Choices | Complete | Added five canon-safe emotional choices across Chapters 2, 6, 8, 10, and 14. Choices set tone flags, add short reflective lines, and influence Chapter 15/final-message callbacks without changing canon events. | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning and reports `5` story menus; visual audit passed and refreshed `58` screenshots. Reviewed `00j_emotional_choice.png`. |
| Ticket 5: Mobile Variant Pass | Complete | Added `small`/`touch`-aware layout branches for core screens: dialogue, quick menu, main menu, chapter cards, hotspots, memory maps, choices, memory gallery/viewer, history, preferences, save/load, confirm, and final modal. Added forced mobile visual-audit coverage for the highest-risk screens. | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed and refreshed `64` screenshots. Reviewed `00k_mobile_main_menu.png`, `00m_mobile_choice.png`, `00n_mobile_preferences.png`, `00o_mobile_save.png`, and `00p_mobile_final_message.png`. Real browser/device QA remains in Ticket 6. |
| Ticket 6: Web Payload Optimization | Blocked | Added a reproducible web asset profile, converted opaque backgrounds/CGs to high-quality JPEG runtime copies, switched runtime image declarations to the web profile, excluded original heavy PNG backgrounds/CGs from distribution archives, added payload reporting, and documented the Ren'Py Web build path/blocker. Final browser build QA is blocked because the local SDK has no Ren'Py Web support installed. Audio remains WAV pending a real OGG/Opus encoder. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; `rtk npm run report:payload` reports `75.0M` referenced payload and `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed and refreshed `64` screenshots; contact sheet regenerated and representative JPEG-backed frames were reviewed. Escalated `web_build` reached "All packages have been built" and then failed because `WEB_PATH` is `None`. |
| Ticket 7: Save/Load Screen Release Polish | Complete | Upgraded save/load slots with designed empty states, current-page styling, disabled empty load slots, clipped thumbnails, latest-save state, chapter metadata, and playtime display. Added save metadata callbacks and a visual-audit-only filled save-slot check. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed and refreshed `65` screenshots. Reviewed `00e_save.png`, `00f_load.png`, `00o_mobile_save.png`, and `00q_filled_save.png`. |
| Ticket 8: Preferences Accessibility Upgrade | Complete | Added persistent Large Text, High Contrast, and Reduced Motion toggles, plus Self-Voicing access in Preferences. Wired large text/high contrast into dialogue, choices, hotspots, chapter cards, and Preferences; reduced motion now disables menu petals, chapter-card motion, and hotspot pulsing. Desktop sliders now have visible thumbs. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `70.2s` and refreshed `67` screenshots. Reviewed `00r_accessibility_preferences.png` and `00s_accessibility_choice.png`. |
| Ticket 9: Dialogue Rewrite Pass for Subtext and Voice | Complete | Rewrote high-impact scenes in Chapters 4, 6, 8, 9, 10, 14, and 15 with more concrete sensory detail, more subtext, stronger emotional progression, and additional Aashna lines. Updated visual audit samples so rewritten lines are covered in screenshots. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `68.6s` and refreshed `67` screenshots. Reviewed rewritten Chapter 4, Chapter 8, and Chapter 10 screenshots. |
| Ticket 10: Final Art Direction QA | Complete | Reviewed the refreshed 67-frame contact sheet and full-size representative frames. Added scene-specific Chapter 7 date transforms so the friend reads as supporting context and Prawal/Aashna carry the composition. Reduced/repositioned the Chapter 6 earphones prop so it sits believably on the gift box instead of reading as a pasted foreground asset. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `68.5s` and refreshed `67` screenshots. Reviewed `09_ch6_office_gift.png`, `10_ch7_restaurant.png`, `27_ch14_wedding.png`, and the contact sheet. |
| Ticket 11: Audio Mix and Cue Direction Pass | Complete | Added a runtime audio direction layer with named scene mix profiles and cue categories. Chapter music/ambience now gets balanced per mood, SFX are routed through volume-controlled cue types, and dialogue tick playback is softened/throttled. Added `docs/AUDIO_MIX_NOTES.md` with current cue rules and remaining release audio work. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual/runtime audit passed in `67.3s` and refreshed `67` screenshots. |
| Ticket 12: Chapter Select and Replay Hub | Complete | Added a locked/unlocked Chapter Select screen, main menu/navigation access, gallery captions, chapter tags, and replay links from the memory viewer. Progress now uses `persistent.max_unlocked_chapter` so replaying an earlier chapter does not erase later unlocks. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `72.9s`, refreshed `69` screenshots, and contact sheet regenerated. Reviewed `00t_chapter_select.png`, `00u_mobile_chapter_select.png`, `00b_memory_gallery.png`, and `00bb_memory_viewer.png`. |
| Ticket 13: Clamp Continue Progress | Complete | Coupled with Ticket 12. Continue now clamps persistent chapter state through a valid chapter helper and jumps through a known label formatter instead of string-concatenating unchecked persistent data. | Covered by Ticket 12 validation: `rtk npm test`, runtime payload scan, static label scan, Ren'Py lint, and visual audit all passed. |
| Ticket 14: Fix Testcase Lint Warning | Complete | Added a small lint anchor before the visual-audit testcase block so Ren'Py no longer reports the testcase as unreachable after the helper label return. No gameplay files were changed. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `22` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with no warnings; visual audit passed in `69.6s` and refreshed `69` screenshots. |
| Ticket 15: Clean Release Artifacts | Complete | Removed all `.DS_Store` metadata files from the project tree, including runtime `game/` asset folders, test screenshot folders, archive folders, and local project metadata folders. `.gitignore` already ignores future `.DS_Store` files. | Exact cleanup scan now returns no `.DS_Store` files. `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `22` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with no warnings; visual audit passed in `69.7s` and refreshed `69` screenshots. |
| Ticket 16: Add Directed Chapter-Specific Transitions | Complete | Added a named directed-transition layer with chapter/scene profiles for lonely, digital, office, gift, date, starlit, page, storm, home, family, promise, vow, and finale beats. Major scene changes now use these profiles, while Reduced Motion collapses them to a short dissolve. | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `22` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with no warnings; visual audit passed in `69.4s`, refreshed `69` screenshots, and contact sheet regenerated. Reviewed `16_ch10_storm_outside.png`, `27b_ch14_vows_cg.png`, and `30_ch15_floating.png`. |

## Implementation Log

| Date | Ticket(s) | Work Completed | Files Updated | Validation Notes |
| --- | --- | --- | --- | --- |
| 2026-05-20 | Ticket 1, Ticket 2 | Added persistent story quick menu, paged dialogue History screen, history retention config, and visual audit coverage for both screens. | `game/screens.rpy`, `game/options.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/00h_quick_menu_story.png`, `tests/screenshots/visual_audit/00i_history.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed, refreshed `52` screenshots, and the quick menu/history screenshots were manually reviewed. |
| 2026-05-20 | Ticket 3 | Added optional memory-interaction maps to Chapters 2, 6, 9, 11, and 12; replaced selected linear hotspots with reveal loops that can be explored in any order and continued after one reveal. | `game/script.rpy`, `game/screens.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/03c_memory_map_ch2.png`, `tests/screenshots/visual_audit/09b_memory_map_ch6.png`, `tests/screenshots/visual_audit/15b_memory_map_ch9.png`, `tests/screenshots/visual_audit/19c_memory_map_ch11.png`, `tests/screenshots/visual_audit/23b_memory_map_ch12.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed, refreshed `57` screenshots, and the five memory-map screenshots were manually reviewed. |
| 2026-05-20 | Ticket 4 | Added low-risk emotional menus to the story, persisted player tone choices, connected selected choices to Chapter 15 callback lines and the final anniversary message, and added a visual-audit preview for the choice UI. | `game/script.rpy`, `game/screens.rpy`, `game/definitions.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/00j_emotional_choice.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed, refreshed `58` screenshots, and the emotional-choice screenshot was manually reviewed after staging it on the Chapter 2 scene background. |
| 2026-05-21 | Ticket 5 | Added mobile/touch-aware layout branches and a forced mobile visual-audit mode. Enlarged touch targets and text for story dialogue, quick menu, main menu, chapter cards, hotspots, memory interactions, choices, gallery, history, preferences, save/load, confirm, and final message screens. | `game/screens.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/00k_mobile_main_menu.png`, `tests/screenshots/visual_audit/00l_mobile_memory_gallery.png`, `tests/screenshots/visual_audit/00m_mobile_choice.png`, `tests/screenshots/visual_audit/00n_mobile_preferences.png`, `tests/screenshots/visual_audit/00o_mobile_save.png`, `tests/screenshots/visual_audit/00p_mobile_final_message.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed, refreshed `64` screenshots, and the mobile preview screenshots were manually reviewed. |
| 2026-05-21 | Ticket 6 | Built the local web payload profile: generated `backgrounds_web` and `images_web/cg` JPEG runtime copies, updated image declarations to use them, excluded original PNG backgrounds/CGs from Ren'Py distribution archives, added reproducible prep/report scripts, and documented the web build command plus current SDK blocker. | `game/definitions.rpy`, `game/options.rpy`, `package.json`, `tools/prepare_web_assets.js`, `tools/report_runtime_payload.js`, `docs/renpy_web_mobile_deployment_plan.md`, `docs/GAME_DIRECTOR_REVIEW.md`, `game/backgrounds_web/`, `game/images_web/cg/`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; `rtk npm run report:payload` reports `75.0M` referenced runtime payload and `0` missing files; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `70.8s` and refreshed `64` screenshots. Manually reviewed the contact sheet plus `03_ch2_social_profile.png`, `27b_ch14_vows_cg.png`, and `00b_memory_gallery.png`. Escalated `web_build` packaged the game but failed while preparing progressive download because Ren'Py Web support is missing from the SDK (`WEB_PATH` is `None`). |
| 2026-05-21 | Ticket 7 | Reworked save/load release presentation: empty slots now have deliberate placeholder art/copy, load slots are disabled when empty, page buttons show the selected page, filled slots show clipped thumbnails, current chapter metadata, playtime, and latest-save state. Added save metadata JSON callbacks and a visual audit filled-save scenario. | `game/screens.rpy`, `game/definitions.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/00e_save.png`, `tests/screenshots/visual_audit/00f_load.png`, `tests/screenshots/visual_audit/00o_mobile_save.png`, `tests/screenshots/visual_audit/00q_filled_save.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `17` labels, `15` static jumps, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `72.9s` and refreshed `65` screenshots. Manually reviewed desktop empty save/load, mobile save, and filled save metadata screenshots. |
| 2026-05-21 | Ticket 8 | Added accessibility-first Preferences controls and presentation modes: Large Text, High Contrast, Reduced Motion, and Self-Voicing. Large text/high contrast now affect dialogue, choices, hotspots, chapter cards, and Preferences; reduced motion removes menu petal drift, chapter-card animation, and hotspot pulse. Desktop sliders now have visible touch-friendly thumbs. | `game/definitions.rpy`, `game/screens.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/00r_accessibility_preferences.png`, `tests/screenshots/visual_audit/00s_accessibility_choice.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `70.2s` and refreshed `67` screenshots. Manually reviewed the high-contrast/large-text Preferences and choice screenshots. |
| 2026-05-21 | Ticket 9 | Rewrote targeted narrative scenes for stronger premium VN voice: Chapter 4 first in-person meeting, Chapter 6 earphones gift, Chapter 8 relationship turn, Chapter 9 morning letters, Chapter 10 conflict repair, Chapter 14 engagement/wedding, and Chapter 15 finale. Added more Aashna dialogue and updated audit sample lines for screenshot coverage. | `game/script.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/05_ch4_office_full.png`, `tests/screenshots/visual_audit/09_ch6_office_gift.png`, `tests/screenshots/visual_audit/17_ch10_storm_inside.png`, `tests/screenshots/visual_audit/27_ch14_wedding.png`, `tests/screenshots/visual_audit/30_ch15_floating.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning and reports `292` dialogue blocks / `2,390` words; visual audit passed in `68.6s` and refreshed `67` screenshots. Manually reviewed representative rewritten scene screenshots for text fit. |
| 2026-05-21 | Ticket 10 | Ran final art-direction QA on the audit contact sheet and adjusted the two clearest staging issues: Chapter 6 earphones prop scale/placement and Chapter 7 restaurant trio composition. Added reusable date-scene transforms for the friend/Prawal/Aashna grouping. | `game/definitions.rpy`, `game/script.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/09_ch6_office_gift.png`, `tests/screenshots/visual_audit/10_ch7_restaurant.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `68.5s` and refreshed `67` screenshots. Manually reviewed the updated prop/date staging plus the wedding frame. |
| 2026-05-21 | Ticket 11 | Added audio scene profiles and cue categories so the mix is directed rather than every sound firing at raw default volume. Replaced raw story `play sound` calls with `play_audio_cue(...)`, applied chapter-level `set_audio_scene(...)`, softened/throttled dialogue tick SFX, and documented cue rules plus remaining web audio work. | `game/audio.rpy`, `game/script.rpy`, `docs/AUDIO_MIX_NOTES.md`, `docs/GAME_DIRECTOR_REVIEW.md` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual/runtime audit passed in `67.3s` and refreshed `67` screenshots. |
| 2026-05-21 | Ticket 12, Ticket 13 | Added the replay layer: Chapter Select with locked/unlocked progress, main menu and navigation access, memory gallery captions, chapter tags, and memory-viewer replay buttons. Added `persistent.max_unlocked_chapter` and clamped Continue/replay label helpers so progress state remains valid. | `game/definitions.rpy`, `game/screens.rpy`, `game/script.rpy`, `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/00t_chapter_select.png`, `tests/screenshots/visual_audit/00u_mobile_chapter_select.png`, `tests/screenshots/visual_audit/00b_memory_gallery.png`, `tests/screenshots/visual_audit/00bb_memory_viewer.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `21` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with the existing `game/testcases.rpy:145` warning; visual audit passed in `72.9s` and refreshed `69` screenshots. Manually reviewed the new chapter select, mobile chapter select, gallery, and memory-viewer replay screenshots. |
| 2026-05-21 | Ticket 14 | Cleared the Ren'Py unreachable-statement lint warning by adding a dedicated lint anchor before the visual-audit testcase declaration. Kept visual audit behavior unchanged. | `game/testcases.rpy`, `docs/GAME_DIRECTOR_REVIEW.md` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `22` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with no warnings; visual audit passed in `69.6s` and refreshed `69` screenshots. |
| 2026-05-21 | Ticket 15 | Removed release-junk `.DS_Store` files from the full project tree, including runtime game folders, test output folders, archive folders, `images-output`, and local metadata directories. Confirmed `.gitignore` already excludes `.DS_Store`. | `.DS_Store` files under project root, `game/`, `tests/`, `archive/`, `images-output/`, and `.qodo/`; `docs/GAME_DIRECTOR_REVIEW.md` | Exact `/usr/bin/find . -name .DS_Store -print` cleanup scan now returns no results. `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `22` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with no warnings; visual audit passed in `69.7s` and refreshed `69` screenshots. |
| 2026-05-21 | Ticket 16 | Added directed chapter-specific transition profiles and replaced major scene changes with named mood transitions: digital screens, office warmth, gifts, dates, starlit turns, letters/pages, storm flash, home/family warmth, promises, vows, and finale light. Reduced Motion now falls back to a short dissolve for these scene transitions. | `game/definitions.rpy`, `game/script.rpy`, `docs/GAME_DIRECTOR_REVIEW.md`, `tests/screenshots/visual_audit/16_ch10_storm_outside.png`, `tests/screenshots/visual_audit/27b_ch14_vows_cg.png`, `tests/screenshots/visual_audit/30_ch15_floating.png`, `tests/screenshots/visual_audit_contact_sheet.png` | `rtk npm test` passed; runtime asset/audio/photo scan found `0` missing files; static label scan found `22` labels, `40` static jumps/calls, and `0` missing targets; Ren'Py lint passed with no warnings; visual audit passed in `69.4s` and refreshed `69` screenshots. Manually reviewed representative storm, vows, and finale frames after the transition pass. |

## Scorecard

| Area | Score out of 10 | Current Observation | Recommended Improvement | Priority |
| --- | ---: | --- | --- | --- |
| UX and player flow | 6.5 | Flow is clear and stable, but the interaction model is mostly "tap hotspot to continue." It does not yet feel authored like a premium VN experience. | Add a persistent quick menu, clearer progress/chapter access, better save prompts, and interaction beats that change presentation or emotional framing. | High |
| Main menu / save-load / settings | 8.4 | Main menu, save/load, and preferences now have touch-aware layout branches and larger mobile controls. Save/load has designed empty states, filled-slot metadata, latest-state styling, and visual audit coverage. Preferences now includes accessibility controls and visible slider thumbs. | Continue with release-device QA, value readouts for sliders, and final visual fit checks on real mobile browsers. | High |
| Dialogue pacing and readability | 7.4 | High-impact chapters now have more concrete sensory detail, less generic explanation, stronger emotional progression, and more active Aashna lines. Some mid-game scenes still need tightening, and the full story needs manual playthrough pacing review. | Continue with a whole-game line edit, tune Chapter 7/11 repetition, and add more authored pauses/expression changes where rewritten beats deserve direction. | High |
| Visual polish and consistency | 7.5 | Art direction is much improved, chapter cards are cleaner, and scenes are generally coherent. Ticket 10 fixed the most obvious prop/staging issues in Chapter 6 and Chapter 7. Some sprite/background integration, contact shadows, and gallery presentation still trail premium standards. | Continue with real-device full-size art review, optional contact-shadow overlays, memory gallery polish, and scene-by-scene lighting tweaks. | High |
| Audio / music / SFX usage | 7.2 | Music, ambience, and SFX exist and now route through scene mix profiles and cue categories. This gives chapter moods, ambience, dialogue ticks, UI confirmations, gifts, pages, rings, and swells clearer volume discipline. All audio is still PCM WAV and needs final web/device testing. | Convert web-safe formats, perform a real headphone/speaker listening pass, replace repetitive generated cues if needed, and test browser audio behavior. | High |
| Transitions, animations, scene direction | 7.2 | Major scene changes now use a named transition direction layer with distinct profiles for digital, office, gift, date, starlit, page, storm, family, wedding, and finale beats. Reduced Motion has a fallback. The next gap is authored pauses, expression changes, and reveal timing inside scenes. | Add camera holds, more expression changes, prop reveal timing, and emotional stingers around the most important dialogue beats. | Medium |
| Choice design and player agency | 5.2 | The story now has five canon-safe emotional choices, optional memory interactions, and a chapter replay layer with visible unlock progress. It still lacks choice journal/scrapbook consequences. | Expand choice consequences into scrapbook notes, replay captions, and ending recap variations without changing the real story. | High |
| Accessibility | 7.4 | The game now has dedicated Large Text, High Contrast, Reduced Motion, and Self-Voicing controls. Dialogue, choices, hotspots, chapter cards, Preferences, and common buttons respond to the new modes, and desktop sliders now expose visible thumbs. | Add real-device accessibility QA, consider dyslexia-friendly font support, expose slider values, and verify self-voicing on target builds. | High |
| Mobile/browser readiness | 6.4 | Core screens now have `small`/`touch`-aware branches and forced mobile screenshot coverage. Runtime backgrounds/CGs now use a much lighter web JPEG profile. Final web export, real browser QA, portrait behavior, and browser audio behavior are still unproven. | Install Ren'Py Web support, produce an HTML5 build, convert audio with a real OGG/Opus encoder, and verify iPhone/iPad/Android browsers. | Critical |
| Technical stability | 8.1 | Core labels and assets validate, Ren'Py lint is warning-free, and local `.DS_Store` release artifacts have been removed. Main risks are generated/local drift, web payload size, and lack of a one-command release validation gate. | Add CI-style validation script, protect local polish from regeneration drift, and keep web build validation reproducible. | Medium |
| Premium feel | 6.8 | The game now has stronger system polish across quick menu, history, accessibility, replay, audio direction, lint cleanliness, release artifact cleanup, and directed transitions. It still needs real-device QA, deeper interaction consequence, and full web build validation. | Focus on HTML5/device QA, choice scrapbook depth, final audio/web compression, and release validation automation. | High |
| Replayability | 6.2 | Chapter Select, memory viewer replay links, gallery captions, chapter tags, optional memory maps, and emotional choices now give players a real replay structure. The next gap is deeper post-game incentives and choice-based scrapbook notes. | Add optional annotations, choice-based scrapbook notes, post-game gallery unlocks, and finale callbacks tied to replayed memories. | Medium |

## Detailed Findings

### UX

- The core flow is easy to understand: main menu, chapter cards, scene, hotspot, next beat. It is stable and does not appear broken in current validation.
- The player flow is less passive after Tickets 3, 4, and 12. Optional memory maps create discovery, five emotional choices add player presence, and Chapter Select/memory replay now gives players a reason to revisit scenes. The remaining gap is deeper consequence and more authored follow-through from those interactions.
- Resolved in Ticket 1: a persistent quick menu now provides Save, Load, History, Skip, Auto, Settings, Menu, and Back access during story reading.
- Resolved in Ticket 13: Continue now clamps persistent chapter state and jumps through a known chapter-label helper instead of unchecked string concatenation.
- Chapter cards are improved after the thumbnail overlap fix. The new centered title plaque is much safer and more premium than the previous side-by-side card. Keep validating long titles and non-16:9 windows.
- Resolved in Ticket 12 first pass: Memory gallery now includes captions, chapter tags, and replay access from the full-photo viewer. It can still grow into a stronger scrapbook with choice notes and post-game unlocks.

### Visual Polish

- The best current visual moments are the main menu, Chapter 4 first-meeting sequence, Chapter 10 storm/reconciliation, Chapter 14 wedding/vows, and the improved chapter cards.
- The game now has a coherent romantic VN palette, but the UI leans heavily on the same dark translucent panel plus gold corner motif. This is consistent, but risks looking template-like if every screen uses the same treatment.
- Sprite/background integration is improved after Ticket 10, especially Chapter 6 prop scale and Chapter 7 trio staging. Some scenes still need final checks for feet placement, scale, contact with ground, rim light direction, and whether characters feel physically located in the space.
- The memory gallery preserves image aspect ratio now, but the grid still feels mechanically arranged. Premium treatment would add stronger captions, date/location tags, better selected state, and a more cinematic full-screen viewer.
- Resolved in Ticket 7: save/load empty slots now use deliberate placeholder copy, filled slots show clipped thumbnails plus chapter/playtime metadata, and the selected page/latest save states are visually clearer.
- Preferences now has a real accessibility section and visible slider thumbs. It still needs value readouts and real device fit checks before release.
- Resolved in Ticket 15: `.DS_Store` release artifacts were removed from the project tree, including runtime asset folders and test/archive folders.

### Narrative

- The emotional spine is strong because it is based on a real relationship. The story has sincerity, specific memories, and a clear progression from discovery to friendship, love, families, wedding, and anniversary.
- Ticket 9 improved the highest-impact chapters with more specific sensory detail, subtext, and scene texture. The remaining writing risk is consistency across the entire script rather than the key scenes alone.
- Aashna's voice is stronger after Ticket 9, especially in Chapters 4, 6, 8, 9, 10, 14, and 15. Chapter 7 and some optional memory beats could still give her more presence.
- The friend in Chapter 7 is now visible, but the scene still reads a little mechanically: the friend exists to justify a line, not to affect the scene. Either give the friend one memorable beat or stage them more quietly as background context.
- Chapter 9 letters now escalate more clearly from uncertainty to routine to commitment. A future polish pass can make each letter visually distinct instead of using the same interaction frame.
- Chapter 11 gift exploration has good personal specificity, but the gift sequence is long and structurally repetitive. Consider making it an optional memory-box interaction with 3-5 selectable keepsakes instead of a linear chain.
- Ticket 4 adds initial finale callback logic based on selected emotional choices. The finale can still hit harder by referencing earlier optional memories, replaying a visual/audio motif, and showing the player's selected emotional lens as part of a scrapbook or recap.

### Audio

- The project has music, ambience, and SFX definitions in `game/audio.rpy`, and chapters use them consistently.
- Ticket 11 added scene mix profiles and cue-category playback, so music/ambience/SFX are now directed by chapter mood and cue purpose rather than raw default playback.
- All audio files are PCM WAV. That is acceptable for local desktop testing, but it is not web/mobile production-ready. The `game/audio` folder is about `31M`; browser load/start behavior needs testing and likely conversion.
- SFX are now split into cue categories: chapter, UI, message, gift, page, ring, and swell. This is a first-pass direction layer, not a substitute for a final listening mix.
- A volume/mix plan now exists in code and in `docs/AUDIO_MIX_NOTES.md`; final loudness normalization still requires real audio-tooling or manual DAW/encoder work.
- Dialogue advance SFX is softened and throttled to reduce fatigue, but it still needs a full playthrough listening check.

### Technical

- Current static validation is good: no missing referenced images/audio, no missing static jump targets, five story menus are detected, and Ren'Py lint now passes with no warnings.
- The main story file is marked auto-generated. Local edits in `game/script.rpy`, `game/definitions.rpy`, and `game/screens.rpy` are intentional, but there is still regeneration risk. Anything that must survive generation should be moved to generator/source or clearly protected.
- Resolved in Ticket 14: the visual-audit testcase no longer triggers Ren'Py's unreachable-statement lint warning.
- `persistent.current_chapter` should be validated before `jump expression`. Clamp to `1...15` or map through a dictionary of valid labels.
- The game has 16 custom screens and many fixed pixel dimensions. This is manageable on desktop but will break or feel cramped on smaller touch screens unless variants are added.
- There is no evidence in this review that a Ren'Py web build has been produced and tested on real browsers/devices.
- Resolved in Ticket 15: no `.DS_Store` files remain in the project tree after cleanup.

### Accessibility

- Desktop dialogue text is readable, but accessibility is not release-level yet.
- Resolved in Ticket 2: a custom History screen now lets VN players re-read recent dialogue.
- Resolved in Ticket 1: the quick menu is now visible during story play.
- Ticket 5 enlarged common touch targets and text in mobile/touch variants. Ticket 8 added explicit Large Text, High Contrast, Reduced Motion, and Self-Voicing access.
- Some interactions rely on keyboard/right-click as shortcuts in modals, with visible buttons also present. That is acceptable for desktop, but mobile/touch needs explicit visible controls everywhere.
- Desktop and mobile sliders now have visible thumbs. The remaining accessibility gap is real-device verification, value readouts, dyslexia-friendly font exploration, and self-voicing QA on target builds.
- Text contrast is generally good against dark panels, but some secondary text uses muted warm colors that may be low contrast on dark translucent backgrounds.

### Mobile

- Ticket 5 added mobile/touch branches for the major screens while preserving the desktop look.
- `config.physical_width = 1280` and `config.physical_height = 720` help local desktop launch, but final mobile readiness still depends on real Ren'Py Web and device testing.
- Memory gallery now has a 2-column touch layout with larger cards and preserved image aspect ratio.
- Save/load now has a 2x3 touch layout with wider horizontal slots and larger page controls.
- Preferences now has a mobile/touch branch with larger buttons and visible slider thumbs.
- Main menu now has a centered touch layout with stacked primary actions and no menu/title overlap in the automated mobile preview.
- Image payload is improved for HTML5 after Ticket 6: opaque backgrounds/CGs now use `18.3M` of JPEG runtime copies instead of `148.2M` of source PNGs. Audio remains heavy at `31.4M` of PCM WAV.
- Remaining mobile risk: this pass is validated through Ren'Py forced mobile preview screenshots, not real iPhone/iPad/Android browser builds.

### Premium Feel

- The game now has premium-looking pieces and the first layer of emotional interactivity, but it does not yet feel fully premium because the supporting systems are still shallow.
- A paid VN needs more than clean art: it needs confident flow, tactile controls, authored pauses, UI responsiveness, save/history/skip polish, optional depth, and emotionally meaningful interaction.
- The current game has a personal story worth preserving. The premium upgrade should not add fake branching that changes the truth; it should add perspective, reflection, optional memories, and presentation consequence.
- Ticket 16 adds the first pass of authored transition language, so chapter shifts now feel more scene-directed and less like repeated generic fades.
- The biggest premium opportunity remains turning each chapter from "scene plus click gate" into a directed memory: inspect object, hear a line, reveal photo/CG, choose emotional framing, then transition. Tickets 3 and 4 establish the pattern; future passes should make it feel more authored and less modular.

## Recommended Update Backlog

### Ticket 1: Add a Persistent Quick Menu

- Title: Add premium in-story quick menu
- Problem: Players cannot quickly access Save, Load, History, Auto, Skip, Preferences, or Main Menu during normal reading.
- Recommended Fix: Add a restrained quick menu overlay or bottom/top-right icon strip that appears during story screens and hides during chapter cards/final modal.
- Files likely impacted: `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy`
- Acceptance Criteria: During any dialogue scene, player can tap/click Save, Load, History, Auto, Skip, Settings, and Return without keyboard/right-click; quick menu does not overlap dialogue or hotspots.
- Priority: Critical

### Ticket 2: Add Dialogue History Screen

- Title: Implement premium history/log screen
- Problem: No visible history screen exists, making accidental taps and replay reading frustrating.
- Recommended Fix: Add a custom `history` screen matching current UI style, with scrollable dialogue entries, speaker names, and touch scrolling.
- Files likely impacted: `game/screens.rpy`, `game/gui.rpy`
- Acceptance Criteria: History opens from quick menu and preferences/navigation, scrolls with mouse/touch, and preserves readability on desktop and mobile.
- Priority: Critical

### Ticket 3: Convert Decorative Hotspots Into Meaningful Memory Interactions

- Title: Make hotspots emotionally meaningful
- Problem: Hotspots are mandatory continue buttons with scene-specific labels, not actual agency.
- Recommended Fix: For selected chapters, make hotspots reveal optional object text, alternate closeups, or memory fragments before the player proceeds.
- Files likely impacted: `game/script.rpy`, `game/screens.rpy`, `game/definitions.rpy`, possibly `game/story.json`
- Acceptance Criteria: At least Chapters 2, 6, 9, 11, and 12 contain optional interaction reveals that can be explored in any order or skipped after minimum progress.
- Priority: Critical

### Ticket 4: Add Low-Risk Emotional Choices

- Title: Add truthful player agency without changing canon
- Problem: Resolved baseline issue: the game previously had no Ren'Py `menu` choices, so replayability and player presence were weak.
- Recommended Fix: Complete for first pass. Keep expanding choices so they affect tone, memory captions, scrapbook notes, and final callback text rather than changing real events.
- Files likely impacted: `game/script.rpy`, `game/story.json`, `game/screens.rpy`
- Acceptance Criteria: Complete for first pass: 5 choices exist across the story, choices influence small callbacks/final message wording, and no canon event changes.
- Priority: Critical

### Ticket 5: Mobile Variant Pass

- Title: Build `small` and `touch` screen variants
- Problem: Resolved baseline issue: the UI previously used fixed desktop layouts for major screens and did not have mobile/touch branches.
- Recommended Fix: Complete for first pass. Continue by validating the new branches in actual HTML5 builds on target devices.
- Files likely impacted: `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy`
- Acceptance Criteria: Complete for automated layout preview: core screens have `small`/`touch` branches and mobile visual-audit screenshots show no obvious clipped text or unreachable buttons. Real iPhone, iPad, Android Chrome, and desktop browser testing remains required under Ticket 6.
- Priority: Critical

### Ticket 6: Web Payload Optimization

- Title: Prepare assets and audio for HTML5
- Problem: Art and audio payloads are large; all audio is WAV PCM.
- Recommended Fix: Create a web asset profile: convert audio to OGG/Opus where Ren'Py Web supports it, compress PNGs safely, and test browser load/memory.
- Files likely impacted: `game/audio/`, `game/backgrounds_ai/`, `game/images_ai/`, `game/sprites_ai/`, `game/options.rpy`, build scripts/docs
- Acceptance Criteria: Web build loads reliably on target mobile browsers; visual quality remains high; audio starts after user gesture; payload size is documented.
- Priority: Critical

### Ticket 7: Save/Load Screen Release Polish

- Title: Upgrade save/load empty states and metadata
- Problem: Resolved baseline issue: empty save slots previously showed large black preview boxes, making the screen feel unfinished.
- Recommended Fix: Complete for first pass. Keep validating filled real-user slots during manual QA and improve further if players need delete/overwrite affordances.
- Files likely impacted: `game/screens.rpy`, `game/definitions.rpy`, `game/testcases.rpy`
- Acceptance Criteria: Complete: empty slots look designed, filled slots show chapter/playtime/thumbnail metadata, current page/latest state is visible, empty load slots are disabled, and touch targets remain large.
- Priority: High

### Ticket 8: Preferences Accessibility Upgrade

- Title: Add accessibility-first preferences
- Problem: Resolved baseline issue: Preferences previously lacked large text, high contrast, reduced motion, self-voicing access, and touch-friendly desktop slider thumbs.
- Recommended Fix: Complete for first pass. Keep validating on real devices and add value readouts/dyslexia-friendly font support if needed.
- Files likely impacted: `game/screens.rpy`, `game/definitions.rpy`, `game/testcases.rpy`
- Acceptance Criteria: Complete: player can enable large text/high contrast/reduced motion, self-voicing is exposed, desktop/mobile sliders have visible thumbs, and large-text/high-contrast states are covered by visual audit screenshots.
- Priority: High

### Ticket 9: Dialogue Rewrite Pass for Subtext and Voice

- Title: Rewrite narration for specificity and reciprocal voice
- Problem: Resolved first-pass issue: the most important emotional scenes were sincere but often direct, generic, and Prawal-heavy.
- Recommended Fix: Complete for first pass. Continue with a whole-game line edit later, especially Chapter 7 friend/date context and Chapter 11 gift rhythm.
- Files likely impacted: `game/script.rpy`, `game/testcases.rpy`
- Acceptance Criteria: Complete: Chapters 4, 6, 8, 9, 10, 14, and 15 have stronger scene-specific language; Aashna has more active lines; no continuity regressions found in automated validation.
- Priority: High

### Ticket 10: Final Art Direction QA

- Title: Art consistency and staging pass
- Problem: Resolved first-pass issue: Chapter 6 prop scale and Chapter 7 friend/date staging were the clearest non-premium composition problems in the audit sheet.
- Recommended Fix: Complete for first pass. Continue with a future full-device art review for contact shadows, lighting polish, and gallery presentation.
- Files likely impacted: `game/definitions.rpy`, `game/script.rpy`, `game/testcases.rpy`
- Acceptance Criteria: Complete: contact sheet refreshed, Chapter 6 earphones no longer read as oversized foreground paste-up, Chapter 7 friend is staged as supporting context, and no new clipping/missing-asset regressions were found.
- Priority: High

### Ticket 11: Audio Mix and Cue Direction Pass

- Title: Professional audio cue and mix pass
- Problem: Resolved first-pass issue: audio existed but cue playback was broad and undirected, with most SFX fired at default channel volume.
- Recommended Fix: Complete for first pass. Continue with compressed audio conversion, manual headphone/speaker listening, and browser audio testing after Ren'Py Web support is installed.
- Files likely impacted: `game/audio.rpy`, `game/script.rpy`, `docs/AUDIO_MIX_NOTES.md`
- Acceptance Criteria: Complete for runtime direction: scene profiles and cue categories are implemented, no ambience leaks were detected by automated chapter sweep, and runtime audit passes. Web/mobile format verification remains blocked by the web build/tooling pass.
- Priority: High

### Ticket 12: Chapter Select and Replay Hub

- Title: Add chapter select and memory replay structure
- Problem: Resolved first-pass issue: replayability was weak because Continue only resumed the current chapter and gallery was passive.
- Recommended Fix: Complete for first pass. Continue by adding choice-based scrapbook notes, optional annotations, and post-game gallery incentives.
- Files likely impacted: `game/screens.rpy`, `game/script.rpy`, `game/definitions.rpy`
- Acceptance Criteria: Complete: player can replay unlocked chapters from the menu/gallery, progress state is visible, locked chapters are clear, and no sequence break bugs were found in automated validation.
- Priority: Medium

### Ticket 13: Clamp Continue Progress

- Title: Harden `continue_game`
- Problem: Resolved: unchecked persistent progress could jump to invalid chapter labels.
- Recommended Fix: Complete. Keep this helper path for future chapter/replay links.
- Files likely impacted: `game/script.rpy`
- Acceptance Criteria: Complete: persistent chapter state is clamped to `1...15` and Continue/replay jumps use the shared helper.
- Priority: Medium

### Ticket 14: Fix Testcase Lint Warning

- Title: Remove unreachable testcase warning
- Problem: Resolved: Ren'Py lint reported unreachable statements for the visual-audit testcase block.
- Recommended Fix: Complete. Keep testcase helper labels separated from executable testcase declarations.
- Files likely impacted: `game/testcases.rpy`
- Acceptance Criteria: Complete: Ren'Py lint passes with no warnings and visual audit still passes.
- Priority: Medium

### Ticket 15: Clean Release Artifacts

- Title: Remove non-runtime junk files from build
- Problem: Resolved: `.DS_Store` files existed under runtime and project support folders, and release builds should not include local OS artifacts.
- Recommended Fix: Complete. Keep `.DS_Store` ignored and rerun cleanup before packaging if macOS Finder recreates metadata files.
- Files likely impacted: `.DS_Store` files under project root, `game/`, `tests/`, `archive/`, `images-output/`, and `.qodo/`
- Acceptance Criteria: Complete: no `.DS_Store` files remain in the project tree.
- Priority: Low

### Ticket 16: Add Directed Chapter-Specific Transitions

- Title: Make each chapter transition feel authored
- Problem: Resolved first-pass issue: most scene direction used similar fades/dissolves, which became repetitive.
- Recommended Fix: Complete for transition layer. Continue with authored pauses, expression changes, prop reveal timing, and emotional stingers.
- Files likely impacted: `game/definitions.rpy`, `game/script.rpy`, `game/audio.rpy`
- Acceptance Criteria: Complete: major chapters have distinct but restrained transition language, and Reduced Motion routes them through a short dissolve.
- Priority: Medium

## Quick Wins

- Add a visible quick menu with Save, Load, History, Auto, Skip, Settings, Return.
- Clamp `persistent.current_chapter` before dynamic continue jump.
- Keep `.DS_Store` files out of release packages.
- Keep Ren'Py lint warning-free as new testcases are added.
- Run `.DS_Store` cleanup before release packaging if Finder recreates local metadata.
- Add delete/overwrite affordance polish for filled save slots if manual QA shows players need it.
- Add Preferences value readouts for text speed, auto-forward, music, and sound.
- Add real-playthrough QA for filled save slots after manual saves exist.
- Add a Chapter Select button to main menu after progress exists.
- Review the five new emotional choices during a full playthrough and tune copy where a choice feels too similar or too abstract.
- Rewrite Chapter 9 letters to escalate emotionally instead of repeating the same structure.
- Convert at least SFX from WAV PCM to a web-safe compressed format and compare load size.
- Add a web build checklist result section after real browser testing.

## Premium Polish Roadmap

Phase status summary:

- Phase 1 is partially complete. Local UI, accessibility, replay, lint, artifact cleanup, visual audit, and implementation validation items are complete; real Ren'Py Web builds, browser/device QA, manual real-save QA, and full manual playthrough validation remain open.
- Phase 2 is partially complete. Chapter select, high-impact dialogue rewrite, first-pass audio direction, first-pass scene transition direction, and asset web JPEG preparation are complete; audio compression, real-device accessibility QA, manual save QA, final audio listening, and browser validation remain open.
- Phase 3 is mostly open. Some scrapbook/replay groundwork exists through gallery captions and chapter links, but premium recap, Aashna perspective unlocks, title/logo asset, deeper reduced-motion-safe scene depth, localization readiness, and automated release QA are not complete.

### Phase 1: Must Fix Before Demo

- Add quick menu and history screen.
- Add first-pass accessibility settings for large text, high contrast, reduced motion, and self-voicing.
- Validate the new mobile/touch variants in actual Ren'Py Web builds on iPhone, iPad, Android, Chrome, and Safari.
- Keep Continue progress clamped and preserve the warning-free lint baseline.
- Preserve the clean release-artifact baseline; no `.DS_Store` files should ship.
- Validate save/load with manual real-user saves after the automated filled-slot audit.
- Validate the new emotional choices and optional memory interactions in a real playthrough so the demo feels playable, not only clickable.
- Run full visual audit after these changes and review every screenshot at full size.
- Produce one local Ren'Py web build and verify it launches in desktop Chrome/Safari.

### Phase 2: Polish Before Public Release

- Convert/compress audio and image assets for HTML5 while preserving premium visual quality.
- Test on iPhone Safari, iPad Safari, Android Chrome, desktop Chrome, and desktop Safari.
- Add chapter select and unlocked replay flow.
- Rewrite high-impact dialogue chapters for specificity, subtext, and stronger Aashna voice.
- QA accessibility modes on real target devices; add value readouts and optional dyslexia-friendly font support if needed.
- Add more authored scene direction: camera holds, pauses, expression changes, prop reveals, and emotional stingers.
- Run manual real-save QA across desktop and web/mobile builds once Ren'Py Web support is installed.
- Finalize audio mix, cue timing, and ambience transitions.

### Phase 3: Premium Upgrades

- Turn memory gallery into a scrapbook: captions, dates, emotional notes, chapter links, and unlock states.
- Add a final recap that references player-selected memories or choices.
- Add optional "Aashna perspective" interludes or post-game unlocks to strengthen reciprocity.
- Add premium title treatment/logo asset instead of text-only title lockup.
- Add animated but reduced-motion-safe background depth on selected scenes.
- Add localization-ready text structure if the project may expand later.
- Add automated release QA script: source check, asset/audio reference scan, lint, visual audit, contact sheet, and web build smoke test.
