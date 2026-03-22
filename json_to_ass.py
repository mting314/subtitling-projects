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

from utils.time import parse_offset


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


def seconds_to_ass(seconds: float) -> str:
    """Convert seconds to ASS timestamp format 'H:MM:SS.CC'."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = round((seconds % 1) * 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


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
            print(f"Error: no chunk_*.json or merged.json found in {path}", file=sys.stderr)
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


def _emit_line(word_data: list[tuple], style: str, comma_split_chars: int,
               lines: list[dict]):
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
        lines.append({
            "start": word_data[0][1],
            "end": word_data[-1][2],
            "style": style,
            "text": text,
        })
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
        lines.append({
            "start": word_data[0][1],
            "end": word_data[-1][2],
            "style": style,
            "text": text,
        })
        return

    # Split at best comma and recurse on both halves
    first_half = word_data[:best_idx + 1]
    second_half = word_data[best_idx + 1:]
    _emit_line(first_half, style, comma_split_chars, lines)
    _emit_line(second_half, style, comma_split_chars, lines)


def extract_dialogue_lines(results: list[dict],
                           pause_threshold: float = DEFAULT_PAUSE_THRESHOLD,
                           max_line_chars: int = DEFAULT_MAX_LINE_CHARS,
                           comma_split_chars: int = DEFAULT_COMMA_SPLIT_CHARS) -> list[dict]:
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
            w_start = _get_word_time(word, "startOffset", last_valid_time, max_valid_time)
            w_end = _get_word_time(word, "endOffset", w_start, max_valid_time)
            if w_end < w_start:
                w_end = w_start
            last_valid_time = max(last_valid_time, w_start, w_end)

            word_text = word.get("word", "")
            if word_text.strip() in PUNCTUATION_ONLY and processed:
                prev_text, prev_start, prev_end = processed[-1]
                processed[-1] = (prev_text + word_text, prev_start, max(prev_end, w_end))
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


def lines_to_ass(lines: list[dict], title: str) -> str:
    """Convert dialogue lines to a complete ASS file string."""
    content = ASS_HEADER_TEMPLATE.format(title=title)
    for line in lines:
        start_ass = seconds_to_ass(line["start"])
        end_ass = seconds_to_ass(line["end"])
        content += f"Dialogue: 0,{start_ass},{end_ass},{line['style']},,0,0,0,,{line['text']}\n"
    return content


def print_quality_report(lines: list[dict]):
    """Print ASS file stats and quality warnings."""
    if not lines:
        print(f"  Dialogue lines: 0")
        print(f"\n  WARNING: No dialogue lines generated!")
        return

    text_lengths = [len(line["text"]) for line in lines]
    durations = [line["end"] - line["start"] for line in lines]
    total_chars = sum(text_lengths)

    print(f"\n  --- ASS File Stats ---")
    print(f"  Dialogue lines:  {len(lines)}")
    print(f"  Total characters: {total_chars}")
    print(f"  Time range:      {seconds_to_ass(lines[0]['start'])} - "
          f"{seconds_to_ass(lines[-1]['end'])}")

    print(f"\n  --- Line Length (characters) ---")
    print(f"  Min:     {min(text_lengths)}")
    print(f"  Max:     {max(text_lengths)}")
    print(f"  Mean:    {total_chars / len(lines):.1f}")
    print(f"  Median:  {sorted(text_lengths)[len(text_lengths) // 2]}")

    print(f"\n  --- Line Duration (seconds) ---")
    print(f"  Min:     {min(durations):.2f}s")
    print(f"  Max:     {max(durations):.2f}s")
    print(f"  Mean:    {sum(durations) / len(durations):.2f}s")
    print(f"  Median:  {sorted(durations)[len(durations) // 2]:.2f}s")

    issues = []

    zero_dur = [i for i, d in enumerate(durations) if d <= 0]
    if zero_dur:
        issues.append(f"  - {len(zero_dur)} line(s) with zero or negative duration "
                      f"(likely bogus timestamps)")
        for idx in zero_dur[:5]:
            line = lines[idx]
            issues.append(f"      line {idx+1}: {seconds_to_ass(line['start'])} -> "
                          f"{seconds_to_ass(line['end'])}  \"{line['text'][:50]}\"")
        if len(zero_dur) > 5:
            issues.append(f"      ... and {len(zero_dur) - 5} more")

    long_lines = [(i, l) for i, l in enumerate(text_lengths) if l > 200]
    if long_lines:
        issues.append(f"  - {len(long_lines)} line(s) over 200 characters "
                      f"(may need manual splitting in Aegisub)")
        for idx, length in long_lines[:3]:
            issues.append(f"      line {idx+1}: {length} chars")
        if len(long_lines) > 3:
            issues.append(f"      ... and {len(long_lines) - 3} more")

    short_lines = [(i, lines[i]["text"]) for i, l in enumerate(text_lengths) if l < 3]
    if short_lines:
        issues.append(f"  - {len(short_lines)} line(s) under 3 characters "
                      f"(likely noise or artifacts)")
        for idx, text in short_lines[:5]:
            issues.append(f"      line {idx+1}: \"{text}\"")
        if len(short_lines) > 5:
            issues.append(f"      ... and {len(short_lines) - 5} more")

    long_dur = [(i, d) for i, d in enumerate(durations) if d > 60]
    if long_dur:
        issues.append(f"  - {len(long_dur)} line(s) spanning over 60 seconds "
                      f"(likely timestamp gaps from API)")
        for idx, dur in long_dur[:3]:
            line = lines[idx]
            issues.append(f"      line {idx+1}: {dur:.1f}s  "
                          f"{seconds_to_ass(line['start'])} -> {seconds_to_ass(line['end'])}")
        if len(long_dur) > 3:
            issues.append(f"      ... and {len(long_dur) - 3} more")

    inverted = [i for i, d in enumerate(durations) if d < 0]
    if inverted:
        issues.append(f"  - {len(inverted)} line(s) with end time before start time "
                      f"(bogus timestamps)")
        for idx in inverted[:3]:
            line = lines[idx]
            issues.append(f"      line {idx+1}: {seconds_to_ass(line['start'])} -> "
                          f"{seconds_to_ass(line['end'])}")
        if len(inverted) > 3:
            issues.append(f"      ... and {len(inverted) - 3} more")

    overlaps = []
    for i in range(len(lines) - 1):
        if lines[i+1]["start"] < lines[i]["end"] - 0.1:
            overlaps.append(i)
    if overlaps:
        issues.append(f"  - {len(overlaps)} pair(s) of overlapping lines "
                      f"(next line starts before current ends)")
        for idx in overlaps[:3]:
            issues.append(f"      lines {idx+1}-{idx+2}: "
                          f"end={seconds_to_ass(lines[idx]['end'])} > "
                          f"start={seconds_to_ass(lines[idx+1]['start'])}")
        if len(overlaps) > 3:
            issues.append(f"      ... and {len(overlaps) - 3} more")

    gaps = []
    for i in range(len(lines) - 1):
        gap = lines[i+1]["start"] - lines[i]["end"]
        if gap > 30:
            gaps.append((i, gap))
    if gaps:
        issues.append(f"  - {len(gaps)} gap(s) over 30 seconds between lines "
                      f"(silence, music, or missed speech)")
        for idx, gap in gaps[:3]:
            issues.append(f"      between lines {idx+1}-{idx+2}: "
                          f"{gap:.1f}s gap at {seconds_to_ass(lines[idx]['end'])}")
        if len(gaps) > 3:
            issues.append(f"      ... and {len(gaps) - 3} more")

    if issues:
        print(f"\n  --- Quality Warnings ({len(issues)} issues) ---")
        for issue in issues:
            print(issue)
    else:
        print(f"\n  --- Quality: No issues detected ---")


def main():
    parser = argparse.ArgumentParser(
        description="Convert GCP Speech-to-Text JSON transcripts to ASS subtitle files. "
                    "Accepts a single JSON file or a directory of chunk files from gcp_transcribe_batch.py."
    )
    parser.add_argument("input",
                        help="Path to JSON transcript file or directory of chunk files")
    parser.add_argument("output",
                        help="Output path for ASS subtitle file")
    parser.add_argument("--title", default=None,
                        help="ASS file title (defaults to output filename)")
    parser.add_argument("--pause-threshold", type=float, default=DEFAULT_PAUSE_THRESHOLD,
                        help=f"Seconds of silence to force a line break (default: {DEFAULT_PAUSE_THRESHOLD})")
    parser.add_argument("--max-line-chars", type=int, default=DEFAULT_MAX_LINE_CHARS,
                        help=f"Max characters per line before forcing a break (default: {DEFAULT_MAX_LINE_CHARS})")
    parser.add_argument("--comma-split-chars", type=int, default=DEFAULT_COMMA_SPLIT_CHARS,
                        help=f"Split at commas when line exceeds this length. 0 to disable (default: {DEFAULT_COMMA_SPLIT_CHARS})")

    args = parser.parse_args()

    title = args.title or Path(args.output).stem

    # Load transcript
    print(f"Loading transcript from: {args.input}")
    results = load_transcript(args.input)
    total_words = sum(len(r["alternatives"][0].get("words", [])) for r in results if r.get("alternatives"))
    print(f"  {len(results)} result(s), {total_words} total words")

    # Extract dialogue lines
    print(f"\nSplitting into dialogue lines...")
    print(f"  Pause threshold:    {args.pause_threshold}s")
    print(f"  Max line chars:     {args.max_line_chars}")
    print(f"  Comma split chars:  {args.comma_split_chars}" +
          (" (disabled)" if args.comma_split_chars <= 0 else ""))
    lines = extract_dialogue_lines(results,
                                   pause_threshold=args.pause_threshold,
                                   max_line_chars=args.max_line_chars,
                                   comma_split_chars=args.comma_split_chars)

    # Sort by start time
    lines.sort(key=lambda x: x["start"])

    # Generate ASS
    ass_content = lines_to_ass(lines, title)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ass_content, encoding="utf-8")

    print(f"\nGenerated: {args.output}")
    print_quality_report(lines)


if __name__ == "__main__":
    main()
