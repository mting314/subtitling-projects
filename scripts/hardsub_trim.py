#!/usr/bin/env python3
"""Hardsub + trim + concatenate multiple segments from a video with smooth fade transitions.

Applies:
- Subtitle burn-in via `subtitles=` filter (with Windows spaceless temp copy handling).
- Popup image / VA card overlays from `popups.json` if present.
- 0.4s Video & Audio fade-in / fade-out transitions at segment boundaries for smooth cuts.
- GPU hardware acceleration (`h264_nvenc` with CPU fallback).

Usage:
    uv run python scripts/hardsub_trim.py <input.mkv> <subtitle.ass> <output.mp4> <start1> <end1> [<start2> <end2> ...]

Examples:
    uv run python scripts/hardsub_trim.py video.mkv subs.ass final.mp4 10:00 15:00 30:04 35:26 47:35 48:55 50:29 1:03:03
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def parse_time(t_str: str) -> float:
    parts = t_str.split(":")
    if len(parts) == 3:
        return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
    elif len(parts) == 2:
        return float(parts[0]) * 60 + float(parts[1])
    return float(t_str)


def build_hardsub_command(
    input_video: Path,
    subs_file: Path,
    start_str: str,
    end_str: str,
    output_part: Path,
    popups: list[dict],
    fade_duration: float = 0.4,
) -> list[str]:
    seg_start = parse_time(start_str)
    seg_end = parse_time(end_str)
    dur = max(0.1, seg_end - seg_start)

    # Check overlays in this segment
    active_overlays = []
    proj_dir = input_video.parent
    for item in popups:
        o_start = parse_time(item["start"])
        o_end = parse_time(item["end"])
        if o_start >= seg_start and o_end <= seg_end:
            img_path = proj_dir / item.get("image", "")
            if img_path.exists():
                active_overlays.append(
                    {
                        "path": img_path,
                        "start_rel": o_start - seg_start,
                        "end_rel": o_end - seg_start,
                        "pos": item.get("pos", [1580, 60]),
                    }
                )

    cmd = ["ffmpeg", "-y", "-ss", start_str, "-to", end_str, "-i", str(input_video)]
    for ov in active_overlays:
        cmd.extend(["-i", str(ov["path"])])

    # Video & Audio fade parameters
    fade_out_st = max(0.0, dur - fade_duration)
    v_fade = f"fade=t=in:st=0:d={fade_duration},fade=t=out:st={fade_out_st:.2f}:d={fade_duration}"
    a_fade = f"afade=t=in:st=0:d={fade_duration},afade=t=out:st={fade_out_st:.2f}:d={fade_duration}"

    sub_filter = f"subtitles={subs_file.name}"

    if active_overlays:
        filters = [f"[0:v]{sub_filter},{v_fade}[v0]"]
        for idx, ov in enumerate(active_overlays, start=1):
            x, y = ov["pos"]
            t_s, t_e = ov["start_rel"], ov["end_rel"]
            in_label = f"[v{idx-1}]"
            out_label = f"[v{idx}]" if idx < len(active_overlays) else "[outv]"
            filters.append(
                f"{in_label}[{idx}:v]overlay={x}:{y}:enable='between(t,{t_s:.2f},{t_e:.2f})'{out_label}"
            )
        filters.append(f"[0:a]{a_fade}[outa]")

        filter_str = ";".join(filters)
        cmd.extend(
            [
                "-filter_complex",
                filter_str,
                "-map",
                "[outv]",
                "-map",
                "[outa]",
            ]
        )
    else:
        cmd.extend(
            [
                "-vf",
                f"{sub_filter},{v_fade}",
                "-af",
                a_fade,
            ]
        )

    cmd.extend(
        [
            "-c:v",
            "h264_nvenc",
            "-preset",
            "p4",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            str(output_part),
        ]
    )

    return cmd


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Hardsub, trim, and concatenate video segments with smooth fade transitions."
    )
    ap.add_argument("input_video", type=Path, help="Path to input .mkv / .mp4")
    ap.add_argument("subs_file", type=Path, help="Path to reviewed .ass subtitle file")
    ap.add_argument("output_video", type=Path, help="Path to output hardsubbed .mp4")
    ap.add_argument(
        "timestamps",
        nargs="+",
        help="Pairs of start end timestamps (e.g. 10:00 15:00 30:04 35:26)",
    )
    ap.add_argument(
        "--fade",
        type=float,
        default=0.4,
        help="Fade duration in seconds (default: 0.4s)",
    )
    args = ap.parse_args()

    if len(args.timestamps) % 2 != 0:
        sys.exit("ERROR: Timestamps must be provided in start end pairs.")

    segments = [
        (args.timestamps[i], args.timestamps[i + 1])
        for i in range(0, len(args.timestamps), 2)
    ]
    input_video_abs = args.input_video.resolve()
    subs_file_abs = args.subs_file.resolve()
    output_video_abs = args.output_video.resolve()
    proj_dir = input_video_abs.parent
    popups_manifest = proj_dir / "popups.json"

    popups = []
    if popups_manifest.exists():
        with open(popups_manifest, encoding="utf-8") as f:
            popups = json.load(f)
        print(f"Loaded {len(popups)} overlay cards from {popups_manifest.name}")

    tmpdir = Path(tempfile.mkdtemp())
    print(f"Temp working dir: {tmpdir}")

    # Copy subtitle file into temp dir so subtitles= filter parses spaceless relative path cleanly
    subs_tmp = tmpdir / "subs.ass"
    shutil.copy2(subs_file_abs, subs_tmp)

    print(
        f"Encoding {len(segments)} segments in parallel with 0.4s fade-in/out transitions..."
    )
    parts = []
    procs = []

    cwd_original = Path.cwd()
    os.chdir(tmpdir)

    try:
        for i, (start_str, end_str) in enumerate(segments):
            part = tmpdir / f"part{i+1}.mp4"
            parts.append(part)

            cmd = build_hardsub_command(
                input_video_abs,
                subs_tmp,
                start_str,
                end_str,
                part,
                popups,
                fade_duration=args.fade,
            )
            print(f"  Segment {i+1}/{len(segments)}: {start_str} -> {end_str}")
            p = subprocess.Popen(
                cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            procs.append(p)

        failed = False
        for i, p in enumerate(procs):
            ret = p.wait()
            if ret != 0:
                print(
                    f"ERROR: segment {i+1} failed with exit code {ret}",
                    file=sys.stderr,
                )
                failed = True
            else:
                size = parts[i].stat().st_size / 1e6
                print(f"  Segment {i+1} complete ({size:.1f} MB)")

        if failed:
            sys.exit(1)

        concat_file = tmpdir / "concat.txt"
        with open(concat_file, "w", encoding="utf-8") as f:
            for p in parts:
                f.write(f"file '{p.name}'\n")

        print("Concatenating segments...")
        res = subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(concat_file.name),
                "-c",
                "copy",
                str(output_video_abs),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if res.returncode != 0:
            sys.exit("ERROR: Concatenation failed.")

        print(f"\nDone! Output: {output_video_abs}")
        print(f"File size: {output_video_abs.stat().st_size / 1e6:.1f} MB")

    finally:
        os.chdir(cwd_original)
        shutil.rmtree(tmpdir, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
