"""OCR in-game story text boxes (speaker name + typewriter dialogue) into speaker-tagged cues.

Usage: ocr_textboxes.py VIDEO OUT.json START END [START END ...]   (seconds)
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from ocrmac import ocrmac

FPS = 4
CROP = "crop=1600:230:180:760"  # text box on 1920x1080
NAME_MIN_Y = 0.6  # Vision boxes are bottom-origin; the name tag sits above the dialogue


def read(frame: Path) -> tuple[str, str]:
    res = ocrmac.OCR(str(frame), framework="livetext", language_preference=["ja-JP"]).recognize()
    name = "".join(t for t, _, b in res if b[1] >= NAME_MIN_Y).strip()
    # Group body glyphs into lines by y, then read lines top-down.
    lines: dict[float, list[tuple[float, str]]] = {}
    for t, _, b in res:
        if b[1] < NAME_MIN_Y:
            key = next((k for k in lines if abs(k - b[1]) < 0.08), b[1])
            lines.setdefault(key, []).append((b[0], t))
    body = "".join(
        "".join(t for _, t in sorted(glyphs)) for _, glyphs in sorted(lines.items(), reverse=True)
    )
    return name, body


def main(video: str, out: str, spans: list[float]) -> None:
    cues = []
    for start, end in zip(spans[::2], spans[1::2]):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(
                ["ffmpeg", "-v", "error", "-ss", str(start), "-to", str(end), "-i", video,
                 "-vf", f"fps={FPS},{CROP}", f"{tmp}/%05d.png"],
                check=True,
            )
            cur = None
            for i, f in enumerate(sorted(Path(tmp).glob("*.png"))):
                t = start + i / FPS
                name, body = read(f)
                if not body:
                    if cur:
                        cues.append(cur)
                        cur = None
                    continue
                # Typewriter growth: same speaker and one reading extends the other.
                if cur and name == cur["speaker"] and (
                    body.startswith(cur["text"][:3]) or cur["text"].startswith(body[:3])
                ):
                    if len(body) >= len(cur["text"]):
                        cur["text"] = body
                    cur["end"] = t + 1 / FPS
                    continue
                if cur:
                    cues.append(cur)
                cur = {"start": t, "end": t + 1 / FPS, "speaker": name, "text": body}
            if cur:
                cues.append(cur)
    Path(out).write_text(json.dumps(cues, ensure_ascii=False, indent=2), encoding="utf-8")
    for c in cues:
        print(f"{c['start']:7.2f}-{c['end']:7.2f} [{c['speaker']}] {c['text']}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3:]])
