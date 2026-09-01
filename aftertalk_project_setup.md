# AfterTalk Project Setup Guide

Repeatable steps to stand up a new ProSeka AfterTalk (or similar) subtitling project from
a YouTube URL: gather metadata, create the project folder + `notes.md`, download the
video, and build the autosub command. This is the **Generate** prep stage in
[`CLAUDE.md`](CLAUDE.md); QC/hardsub come later (see [`subtitle_review_guide.md`](subtitle_review_guide.md)).

Run everything from the `projects/` repo root. Tooling: `yt-dlp` (`brew install yt-dlp`).

---

## 1. Pull video metadata

Get the title, duration, and id. `yt-dlp`'s plain output is buried under warnings, so
print specific fields and discard stderr. Use `--no-playlist` (AfterTalk links often carry
a `&list=` param) and `--no-update` (silences the version nag):

```bash
URL="https://www.youtube.com/watch?v=XXXXXXXXXXX"
yt-dlp --no-update --no-playlist --print title --print duration_string --print id "$URL" 2>/dev/null
```

## 2. Extract the YouTube description (the key step)

The description is the most reliable source for event identity — it names the **stream
date**, the **event title**, and the **host VA + the character they voice**, which together
tell you the **unit** (and therefore the profile). WebFetch/browser are usually gated off
in this environment, so pull it straight from `yt-dlp`:

```bash
yt-dlp --no-update --no-playlist --print description "$URL" 2>/dev/null
```

What to read out of it (example from event 188):
- `2025年12月8日（月）21時30分より` → **stream date** 2025-12-08 21:30 JST
- `仰ぐ夜空に、星は紛れて編` → **event name** (JP)
- `天馬 咲希役の礒部花凜さんが出演` → **host** Karin Isobe, **character** Saki Tenma → **unit** Leo/need
- `【出演者】` lists all cast (solo vs multi-host)

The user usually supplies the **event id** (e.g. "event 188"); record it. Episode titles,
event dates, and the commissioned song/composer are NOT in the description — pull them
from the master DB (next step).

### Event details from the master DB (event id required)

Don't use sekai.best for this: it's a client-side JS app (the served HTML is an empty
shell), and WebFetch/browser tools are gated off in this environment anyway. Instead pull
the **raw static JSON** straight from the sekai-world master DB. Plain `curl` in Bash has
network even when WebFetch is blocked (different code path):

```bash
ID=188
cd /tmp
for f in events eventMusics musics eventStories; do
  curl -s --max-time 20 "https://sekai-world.github.io/sekai-master-db-diff/$f.json" -o "$f.json"
done
python3 - "$ID" <<'PY'
import json,sys,datetime
ID=int(sys.argv[1])
ev={x["id"]:x for x in json.load(open("events.json"))}[ID]
print("event:", ev["name"], "| type:", ev["eventType"], "| unit:", ev.get("unit"))
for k in ("startAt","aggregateAt"):
    print(k, datetime.datetime.fromtimestamp(ev[k]/1000, datetime.UTC).strftime("%Y-%m-%d"))
mus={m["id"]:m for m in json.load(open("musics.json"))}
for x in json.load(open("eventMusics.json")):
    if x.get("eventId")==ID:
        m=mus[x["musicId"]]; print("song:", m["title"], "| composer:", m["composer"], "| lyricist:", m["lyricist"])
es=next((x for x in json.load(open("eventStories.json")) if x.get("eventId")==ID), None)
for ep in (es or {}).get("eventStoryEpisodes",[]):
    print(f"  {ep['episodeNo']}. {ep['title']}")
PY
```

`unit` is the internal id: `light_sound`=Leo/need, `idol`=MMJ, `street`=VBS,
`theme_park`=WxS, `school_refusal`=N25, `piapro`=Virtual Singer. Episode titles and the
song are in Japanese — translate as working titles and flag for confirmation.

## 3. Pick the profile

The host's unit determines the profile. Available proseka profiles:

```bash
ls /Users/michaelting/github/autosub/profiles/local/proseka/   # leoneed, mmj, n25, vbs, wxs, aftertalk
```

