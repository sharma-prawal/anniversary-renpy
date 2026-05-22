# Final HTML5 Release Polish Checklist

Last updated: 2026-05-22

This document preserves the HTML5 polish/readiness work completed before the release target pivot. HTML5 deployment is paused for now; the active release direction is an itch.io upload using standard Ren'Py distributable builds.

- `docs/PREMIUM_UX_AUDIT.md`
- `docs/GAME_DIRECTOR_REVIEW.md`
- `docs/renpy_web_mobile_deployment_plan.md`
- `docs/dialogue_ux_flow_polish_roadmap.md`
- `docs/premium_polish_roadmap.md`
- `docs/AUDIO_MIX_NOTES.md`

## Current Release Read

The game is now a polished, premium-looking personal romance VN with custom UI, chapter select, save/load polish, accessibility toggles, mobile-preview layouts, memory interactions, player-choice echoes, cinematic CG treatment, streamer-friendly peak captions, and a stronger title identity.

HTML5 is paused before final device QA. Completed HTML5 work should be preserved, but the next release work should focus on desktop Ren'Py distributables for itch.io.

## Active Release Direction: Itch Ren'Py Distributable

| Priority | Item | Done When |
| --- | --- | --- |
| P0 | Build desktop distributions from Ren'Py Launcher / SDK | Windows, macOS, and Linux packages are generated from the latest polished project. |
| P0 | Run full desktop playthrough | New Game through finale, save/load, chapter select, memory gallery, choices, final recap, and Play Again all work. |
| P0 | Validate packaged payload | Test labels/screenshots/docs/tools/web build artifacts are excluded; runtime assets/audio are present. |
| P0 | Itch upload preparation | Build zips are named clearly, itch page copy/screenshots are ready, and install/run notes are documented. |

## Non-Negotiable Device Parity Goal

The HTML5 build must feel like one polished game everywhere, not separate compromised versions. Laptop/desktop, iPad, Android, and iPhone players should all be able to finish the full story with the same content, choices, audio intent, save/load flow, gallery/replay access, accessibility options, and final recap.

| Device Class | Required Browser/Mode | Parity Requirement |
| --- | --- | --- |
| Laptop / desktop | Chrome and Safari, keyboard + mouse/trackpad | Full 16:9 layout, readable UI, hover states readable, keyboard/mouse controls work, no black-bar or scaling artifacts. |
| iPad | Safari touch browser | Full story playable by touch, no cropped panels, no unreachable buttons, gallery/save/preferences scroll correctly, orientation/viewport behavior is stable. |
| Android | Chrome touch browser on phone and tablet where available | Full story playable by touch, audio unlock works, scrolling and modals work, no browser-specific missing assets or canvas scaling issues. |
| iPhone | Safari touch browser | Full story playable by touch in the constrained viewport, dialogue/choices remain readable, all Back/Close/Continue controls are visible, no required hover/right-click/keyboard path. |

If any one of these device classes cannot complete the full story cleanly, the HTML5 release is not ready.

## Active Pass Tracking

| Pass | Status | Latest Result | Next Action |
| --- | --- | --- | --- |
| Baseline validation | Complete | `rtk proxy npm test`, payload report, Ren'Py lint, and visual audit passed. Current referenced runtime payload is `47.9M` with `0` missing referenced files after MP3 audio conversion. | Keep this green after every release-readiness change. |
| Web support / HTML5 build | Complete for local smoke | Installed official Ren'Py Web support into the local `renpy-8.5.2-sdk/web` folder. `web_build` now completes and the generated `index.html` returns HTTP 200 from a local static server. | Keep using fresh timestamped/session output folders for release-candidate builds. |
| Web package exclusions | Complete for first pass | Added build exclusions for `tests/`, `archive/`, `images-output/`, `docs/`, `tools/`, `node_modules/`, package files, `game/testcases.rpy`, and runtime WAV files. Current local web smoke output is `111.9M` total, with `game.zip` at `5.4M` and progressive files/assets outside the zip. | Keep checking release-candidate output for accidental debug/test payloads. |
| Audio strategy | Complete for local smoke | Installed `ffmpeg`, converted runtime audio from WAV to MP3, updated `game/audio.rpy`, and added `npm run convert:audio-web` for repeatability. Referenced audio dropped from `31.4M` to `4.3M`; the web output contains `26` MP3s and `0` WAVs. | Confirm audio unlock and audible music/ambience/SFX on real target browsers during device QA. |
| Real device parity QA | Paused | Latest mobile-polished HTML5 build included branded web presplash, hidden Ren'Py web hamburger, phone-only rotate hint, MP3 audio, and raised choice panels to avoid dialogue overlap. Local QA server has been stopped. | Resume only if HTML5/web release becomes active again. |
| Manual full browser playthrough | Paused | Browser flow was ready for validation, but HTML5 release is no longer the current target. | Replace with desktop distributable playthrough for itch release. |

