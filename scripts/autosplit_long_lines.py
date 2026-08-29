#!/usr/bin/env python3
"""Auto-fix 3+ row subtitle lines by splitting them at real clause boundaries.

Drives `detect_long_lines.py` (to find offenders) and `split_subtitle_line.py` (to split
each near its midpoint), looping until nothing improves. Lines with no safe boundary are
left for you to reword by hand, and the result is audited for stranded conjunctions.

WHERE TO BREAK — this encodes the Netflix Timed Text Style Guide line-break rules
(the de-facto industry standard; BBC's guidelines and the academic subtitle-segmentation
literature — Karakanta et al., MuST-Cinema — say the same):
    Break: after punctuation · before conjunctions · before prepositions.
    NEVER separate: article/adjective from noun · first from last name · verb from its
    subject pronoun · a prepositional verb from its preposition · a verb from an auxiliary,
    reflexive pronoun, or negation.

Two engines pick the boundary:
  - **dep** (default, preferred): a spaCy dependency parse. Only breaks where the two sides
    are separate subtrees — structurally guaranteeing none of the "never separate" pairs are
    split (this is the "syntactically aware segmentation" the literature recommends).
  - **regex**: a dependency-free approximation (sentence ends, commas, comma-gated
    coordinators, no infinitive "to"). Used automatically if spaCy/model aren't installed.

Usage (dep engine needs spaCy + the small English model):
    uv run --with pillow --with numpy --with spacy --with click \
        --with "en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl" \
        python3 scripts/autosplit_long_lines.py "<name>_translated.ass" \
        --transcript "<name>_transcript.json" [--apply]

    # regex engine only (no spaCy):
    uv run --with pillow --with numpy python3 scripts/autosplit_long_lines.py \
        "<name>_translated.ass" --transcript "<name>_transcript.json" --engine regex [--apply]
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

COORD = ("and", "but", "so", "or", "yet", "nor")
SUBORD = ("because", "when", "while", "since", "although", "though",
          "which", "where", "who", "that", "if")
COMPLEMENTIZERS = {"that", "how", "why", "what", "whether", "if", "when", "where", "who"}

# Proper nouns a break must never fall inside. spaCy tokenises on the internal
# punctuation, so "Leo/need" looks like two words and a boundary can land between
# them, leaving a line ending in "Leo/". Matched case-insensitively.
ATOMIC_TERMS = (
    "Leo/need",
    "Wonderlands\u00d7Showtime", "Wonderlands x Showtime",
    "MORE MORE JUMP!", "MORE MORE JUMP",
    "Vivid BAD SQUAD",
    "25-ji, Nightcord de.", "Nightcord at 25:00",
    "Virtual Singer",
    "Hatsune Miku", "Kagamine Rin", "Kagamine Len", "Megurine Luka",
)


def _atomic_spans(prose):
    """Character ranges of any atomic term occurring in prose."""
    low = prose.lower()
    spans = []
    for term in ATOMIC_TERMS:
        t = term.lower()
        start = low.find(t)
        while start != -1:
            spans.append((start, start + len(t)))
            start = low.find(t, start + 1)
    return spans


def _splits_atomic(prose, idx, spans=None):
    """True when breaking at idx would cut through one of those names."""
    for a, b in (_atomic_spans(prose) if spans is None else spans):
        if a < idx < b:
            return True
    return False
SENT_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'])|(?<=\.\.\.)\s+")

# Dependency labels that bind two tokens into one tight unit — a subtitle break must never
# fall between them (encodes the Netflix "never separate" list structurally).
HARD_TIGHT = {
    "det", "poss", "predet", "amod", "compound", "nummod", "flat", "fixed", "aux", "auxpass",
    "cop", "neg", "prt", "case", "nsubj", "nsubjpass", "csubj", "csubjpass", "expl", "dobj",
    "dative", "attr", "acomp", "oprd", "agent", "nmod", "appos", "pcomp", "pobj", "quantmod",
}

# cognition/speech verbs that take a (often that-less) complement; ending a line on one
# strands the complement ("I really felt | they wrote…").
COMPLEMENT_VERBS = {
    "felt", "feel", "feels", "think", "thinks", "thought", "know", "knows", "knew",
    "believe", "believed", "realize", "realized", "said", "say", "says", "hope", "hoped",
    "wish", "wished", "guess", "suppose", "mean", "meant", "see", "saw", "notice", "noticed",
    "find", "found", "heard", "hear", "wonder", "wondered", "assume", "assumed", "decided",
    "remember", "remembered", "imagine", "imagined", "figured", "worried",
}


def _strip_tags(text):
    return re.sub(r"\{[^}]*\}", "", text)


def _load_nlp():
    try:
        import spacy
        return spacy.load("en_core_web_sm")
    except Exception:
        return None


def pick_boundary_dep(nlp, text, min_share):
    """spaCy dependency-parse boundary picker. Returns the substring that begins line B."""
    prose = _strip_tags(text)
    doc = nlp(prose)
    toks = list(doc)
    n = len(prose)
    if n < 20 or len(toks) < 4:
        return None
    atomic = _atomic_spans(prose)
    best = None
    for k in range(1, len(toks)):
        tk = toks[k]
        idx = tk.idx
        if not (min_share * n <= idx <= (1 - min_share) * n):
            continue
        if _splits_atomic(prose, idx, atomic):
            continue
        if tk.tag_ == "TO":                                   # infinitive marker
            continue
        if (tk.dep_ == "cc" or tk.pos_ == "CCONJ" or tk.text.lower() in COORD) \
                and toks[k - 1].text != ",":                  # coordinator needs a comma
            continue
        if toks[k - 1].text.lower() in COORD:                 # no dangling 'and'/'but' at line end
            continue
        crossing = [t for t in doc if min(t.head.i, t.i) < k <= max(t.head.i, t.i)]
        forbid = False
        for t in crossing:
            if t.dep_ in HARD_TIGHT:
                forbid = True
                break
            if t.dep_ in ("ccomp", "xcomp"):                  # verb | bare complement
                first = min(t.subtree, key=lambda x: x.i)
                if first.i == k and tk.dep_ != "mark" and tk.tag_ != "WDT" \
                        and tk.text.lower() not in COMPLEMENTIZERS:
                    forbid = True
                    break
        if forbid:
            continue
        prev = toks[k - 1]
        score = 0.0
        if prev.is_punct or prev.text in ".!?":
            score -= 100
        if tk.dep_ in ("mark", "advcl", "cc", "conj", "relcl", "parataxis", "prep", "advmod"):
            score -= 30
        score += len(crossing) * 5
        score += abs(idx - n / 2) * 0.1
        b = prose[idx:].strip()
        if len(b) > 3 and (best is None or score < best[0]):
            best = (score, b)
    return best[1] if best else None


def pick_boundary_regex(text, min_share):
    """Dependency-free fallback: sentence ends > commas > comma-gated coordinators > subordinators."""
    prose = _strip_tags(text)
    n = len(prose)
    if n < 20:
        return None
    mid = n / 2
    lo, hi = min_share * n, (1 - min_share) * n
    cands = []
    for m in SENT_END.finditer(prose):
        cands.append((m.end(), prose[m.end():], 0))
    for m in re.finditer(r", ", prose):
        cands.append((m.end(), prose[m.end():], 1))
    for c in COORD:
        for m in re.finditer(rf", {c} ", prose):
            i = m.start() + 2
            cands.append((i, prose[i:], 2))
    for c in SUBORD:
        for m in re.finditer(rf"\b{c} ", prose):
            i = m.start()
            if i:
                cands.append((i, prose[i:], 3))
    atomic = _atomic_spans(prose)
    cands = [(i, b, pr) for (i, b, pr) in cands
             if lo <= i <= hi and len(b.strip()) > 3 and not _splits_atomic(prose, i, atomic)]
    if not cands:
        return None
    i, b, pr = min(cands, key=lambda t: (abs(t[0] - mid), t[2]))
    return b.strip()


def _flagged(ass, flag_over):
    r = subprocess.run(
        ["uv", "run", "--with", "pillow", "--with", "numpy", "python3", str(DETECT),
         str(ass), "--flag-over", str(flag_over)],
        capture_output=True, text=True)
    return [int(m.group(1)) for ln in r.stdout.splitlines()
            if "FLAG" in ln and (m := re.match(r"\s*(\d+)\s+\d+:\d+:", ln))]


def audit_pairs(ass):
    """Flag split pairs that strand a conjunction / break a phrase (safety net)."""
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
        if st1 != st2 or e1 != s2 or not t1 or not t2:
            continue
        t1r = t1.rstrip()
        if t1r.rstrip('"\'').endswith((".", "!", "?")):     # sentence boundary — fine
            continue
        first_raw = t2.split()[0]
        first = first_raw.lower().strip('.,!?"\'')
        cont = first_raw[:1].islower()
        lastword = re.sub(r"[^a-zA-Z']", "", t1.split()[-1]).lower()
        if lastword in COMPLEMENT_VERBS and cont and not t1r.endswith((",", "-", "—")):
            bad.append((n2, f"verb '{lastword}' split from its complement"))
        elif first == "to":
            bad.append((n2, "mid-sentence 'to' (infinitive/prep split)"))
        elif first in ("and", "or") and not t1r.endswith(","):
            bad.append((n2, f"mid-sentence '{first}' with no preceding comma"))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description="Auto-split 3+ row lines at clause boundaries.")
    ap.add_argument("ass", type=Path)
    ap.add_argument("--transcript", type=Path, help="transcript.json for pause-snapped timing")
    ap.add_argument("--flag-over", type=int, default=2)
    ap.add_argument("--min-share", type=float, default=0.3)
    ap.add_argument("--engine", choices=("dep", "regex"), default="dep")
    ap.add_argument("--apply", action="store_true", help="write splits (default: dry-run)")
    args = ap.parse_args()
    if not args.ass.exists():
        print(f"Error: {args.ass} not found", file=sys.stderr)
        return 1

    nlp = _load_nlp() if args.engine == "dep" else None
    if args.engine == "dep" and nlp is None:
        print("spaCy/en_core_web_sm not available — falling back to regex engine.", file=sys.stderr)
    engine = "dep" if nlp else "regex"
    pick = (lambda t: pick_boundary_dep(nlp, t, args.min_share)) if nlp \
        else (lambda t: pick_boundary_regex(t, args.min_share))
    print(f"engine: {engine}")

    flagged = _flagged(args.ass, args.flag_over)
    print(f"{len(flagged)} line(s) over {args.flag_over} rows")
    if not flagged:
        return 0
    lines = args.ass.read_text(encoding="utf-8").split("\n")
    plan, reword = [], []
    for nline in flagged:
        b = pick(lines[nline - 1].split(",", 9)[9])
        (plan if b else reword).append((nline, b))
    for nline, b in plan:
        print(f"  split L{nline} @ {b[:46]!r}")
    for nline, _ in reword:
        print(f"  REWORD L{nline}: {_strip_tags(lines[nline-1].split(',',9)[9]).strip()[:58]!r}")

    if not args.apply:
        print("\n[dry-run] pass --apply to write; reword the REWORD lines by hand after.")
        return 0

    tcmd = ["--transcript", str(args.transcript)] if args.transcript else []
    done = 0
    for nline, b in sorted(plan, reverse=True):
        r = subprocess.run(["python3", str(SPLIT), str(args.ass), "--line", str(nline),
                            "--before", b, *tcmd], capture_output=True, text=True)
        if r.returncode == 0:
            done += 1
        else:
            print(f"  L{nline} split failed: {r.stderr.strip()[-70:]}")
    print(f"\napplied {done} split(s)")
    remaining = _flagged(args.ass, args.flag_over)
    if remaining:
        print(f"still {len(remaining)} over-length (reword): {remaining}")
    bad = audit_pairs(args.ass)
    print("audit: clean" if not bad else "AUDIT — review these pairs:")
    for n2, why in bad:
        print(f"  L{n2}: {why}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
