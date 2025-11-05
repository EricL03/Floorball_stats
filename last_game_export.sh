#!/usr/bin/env bash
# Usage: ./last_game_export.sh LAST_GAME_ID OPPENENT_NAME

GAME_ID="$1"
OPPONENT="$2"

./export_game_page.sh ${GAME_ID} ${OPPONENT}
./export_stats_page.sh ${OPPONENT}
