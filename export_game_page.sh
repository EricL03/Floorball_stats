#!/usr/bin/env bash
# Usage: ./export_game_page.sh GAME_ID OPPONENT
# Automatically saves the game detail page as a self-contained HTML file,
# then re-injects the JS block from your Django template.

GAME_ID="$1"
OPPONENT="$2"
OUT_DIR="game_export"
OUT_FILE="$OUT_DIR/matchstatistik_${OPPONENT}.html"
TEMPLATE_FILE="~/my_stuff/Floorball_stats/floorball_stats/games/templates/games/detail.html"

mkdir -p "$OUT_DIR"

# 1. Run SingleFile to save the page
single-file "http://127.0.0.1:8000/games/${GAME_ID}/view/" "$OUT_FILE" \
  --remove-hidden-elements=false \
  --remove-unused-styles=false

# 2. Extract the <script> block(s) from your template
JS_BLOCK=$(awk '/<script>/{flag=1;next}/<\/script>/{print;flag=0}flag' "$TEMPLATE_FILE")

# 3. Append them at the end of the exported file
echo "" >>"$OUT_FILE"
echo "$JS_BLOCK" >>"$OUT_FILE"

echo "Exported ${OUT_FILE} with JS from template re-added."
