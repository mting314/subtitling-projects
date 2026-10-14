---
name: video-launch
description: >-
  Use when finishing any Japanese-to-English subtitle translation for release
  (ProSeka AfterTalks, Stage Dramas, Event streams, Sekaraji, Lieraji), after
  the QC text review. Covers the complete pre-flight and publish pipeline:
  (1) positional styles (PiP / song-shift), (2) line length QC (max 2 rows),
  (3) Overlays & Popups pre-flight audit (popups.json), (4) hardsub rendering
  (full video for Dramas/Events or segment trimming for AfterTalks), (5) YouTube
  title + description copy, and (6) YouTube upload. Self-contained: drives
  `apply_positional_styles.py`, `detect_long_lines.py`, `find_segments.py`,
  `hardsub_trim.py`, and `youtube_upload.py`.
---

# Video Launch Pipeline (QC → Overlays → Hardsub → Publish)

The finishing pass on a reviewed `.ass` subtitle file, after the four-dimension QC text review
(documented in `subtitle_review_guide.md`). Five deterministic steps backed by scripts in
**`scripts/`** under the projects repo root:

1. **Positional styles** — reposition subs so they clear on-screen content (PiP, MV watchalong).
2. **Line length** — flag + fix any line rendering to 3+ rows.
3. **Overlays & Popups pre-flight** — audit `popups.json`, verify assets, deconflict subtitle collisions.
4. **Hardsub render** — burn subs and overlays (full video for Events/Radio, or keep-segments for AfterTalks).
5. **YouTube metadata & upload** — title, description, and resumable API upload.

---

## 1. Positional styles (PiP / song-shift)

Repositions subtitles so they never sit on top of on-screen content.

| Role | When | Reference style | Gets `\pos`? |
|---|---|---|---|
| **pip** | host cam / card art fills the frame; subs sit mid-frame | `PiP` (Alignment 8, margins 100/800/50) | yes — `{\pos(650,750)}` per line |
| **shift** | a 2D/3D MV plays lower-right; shift subs left to clear it | `DefaultOnibe - Shifted` (Alignment 2, margins 100/730/60) | no — style margins do it |

**Discover & confirm**:
```bash
f="projects/Project Sekai/Aftertalk/<event>/<name>_translated.ass"
grep -oE "^Dialogue: [0-9]+,[^,]+,[^,]+,[^,]+" "$f" | awk -F, '{print $4}' | sort | uniq -c
grep "^Style:" "$f"
```

**Apply** (copies only Alignment + MarginL/R/V; color/font preserved):
```bash
python scripts/apply_positional_styles.py "<path_to_subs.ass>" \
  --reference "projects/Project Sekai/Events/Colors of Pure Sense/Colors of Pure Sense_translated.ass" \
  --pip   "<Char> - PiP:PiP:650,750" \
  --shift "<Char> - Side Song:DefaultOnibe - Shifted" \
  --dry-run
```

---

## 2. Line length (max 2 rows on screen)

3+ rows is bad practice (eye-sweep, screen real estate). Run after positional styles and any text rewording:

```bash
uv run --with pillow --with numpy python scripts/detect_long_lines.py "<path_to_subs.ass>"
```

For each flagged line, offer the user **both** fixes and apply their choice:
- **Split into two events** at a clause boundary (comma, conjunction, breath gap).
- **Reword shorter**, preserving natural spoken style.
- Re-run the detector until 0 lines are flagged.

---

## 3. Overlays & Popups Pre-Flight (`popups.json`)

> [!IMPORTANT]
> **Mandatory Pre-Flight Guardrail**: Never hardsub or upload a video without completing this overlay audit. Memes, reaction stamps, and VA cards must never be lost in chat logs or temporary scratch folders.

### Checklist:
1. **Audit discussion & notes**: Check `notes.md` (`## Overlays`) and past QC discussions for any planned memes, reaction stamps, or VA cards.
2. **Commit raw and finished assets**:
   - Event-specific memes, stamps, and cards go in the **project folder**.
   - Recurring VA press photos go in the shared **`official_cast_photos/`** (`given_family.webp`).
   - All assets MUST be committed to git, never left only in ephemeral scratch directories.
