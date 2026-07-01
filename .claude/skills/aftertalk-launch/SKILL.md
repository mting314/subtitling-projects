---
name: aftertalk-launch
description: >-
  Use when finishing a ProSeka AfterTalk (or similar) `_translated.ass` for
  release, after the QC text pass — the layout + publish steps in one place:
  (1) applying PiP / song-shift positional styles, (2) finding hardsub
  keep-segments (cutting the intro delay, PV, story watchalong, and song/2DMV),
  and (3) writing the YouTube title + description. Self-contained: drives
  `apply_positional_styles.py`, `find_segments.py`, and `hardsub_trim.sh`, and
  inlines the YouTube blurb style rules. Composes with the `aegisub-ass` skill
  for render verification.
---

# AfterTalk launch (positioning → hardsub → publish)

The finishing pass on a `_translated.ass`, after the four-dimension QC text review
(that's in `subtitle_review_guide.md`). Three steps, each backed by a deterministic
script at the **projects repo root** so this skill only supplies judgment. Run
everything from the projects repo root.

1. **Positional styles** — reposition subs so they clear on-screen content.
2. **Hardsub segments** — find the host-talk ranges to keep and burn them in.
3. **YouTube title + description** — write the release copy.

---

## 1. Positional styles (PiP / song-shift)

Repositions subtitles so they never sit on top of on-screen content. The pipeline
pre-assigns the style *names* to the right line ranges but usually ships them as
plain copies of the main style (wrong margins) with no `\pos` on PiP lines. The
script fixes both, copying layout from a known-good reference; this skill resolves
the per-episode style names to roles (they differ per character).

| Role | When | Reference style (Colors of Pure Sense) | Gets `\pos`? |
|---|---|---|---|
| **pip** | host cam / card art fills the frame; subs sit mid-frame | `PiP` (Alignment 8, margins 100/800/50) | yes — `{\pos(650,750)}` per line |
| **shift** | a 2D/3D MV plays lower-right; shift subs left to clear it | `DefaultOnibe - Shifted` (Alignment 2, margins 100/730/60) | no — style margins do it |

**Discover** the target's positional styles, then infer role from name tokens
(`PiP`→pip; `Shifted`/`Side Song`/`Shift`→shift) and **confirm with the user**:
```bash
f="projects/Project Sekai/<event>/<name>_translated.ass"
grep -oE "^Dialogue: [0-9]+,[^,]+,[^,]+,[^,]+" "$f" | awk -F, '{print $4}' | sort | uniq -c
grep "^Style:" "$f"
```
**Apply** (copies only Alignment + MarginL/R/V — color/font preserved; skips
`Comment:` and already-positioned lines; idempotent, `--dry-run`):
```bash
python3 apply_positional_styles.py "projects/Project Sekai/<event>/<name>_translated.ass" \
  --reference "projects/Project Sekai/Colors of Pure Sense/Colors of Pure Sense_translated.ass" \
  --pip   "<Char> - PiP:PiP:650,750" \
  --shift "<Char> - Side Song:DefaultOnibe - Shifted" \
  --dry-run
```
Mapping: `TARGET_STYLE:REF_STYLE[:X,Y]`; `--pip`/`--shift` repeatable per character.
Confirm the target and reference share the same `PlayResX/Y`.

**Verify by rendering** (defer to the `aegisub-ass` skill): retime one pip and one
shift line to `0:00:00.00–0:00:05.00`, render a frame over flat gray, and confirm
the pip text sits mid-frame and the shift text clears the lower-right.

---

## 2. Hardsub segments (find keep-ranges → burn)

An AfterTalk interleaves host talk (keep) with watchalongs (cut): intro delay, an
opening PV/digest, the in-game story watchalong, and the song/2DMV. Cut regions are
non-rendering `Comment:` lines (or nothing), so they appear as **gaps** in the
rendered `Dialogue` timeline. `find_segments.py` finds them and, with
`--transcript`, reports whether each gap is silent (safe) or watchalong audio.

```bash
python3 find_segments.py "projects/Project Sekai/<event>/<name>_translated.ass" \
  --transcript "projects/Project Sekai/<event>/<name>_transcript.json" \
  --hardsub "projects/Project Sekai/<event>/<name>.mkv:projects/Project Sekai/<event>/<name>_final.mp4"
```
Read the CUT regions: `~0 words` = silent (safe to drop); many words = a story/song
watchalong you're intentionally cutting (its own audio, not host talk). **Confirm
the cut plan with the user** before rendering — cutting is an editorial call, and
the render is expensive. Record the ranges in the project's `notes.md` "Segments".

Then **hardsub** (the `--hardsub` flag prints this command; must hardsub before
trimming — trimming invalidates .ass timestamps):
```bash
./hardsub_trim.sh "<name>.mkv" "<name>_translated.ass" "<name>_final.mp4" \
  0:01:37 0:05:27  0:10:53 0:27:40  0:36:05 0:51:00  0:52:25 1:00:09
```
Requires ffmpeg built with libass. Segments encode in parallel, then concat with
`-c copy`. The script symlinks the subs to a spaceless name (the `ass=` filter
can't handle spaces).

---

## 3. YouTube title + description

Write these into the project's `notes.md` (`## YouTube Title`, `## YouTube Blurb`).

**Title** — `[ENG SUB] <Event Title> Aftertalk feat. <VA Name> (<Character>'s VA)`
e.g. `[ENG SUB] Gazing Upon the Night Sky's Fading Stars Aftertalk feat. Karin Isobe (Saki's VA)`.

**Blurb** — two paragraphs, casual and enthusiastic, recap voice (fans who want a
recap, not a teaser). Style rules:

1. **No em dashes (`—`).** Use commas, parentheses, or separate clauses. Scan the
   draft and replace any `—` before saving.
2. **Open with the series framing:** `This episode of ProSeka AfterTalk has <VA name>
   (voice of <character>) covering <event/topic>...`. It's a recurring series, so
   "this episode of," not "in the AfterTalk."
3. **Weave personality into substance.** The spine is the substantive coverage
   (story, card art, song, recording); pair each topic with a personality detail
   from that same topic (e.g. discussing the song *and* fumbling "2DMV"). Don't
   ghetto the silly bits into their own paragraph.
4. **No hook sentences** ("Bonus:", "Don't miss...", "Plus:"). Keep the descriptive
   recap voice throughout.

End with `Original video: <url>`.

Structure to mirror: paragraph 1 identifies VA + event + framing (solo/duo host,
what she watches); paragraph 2 covers story/recording, card illustrations, and the
song/MV, with personality woven in. See `Grow Glorious Glow Aftertalk/notes.md` or
`Gazing Upon the Night Sky's Fading Stars Aftertalk/notes.md` for worked examples.

---

## Guardrails
- Positional: only Alignment + MarginL/R/V change; never recolor; never touch
  `Comment:` lines or overwrite an existing `\pos`.
- Segments: cutting is editorial — confirm before the (expensive) render; log the
  ranges to `notes.md`; the transcript word-count tells you *why* a gap is a cut.
- The scripts error out on unknown style/paths — fix the args rather than forcing.
