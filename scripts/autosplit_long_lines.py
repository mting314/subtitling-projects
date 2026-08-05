#!/usr/bin/env python3
"""Auto-fix 3+ row subtitle lines by splitting them at real clause boundaries.

Drives `detect_long_lines.py` (to find offenders) and `split_subtitle_line.py` (to split
each at a boundary near its midpoint), looping until nothing improves. Lines with no safe
boundary are left for you to reword by hand. Finally it audits every split pair for a
stranded conjunction / broken phrase.

Boundary rules (learned the hard way — see the Gazing pass):
  - PREFER a sentence end (`. ! ? …`) inside the line, then a comma, then a subordinator.
  - Coordinating conjunctions (and/but/so/or/yet) are only used **with a preceding comma**
    (`, and`). Without the comma, "and" usually joins a phrase, not a clause
    ("both Saki-chan and I", "between X and Y") — splitting there reads wrong.
  - NEVER split before "to": it's almost always an infinitive marker or preposition
    ("able to reach", "going to happen", "the way to do it").
  - Only accept a boundary that leaves both halves within [--min-share, 1-min-share] of
    the line, so neither half is a stranded fragment.

Usage:
    # dry-run: show the plan, change nothing
    uv run --with pillow --with numpy python3 scripts/autosplit_long_lines.py \
        "<name>_translated.ass" --transcript "<name>_transcript.json"

    # apply
    uv run --with pillow --with numpy python3 scripts/autosplit_long_lines.py \
        "<name>_translated.ass" --transcript "<name>_transcript.json" --apply
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
DETECT = SCRIPTS / "detect_long_lines.py"
SPLIT = SCRIPTS / "split_subtitle_line.py"

COORD = ("and", "but", "so", "or", "yet")
SUBORD = ("because", "when", "while", "since", "although", "though",
          "which", "where", "who", "that", "if")
SENT_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'])|(?<=\.\.\.)\s+")


def _strip_tags(text):
    return re.sub(r"\{[^}]*\}", "", text)


def _flagged(ass, flag_over):
    """Return line numbers detect_long_lines.py flags (>flag_over rows)."""
    r = subprocess.run(
        ["uv", "run", "--with", "pillow", "--with", "numpy", "python3", str(DETECT),
         str(ass), "--flag-over", str(flag_over)],
        capture_output=True, text=True)
    nums = []
    for ln in r.stdout.splitlines():
        m = re.match(r"\s*(\d+)\s+\d+:\d+:", ln)
        if m and "FLAG" in ln:
            nums.append(int(m.group(1)))
    return nums


def pick_boundary(text, min_share):
    """Choose the substring that should begin line B, or None if no safe boundary."""
    prose = _strip_tags(text)
    n = len(prose)
    if n < 20:
        return None
    mid = n / 2
    lo, hi = min_share * n, (1 - min_share) * n
    cands = []  # (index_in_prose, B_substring)

    # 1) sentence ends (highest priority)
    for m in SENT_END.finditer(prose):
        cands.append((m.end(), prose[m.end():], 0))
    # 2) comma boundaries
    for m in re.finditer(r", ", prose):
        cands.append((m.end(), prose[m.end():], 1))
    # 3) coordinating conjunctions — ONLY with a preceding comma (", and")
    for c in COORD:
        for m in re.finditer(rf", {c} ", prose):
            i = m.start() + 2  # B starts at the conjunction word
            cands.append((i, prose[i:], 2))
    # 4) subordinators / relatives (no comma required)
    for c in SUBORD:
        for m in re.finditer(rf"\b{c} ", prose):
            i = m.start()
            if i == 0:
                continue
            cands.append((i, prose[i:], 3))
    # NOTE: never split before "to" (infinitive/preposition) — intentionally absent.

    cands = [(i, b, pr) for (i, b, pr) in cands
             if lo <= i <= hi and len(b.strip()) > 3]
    if not cands:
        return None
    # closest to midpoint, tie-broken by priority
    i, b, pr = min(cands, key=lambda t: (abs(t[0] - mid), t[2]))
    return b.strip()


def audit_pairs(ass):
    """Flag split pairs where line B strands a conjunction / breaks a fixed phrase."""
    lines = Path(ass).read_text(encoding="utf-8").split("\n")
    dl = []
    for i, ln in enumerate(lines):
        if ln.startswith("Dialogue:"):
            p = ln.split(",", 9)
            dl.append((i + 1, p[1], p[2], p[3], _strip_tags(p[9]).strip()))
    bad = []
    for a, b in zip(dl, dl[1:]):
        _, s1, e1, st1, t1 = a
        n2, s2, e2, st2, t2 = b
        if st1 != st2 or e1 != s2:
            continue
        # Only a MID-SENTENCE continuation can strand a conjunction. If line 1 ends a
        # sentence (. ! ? possibly + closing quote), line 2's "And"/"To" starts a new
        # sentence — that's fine, not a broken phrase.
        if t1.rstrip().rstrip('"\'').endswith((".", "!", "?")):
            continue
        first = t2.split()[:1]
        first = first[0].lower().strip('.,!?"\'') if first else ""
        if first == "to":
            bad.append((n2, "mid-sentence 'to' (infinitive/prep split)", t1, t2))
        elif first in ("and", "or") and not t1.rstrip().endswith(","):
            bad.append((n2, f"mid-sentence '{first}' with no preceding comma (likely phrase, not clause)", t1, t2))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description="Auto-split 3+ row lines at clause boundaries.")
    ap.add_argument("ass", type=Path)
    ap.add_argument("--transcript", type=Path, help="transcript.json for pause-snapped timing")
    ap.add_argument("--flag-over", type=int, default=2)
    ap.add_argument("--min-share", type=float, default=0.3, help="min fraction each half must keep")
    ap.add_argument("--apply", action="store_true", help="write splits (default: dry-run)")
    args = ap.parse_args()

    if not args.ass.exists():
        print(f"Error: {args.ass} not found", file=sys.stderr)
        return 1

    flagged = _flagged(args.ass, args.flag_over)
    print(f"{len(flagged)} line(s) over {args.flag_over} rows")
    if not flagged:
        return 0

    lines = args.ass.read_text(encoding="utf-8").split("\n")
    plan, reword = [], []
    for n in flagged:
        b = pick_boundary(lines[n - 1].split(",", 9)[9], args.min_share)
        (plan if b else reword).append((n, b))

    for n, b in plan:
        print(f"  split L{n} @ {b[:44]!r}")
    for n, _ in reword:
        txt = _strip_tags(lines[n - 1].split(",", 9)[9]).strip()
        print(f"  REWORD L{n} (no safe boundary): {txt[:60]!r}")

    if not args.apply:
        print("\n[dry-run] pass --apply to write. Reword the REWORD lines by hand afterward.")
        return 0

    # apply splits descending so earlier line numbers stay valid
    tcmd = ["--transcript", str(args.transcript)] if args.transcript else []
    done = 0
    for n, b in sorted(plan, reverse=True):
        r = subprocess.run(["python3", str(SPLIT), str(args.ass), "--line", str(n),
                            "--before", b, *tcmd], capture_output=True, text=True)
        if r.returncode == 0:
            done += 1
        else:
            reword.append((n, None))
            print(f"  L{n} split failed: {r.stderr.strip()[-70:]}")
    print(f"\napplied {done} split(s)")

    remaining = _flagged(args.ass, args.flag_over)
    if remaining:
        print(f"still {len(remaining)} over-length (reword these): {remaining}")
    bad = audit_pairs(args.ass)
    if bad:
        print("\nAUDIT — split pairs to review (stranded conjunction / broken phrase):")
        for n2, why, t1, t2 in bad:
            print(f"  L{n2}: …{t1.strip()[-34:]!r} | {t2.strip()[:34]!r}  <-- {why}")
    else:
        print("audit: no stranded-conjunction split pairs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
