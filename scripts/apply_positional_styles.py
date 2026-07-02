#!/usr/bin/env python3
"""Apply positional subtitle styles (PiP / song-shift) to an .ass file.

Deterministic mechanics only — this script never guesses style names. The caller
(a human or the positional-styles skill) resolves the fuzzy part (which styles in
this file play the PiP / song-shift roles, since names differ per character/episode)
and passes them explicitly.

For each role it copies ONLY the layout fields (Alignment, MarginL, MarginR,
MarginV) from a reference style into the target style — color, font, bold, outline,
and shadow are preserved so the look stays consistent with the episode's main style.
PiP roles additionally get a ``{\\pos(x,y)}`` tag prepended to every *Dialogue* line
using that style (Comment lines and lines already carrying a ``\\pos`` are skipped).

Idempotent: re-running produces no further changes.

Usage:
    apply_positional_styles.py TARGET.ass \\
        --reference "Colors of Pure Sense_translated.ass" \\
        --pip   "Saki - PiP:PiP:650,750" \\
        --shift "Saki - Side Song:DefaultOnibe - Shifted" \\
        [--dry-run]

Mapping format (style names must not contain ':'):
    --pip    TARGET_STYLE:REF_STYLE[:X,Y]   (X,Y default 650,750)
    --shift  TARGET_STYLE:REF_STYLE          (no pos tag — style margins do the work)

Both flags are repeatable (e.g. multiple characters).
"""
from __future__ import annotations

import argparse
import sys

# Layout fields copied from reference -> target. Everything else is preserved.
LAYOUT_FIELDS = ("Alignment", "MarginL", "MarginR", "MarginV")
DEFAULT_POS = (650, 750)


def _parse_styles(text: str):
    """Return (format_fields, {style_name: [field_values]}) from [V4+ Styles]."""
    fmt = None
    styles = {}
    in_section = False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("[") and s.endswith("]"):
            in_section = s.lower() == "[v4+ styles]"
            continue
        if not in_section:
            continue
        if s.startswith("Format:"):
            fmt = [f.strip() for f in s[len("Format:"):].split(",")]
        elif s.startswith("Style:"):
            vals = s[len("Style:"):].split(",")
            vals = [v.strip() for v in vals]
            if fmt and vals:
                styles[vals[0]] = vals
    return fmt, styles


def _events_layout(text: str):
    """Return (style_col_index, num_fields) from the [Events] Format line."""
    in_section = False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("[") and s.endswith("]"):
            in_section = s.lower() == "[events]"
            continue
        if in_section and s.startswith("Format:"):
            fields = [f.strip() for f in s[len("Format:"):].split(",")]
            return fields.index("Style"), len(fields)
    raise ValueError("No [Events] Format line found")


