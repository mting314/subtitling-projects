#!/usr/bin/env python3
"""Convert GCP Speech-to-Text JSON transcripts to ASS subtitle files.

Handles two input formats:
  1. A single JSON file (merged.json or transcript.json from gcp_transcribe_batch.py)
  2. A directory of chunk JSON files (reads all chunk_*.json and merged.json)

Splits Chirp 3's single-result-per-chunk output into subtitle-sized lines
using word-level timestamps, sentence boundaries, and pause detection.
"""

import argparse
import json
import sys
from pathlib import Path

from quality_report import write_reports
from utils.time import parse_offset, seconds_to_timestamp


MAX_AUDIO_LENGTH_SECS = 8 * 60 * 60

# ASS file template
ASS_HEADER_TEMPLATE = """\
[Script Info]
; Generated from speech-to-text transcript
Title: {title}
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Lato ExtraBold,72,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,4,1.33,2,200,200,60,1
Style: JP,Lato ExtraBold,72,&H00FFFFFF,&H000000FF,&H006381A1,&H00000000,0,0,0,0,100,100,0,0,1,4,1.33,2,200,200,60,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

DEFAULT_PAUSE_THRESHOLD = 1.0
DEFAULT_MAX_LINE_CHARS = 200
DEFAULT_COMMA_SPLIT_CHARS = 40
DEFAULT_LEAD_IN = 0.125
DEFAULT_LEAD_OUT = 0.5
DEFAULT_SNAP_GAP = 0.25
DEFAULT_MIN_DURATION = 0.5


def load_transcript(input_path: str) -> list[dict]:
    """Load transcript results from a JSON file or directory.

    Returns the list of result dicts from the 'results' key.
    """
    path = Path(input_path)

    if path.is_file():
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("results", [])

    if path.is_dir():
        # Prefer merged.json if it exists
        merged = path / "merged.json"
        if merged.exists():
            with open(merged, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("results", [])

        # Otherwise load all chunk files in order
        chunk_files = sorted(path.glob("chunk_*.json"))
        if not chunk_files:
            print(
                f"Error: no chunk_*.json or merged.json found in {path}",
                file=sys.stderr,
            )
            sys.exit(1)

        all_results = []
        for cf in chunk_files:
            with open(cf, "r", encoding="utf-8") as f:
                data = json.load(f)
            all_results.extend(data.get("results", []))
        return all_results

    print(f"Error: {input_path} is not a file or directory", file=sys.stderr)
    sys.exit(1)


def _get_word_time(word: dict, key: str, fallback: float, max_time: float) -> float:
    """Get a word's start or end time, falling back if the value is 0 or bogus.

    Also rejects a startOffset that is wildly inconsistent with its own endOffset,
    which happens when the API returns garbage for one but not the other.
    """
    val = parse_offset(word.get(key, "0s"))
    if val <= 0 or val > max_time:
        return fallback
    # Cross-check: if this is a start offset, reject if it's way past the word's own end
    if key == "startOffset":
        end_val = parse_offset(word.get("endOffset", "0s"))
        if end_val > 0 and val > end_val + 60:
            return fallback
    return val


def _emit_line(
    word_data: list[tuple], style: str, comma_split_chars: int, lines: list[dict]
):
    """Emit one or more dialogue lines from accumulated word data.

    If the text exceeds comma_split_chars and contains commas, splits at the
    comma with the longest pause after it (the most natural breath pause).
    Applies recursively so both halves can be further split if still long.

    word_data: list of (text, start, end) tuples
    """
    if not word_data:
        return
    text = "".join(w[0] for w in word_data).strip()
    if not text:
        return

    # If short enough or comma splitting disabled, emit as-is
    if comma_split_chars <= 0 or len(text) < comma_split_chars:
        lines.append(
            {
                "start": word_data[0][1],
                "end": word_data[-1][2],
                "style": style,
                "text": text,
            }
        )
        return

    # Find the best comma to split at: the one with the longest pause,
    # as long as the first part is at least half the threshold (avoid tiny fragments)
    min_first_part = comma_split_chars // 2
    best_idx = -1
    best_pause = -1.0
    running_len = 0

    for i in range(len(word_data) - 1):
        w_text, w_start, w_end = word_data[i]
        running_len += len(w_text)

        if running_len < min_first_part:
            continue
        if not (w_text and w_text[-1] in "、,"):
            continue

        # Pause = gap between this word's end and next word's start
        next_start = word_data[i + 1][1]
        pause = next_start - w_end
        if pause > best_pause:
            best_pause = pause
            best_idx = i

    if best_idx < 0:
        # No suitable comma found, emit as-is
        lines.append(
            {
                "start": word_data[0][1],
                "end": word_data[-1][2],
                "style": style,
                "text": text,
            }
        )
        return

    # Split at best comma and recurse on both halves
    first_half = word_data[: best_idx + 1]
    second_half = word_data[best_idx + 1 :]
    _emit_line(first_half, style, comma_split_chars, lines)
    _emit_line(second_half, style, comma_split_chars, lines)


def extract_dialogue_lines(
    results: list[dict],
    pause_threshold: float = DEFAULT_PAUSE_THRESHOLD,
    max_line_chars: int = DEFAULT_MAX_LINE_CHARS,
    comma_split_chars: int = DEFAULT_COMMA_SPLIT_CHARS,
) -> list[dict]:
    """Extract dialogue lines from transcript results using word-level timestamps.

    Chirp 3 often returns a single result containing all text for a chunk.
    We split into subtitle-sized lines at:
      - Sentence boundaries (。？！?!)
      - Pauses (gap between words >= pause_threshold)
      - Length limit (>= max_line_chars forces a break)

    Lines exceeding comma_split_chars are further split at the comma with
    the longest pause (most natural breath pause). This applies recursively.

    Punctuation-only tokens are merged into the preceding word.

    Returns list of dicts with keys: start, end, style, text
    """
    SENTENCE_ENDERS = "。？！?!"
    PUNCTUATION_ONLY = set("。、？！?!,.…──")

    lines = []
    for result in results:
        if not result.get("alternatives"):
            continue
        alt = result["alternatives"][0]
        words = alt.get("words", [])

        if not words:
            text = alt.get("transcript", "").strip()
            if text:
                start = parse_offset(words[0]["startOffset"]) if words else 0.0
                end = parse_offset(result.get("resultEndOffset", "0s"))
                style = "JP" if result.get("languageCode") == "ja-jp" else "Default"
                lines.append({"start": start, "end": end, "style": style, "text": text})
            continue

        style = "JP" if result.get("languageCode") == "ja-jp" else "Default"

        # Estimate max valid time from the valid end offsets in this result.
        valid_ends = [parse_offset(w.get("endOffset", "0s")) for w in words]
        valid_ends = [e for e in valid_ends if e > 0]
        max_valid_time = max(valid_ends) * 1.1 if valid_ends else MAX_AUDIO_LENGTH_SECS

        # Pre-process: collect words with valid timestamps, merge punctuation tokens
        processed = []  # list of (text, start, end)
        last_valid_time = 0.0

        for word in words:
            w_start = _get_word_time(
                word, "startOffset", last_valid_time, max_valid_time
            )
            w_end = _get_word_time(word, "endOffset", w_start, max_valid_time)
            if w_end < w_start:
                w_end = w_start
            last_valid_time = max(last_valid_time, w_start, w_end)

            word_text = word.get("word", "")
            if word_text.strip() in PUNCTUATION_ONLY and processed:
                prev_text, prev_start, prev_end = processed[-1]
                processed[-1] = (
                    prev_text + word_text,
                    prev_start,
                    max(prev_end, w_end),
                )
                continue

            processed.append((word_text, w_start, w_end))

        # Build lines from processed words.
        # First pass: split at sentence enders, hard pauses, and max chars.
        # Then _emit_line handles comma splitting on the resulting segments.
        current_word_data = []  # list of (text, start, end) tuples

        for i, (word_text, w_start, w_end) in enumerate(processed):
            should_break = False
            if current_word_data:
                prev_end = current_word_data[-1][2]
                pause = w_start - prev_end
                if pause >= pause_threshold:
                    should_break = True

                prev_text = current_word_data[-1][0]
                if prev_text and prev_text[-1] in SENTENCE_ENDERS:
                    should_break = True

                if sum(len(w[0]) for w in current_word_data) >= max_line_chars:
                    should_break = True

            if should_break and current_word_data:
                _emit_line(current_word_data, style, comma_split_chars, lines)
                current_word_data = []

            current_word_data.append((word_text, w_start, w_end))

        # Flush remaining words
        if current_word_data:
            _emit_line(current_word_data, style, comma_split_chars, lines)

    return lines


def pad_timing(lines: list[dict], lead_in: float, lead_out: float) -> int:
    """Add lead-in and lead-out padding to subtitle timing.

    Lead-in always applies the full amount (capped only at 0.0), even if it
    overlaps into the previous line's time — per standard fansubbing practice,
    the subtitle must appear the full lead-in duration before speech starts.
    The previous line's lead-out then yields to the next line's shifted start.

    Two-pass approach: lead-in is applied first to all lines, then lead-out
    extends ends but caps at the next line's (already shifted) start.

    Lines must already be sorted by start time. Mutates in place.
    Returns the number of lines modified.
    """
    modified = [False] * len(lines)

    # Pass 1: lead-in (shift starts earlier, capped only at 0)
    if lead_in > 0:
        for i in range(len(lines)):
            new_start = max(lines[i]["start"] - lead_in, 0.0)
            if new_start < lines[i]["start"]:
                lines[i]["start"] = new_start
                modified[i] = True

    # Pass 2: lead-out (extend ends, cap/shrink at next line's shifted start)
    for i in range(len(lines)):
        max_end = lines[i + 1]["start"] if i + 1 < len(lines) else float("inf")
        new_end = min(lines[i]["end"] + lead_out, max_end)
        if new_end != lines[i]["end"]:
            lines[i]["end"] = new_end
            modified[i] = True

    return sum(modified)


def snap_gaps(lines: list[dict], max_gap: float) -> int:
    """Snap near-adjacent lines together to eliminate subtitle flashing.

    When consecutive lines of the same style have a small gap (0 < gap <= max_gap),
    extends the earlier line's end to match the next line's start.

    Lines must already be sorted by start time. Mutates in place.
    Returns the number of gaps snapped.
    """
    count = 0
    for i in range(len(lines) - 1):
        if lines[i]["style"] != lines[i + 1]["style"]:
            continue
        gap = lines[i + 1]["start"] - lines[i]["end"]
        if 0 < gap <= max_gap:
            lines[i]["end"] = lines[i + 1]["start"]
            count += 1
    return count


def enforce_min_duration(lines: list[dict], min_dur: float) -> int:
    """Ensure every line stays on screen for at least min_dur seconds.

    For lines shorter than min_dur, extends lead-out (end time) first,
    then lead-in (start time) if needed, without overlapping neighbors.

    Lines must already be sorted by start time. Mutates in place.
    Returns the number of lines extended.
    """
    count = 0
    for i in range(len(lines)):
        duration = lines[i]["end"] - lines[i]["start"]
        if duration >= min_dur:
            continue

        needed = min_dur - duration
        extended = False

        # Lead-out: extend end toward next line's start
        max_end = lines[i + 1]["start"] if i + 1 < len(lines) else float("inf")
        end_room = max_end - lines[i]["end"]
        if end_room > 0:
            extend = min(needed, end_room)
            lines[i]["end"] += extend
            needed -= extend
            extended = True

        # Lead-in: extend start earlier toward previous line's end
        if needed > 0:
            min_start = lines[i - 1]["end"] if i > 0 else 0.0
            start_room = lines[i]["start"] - min_start
            if start_room > 0:
                extend = min(needed, start_room)
                lines[i]["start"] -= extend
                extended = True

        if extended:
            count += 1
    return count


def lines_to_ass(lines: list[dict], title: str) -> str:
    """Convert dialogue lines to a complete ASS file string."""
    content = ASS_HEADER_TEMPLATE.format(title=title)
    for line in lines:
        start_ass = seconds_to_timestamp(line["start"])
        end_ass = seconds_to_timestamp(line["end"])
        content += f"Dialogue: 0,{start_ass},{end_ass},{line['style']},,0,0,0,,{line['text']}\n"
    return content


def main():
    parser = argparse.ArgumentParser(
        description="Convert GCP Speech-to-Text JSON transcripts to ASS subtitle files. "
        "Accepts a single JSON file or a directory of chunk files from gcp_transcribe_batch.py."
    )
    parser.add_argument(
        "input", help="Path to JSON transcript file or directory of chunk files"
    )
    parser.add_argument("output", help="Output path for ASS subtitle file")
    parser.add_argument(
        "--title", default=None, help="ASS file title (defaults to output filename)"
    )
    parser.add_argument(
        "--pause-threshold",
        type=float,
        default=DEFAULT_PAUSE_THRESHOLD,
        help=f"Seconds of silence to force a line break (default: {DEFAULT_PAUSE_THRESHOLD})",
    )
    parser.add_argument(
        "--max-line-chars",
        type=int,
        default=DEFAULT_MAX_LINE_CHARS,
        help=f"Max characters per line before forcing a break (default: {DEFAULT_MAX_LINE_CHARS})",
    )
    parser.add_argument(
        "--comma-split-chars",
        type=int,
        default=DEFAULT_COMMA_SPLIT_CHARS,
        help=f"Split at commas when line exceeds this length. 0 to disable (default: {DEFAULT_COMMA_SPLIT_CHARS})",
    )
    parser.add_argument(
        "--lead-in",
        type=float,
        default=DEFAULT_LEAD_IN,
        help=f"Lead-in padding in seconds (subtitle appears before speech). 0 to disable (default: {DEFAULT_LEAD_IN})",
    )
    parser.add_argument(
        "--lead-out",
        type=float,
        default=DEFAULT_LEAD_OUT,
        help=f"Lead-out padding in seconds (subtitle lingers after speech). 0 to disable (default: {DEFAULT_LEAD_OUT})",
    )
    parser.add_argument(
        "--snap-gap",
        type=float,
        default=DEFAULT_SNAP_GAP,
        help=f"Snap gaps smaller than this (seconds) between same-style lines. 0 to disable (default: {DEFAULT_SNAP_GAP})",
    )
    parser.add_argument(
        "--min-duration",
        type=float,
        default=DEFAULT_MIN_DURATION,
        help=f"Minimum line duration in seconds. Short lines get lead-in/lead-out. 0 to disable (default: {DEFAULT_MIN_DURATION})",
    )
    parser.add_argument(
        "--video",
        default=None,
        help="Path to source video file. Embeds a player in the HTML report for click-to-seek",
    )

    args = parser.parse_args()

    title = args.title or Path(args.output).stem

    # Load transcript
    print(f"Loading transcript from: {args.input}")
    results = load_transcript(args.input)
    total_words = sum(
        len(r["alternatives"][0].get("words", []))
        for r in results
        if r.get("alternatives")
    )
    print(f"  {len(results)} result(s), {total_words} total words")

    # Extract dialogue lines
    print("\nSplitting into dialogue lines...")
    print(f"  Pause threshold:    {args.pause_threshold}s")
    print(f"  Max line chars:     {args.max_line_chars}")
    print(
        f"  Comma split chars:  {args.comma_split_chars}"
        + (" (disabled)" if args.comma_split_chars <= 0 else "")
    )
    lines = extract_dialogue_lines(
        results,
        pause_threshold=args.pause_threshold,
        max_line_chars=args.max_line_chars,
        comma_split_chars=args.comma_split_chars,
    )

    # Sort by start time
    lines.sort(key=lambda x: x["start"])

    # Add lead-in/lead-out padding
    if args.lead_in > 0 or args.lead_out > 0:
        padded = pad_timing(lines, args.lead_in, args.lead_out)
        print(
            f"  Padded {padded} line(s) (lead-in: {args.lead_in}s, lead-out: {args.lead_out}s)"
        )

    # Snap small gaps between same-style lines to prevent flashing
    if args.snap_gap > 0:
        snapped = snap_gaps(lines, args.snap_gap)
        print(f"  Snapped {snapped} gap(s) under {args.snap_gap}s")

    # Enforce minimum line duration
    if args.min_duration > 0:
        extended = enforce_min_duration(lines, args.min_duration)
        print(
            f"  Extended {extended} line(s) to meet {args.min_duration}s minimum duration"
        )

    # Generate ASS
    ass_content = lines_to_ass(lines, title)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ass_content, encoding="utf-8")

    print(f"\nGenerated: {args.output}")
    write_reports(lines, args.output, video_path=args.video, title=title)


if __name__ == "__main__":
    main()
