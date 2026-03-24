"""Shared ASS (Advanced SubStation Alpha) file parsing and writing utilities."""

import re
from pathlib import Path


# Regex for parsing Dialogue/Comment lines in the Events section.
# Format: Type: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
_EVENT_RE = re.compile(
    r"^(Dialogue|Comment):\s*"
    r"(\d+),"           # Layer
    r"(\d+:\d{2}:\d{2}\.\d{2}),"  # Start
    r"(\d+:\d{2}:\d{2}\.\d{2}),"  # End
    r"([^,]*),"         # Style
    r"([^,]*),"         # Name
    r"(\d+),"           # MarginL
    r"(\d+),"           # MarginR
    r"(\d+),"           # MarginV
    r"([^,]*),"         # Effect
    r"(.*)"             # Text (may contain commas)
)


def timestamp_to_seconds(ts: str) -> float:
    """Convert ASS timestamp 'H:MM:SS.CC' to float seconds."""
    h, m, rest = ts.split(":")
    s, cs = rest.split(".")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(cs) / 100


def seconds_to_timestamp(seconds: float) -> str:
    """Convert float seconds to ASS timestamp 'H:MM:SS.CC'."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = round((seconds % 1) * 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def parse_ass(path: str | Path) -> dict:
    """Parse an ASS file into structured data.

    Returns a dict with:
        - script_info: str (everything from [Script Info] to next section)
        - garbage: str (Aegisub Project Garbage section, if present)
        - styles_header: str (the Format line from [V4+ Styles])
        - styles: list[str] (raw Style lines)
        - events_header: str (the Format line from [Events])
        - events: list[dict] (parsed event lines)
        - raw_lines: list[str] (original file lines, for faithful reproduction)
    """
    text = Path(path).read_text(encoding="utf-8-sig")
    lines = text.splitlines()

    result = {
        "script_info": "",
        "garbage": "",
        "styles_header": "",
        "styles": [],
        "events_header": "",
        "events": [],
        "raw_lines": lines,
    }

    section = None
    script_info_lines = []
    garbage_lines = []

    for line in lines:
        stripped = line.strip()

        # Section headers
        if stripped == "[Script Info]":
            section = "script_info"
            script_info_lines.append(line)
            continue
        elif stripped == "[Aegisub Project Garbage]":
            section = "garbage"
            garbage_lines.append(line)
            continue
        elif stripped == "[V4+ Styles]":
            section = "styles"
            continue
        elif stripped == "[Events]":
            section = "events"
            continue
        elif stripped.startswith("[") and stripped.endswith("]"):
            section = "other"
            continue

        if section == "script_info":
            script_info_lines.append(line)
        elif section == "garbage":
            garbage_lines.append(line)
        elif section == "styles":
            if stripped.startswith("Format:"):
                result["styles_header"] = line
            elif stripped.startswith("Style:"):
                result["styles"] = result["styles"] + [line]
        elif section == "events":
            if stripped.startswith("Format:"):
                result["events_header"] = line
            else:
                m = _EVENT_RE.match(stripped)
                if m:
                    result["events"].append({
                        "type": m.group(1),
                        "layer": int(m.group(2)),
                        "start": m.group(3),
                        "end": m.group(4),
                        "style": m.group(5),
                        "name": m.group(6),
                        "marginl": int(m.group(7)),
                        "marginr": int(m.group(8)),
                        "marginv": int(m.group(9)),
                        "effect": m.group(10),
                        "text": m.group(11),
                    })

    result["script_info"] = "\n".join(script_info_lines)
    result["garbage"] = "\n".join(garbage_lines)

    return result


def write_ass(data: dict, path: str | Path):
    """Write structured ASS data back to a file.

    Reproduces the file faithfully from parsed sections.
    """
    out = []

    # Script Info
    if data["script_info"]:
        out.append(data["script_info"])
        out.append("")

    # Aegisub Project Garbage
    if data.get("garbage"):
        out.append(data["garbage"])
        out.append("")

    # Styles
    out.append("[V4+ Styles]")
    if data["styles_header"]:
        out.append(data["styles_header"])
    for style in data["styles"]:
        out.append(style)
    out.append("")

    # Events
    out.append("[Events]")
    if data["events_header"]:
        out.append(data["events_header"])
    for event in data["events"]:
        line = (
            f"{event['type']}: {event['layer']},"
            f"{event['start']},{event['end']},"
            f"{event['style']},{event['name']},"
            f"{event['marginl']},{event['marginr']},{event['marginv']},"
            f"{event['effect']},{event['text']}"
        )
        out.append(line)
    out.append("")

    Path(path).write_text("\n".join(out), encoding="utf-8")


def extract_dialogue_lines(events: list[dict]) -> list[dict]:
    """Extract Dialogue events (not Comments) with timing as floats.

    Returns list of dicts compatible with quality_report.py:
        {start: float, end: float, style: str, text: str}
    """
    return [
        {
            "start": timestamp_to_seconds(e["start"]),
            "end": timestamp_to_seconds(e["end"]),
            "style": e["style"],
            "text": e["text"],
        }
        for e in events
        if e["type"] == "Dialogue"
    ]
