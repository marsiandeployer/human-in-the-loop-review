#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

timeout 90s node scripts/capture-demo-screenshots.js

convert logs/visual-bug-full.png -crop 420x250+230+92 +repage logs/visual-bug-crop.png
convert logs/visual-fix-full.png -crop 420x250+230+92 +repage logs/visual-fix-crop.png

convert -size 640x400 canvas:'#0f172a' \
  \( logs/visual-bug-crop.png -resize 280x166 -background white -gravity center -extent 280x166 -bordercolor '#ef4444' -border 4 \) \
  -geometry +24+118 -composite \
  \( logs/visual-fix-crop.png -resize 280x166 -background white -gravity center -extent 280x166 -bordercolor '#22c55e' -border 4 \) \
  -geometry +332+118 -composite \
  -font DejaVu-Sans-Bold -fill '#f8fafc' -pointsize 30 \
  -annotate +104+64 'Before' \
  -annotate +426+64 'After' \
  -font DejaVu-Sans -fill '#cbd5e1' -pointsize 16 \
  -annotate +58+360 'Overflowing button label' \
  -annotate +374+360 'Button resized to fit label' \
  demo/chrome-store-before-after-640x400.png

convert -size 1280x800 canvas:'#0f172a' \
  \( logs/visual-bug-crop.png -resize 560x333 -background white -gravity center -extent 560x333 -bordercolor '#ef4444' -border 8 \) \
  -geometry +56+220 -composite \
  \( logs/visual-fix-crop.png -resize 560x333 -background white -gravity center -extent 560x333 -bordercolor '#22c55e' -border 8 \) \
  -geometry +656+220 -composite \
  -font DejaVu-Sans-Bold -fill '#f8fafc' -pointsize 58 \
  -annotate +210+110 'Before' \
  -annotate +842+110 'After' \
  -font DejaVu-Sans -fill '#cbd5e1' -pointsize 28 \
  -annotate +132+722 'Overflowing button label' \
  -annotate +760+722 'Button resized to fit label' \
  demo/chrome-store-before-after-1280x800.png

cp demo/chrome-store-before-after-1280x800.png demo/before-after.png
