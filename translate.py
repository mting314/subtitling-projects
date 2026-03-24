#!/usr/bin/env python3
"""Translate ASS subtitle files from Japanese to English using Gemini via Vertex AI.

Reads a Japanese ASS file, sends dialogue lines to Gemini with translation context
(instructions, style guide, project reference with fixed translations), and writes
a translated ASS file preserving all timing, styles, and formatting.
"""

import argparse
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig

from utils.ass_parser import parse_ass, write_ass


DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_BATCH_SIZE = 50
DEFAULT_INSTRUCTIONS_PATH = "translation_instructions.md"
STYLE_GUIDE_PATH = "style_guide.md"


def load_text_file(path: str) -> str | None:
    """Load a text file, returning None if it doesn't exist."""
    p = Path(path)
    if p.is_file():
        return p.read_text(encoding="utf-8")
    return None


def build_system_prompt(
    instructions_path: str,
    style_guide_path: str,
    project_ref_path: str | None,
) -> str:
    """Build the system instruction from translation context files."""
    parts = []

    instructions = load_text_file(instructions_path)
    if instructions:
        parts.append(instructions)
    else:
        print(f"  Warning: instructions file not found: {instructions_path}", file=sys.stderr)

    style_guide = load_text_file(style_guide_path)
    if style_guide:
        parts.append(style_guide)

    if project_ref_path:
        project_ref = load_text_file(project_ref_path)
        if project_ref:
            parts.append(project_ref)
        else:
            print(f"  Warning: project reference not found: {project_ref_path}", file=sys.stderr)

    parts.append(
        "## Output Format\n\n"
        "You will receive numbered subtitle lines. Return ONLY the translated lines "
        "in the exact same numbered format. Do not add or remove lines. "
        "Do not include the original Japanese. Each line must start with its number "
        "followed by a pipe and the translated text.\n\n"
        "Example input:\n"
        "1|[Speaker1] こんにちは\n"
        "2|[Speaker2] ありがとう\n\n"
        "Example output:\n"
        "1|Hello!\n"
        "2|Thank you!\n\n"
        "If a line is empty or contains only whitespace, return the number with an empty text.\n"
        "Preserve any ASS override tags like {\\i1}text{\\i0} in the translation."
    )

    return "\n\n---\n\n".join(parts)


def format_lines_for_prompt(events: list[dict], start_idx: int) -> str:
    """Format dialogue events as numbered lines for the Gemini prompt."""
    lines = []
    for i, event in enumerate(events):
        num = start_idx + i + 1
        style_tag = f"[{event['style']}] " if event["style"] else ""
        lines.append(f"{num}|{style_tag}{event['text']}")
    return "\n".join(lines)


def parse_translation_response(response_text: str, expected_count: int, start_idx: int) -> list[str]:
    """Parse numbered translation lines from Gemini response.

    Handles multiple formats Gemini may return:
      - "1|text" (requested format)
      - "1. text" (numbered list)
      - "1: text" (colon-separated)
      - Lines inside ```code blocks```

    Returns a list of translated text strings in order.
    """
    # Strip markdown code fences if present
    text = response_text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        # Remove first and last ``` lines
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines)

    translations = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # Try multiple numbered formats: "N|text", "N. text", "N: text"
        m = re.match(r"^(\d+)\s*[|.:)\-]\s*(.*)$", line)
        if m:
            num = int(m.group(1))
            translated = m.group(2).strip()
            # Skip if the "translation" is just the style tag repeated (Gemini echo)
            if translated.startswith("[") and "] " in translated:
                translated = translated.split("] ", 1)[1]
            translations[num] = translated

    # Check if Gemini renumbered from 1 instead of using the expected offset
    first_expected = start_idx + 1
    if first_expected not in translations and 1 in translations:
        # Gemini returned 1-based numbering — shift all keys
        shifted = {}
        for num, val in translations.items():
            shifted[num + start_idx] = val
        translations = shifted

    result = []
    missing = 0
    for i in range(expected_count):
        num = start_idx + i + 1
        if num in translations:
            result.append(translations[num])
        else:
            missing += 1
            result.append("")

    if missing > 0:
        print(f"  Warning: {missing}/{expected_count} lines missing from response", file=sys.stderr)

    return result


MAX_RETRIES = 2