Map unit → profile: Leo/need → `proseka/leoneed`, MORE MORE JUMP! → `proseka/mmj`,
Vivid BAD SQUAD → `proseka/vbs`, Wonderlands×Showtime → `proseka/wxs`,
Nightcord at 25:00 → `proseka/n25`. Each extends `proseka/aftertalk` and preconfigures its
cast. **Always prefix with the subdir** (`proseka/leoneed`, never bare `leoneed`) — the CLI
silently falls through with only a WARNING otherwise.

Confirm the focus character is in the profile's `[[speakers.cast]]`:
```bash
grep -A2 "speakers.cast" profiles/local/proseka/<unit>.toml
```

## 4. Create the project folder + notes.md

Folder: `projects/Project Sekai/Aftertalk/<English event name> Aftertalk/`. Translate the JP event
name to a working English title (Colorful Stage EN runs ~1.5 yr behind, so recent events
have no official EN name — flag the translation for confirmation). Commas/spaces are fine.

```bash
mkdir -p "projects/Project Sekai/Aftertalk/<English event name> Aftertalk"
```

Create `notes.md` from the template (copy an existing one, e.g.
`Grow Glorious Glow Aftertalk/notes.md`). Sections: event details (JP/EN name, id, unit,
focus character, host VA, stream date, song/composer), episode titles, story premise,
segments, the autosub command, profile, cast, VA, YouTube title/blurb, source URL, and
the **raw yt-dlp download command** (see step 5 — paste the exact command used).
Set the commit prefix per character+number (e.g. `shizu5` for Shizuku, `saki1` for Saki).

## 5. Download the video as mkv

Check formats first (the JS-runtime warning can cap resolution if no `deno`):
```bash
yt-dlp --no-update --no-playlist -F "$URL" 2>/dev/null | grep 1080
```

Download 1080p H.264 + best audio, merged to mkv (matches the 1080p hardsub pipeline).
Name the mkv after the folder. This is large (~0.5–1 GB) and slow — run in the background:

```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/Project Sekai/Aftertalk/<English event name> Aftertalk/<English event name> Aftertalk.mkv" \
  "$URL"
```

> `137` = 1080p AVC video, `251` = opus audio; the `/bv*[height<=1080]+ba/b` fallback covers
> cases where those exact ids are absent. mkv muxes avc+opus without re-encoding.
> `.mkv` and the rest of the video files are gitignored — only `notes.md` and the `.ass`
> outputs get committed.

**Record this exact command in the project's `notes.md`** (under a `## Source` →
`### Download command (yt-dlp)` block). The `.mkv` itself is gitignored, so the command is
the only committed record of how to re-fetch it — keep it reproducible.

## 6. Scope segments + build the autosub command

Decide which ranges to keep (cut the intro delay, in-stream story watchalongs, and MV
viewings; keep the host's talking segments). Two ways:

- **Auto-scope (preferred for the classic layout):** `scripts/scope_segments.py <mkv>
  --profile proseka/<unit>` classifies each second (standby / watchalong / talk) from the
  on-screen layout — no STT — and prints `--start/--end` pairs plus a boundary
  contact-sheet PNG. **Confirm the boundaries against the contact sheet**, then paste the
  command. The video signal is format-specific (tuned for full-frame-talk vs the right-side
  "Talk about" panel of watchalongs); if a stream uses a different layout, fall back to a skim.
- **Manual skim:** scrub the video and note the host-talk ranges by hand.

Record the ranges in the `notes.md` "Segments" section, then mirror them as repeatable
`--start/--end` pairs:

```bash
uv run autosub run \
  "projects/Project Sekai/Aftertalk/<English event name> Aftertalk/<English event name> Aftertalk.mkv" \
  --profile proseka/<unit> \
  --backend chirp_3 \
  --start HH:MM:SS --end HH:MM:SS \
  --start HH:MM:SS --end HH:MM:SS \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

Standard flags: `--backend chirp_3` (Opus transcription), `--chunk-size 30` and
`--llm-reasoning-effort low` (keeps each translate chunk under the OD-proxy 60s cap),
`--mark-chunks` (inserts chunk-boundary review markers), `--save-log` (per-chunk logs).
For unreliable local networks, run via Docker remote: `./scripts/remote.sh "<mkv>" run ...`
with the same flags.

After the pipeline produces `<name>_translated.ass`, continue with the
[QC review](subtitle_review_guide.md) → hardsub → publish stages.
