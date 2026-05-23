# Audio Mix Notes

## Current Pass

The runtime audio pass now uses two small direction helpers in `game/audio.rpy`:

- `set_audio_scene(profile)` sets music and ambience balance per chapter mood.
- `play_audio_cue(clip, cue)` applies cue-category volume before playing SFX.

## Scene Mix Profiles

- `lonely_room`: restrained music, quiet city ambience.
- `digital`: lighter music, low digital-room ambience.
- `office`: warm music, low office ambience.
- `date`: slightly fuller music, restaurant ambience under dialogue.
- `starlit`: fuller emotional music, low garden ambience.
- `letters`: gentler music, low home ambience.
- `storm`: stronger music and rain, but rain stays below dialogue.
- `home`: warm music and ambience for gift scenes.
- `family`: warm music with subtle home ambience.
- `wedding`: stronger music, restrained hall ambience.
- `finale`: strongest emotional music, minimal ambience.

## Cue Rules

- `chapter`: quiet chapter-card reveal, not a loud sting.
- `ui`: subtle confirmation only for meaningful touch/hotspot actions.
- `message`: notification and social app actions.
- `gift`: object reveal or opening cue.
- `page`: letters, books, and family notes.
- `ring`: engagement/wedding ring emphasis.
- `swell`: major emotional peaks only.

## Voice Generation

- Ren'Py voice support is enabled for Prawal, Aashna, and narrator dialogue.
- `tools/voice_config.json` controls Edge TTS voice, rate, pitch, and volume defaults per speaker role.
- `npm run generate:voice-manifest` scans `game/script.rpy` and writes `game/audio/voice/manifest.json` without contacting Edge TTS.
- `npm run generate:voice` generates missing voice files through the Edge TTS CLI, warms and converts them to OGG with FFmpeg, then injects `voice "audio/voice/..."` statements into `game/script.rpy`.
- Normal `npm run generate` only re-injects voices when a manifest and generated voice assets already exist; it does not make networked TTS calls.
- The dialogue advance tick is skipped while the Ren'Py voice channel is playing so spoken lines stay clean.
- The current premium voice pass uses expressive/caring neural voices where available, slower romantic SSML `prosody`, subtle deterministic line-by-line rate/pitch variation, and TTS-only text cleanup for symbols and ellipses. The Edge read-aloud endpoint rejected `mstts:express-as`, `emphasis`, and `break` tags for the selected voices, so emotional warmth and pacing are handled through expressive voice selection plus accepted prosody shaping.
- Generated `voice sustain` and `voice_line_pause()` statements keep fast clicks from chopping off audio between adjacent lines and add a short cinematic breath between voiced lines.
- Preferences include master voice volume, per-character volume/mute/test controls, a Wait Voice toggle for auto-forward, and Replay Voice.
- Final runtime voice assets are warmed OGG files. FFmpeg applies gentle high/low-pass filtering, warmth around 180 Hz, mild presence taming, light compression, loudness normalization, and 44.1 kHz resampling.

## Remaining Release Work

- Convert WAV assets to web-safe compressed formats once a reliable encoder is available.
- Test browser autoplay/user-gesture behavior in the final Ren'Py Web build.
- Do manual headphone/speaker listening passes for music-vs-dialogue balance.
- Consider replacing repeated generated SFX with bespoke cues if the same texture becomes noticeable during full playthrough.
