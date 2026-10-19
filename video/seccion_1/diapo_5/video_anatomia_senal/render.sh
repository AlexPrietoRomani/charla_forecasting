#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo ../../../../..)"
PY="$ROOT/.venv/bin/python"
[ -x "$PY" ] || PY=python3

FPS=30
DUR_MS=34000
START_MS=0
TIME_SCALE=1
DPR=1.2

FRAMES="$(mktemp -d /tmp/anatomia_senal_frames.XXXXXX)"
trap 'rm -rf "$FRAMES"' EXIT

"$PY" build_scene.py
node capture.mjs scene.html "$FRAMES" "$FPS" "$DUR_MS" "$START_MS" "$TIME_SCALE" "$DPR"
ffmpeg -y -loglevel error -framerate "$FPS" -i "$FRAMES/f%05d.png" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart \
  anatomia_senal.mp4
echo "OK → anatomia_senal.mp4 ($(du -h anatomia_senal.mp4 | cut -f1))"