3. **Verify `popups.json` manifest**:
   - Manifest must live in the project folder alongside the video and `.ass`.
   - Each entry defines: `id`, `image` (the rendered file on disk), `start`, `end`, and `pos: [X, Y]` (top-left coordinate).
   - For animated GIFs, `hardsub_trim.py` automatically enables looping (`-ignore_loop 0`).
4. **Deconflict Subtitles**:
   - If an overlay replaces a subtitle line (e.g. an Ichika reaction stamp replacing an "Oh..." line), comment out the subtitle (`Comment:`) so text and graphic do not collide.
5. **Render-Verify**:
   - Render a short 5–10s test clip or still frame at the overlay timestamp to confirm position, scaling, and subtitle synchronization before running the full render.

---

## 4. Hardsubbing & Cutting (`scripts/hardsub_trim.py`)

`scripts/hardsub_trim.py` auto-detects hardware encoding (`h264_nvenc` on NVIDIA, `h264_videotoolbox` on macOS, or `libx264`), auto-loads `popups.json` if present, and handles both full-video and segmented releases.

### Branch A: Full Video Releases (Events, Stage Dramas, Radio)
No watchalongs to cut; the entire video is kept without fade transitions:
```bash
uv run python scripts/hardsub_trim.py \
  "<path_to_video.mkv>" \
  "<path_to_subs.ass>" \
  "<path_to_output_hardsubbed.mp4>"
```

### Branch B: Watchalong Trimming (AfterTalk Streams)
Interleaves host talk (keep) with watchalongs (cut): intro delay, PV/digest, in-game story, and song 2DMV.

1. **Find keep segments**:
   ```bash
   python scripts/find_segments.py "<name>_translated.ass" \
     --transcript "<name>_transcript.json" \
     --hardsub "<name>.mkv:<name>_hardsubbed.mp4"
   ```
2. **Confirm cuts with user** and record ranges in `notes.md`.
3. **Hardsub & Concatenate with 0.4s fades**:
   ```bash
   uv run python scripts/hardsub_trim.py "<name>.mkv" "<name>_translated.ass" "<name>_hardsubbed.mp4" \
     0:01:37 0:05:27  0:10:53 0:27:40  0:36:05 0:51:00  0:52:25 1:00:09
   ```

---

## 5. YouTube title + description

Write these into the project's `notes.md` (`## YouTube Title`, `## YouTube Blurb`).

- **Title rules**:
  - ProSeka format: `[ENG SUB] <Event Title> Aftertalk feat. <VA Name> (<Character>'s VA)` or `[ENG SUB] Project SEKAI <Event Name> — <Subtitle>`
  - **No em dashes (`—`) in AfterTalk titles** (use commas, parentheses, or spaced en dash/hyphen as established).
- **Blurb rules**:
  - Two to three paragraphs, casual, enthusiastic, descriptive recap voice.
  - Weave personality details into the substantive topic coverage.
  - Include chapter timestamps and original clean video link.

---

## 6. YouTube upload (`scripts/youtube_upload.py`)

Uploads the hardsubbed video to YouTube using the title and description from `notes.md`:

```bash
uv run --script scripts/youtube_upload.py \
  --video "<path_to_hardsubbed.mp4>" \
  --notes "<path_to_notes.md>" \
  --privacy private
```

Defaults to `PRIVATE`. Never set `public` or `unlisted` unless explicitly instructed by the user.

---

## Guardrails
- **Overlays**: Check `popups.json` before hardsubbing. No uncommitted assets.
- **Positional**: Only Alignment + MarginL/R/V change; never recolor or wipe existing `\pos`.
- **Segments**: Cutting is editorial — always confirm with the user before rendering.
- **Privacy**: Releases default to `private` on YouTube.