## Latest Preserved HTML5 Work Before Pause

- Installed official Ren'Py Web support into the local SDK and produced successful local web builds.
- Added package exclusions for non-runtime folders/files and WAV runtime audio.
- Converted runtime audio references to MP3; payload report is `47.9M` referenced assets with `0` missing files.
- Added repeatable scripts: `npm run convert:audio-web`, `npm run generate:web-presplash`, and `npm run patch:web-shell`.
- Generated branded `game/web-presplash.jpg`.
- Patched generated web shell to hide the Ren'Py hamburger menu, use `#050007`, and show rotate guidance only on phone-width portrait screens.
- Raised custom choice panels so options no longer overlap the dialogue window on phone/tablet screenshots.
- Stopped the local QA server on port `8765`.

## Hard Blockers Before HTML5 Deployment

| Priority | Item | Why It Matters | Done When |
| --- | --- | --- | --- |
| P0 | Install Ren'Py Web support in the local SDK | Current web build is blocked because `WEB_PATH` is `None`. | Ren'Py launcher has web support installed and `web_build` produces a complete static web folder. |
| P0 | Produce a real HTML5 build | Forced mobile screenshots are not a substitute for an actual browser build. | Build completes, launches locally, and can be served from a static HTTP server. |
| P0 | Test real target browsers/devices | Mobile/browser readiness is still inferred, not proven. | Verified on laptops/desktops, iPad Safari, Android Chrome, and iPhone Safari with the same story and feature coverage. |
| P0 | Convert or validate audio for web | Browser audio must be small enough for mobile and compatible with Safari/Chrome. | MP3 runtime audio is generated, referenced, packaged without WAVs, and ready for real-device audio unlock testing. |
| P0 | Verify browser audio unlock/autoplay behavior | Web builds often require a user gesture before audio can play. | Music, ambience, and SFX start predictably after first interaction on all target browsers. |

## Final Web Build Commands

Run from the repository root, with `rtk` prefix.

```bash
rtk proxy npm test
rtk proxy npm run report:payload
rtk proxy npm run generate:web-presplash
rtk proxy /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.sh . lint
rtk proxy /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.sh . test --overwrite-screenshots visual_audit
rtk proxy /Users/prawalsharma/Applications/renpy-8.5.2-sdk/renpy.sh /Users/prawalsharma/Applications/renpy-8.5.2-sdk/launcher web_build /Users/prawalsharma/Documents/Projects/anniversary-renpy --destination /path/to/web-output
rtk proxy npm run patch:web-shell -- /path/to/web-output
```

If the web build fails with `WEB_PATH` as `None`, install Ren'Py Web support from the Ren'Py launcher and rerun the build.

## Paused HTML5 QA Checklist

### HTML5 Build and Hosting

- [x] Web build completes without `WEB_PATH` / progressive download errors.
- [x] Generated output runs from a local static server, not only from `file://`.
- [x] Page background / letterbox color matches `#050007`.
- [ ] 16:9 game frame fits without cropping UI on phones/tablets.
- [ ] Desktop browser resizing does not expose ugly black bars or clipped UI.
- [ ] Loading time is acceptable on mobile network conditions.
- [ ] Browser console has no missing asset or audio errors.

### Real Device Coverage

- [ ] Laptop/Desktop Chrome: full story, keyboard/mouse, resize behavior, audio, save/load, gallery, chapter select, final modal.
- [ ] Laptop/Desktop Safari: full story, keyboard/mouse, resize behavior, audio, save/load, gallery, chapter select, final modal.
- [ ] iPad Safari: full story by touch, orientation/viewport behavior, scrolling, modals, audio unlock, save/load, gallery, chapter select.
- [ ] Android Chrome: full story by touch, audio unlock, scrolling, modals, save/load, gallery, chapter select, no missing/cached asset issues.
- [ ] iPhone Safari: full story by touch in constrained viewport, readable dialogue/choices, visible controls, save/load, gallery, chapter select, final modal.
- [ ] Cross-device parity check: content, choices, recap, chapter unlocks, memory notes, and accessibility options behave the same across all tested devices.

### Audio

- [x] Decide final web audio format strategy.
- [x] Convert WAVs only with a reliable encoder (`ffmpeg`, `opusenc`, or `oggenc`) and verify Ren'Py compatibility.
- [x] Re-run payload report after audio conversion.
- [ ] Manual headphone pass: dialogue tick, music, ambience, and SFX balance.
- [ ] Manual speaker pass: music/ambience does not bury dialogue.
- [ ] Storm, wedding, finale, and peak-caption cue levels feel intentional.
- [ ] No ambience leaks between chapters after replay/chapter select.

### Manual Playthrough

- [ ] New game full playthrough from cold open to finale.
- [ ] Continue from mid-game save.
- [ ] Load filled save slots with metadata.
- [ ] Replay earlier chapters from Chapter Select without losing unlock progress.
- [ ] Memory Gallery replay links work for unlocked chapters.
- [ ] All five emotional choices set and reflect correctly in chapter annotations, memory notes, and finale recap.
- [ ] Final message and Play Again return flow work.

