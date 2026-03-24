#!/usr/bin/env python3
"""Translate ASS subtitle files from Japanese to English using Gemini via Vertex AI.

Reads a Japanese ASS file, sends dialogue lines to Gemini with translation context
(instructions, style guide, project reference with fixed translations), and writes
a translated ASS file preserving all timing, styles, and formatting.

Uses structured JSON output for reliable 1:1 line correspondence.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel

from utils.ass_parser import parse_ass, write_ass


DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_BATCH_SIZE = 50
DEFAULT_INSTRUCTIONS_PATH = "translation_instructions.md"
STYLE_GUIDE_PATH = "style_guide.md"


class TranslatedSubtitle(BaseModel):
    """Schema for a single translated subtitle line."""

    id: int
    original: str
    translated: str


SYSTEM_PREAMBLE = """\
You are a professional Japanese-to-English subtitle translator and localizer.

You will receive batches of subtitle lines from a transcribed and timed Japanese \
subtitle file (ASS format). The lines have already been split and timed from speech \
recognition — your job is only to translate the text, not to change timing or structure.

Each batch is a JSON array of objects with "id", "style" (speaker), and "text" (Japanese). \
Return a JSON array with the same number of objects, each containing "id" (matching the input), \
"original" (the input text), and "translated" (your English translation).

Follow the translation instructions, style guide, and project reference below."""


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
    parts = [SYSTEM_PREAMBLE]

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

    return "\n\n---\n\n".join(parts)


def format_batch_input(events: list[dict], start_idx: int) -> str:
    """Format dialogue events as a JSON array for the Gemini prompt."""
    items = []
    for i, event in enumerate(events):
        items.append({
            "id": start_idx + i + 1,
            "style": event["style"],
            "text": event["text"],
        })
    return json.dumps(items, ensure_ascii=False)


def parse_structured_response(response_text: str, expected_count: int, start_idx: int) -> list[str]:
    """Parse structured JSON response into ordered translation list.

    Expects a JSON array of {id, original, translated} objects.
    Falls back gracefully if the structure is slightly off.
    """
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        print(f"  Warning: response is not valid JSON", file=sys.stderr)
        return [""] * expected_count

    if not isinstance(data, list):
        print(f"  Warning: response is not a JSON array", file=sys.stderr)
        return [""] * expected_count

    # Build lookup by id
    translations = {}
    for item in data:
        if isinstance(item, dict) and "id" in item and "translated" in item:
            translations[item["id"]] = item["translated"]

    # Check if IDs are 1-based instead of using expected offset
    first_expected = start_idx + 1
    if first_expected not in translations and 1 in translations:
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


MAX_RETRIES = 3


def translate_batch(
    client: genai.Client,
    model: str,
    system_prompt: str,
    events: list[dict],
    start_idx: int,
) -> list[str]:
    """Translate a batch of events via Gemini, with retry on high miss rate."""
    user_content = format_batch_input(events, start_idx)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=model,
                contents=user_content,
                config=GenerateContentConfig(
                    system_instruction=system_prompt,
                    response_mime_type="application/json",
                    response_schema=list[TranslatedSubtitle],
                    temperature=0.1,
                ),
            )
        except Exception as e:
            if attempt < MAX_RETRIES:
                print(f"  API error: {e.__class__.__name__}, retrying in 5s...", file=sys.stderr)
                time.sleep(5)
                continue
            raise

        result = parse_structured_response(response.text, len(events), start_idx)
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
        for line in result.stdout.strip().splitlines()[-3:]:
            print(f"  {line}")
    else:
        print(f"  Warning: comparison report failed: {result.stderr[:200]}", file=sys.stderr)

    print(f"\nTranslation complete: {output_path}")


if __name__ == "__main__":
    main()