def translate_batch(
    client: genai.Client,
    model: str,
    system_prompt: str,
    events: list[dict],
    start_idx: int,
) -> list[str]:
    """Translate a batch of events via Gemini, with retry on high miss rate."""
    import time

    user_content = format_lines_for_prompt(events, start_idx)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=model,
                contents=user_content,
                config=GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0.3,
                ),
            )
        except Exception as e:
            if attempt < MAX_RETRIES:
                print(f"  API error: {e.__class__.__name__}, retrying in 5s...", file=sys.stderr)
                time.sleep(5)
                continue
            raise

        result = parse_translation_response(response.text, len(events), start_idx)
        missing = sum(1 for t in result if t == "")
        if missing == 0 or attempt == MAX_RETRIES:
            return result
        print(f"  Retrying batch (attempt {attempt + 1}/{MAX_RETRIES}, {missing} missing)...")
        time.sleep(2)

    return result


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Translate Japanese ASS subtitles to English using Gemini. "
        "Preserves timing, styles, and formatting. Sends lines in batches."
    )
    parser.add_argument(
        "--input", required=True,
        help="Source ASS file (Japanese)",
    )
    parser.add_argument(
        "--output", default=None,
        help="Output ASS file (English). Default: {input_stem}_en.ass",
    )
    parser.add_argument(
        "--project", default=None,
        help="Path to project translation_reference.md",
    )
    parser.add_argument(
        "--instructions", default=DEFAULT_INSTRUCTIONS_PATH,
        help=f"Path to translation instructions (default: {DEFAULT_INSTRUCTIONS_PATH})",
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL,
        help=f"Gemini model to use (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--batch-size", type=int, default=DEFAULT_BATCH_SIZE,
        help=f"Lines per API request (default: {DEFAULT_BATCH_SIZE})",
    )
    parser.add_argument(
        "--project-id", default=None,
        help="GCP project ID (default: $GOOGLE_CLOUD_PROJECT)",
    )
    parser.add_argument(
        "--video", default=None,
        help="Video path for comparison report",
    )

    args = parser.parse_args()

    project_id = args.project_id or os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        parser.error(
            "GCP project ID required: set GOOGLE_CLOUD_PROJECT env var or pass --project-id"
        )

    input_path = Path(args.input)
    if not input_path.is_file():
        parser.error(f"Input file not found: {args.input}")

    output_path = Path(args.output) if args.output else input_path.with_stem(input_path.stem + "_en")

    print(f"\n{'=' * 60}")
    print("Gemini Translation")
    print(f"{'=' * 60}")
    print(f"  Input:        {input_path}")
    print(f"  Output:       {output_path}")
    print(f"  Model:        {args.model}")
    print(f"  Batch size:   {args.batch_size}")
    print(f"  Instructions: {args.instructions}")
    if args.project:
        print(f"  Project ref:  {args.project}")
    print(f"{'=' * 60}\n")

    # Parse input ASS
    print("[1/4] Parsing input ASS file...")
    data = parse_ass(input_path)
    all_events = data["events"]
    dialogue_indices = [i for i, e in enumerate(all_events) if e["type"] == "Dialogue"]
    dialogue_events = [all_events[i] for i in dialogue_indices]
    print(f"  {len(all_events)} events total, {len(dialogue_events)} dialogue lines")

    if not dialogue_events:
        print("  No dialogue lines to translate.")
        sys.exit(0)

    # Build system prompt
    print("\n[2/4] Building translation context...")
    system_prompt = build_system_prompt(
        args.instructions,
        STYLE_GUIDE_PATH,
        args.project,
    )
    print(f"  System prompt: {len(system_prompt)} chars")

    # Translate in batches
    print(f"\n[3/4] Translating {len(dialogue_events)} lines...")
    client = genai.Client(
        vertexai=True,
        project=project_id,
        location="us-central1",
    )

    all_translations = []
    num_batches = (len(dialogue_events) + args.batch_size - 1) // args.batch_size

    for batch_num in range(num_batches):
        start = batch_num * args.batch_size
        end = min(start + args.batch_size, len(dialogue_events))
        batch = dialogue_events[start:end]

        print(f"  Batch {batch_num + 1}/{num_batches} (lines {start + 1}-{end})...")
        translations = translate_batch(client, args.model, system_prompt, batch, start)
        all_translations.extend(translations)

    # Apply translations to events
    print(f"\n[4/4] Writing translated ASS file...")
    for idx, translation in zip(dialogue_indices, all_translations):
        data["events"][idx]["text"] = translation

    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_ass(data, output_path)
    print(f"  Generated: {output_path}")

    # Auto-run comparison report
    print("\n  Generating comparison report...")
    compare_args = [
        sys.executable, "compare_translations.py",
        "--source", str(input_path),
        "--translated", str(output_path),
    ]
    if args.video:
        compare_args.extend(["--video", args.video])

    import subprocess
    result = subprocess.run(compare_args, capture_output=True, text=True)
    if result.returncode == 0:
        # Print last few lines which contain the output path
        for line in result.stdout.strip().splitlines()[-3:]:
            print(f"  {line}")
    else:
        print(f"  Warning: comparison report failed: {result.stderr[:200]}", file=sys.stderr)

    print(f"\nTranslation complete: {output_path}")


if __name__ == "__main__":
    main()
