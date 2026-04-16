#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

timeout 90s node scripts/capture-demo-screenshots.js

convert logs/visual-bug-full.png -crop 420x250+230+92 +repage logs/visual-bug-crop.png
convert logs/visual-fix-full.png -crop 420x250+230+92 +repage logs/visual-fix-crop.png

convert -size 280x214 canvas:none \
  \( -size 280x214 xc:'#ffffff12' -fill '#ffffff10' -draw "roundrectangle 0,0 279,213 24,24" \) \
  -compose over -composite \
  -gravity northwest \
  -font DejaVu-Sans-Bold -fill '#fda4af' -pointsize 18 \
  -annotate +26+30 'BEFORE' \
  \( logs/visual-bug-crop.png -resize 272x162 -background white -gravity center -extent 272x162 -bordercolor '#ef4444' -border 4 \) \
  -geometry +4+54 -composite \
  -font DejaVu-Sans -fill '#dbe4f0' -pointsize 15 \
  -annotate +26+196 'Label overflows' \
  logs/visual-before-panel-640.png

convert -size 280x214 canvas:none \
  \( -size 280x214 xc:'#ffffff12' -fill '#ffffff10' -draw "roundrectangle 0,0 279,213 24,24" \) \
  -compose over -composite \
  -gravity northwest \
  -font DejaVu-Sans-Bold -fill '#86efac' -pointsize 18 \
  -annotate +26+30 'AFTER' \
  \( logs/visual-fix-crop.png -resize 272x162 -background white -gravity center -extent 272x162 -bordercolor '#22c55e' -border 4 \) \
  -geometry +4+54 -composite \
  -font DejaVu-Sans -fill '#dbe4f0' -pointsize 15 \
  -annotate +26+196 'Label fits button' \
  logs/visual-after-panel-640.png

convert logs/visual-before-panel-640.png \
  \( -size 44x214 canvas:none \) \
  logs/visual-after-panel-640.png \
  +append +repage \
  logs/visual-before-after-strip-640.png

convert \
  \( demo/dashboard-bg.jpg -resize 640x400^ -gravity center -extent 640x400 -blur 0x8 \) \
  \( -size 640x400 xc:'#08111f' -alpha set -channel A -evaluate set 68% \) \
  -compose over -composite \
  -font DejaVu-Sans-Bold -fill '#f8fafc' -pointsize 24 \
  -gravity north -annotate +0+34 'Before / After' \
  -gravity northwest \
  \( logs/visual-before-after-strip-640.png \) \
  -geometry +18+92 -composite \
  demo/chrome-store-before-after-640x400.png

convert -size 572x428 canvas:none \
  \( -size 572x428 xc:'#ffffff12' -fill '#ffffff10' -draw "roundrectangle 0,0 571,427 34,34" \) \
  -compose over -composite \
  -gravity northwest \
  -font DejaVu-Sans-Bold -fill '#fda4af' -pointsize 32 \
  -annotate +44+50 'BEFORE' \
  \( logs/visual-bug-crop.png -resize 556x331 -background white -gravity center -extent 556x331 -bordercolor '#ef4444' -border 8 \) \
  -geometry +8+89 -composite \
  -font DejaVu-Sans -fill '#dbe4f0' -pointsize 28 \
  -annotate +44+396 'Label overflows' \
  logs/visual-before-panel-1280.png

convert -size 572x428 canvas:none \
  \( -size 572x428 xc:'#ffffff12' -fill '#ffffff10' -draw "roundrectangle 0,0 571,427 34,34" \) \
  -compose over -composite \
  -gravity northwest \
  -font DejaVu-Sans-Bold -fill '#86efac' -pointsize 32 \
  -annotate +44+50 'AFTER' \
  \( logs/visual-fix-crop.png -resize 556x331 -background white -gravity center -extent 556x331 -bordercolor '#22c55e' -border 8 \) \
  -geometry +8+89 -composite \
  -font DejaVu-Sans -fill '#dbe4f0' -pointsize 28 \
  -annotate +44+396 'Label fits button' \
  logs/visual-after-panel-1280.png

convert logs/visual-before-panel-1280.png \
  \( -size 28x428 canvas:none \) \
  logs/visual-after-panel-1280.png \
  +append +repage \
  logs/visual-before-after-strip-1280.png

convert \
  \( demo/dashboard-bg.jpg -resize 1280x800^ -gravity center -extent 1280x800 -blur 0x10 \) \
  \( -size 1280x800 xc:'#08111f' -alpha set -channel A -evaluate set 68% \) \
  -compose over -composite \
  -font DejaVu-Sans-Bold -fill '#f8fafc' -pointsize 48 \
  -gravity north -annotate +0+72 'Before / After' \
  -gravity northwest \
  \( logs/visual-before-after-strip-1280.png \) \
  -geometry +54+184 -composite \
  demo/chrome-store-before-after-1280x800.png

cp demo/chrome-store-before-after-1280x800.png demo/before-after.png
