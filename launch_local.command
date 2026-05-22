#!/bin/bash
set -euo pipefail

SDK_ROOT="/Users/prawalsharma/Applications/renpy-8.5.2-sdk"
RUNNER="$SDK_ROOT/renpy.sh"
PROJECT_PATH="/Users/prawalsharma/Documents/Projects/anniversary-renpy"

if [ ! -x "$RUNNER" ]; then
  echo "Ren'Py runner not found at: $RUNNER"
  echo "Install or copy Ren'Py SDK to that location, then retry."
  exit 1
fi

if [ ! -d "$PROJECT_PATH" ]; then
  echo "Project folder not found at: $PROJECT_PATH"
  exit 1
fi

if [ ! -d "$PROJECT_PATH/game" ]; then
  echo "Game folder not found at: $PROJECT_PATH/game"
  exit 1
fi

rm -f "$PROJECT_PATH"/game/*.rpyc
rm -f "$PROJECT_PATH"/game/cache/*

if command -v node >/dev/null 2>&1 && [ -f "$PROJECT_PATH/tools/remove_checkerboard_bg.js" ]; then
  (
    cd "$PROJECT_PATH"
    if [ -f "tools/generate_audio_assets.js" ] && [ ! -f "game/audio/music/forever_theme.wav" ]; then
      node tools/generate_audio_assets.js >/dev/null
    fi
    node tools/remove_checkerboard_bg.js >/dev/null
  )
fi

"$RUNNER" "$PROJECT_PATH"
