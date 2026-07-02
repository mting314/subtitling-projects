#!/bin/bash
# Hardsub + trim + concatenate multiple segments from a video.
# Usage: ./hardsub_trim.sh <input.mkv> <subtitle.ass> <output.mp4> <start1> <end1> [<start2> <end2> ...]
#
# Examples:
#   # Single segment:
#   ./hardsub_trim.sh video.mkv subs.ass final.mp4 00:09:45 00:18:19
#
#   # Multiple segments (gaps are skipped, parts concatenated):
#   ./hardsub_trim.sh video.mkv subs.ass final.mp4 00:09:45 00:18:19 00:33:35 00:55:30

set -euo pipefail

if [ $# -lt 5 ] || [ $(( ($# - 3) % 2 )) -ne 0 ]; then
  echo "Usage: $0 <input> <subtitle> <output> <start1> <end1> [<start2> <end2> ...]"
  exit 1
fi

INPUT="$1"
SUBS="$2"
OUTPUT="$3"
shift 3

SEGMENTS=()
while [ $# -ge 2 ]; do
  SEGMENTS+=("$1" "$2")
  shift 2
done

NUM_SEGMENTS=$(( ${#SEGMENTS[@]} / 2 ))
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

# Symlink subtitle file to a spaceless name (ass= filter can't handle spaces)
SUBS_LINK="$TMPDIR/subs.ass"
ln -sf "$(cd "$(dirname "$SUBS")" && pwd)/$(basename "$SUBS")" "$SUBS_LINK"

if [ "$NUM_SEGMENTS" -eq 1 ]; then
  # Single segment — no concat needed
  echo "Hardsubbing + trimming: ${SEGMENTS[0]} to ${SEGMENTS[1]}"
  ffmpeg -i "$INPUT" -vf "ass=$SUBS_LINK" -ss "${SEGMENTS[0]}" -to "${SEGMENTS[1]}" "$OUTPUT" -y
else
  # Multiple segments — hardsub+trim each, then concat
  CONCAT_FILE="$TMPDIR/concat.txt"
  PIDS=()

  for (( i=0; i<NUM_SEGMENTS; i++ )); do
    START="${SEGMENTS[$((i*2))]}"
    END="${SEGMENTS[$((i*2+1))]}"
    PART="$TMPDIR/part$((i+1)).mp4"
    echo "Segment $((i+1))/$NUM_SEGMENTS: $START to $END"
    ffmpeg -i "$INPUT" -vf "ass=$SUBS_LINK" -ss "$START" -to "$END" "$PART" -y 2>/dev/null &
    PIDS+=($!)
    echo "file '$PART'" >> "$CONCAT_FILE"
  done

  # Wait for all segments
  for pid in "${PIDS[@]}"; do
    wait "$pid" || { echo "Error: ffmpeg segment failed (pid $pid)"; exit 1; }
  done

  echo "Concatenating $NUM_SEGMENTS segments..."
  ffmpeg -f concat -safe 0 -i "$CONCAT_FILE" -c copy "$OUTPUT" -y 2>/dev/null

  echo "Done: $OUTPUT"
fi

# Post-render sanity check: black frames often mean a source fade got caught at a
# cut boundary (a black flash at a concat join). If find_segments.py --mkv was used
# the boundaries are already fade-clear; this catches anything that slipped through.
echo "Checking for black frames..."
BLACK=$(ffmpeg -hide_banner -i "$OUTPUT" -vf "blackdetect=d=0.05:pix_th=0.10" -an -f null - 2>&1 \
  | grep -oE "black_start:[0-9.]+ black_end:[0-9.]+" || true)
if [ -n "$BLACK" ]; then
  echo "⚠️  Black intervals detected — check these (often a source fade at a cut boundary):"
  echo "$BLACK" | sed 's/^/    /'
else
  echo "✓ No black intervals >=0.05s."
fi
