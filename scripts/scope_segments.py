#!/usr/bin/env python3
"""Pre-pipeline segment scoping for ProSeka AfterTalk videos (video/audio only, no STT).

The pre-pipeline sibling of ``find_segments.py`` (which works post-translation on a
rendered .ass). This one takes the *raw* video and proposes the host-talk keep-ranges
to feed to ``autosub run --start/--end``, by classifying each sampled second into one
of three program modes:

  - standby   (CUT): the static title/standby card (intro delay, outro) — near-zero
                     frame-to-frame motion over a sustained run.
  - watchalong (CUT): in-game story OR the song/2DMV, shown with the fixed right-side
                     "Talk about <event logo>" panel + a shrunk webcam PiP. Detected by
                     normalized cross-correlation of that panel region against a template
                     auto-bootstrapped from the video itself (watchalong ~1.0, talk ~0.02).
  - talk      (KEEP): full-frame host webcam. Everything that isn't standby or watchalong.

An audio pass then rescues full-screen songs the video misses: newer streams show the
song/MV full-frame with NO "Talk about" panel, so video calls them talk. A sustained
continuous-music run (low low-energy-rate: speech pauses ~0.3, a song is continuous <0.1)
over non-static talk frames is reclassified to watchalong. Format-invariant; needs librosa
(``--with librosa``) — skipped with a warning if absent, or disable with ``--no-audio``.

Only ``talk`` runs are kept. Boundaries are (optionally) snapped to the nearest source
fade via ``blackdetect`` in a small window, the same fade-aware idea find_segments uses.

The tool PROPOSES; a human confirms. It writes a boundary contact-sheet PNG (thumbnails
at each cut +/- a couple seconds) so the cut plan can be eyeballed in seconds, and never
runs the (expensive) pipeline itself.

Usage (run from the projects repo root):
    uv run --with opencv-python-headless --with numpy --with librosa \
      python3 scripts/scope_segments.py "projects/Project Sekai/Aftertalk/<event>/<name>.mkv"

    # validate against a past episode whose ranges you already know:
    ... scripts/scope_segments.py "<past>.mkv" --truth 9:30-15:00,24:45-35:45,37:55-55:00

    # emit a ready-to-run autosub command:
    ... scripts/scope_segments.py "<name>.mkv" --profile proseka/n25
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

import cv2
import numpy as np


def hms(sec: float) -> str:
    sec = max(0, int(round(sec)))
    h, r = divmod(sec, 3600)
    m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def parse_ts(t: str) -> float:
    parts = [float(p) for p in t.strip().split(":")]
    return sum(p * 60**i for i, p in enumerate(reversed(parts)))


def ffprobe_duration(path: str) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def extract_frames(path: str, fps: float, width: int, tmp: str) -> list[str]:
    """Decode the whole file once at `fps`, scaled to `width`, to jpgs. Returns paths."""
    subprocess.run(
        ["ffmpeg", "-nostdin", "-loglevel", "error", "-i", path,
         "-vf", f"fps={fps},scale={width}:-1", "-q:v", "3",
         os.path.join(tmp, "f_%06d.jpg")], check=True)
    return sorted(os.path.join(tmp, f) for f in os.listdir(tmp) if f.startswith("f_"))


# --- per-frame features -----------------------------------------------------------
def panel_roi(img, roi):
    h, w = img.shape[:2]
    y0, y1, x0, x1 = roi
    return img[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)]


def left_roi(img):
    h, w = img.shape[:2]
    return img[int(0.15 * h):int(0.85 * h), int(0.02 * w):int(0.62 * w)]


def ncc(a, b) -> float:
    a = a.astype(np.float32).ravel(); a -= a.mean()
    b = b.astype(np.float32).ravel(); b -= b.mean()
    d = float(np.linalg.norm(a) * np.linalg.norm(b))
    return float(a @ b / d) if d else 0.0


def median_filter(labels: list[str], k: int) -> list[str]:
    if k <= 1:
        return labels
    out, n, half = [], len(labels), k // 2
    for i in range(n):
        win = labels[max(0, i - half):min(n, i + half + 1)]
        out.append(max(set(win), key=win.count))
    return out


def runs(labels: list[str]):
    out, start = [], 0
    for i in range(1, len(labels) + 1):
        if i == len(labels) or labels[i] != labels[start]:
            out.append((start, i - 1, labels[start]))
            start = i
    return out


def song_mask(path: str, nsec: int, ler_thresh: float, silence_frac: float):
    """Per-second bool: is this a continuous-music (song) run?

    Low-energy rate (fraction of short frames below half the local mean level) is a
    format-invariant music/speech discriminator: speech pauses between words (LER
    ~0.3), a song is continuous (LER <0.1). This rescues full-screen song/MV segments
    that carry no on-screen "Talk about" panel (newer stream layout). Returns None if
    librosa isn't available (audio fusion is then skipped).
    """
    try:
        import librosa
        from scipy.ndimage import uniform_filter1d
    except ImportError:
        return None
    tmp = tempfile.mktemp(suffix=".wav")
    subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", path,
                    "-ac", "1", "-ar", "16000", tmp], check=True)
    try:
        y, sr = librosa.load(tmp, sr=16000)
    finally:
        os.remove(tmp)
    hop = 512
    rms = librosa.feature.rms(y=y, hop_length=hop)[0]
    fps_a = sr / hop
    ref = uniform_filter1d(rms, size=max(3, int(fps_a * 20)))  # local level (+/-10s)
    low = rms < 0.5 * ref
    floor = silence_frac * float(np.median(rms))
    out = np.zeros(nsec, bool)
    for s in range(nsec):
        fr = rms[int(s * fps_a):int((s + 1) * fps_a)]
        lr = low[int(s * fps_a):int((s + 1) * fps_a)]
        if len(fr) and fr.mean() > floor and lr.mean() < ler_thresh:
            out[s] = True
    return out


def snap_fade(path: str, t: float, dur: float, window: float = 3.0) -> float:
    """Pull a boundary to the nearest blackdetect edge within +/- window (fade-aware)."""
    ss = max(0, t - window)
    out = subprocess.run(
        ["ffmpeg", "-nostdin", "-ss", f"{ss}", "-t", f"{2*window}", "-i", path,
         "-vf", "blackdetect=d=0.05:pic_th=0.90", "-an", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    edges = []
    for m in re.finditer(r"black_start:([\d.]+).*?black_end:([\d.]+)", out):
        edges += [ss + float(m.group(1)), ss + float(m.group(2))]
    edges = [e for e in edges if abs(e - t) <= window and 0 <= e <= dur]
    return min(edges, key=lambda e: abs(e - t)) if edges else t


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--fps", type=float, default=1.0, help="sampling rate (default 1/s)")
    ap.add_argument("--width", type=int, default=480, help="analysis frame width")
    ap.add_argument("--panel-thresh", type=float, default=0.5, help="watchalong NCC threshold")
    ap.add_argument("--still-eps", type=float, default=1.5, help="mean |diff| below this = static frame")
    ap.add_argument("--min-standby", type=float, default=8.0, help="min static run to call standby (s)")
    ap.add_argument("--min-talk", type=float, default=20.0, help="drop talk runs shorter than this (s)")
    ap.add_argument("--merge-gap", type=float, default=8.0, help="merge talk runs across gaps up to this (s)")
    ap.add_argument("--roi", default="0.06,0.52,0.70,0.99", help="panel ROI y0,y1,x0,x1 (fractions)")
    ap.add_argument("--no-audio", action="store_true", help="skip the audio song-rescue pass")
    ap.add_argument("--song-ler", type=float, default=0.12, help="low-energy-rate below this = continuous music")
    ap.add_argument("--min-song", type=float, default=15.0, help="min run to rescue as a full-screen song (s)")
    ap.add_argument("--watch-sample", help="timestamp known to be watchalong (override auto-bootstrap)")
    ap.add_argument("--no-snap", action="store_true", help="skip blackdetect fade-snapping")
    ap.add_argument("--profile", help="also print an autosub run command with this profile")
    ap.add_argument("--truth", help="comma list of known keep ranges A-B,C-D for validation")
    ap.add_argument("--contact-sheet", help="output PNG path (default alongside video)")
    args = ap.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            sys.exit(f"error: {tool} not found on PATH")
    if not os.path.isfile(args.video):
        sys.exit(f"error: no such file: {args.video}")

    roi = tuple(float(x) for x in args.roi.split(","))
    dur = ffprobe_duration(args.video)
    tmp = tempfile.mkdtemp(prefix="scope_")
    try:
        print(f"decoding {hms(dur)} at {args.fps} fps ...", file=sys.stderr)
        paths = extract_frames(args.video, args.fps, args.width, tmp)
        imgs = [cv2.imread(p) for p in paths]
        imgs = [im for im in imgs if im is not None]
        n = len(imgs)
        if not n:
            sys.exit("error: no frames decoded")
        times = [i / args.fps for i in range(n)]

        # per-frame features
        satL = np.array([cv2.cvtColor(left_roi(im), cv2.COLOR_BGR2HSV)[..., 1].mean() for im in imgs])
        still = np.zeros(n)
        grays = [cv2.cvtColor(cv2.resize(im, (160, 90)), cv2.COLOR_BGR2GRAY).astype(np.int16) for im in imgs]
        for i in range(1, n):
            still[i] = np.abs(grays[i] - grays[i - 1]).mean()
        still[0] = still[1] if n > 1 else 0.0

        # bootstrap the watchalong panel template from the video itself
        if args.watch_sample:
            seed = imgs[min(n - 1, int(round(parse_ts(args.watch_sample) * args.fps)))]
            template = panel_roi(seed, roi).astype(np.float32)
        else:
            cand = np.where((satL > np.percentile(satL, 55)) & (still > args.still_eps))[0]
            if len(cand) < 5:
                cand = np.argsort(satL)[-max(5, n // 10):]
            stack = np.stack([panel_roi(imgs[i], roi).astype(np.float32) for i in cand])
            template = np.median(stack, axis=0)

        panel = np.array([ncc(panel_roi(im, roi), template) for im in imgs])

        # classify each sampled second. watchalong (panel) wins; then standby is only a
        # SUSTAINED static run (the intro/outro card is ~byte-identical, diff~0 — a calm
        # talking head still moves, so a low per-frame eps + a run-length floor avoids
        # shredding talk into fake "standby"); everything else is talk.
        static = still < args.still_eps
        labels = ["watch" if panel[i] >= args.panel_thresh else "talk" for i in range(n)]

        # audio rescue: full-screen songs carry no panel, so video calls them "talk".
        # A sustained continuous-music run (low LER) over talk frames -> watch (song).
        if not args.no_audio:
            print("analyzing audio for full-screen songs ...", file=sys.stderr)
            sm = song_mask(args.video, int(dur) + 1, args.song_ler, silence_frac=0.15)
            if sm is None:
                print("  (librosa unavailable — skipping audio; add --with librosa)", file=sys.stderr)
            else:
                songf = [bool(sm[min(len(sm) - 1, int(times[i]))]) for i in range(n)]
                min_sg = max(1, int(round(args.min_song * args.fps)))
                # a song MV has motion; never rescue a static frame (that's a standby card
                # with BGM, not a song to translate) — else it voids the standby run it sits in.
                cand = ["s" if songf[i] and labels[i] == "talk" and not static[i] else "x" for i in range(n)]
                for a, b, lab in runs(cand):
                    if lab == "s" and (b - a + 1) >= min_sg:
                        for i in range(a, b + 1):
                            labels[i] = "watch"

        min_sb = max(1, int(round(args.min_standby * args.fps)))
        for a, b, lab in runs(["static" if static[i] else "x" for i in range(n)]):
            if lab == "static" and (b - a + 1) >= min_sb and all(l != "watch" for l in labels[a:b+1]):
                for i in range(a, b + 1):
                    labels[i] = "standby"
        labels = median_filter(labels, int(round(5 * args.fps)) | 1)

        # merge into segments; keep talk, bridging short gaps and dropping short talk
        keep = [(times[a], times[min(b + 1, n - 1)]) for a, b, lab in runs(labels) if lab == "talk"]
        merged = []
        for s, e in keep:
            if merged and s - merged[-1][1] <= args.merge_gap:
                merged[-1] = (merged[-1][0], e)
            else:
                merged.append((s, e))
        merged = [(s, e) for s, e in merged if e - s >= args.min_talk]

        # snap boundaries to fades
        if not args.no_snap:
            print("snapping boundaries to source fades ...", file=sys.stderr)
            merged = [(snap_fade(args.video, s, dur) if s > 1 else 0.0,
                       snap_fade(args.video, e, dur) if e < dur - 1 else dur) for s, e in merged]

        # ---- report ----
        print("\n=== detected program modes ===")
        for a, b, lab in runs(labels):
            tag = {"talk": "KEEP", "watch": "cut ", "standby": "cut "}[lab]
            conf = panel[a:b+1].mean()
            print(f"  {tag} {hms(times[a]):>7}-{hms(times[min(b+1,n-1)]):<7} {lab:8} "
                  f"({hms(times[min(b+1,n-1)]-times[a])}, panelNCC={conf:+.2f})")

        print(f"\n=== proposed keep-segments ({len(merged)}) ===")
        for s, e in merged:
            print(f"  {hms(s)} -> {hms(e)}  ({hms(e - s)})")
        kept = sum(e - s for s, e in merged)
        print(f"  total kept {hms(kept)} of {hms(dur)} ({100*kept/dur:.0f}%)")

        print("\n=== autosub --start/--end ===")
        print(" ".join(f"--start {hms(s)} --end {hms(e)}" for s, e in merged))

        if args.profile:
            body = " \\\n  ".join(f"--start {hms(s)} --end {hms(e)}" for s, e in merged)
            print("\n=== ready-to-run command ===")
            print(f'uv run autosub run \\\n  "{args.video}" \\\n  --profile {args.profile} '
                  f'--backend chirp_3 \\\n  {body} \\\n  --chunk-size 30 '
                  f'--llm-reasoning-effort low --mark-chunks --save-log')

        if args.truth:
            truth = []
            for rng in args.truth.split(","):
                a, b = rng.split("-"); truth.append((parse_ts(a), parse_ts(b)))
            grid = np.zeros(int(dur) + 1, bool)
            for s, e in merged:
                grid[int(s):int(e)] = True
            tg = np.zeros(int(dur) + 1, bool)
            for s, e in truth:
                tg[int(s):int(e)] = True
            inter = np.logical_and(grid, tg).sum()
            union = np.logical_or(grid, tg).sum()
            print(f"\n=== validation vs truth ===")
            print(f"  IoU={inter/union:.3f}  precision={inter/max(1,grid.sum()):.3f}  "
                  f"recall={inter/max(1,tg.sum()):.3f}")
            print(f"  truth keep: " + ", ".join(f"{hms(s)}->{hms(e)}" for s, e in truth))

        # ---- boundary contact sheet ----
        out_png = args.contact_sheet or os.path.splitext(args.video)[0] + "_segments.png"
        bounds = sorted({0.0, dur} | {t for se in merged for t in se})
        rows = []
        for bt in bounds:
            strip = []
            for dt in (-2, -1, 0, 1, 2):
                idx = int(round((bt + dt) * args.fps))
                if 0 <= idx < n:
                    im = cv2.resize(imgs[idx], (240, 135))
                    cv2.putText(im, f"{hms(bt+dt)}", (4, 128), cv2.FONT_HERSHEY_SIMPLEX,
                                0.4, (0, 255, 0), 1, cv2.LINE_AA)
                    strip.append(im)
                else:
                    strip.append(np.zeros((135, 240, 3), np.uint8))
            rows.append(np.hstack(strip))
        cv2.imwrite(out_png, np.vstack(rows))
        print(f"\ncontact sheet (rows = each cut boundary, +/-2s): {out_png}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
