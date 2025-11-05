#!/usr/bin/env bash
# Usage: ./export_stats_page.sh LAST_OPPENENT_NAME
# Automatically saves the game stats page as a self-contained HTML file,
# then re-injects the JS block from your Django template.

OPPONENT="$1"
OUT_DIR="game_export"
OUT_FILE="$OUT_DIR/totalstatistik_efter_${OPPONENT}.html"
TEMPLATE_FILE="$HOME/my_stuff/Floorball_stats/floorball_stats/stats/templates/stats/stats.html"

mkdir -p "$OUT_DIR"

# 1. Run SingleFile to save the page
single-file "http://127.0.0.1:8000/stats/" "$OUT_FILE" \
  --remove-hidden-elements=false \
  --remove-unused-styles=false

# 2. Extract the <script> block(s) from your template
JS_BLOCK=$(awk '/<script>/{flag=1;next}/<\/script>/{print;flag=0}flag' "$TEMPLATE_FILE")

# 3. Append it directly to the end of the file
echo "<script>" >>"$OUT_FILE"
echo "$JS_BLOCK" >>"$OUT_FILE"

echo "Exported ${OUT_FILE} with JS from template re-added."
echo "Opening ${OUT_FILE} in firefox!"

firefox ${OUT_FILE}
