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

import yaml
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel

from utils.ass_parser import parse_ass, write_ass


DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_BATCH_SIZE = 50
DEFAULT_INSTRUCTIONS_PATH = "translation_instructions.md"


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

Follow the translation instructions and project reference below."""


def load_text_file(path: str) -> str | None:
    """Load a text file, returning None if it doesn't exist."""
    p = Path(path)
    if p.is_file():
        return p.read_text(encoding="utf-8")
    return None


def load_speaker_files(ref_path: Path) -> list[dict]:
    """Auto-discover and load speakers/*.yaml files relative to a reference file."""
    speakers_dir = ref_path.parent / "speakers"
    if not speakers_dir.is_dir():
        return []
    speakers = []
    for f in sorted(speakers_dir.glob("*.yaml")):
        with open(f, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
            if data:
                speakers.append(data)
    return speakers


def format_yaml_reference(data: dict, speakers: list[dict]) -> str:
    """Format parsed YAML reference data into targeted prompt sections."""
    sections = []

    # Project context
    project = data.get("project", {})
    if project:
        lines = [f"## Project: {project.get('name', 'Unknown')}"]
        if project.get("description"):
            lines.append(project["description"])
        if project.get("franchise"):
            lines.append(f"Franchise: {project['franchise']}")
        sections.append("\n".join(lines))

    # Glossary
    glossary = data.get("glossary", [])
    if glossary:
        lines = [
            "## Glossary",
            "Use these translations for the following terms:",
        ]
        for entry in glossary:
            line = f"- {entry['term']} → {entry['translation']}"
            if entry.get("notes"):
                line += f" ({entry['notes']})"
            lines.append(line)
        sections.append("\n".join(lines))

    # Segments
    segments = data.get("segments", [])
    if segments:
        lines = [
            "## Segment Names",
            "These are segment/section markers in the show:",
        ]
        for entry in segments:
            lines.append(f"- {entry['term']} → {entry['translation']}")
        sections.append("\n".join(lines))

    # Replacements
    replacements = data.get("replacements", [])
    if replacements:
        lines = [
            "## Fixed Translations",
            "Use these exact translations for recurring scripted lines "
            "(allow for minor transcription variations):",
        ]
        for entry in replacements:
            line = f"- {entry['original']} → {entry['translation']}"
            if entry.get("context"):
                line += f" [{entry['context']}]"
            lines.append(line)
        sections.append("\n".join(lines))

    # Speakers (merged from inline + speaker files)
    inline_speakers = data.get("speakers", [])
    all_speakers = inline_speakers + speakers
    if all_speakers:
        lines = [
            "## Speaker Profiles",
            "Speaker profiles for voice and style reference. "
            "Prioritize translation accuracy over matching speaker tone.",
        ]
        for speaker in all_speakers:
            name = speaker.get("name", "Unknown")
            name_jp = speaker.get("name_jp", "")
            nickname = speaker.get("nickname", "")
            header = name
            if name_jp:
                header += f" ({name_jp})"
            if nickname:
                header += f" — {nickname}"
            lines.append(f"\n**{header}**")
            for role in speaker.get("roles", []):
                char = role.get("character", "")
                char_jp = role.get("character_jp", "")
                unit = role.get("unit", "")
                style = role.get("style", "")
                greeting = role.get("greeting", "")
                role_line = f"  - Character: {char}"
                if char_jp:
                    role_line += f" ({char_jp})"
                if unit:
                    role_line += f" | Unit: {unit}"
                lines.append(role_line)
                if style:
                    lines.append(f"    Style: {style}")
                if greeting:
                    lines.append(f"    Greeting: {greeting}")
        sections.append("\n".join(lines))

    # Notes
    notes = data.get("notes")
    if notes:
        sections.append(f"## Additional Notes\n{notes.strip()}")

    # Hosts
    hosts = data.get("hosts", [])
    if hosts:
        lines = ["## Hosts"]
        for h in hosts:
            lines.append(
                f"- {h.get('aftertalk', '')}: {h.get('host', '')} ({h.get('unit', '')})"
            )
        sections.append("\n".join(lines))

    return "\n\n".join(sections)


def build_system_prompt(
    instructions_path: str,
    project_ref_path: str | None,
) -> str:
    """Build the system instruction from translation context files.

    Supports both YAML (.yaml) and legacy markdown (.md) reference files.
    YAML files are parsed into structured prompt sections with auto-discovered
    speaker profiles from speakers/*.yaml.
    """
    parts = [SYSTEM_PREAMBLE]

    instructions = load_text_file(instructions_path)
    if instructions:
        parts.append(instructions)
    else:
        print(
            f"  Warning: instructions file not found: {instructions_path}",
            file=sys.stderr,
        )

    if project_ref_path:
        ref_p = Path(project_ref_path)
        if not ref_p.is_file():
            print(
                f"  Warning: project reference not found: {project_ref_path}",
                file=sys.stderr,
            )
        elif ref_p.suffix in (".yaml", ".yml"):
            with open(ref_p, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            speakers = load_speaker_files(ref_p)
            formatted = format_yaml_reference(data, speakers)
            parts.append(formatted)
        else:
            project_ref = ref_p.read_text(encoding="utf-8")
            parts.append(project_ref)

    return "\n\n---\n\n".join(parts)


def format_batch_input(events: list[dict], start_idx: int) -> str:
    """Format dialogue events as a JSON array for the Gemini prompt."""
    items = []
    for i, event in enumerate(events):
        items.append(
            {
                "id": start_idx + i + 1,
                "style": event["style"],
                "text": event["text"],
            }
        )
    return json.dumps(items, ensure_ascii=False)


def parse_structured_response(
    response_text: str, expected_count: int, start_idx: int
) -> list[str]:
    """Parse structured JSON response into ordered translation list.

    Expects a JSON array of {id, original, translated} objects.
    Falls back gracefully if the structure is slightly off.
    """
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        print("  Warning: response is not valid JSON", file=sys.stderr)
        return [""] * expected_count

    if not isinstance(data, list):
        print("  Warning: response is not a JSON array", file=sys.stderr)
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
        print(
            f"  Warning: {missing}/{expected_count} lines missing from response",
            file=sys.stderr,
        )

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
                print(
                    f"  API error: {e.__class__.__name__}, retrying in 5s...",
                    file=sys.stderr,
                )
                time.sleep(5)
                continue
            raise

        result = parse_structured_response(response.text, len(events), start_idx)
        missing = sum(1 for t in result if t == "")
        if missing == 0 or attempt == MAX_RETRIES:
            return result
        print(
            f"  Retrying batch (attempt {attempt + 1}/{MAX_RETRIES}, {missing} missing)..."
        )
        time.sleep(2)

    return result


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Translate Japanese ASS subtitles to English using Gemini. "
        "Preserves timing, styles, and formatting. Sends lines in batches."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Source ASS file (Japanese)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output ASS file (English). Default: {input_stem}_en.ass",
    )
    parser.add_argument(
        "--project",
        default=None,
        help="Path to project translation_reference.yaml (or legacy .md)",
    )
    parser.add_argument(
        "--instructions",
        default=DEFAULT_INSTRUCTIONS_PATH,
        help=f"Path to translation instructions (default: {DEFAULT_INSTRUCTIONS_PATH})",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Gemini model to use (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=f"Lines per API request (default: {DEFAULT_BATCH_SIZE})",
    )
    parser.add_argument(
        "--project-id",
        default=None,
        help="GCP project ID (default: $GOOGLE_CLOUD_PROJECT)",
    )
    parser.add_argument(
        "--video",
        default=None,
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

    output_path = (
        Path(args.output)
        if args.output
        else input_path.with_stem(input_path.stem + "_en")
    )

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
    print("\n[4/4] Writing translated ASS file...")
    for idx, translation in zip(dialogue_indices, all_translations):
        data["events"][idx]["text"] = translation

    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_ass(data, output_path)
    print(f"  Generated: {output_path}")

    # Auto-run comparison report
    print("\n  Generating comparison report...")
    compare_args = [
        sys.executable,
        "compare_translations.py",
        "--source",
        str(input_path),
        "--translated",
        str(output_path),
    ]
    if args.video:
        compare_args.extend(["--video", args.video])

    import subprocess

    result = subprocess.run(compare_args, capture_output=True, text=True)
    if result.returncode == 0:
        for line in result.stdout.strip().splitlines()[-3:]:
            print(f"  {line}")
    else:
        print(
            f"  Warning: comparison report failed: {result.stderr[:200]}",
            file=sys.stderr,
        )

    print(f"\nTranslation complete: {output_path}")


if __name__ == "__main__":
    main()