## P1 Polish Before Public Link

### Story and Dialogue

- [ ] Full line edit for over-explained narration; remove repeated emotional summaries where scene action already carries the feeling.
- [ ] Re-check Chapter 6 earphones continuity: Aashna is sad/almost crying, not laughing it off.
- [ ] Re-check Chapter 7 friend/date context so the friend feels authored, not patched.
- [ ] Re-check Chapter 9 letters for emotional escalation; avoid repeated letter structure.
- [ ] Re-check Chapter 11 keepsake sequence so each item has a distinct emotional rhythm.
- [ ] Confirm no visual-audit/test labels leak into playable copy.

### UI and Identity

- [ ] Review main menu at full size after latest identity lockup; ensure it feels player-facing, not like internal art-direction text.
- [ ] Review mobile main menu after identity changes for overlap/crowding.
- [ ] Review chapter cards after the `scene black` transition fix; ensure no previous frame flashes.
- [ ] Add Preference value readouts for text speed, auto-forward, music, ambience, and SFX if there is time.
- [ ] Consider Continue microcopy: "Continue from Chapter X" / "Previously: ..." if it can stay elegant.
- [ ] Verify hover text remains readable on all button hover states.

### Accessibility

- [ ] Real-device Large Text QA.
- [ ] Real-device High Contrast QA.
- [ ] Real-device Reduced Motion QA.
- [ ] Self-voicing smoke test.
- [ ] Confirm secondary warm text is still readable on translucent dark panels.
- [ ] Confirm every modal has visible Back/Close controls on touch devices.

### Save/Load

- [ ] Manual save into empty slot.
- [ ] Overwrite filled slot.
- [ ] Load filled slot.
- [ ] Check latest-save state.
- [ ] Confirm empty load slots are disabled.
- [ ] Decide whether delete/overwrite affordance needs additional polish.

## P2 Optional Premium Upgrades

These are not required for the first HTML5 deployment, but they are the strongest next refinements if there is more time.

- [ ] Turn Memory Gallery into a fuller scrapbook: dates, notes, unlock states, choice reflections, and stronger selected-state drama.
- [ ] Add optional Aashna-perspective interludes or post-game unlocks.
- [ ] Add real logo/capsule art asset beyond the current text-based title lockup.
- [ ] Add reduced-motion-safe background depth to selected scenes: light drift, rain intensity shifts, object glints, subtle parallax.
- [ ] Add controller / Steam Deck focus styling if Steam remains a target.
- [ ] Add automated release QA script that runs source check, payload report, lint, visual audit, contact sheet, and web smoke test.

## Regeneration and Source-of-Truth Risk

`game/script.rpy` is marked generated, but several final polish fixes currently live in local Ren'Py files. Before any regeneration:

- Prefer story/dialogue changes in `../anniversary-game/src/data/story.json`.
- Preserve intentional local polish in:
  - `game/screens.rpy`
  - `game/definitions.rpy`
  - `game/polish.rpy`
  - `game/audio.rpy`
  - `game/testcases.rpy`
- Re-check local-only edits in `game/script.rpy`, especially:
  - Pass 8 peak caption beats.
  - Chapter 6 earphones sadness correction.
  - Player-choice presentation callbacks.
- If regeneration becomes necessary, either move these edits into the source/generator path or re-apply them after generation.

## Final Screenshot Review Set

Before publishing a web link, manually review these at full size:

- Main menu: `00_main_menu.png`, `00k_mobile_main_menu.png`
- Chapter select: `00t_chapter_select.png`, `00u_mobile_chapter_select.png`
- Choice UI: `00j_emotional_choice.png`, `00m_mobile_choice.png`
- Save/load: `00e_save.png`, `00f_load.png`, `00o_mobile_save.png`, `00q_filled_save.png`
- Accessibility: `00r_accessibility_preferences.png`, `00s_accessibility_choice.png`
- Chapter cards: `00a_chapter_card.png`, `00aa_chapter_card_ch1.png`, `00ab_chapter_card_ch5.png`, `00ac_chapter_card_ch14.png`
- Pass 8 peaks: `39_peak_first_meeting.png`, `40_peak_storm_reconciliation.png`, `41_peak_wedding_vow.png`
- Keepsake box: `19c_keepsake_box_ch11.png`
- Finale: `00g_final_message.png`, `00p_mobile_final_message.png`, `34_cinematic_say_ch15_finale.png`

## Release Gate

Do not deploy the public HTML5 build until all P0 items are complete, including laptop, iPad, Android, and iPhone parity.

If P0 is complete and only P1/P2 items remain, the game is acceptable for a controlled private/beta web link. For a public paid launch, complete P1 as well and document the device QA results in this file.