def _parse_mapping(raw: str, want_pos: bool):
    parts = raw.split(":")
    if len(parts) < 2:
        sys.exit(f"ERROR: bad mapping {raw!r} — need TARGET_STYLE:REF_STYLE[:X,Y]")
    target, ref = parts[0], parts[1]
    pos = None
    if want_pos:
        if len(parts) >= 3 and parts[2]:
            try:
                x, y = (int(n) for n in parts[2].split(","))
            except ValueError:
                sys.exit(f"ERROR: bad coordinate in {raw!r} — expected X,Y")
            pos = (x, y)
        else:
            pos = DEFAULT_POS
    return target, ref, pos


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="the _translated.ass file to edit in place")
    ap.add_argument("--reference", required=True,
                    help="known-good .ass to copy layout fields from")
    ap.add_argument("--pip", action="append", default=[],
                    metavar="TARGET:REF[:X,Y]",
                    help="PiP role: copy layout + prepend {\\pos(X,Y)} to its lines")
    ap.add_argument("--shift", action="append", default=[],
                    metavar="TARGET:REF",
                    help="song-shift role: copy layout only (no pos tag)")
    ap.add_argument("--dry-run", action="store_true",
                    help="report changes without writing")
    args = ap.parse_args(argv)

    if not args.pip and not args.shift:
        ap.error("provide at least one --pip or --shift mapping")

    target_text = open(args.target, encoding="utf-8").read()
    ref_text = open(args.reference, encoding="utf-8").read()

    _, ref_styles = _parse_styles(ref_text)
    tgt_fmt, tgt_styles = _parse_styles(target_text)
    if not tgt_fmt:
        sys.exit("ERROR: target has no [V4+ Styles] Format line")
    idx = {f: tgt_fmt.index(f) for f in LAYOUT_FIELDS}

    pip_maps = [_parse_mapping(m, want_pos=True) for m in args.pip]
    shift_maps = [_parse_mapping(m, want_pos=False) for m in args.shift]

    # ---- 1. Rewrite target style headers (layout fields only) ----
    # style name -> new field-value list (only recompute changed styles)
    new_style_vals = {}
    style_changes = []  # (name, [(field, old, new)])
    for target, ref, _ in pip_maps + shift_maps:
        if target not in tgt_styles:
            sys.exit(f"ERROR: target style {target!r} not found in {args.target}")
        if ref not in ref_styles:
            sys.exit(f"ERROR: reference style {ref!r} not found in {args.reference}")
        vals = list(tgt_styles[target])
        diffs = []
        for f in LAYOUT_FIELDS:
            old = vals[idx[f]]
            new = ref_styles[ref][idx[f]]
            if old != new:
                diffs.append((f, old, new))
            vals[idx[f]] = new
        new_style_vals[target] = vals
        style_changes.append((target, ref, diffs))

    # ---- 2. Prepend \pos to PiP dialogue lines ----
    style_col, n_events_fields = _events_layout(target_text)
    pip_pos = {target: pos for target, _, pos in pip_maps}

    out_lines = []
    pos_added = {t: 0 for t in pip_pos}
    pos_skipped = {t: 0 for t in pip_pos}
    for line in target_text.split("\n"):
        # rewrite style header lines
        if line.strip().startswith("Style:"):
            name = line.split(":", 1)[1].split(",", 1)[0].strip()
            if name in new_style_vals:
                line = "Style: " + ",".join(new_style_vals[name])
            out_lines.append(line)
            continue
        # prepend \pos to matching Dialogue lines (Comment lines untouched)
        if line.startswith("Dialogue:"):
            body = line[len("Dialogue:"):]
            parts = body.split(",", n_events_fields - 1)
            if len(parts) == n_events_fields:
                style = parts[style_col].strip()
                if style in pip_pos:
                    text = parts[-1]
                    if "\\pos(" in text:
                        pos_skipped[style] += 1
                    else:
                        x, y = pip_pos[style]
                        parts[-1] = f"{{\\pos({x},{y})}}" + text
                        line = "Dialogue:" + ",".join(parts)
                        pos_added[style] += 1
        out_lines.append(line)

    new_text = "\n".join(out_lines)

    # ---- report ----
    print(f"Target:    {args.target}")
    print(f"Reference: {args.reference}\n")
    for target, ref, diffs in style_changes:
        role = "PiP" if target in pip_pos else "shift"
        if diffs:
            desc = ", ".join(f"{f} {o}->{n}" for f, o, n in diffs)
            print(f"  [{role}] {target}  <- {ref}: {desc}")
        else:
            print(f"  [{role}] {target}  <- {ref}: already matches (no change)")
    for target, pos in pip_pos.items():
        print(f"  [PiP] {target}: +{{\\pos{pos}}} on {pos_added[target]} lines"
              f" (skipped {pos_skipped[target]} already-positioned)")

    changed = new_text != target_text
    if not changed:
        print("\nNo changes needed — file already correct.")
        return
    if args.dry_run:
        print("\n[dry-run] would write the above changes.")
        return
    open(args.target, "w", encoding="utf-8").write(new_text)
    print("\nWrote changes.")


if __name__ == "__main__":
    main()
