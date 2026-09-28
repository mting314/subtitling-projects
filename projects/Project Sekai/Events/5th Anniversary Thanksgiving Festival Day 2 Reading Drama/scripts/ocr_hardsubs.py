"""OCR burned-in subtitles into an SRT.

Crops the subtitle band, samples at FPS, OCRs with macOS Live Text only when the
white-text mask changes, and merges consecutive identical readings into cues.
"""

import difflib
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

import numpy as np
from ocrmac import ocrmac
from PIL import Image

FPS = 5
CROP = "crop=1500:120:210:960"  # w:h:x:y on 1920x1080; excludes ABEMA/bilibili marks
WHITE = 215  # text fill threshold
MIN_TEXT_PX = 400  # below this many white pixels, assume no subtitle
MASK_CHANGE = 0.02  # fraction of mask pixels that must flip to re-OCR
MIN_DUR = 0.3


def srt_time(t: float) -> str:
    ms = round(t * 1000)
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def similar(a: str, b: str) -> bool:
    return difflib.SequenceMatcher(None, a, b).ratio() >= 0.8


def main(video: str, out: str) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["ffmpeg", "-v", "error", "-i", video, "-vf", f"fps={FPS},{CROP}",
             f"{tmp}/%06d.png"],
            check=True,
        )
        frames = sorted(Path(tmp).glob("*.png"))
        readings: list[str] = []
        prev_mask, prev_text, ocr_calls = None, "", 0
        for i, f in enumerate(frames):
            gray = np.asarray(Image.open(f).convert("L"))
            mask = gray > WHITE
            if mask.sum() < MIN_TEXT_PX:
                text = ""
            elif prev_mask is not None and prev_text and (
                (mask ^ prev_mask).mean() < MASK_CHANGE
            ):
                text = prev_text
            else:
                res = ocrmac.OCR(str(f), framework="livetext").recognize()
                text = "".join(t for t, _, _ in res).strip()
                ocr_calls += 1
            readings.append(text)
            prev_mask, prev_text = mask, text
            if i % 500 == 0:
                print(f"  {i}/{len(frames)} frames, {ocr_calls} OCR calls", file=sys.stderr)

    # Merge runs of similar readings into cues; take the most common reading as text.
    cues, start, run = [], None, []
    for i, text in enumerate(readings + [""]):
        if run and (not text or not similar(text, run[-1])):
            s, e = start / FPS, i / FPS
            if e - s >= MIN_DUR:
                cues.append((s, e, Counter(run).most_common(1)[0][0]))
            run, start = [], None
        if text:
            if start is None:
                start = i
            run.append(text)

    with open(out, "w", encoding="utf-8") as fh:
        for n, (s, e, text) in enumerate(cues, 1):
            fh.write(f"{n}\n{srt_time(s)} --> {srt_time(e)}\n{text}\n\n")
    print(f"{len(cues)} cues, {ocr_calls} OCR calls -> {out}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
