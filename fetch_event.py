#!/usr/bin/env python3
"""Fetch Project Sekai event story data from sekai-world master DB and asset CDN.

Usage:
    python3 fetch_event.py "grow glorious"
    python3 fetch_event.py "unraveled thread"
    python3 fetch_event.py 151
    python3 fetch_event.py "grow" --transcript --episodes 7 8
    python3 fetch_event.py --list
"""

import argparse
import json
import sys
import urllib.request
from datetime import datetime, timezone

MASTER_DB = "https://sekai-world.github.io/sekai-master-db-diff"
ASSET_CDN = "https://storage.sekai.best/sekai-jp-assets"


def fetch_json(url: str) -> list | dict:
    req = urllib.request.Request(url, headers={"User-Agent": "fetch_event/1.0"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def find_by_id(data: list, target_id: int, key: str = "id") -> dict | None:
    for entry in data:
        if entry.get(key) == target_id:
            return entry
    return None


def ts_to_date(ts_ms: int) -> str:
    return datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def fetch_all_events() -> list[dict]:
    return fetch_json(f"{MASTER_DB}/events.json")


def fuzzy_match_event(events: list[dict], query: str) -> list[dict]:
    query_lower = query.lower()
    tokens = query_lower.split()
    matches = []
    for event in events:
        name = event.get("name", "").lower()
        if all(tok in name for tok in tokens):
            matches.append(event)
    return matches


def resolve_event(query: str) -> dict:
    events = fetch_all_events()
    if query.isdigit():
        event = find_by_id(events, int(query))
        if not event:
            print(f"Error: event ID {query} not found", file=sys.stderr)
            sys.exit(1)
        return event

    matches = fuzzy_match_event(events, query)
    if not matches:
        print(f"No events matching '{query}'.", file=sys.stderr)
        print("Try --list to see all events, or use a different search term.", file=sys.stderr)
        sys.exit(1)
    if len(matches) == 1:
        return matches[0]

    print(f"Multiple events matching '{query}':\n", file=sys.stderr)
    for m in matches:
        date = ts_to_date(m["startAt"])
        print(f"  {m['id']:>4}  {date}  {m['name']}", file=sys.stderr)
    print(f"\nNarrow your search or use the event ID.", file=sys.stderr)
    sys.exit(1)


def list_events(query: str | None = None):
    events = fetch_all_events()
    if query:
        events = fuzzy_match_event(events, query)
    events.sort(key=lambda e: e.get("startAt", 0), reverse=True)
    for e in events:
        date = ts_to_date(e["startAt"])
        unit = e.get("unit", "?")
        print(f"  {e['id']:>4}  {date}  [{unit:<10}]  {e['name']}")


def fetch_event_metadata(event_id: int) -> dict:
    events = fetch_all_events()
    event = find_by_id(events, event_id)
    if not event:
        print(f"Error: event {event_id} not found", file=sys.stderr)
        sys.exit(1)
    return event


def fetch_event_stories(event_id: int) -> dict:
    stories = fetch_json(f"{MASTER_DB}/eventStories.json")
    story = find_by_id(stories, event_id, key="eventId")
    if not story:
        print(f"Error: no stories for event {event_id}", file=sys.stderr)
        sys.exit(1)
    return story


def fetch_event_music(event_id: int) -> dict | None:
    event_musics = fetch_json(f"{MASTER_DB}/eventMusics.json")
    em = find_by_id(event_musics, event_id, key="eventId")
    if not em:
        return None
    musics = fetch_json(f"{MASTER_DB}/musics.json")
    return find_by_id(musics, em["musicId"])


def fetch_characters() -> dict[int, dict]:
    chars = fetch_json(f"{MASTER_DB}/gameCharacters.json")
    return {c["id"]: c for c in chars}


def fetch_scenario(asset_bundle: str, scenario_id: str) -> list[dict]:
    url = f"{ASSET_CDN}/event_story/{asset_bundle}/scenario/{scenario_id}.asset"
    data = fetch_json(url)
    talks = data.get("TalkData", [])
    return [
        {"speaker": t.get("WindowDisplayName", ""), "text": t.get("Body", "")}
        for t in talks
        if t.get("Body")
    ]


def print_summary(event_id: int) -> dict:
    print(f"Fetching event {event_id}...", file=sys.stderr)

    event = fetch_event_metadata(event_id)
    story = fetch_event_stories(event_id)
    music = fetch_event_music(event_id)

    info = {
        "event_id": event_id,
        "name": event["name"],
        "unit": event.get("unit", "unknown"),
        "type": event.get("eventType", "unknown"),
        "start": ts_to_date(event["startAt"]),
        "end": ts_to_date(event["aggregateAt"]),
        "asset_bundle": story["assetbundleName"],
        "outline": story.get("outline", ""),
    }

    print(f"\n{'='*60}")
    print(f"Event: {info['name']}")
    print(f"Unit: {info['unit']}  |  Type: {info['type']}")
    print(f"Dates: {info['start']} → {info['end']}")
    print(f"Asset bundle: {info['asset_bundle']}")
    print(f"{'='*60}")

    print(f"\nOutline (JP):\n  {info['outline']}")

    if music:
        info["song"] = music["title"]
        info["composer"] = music.get("composer", "")
        info["lyricist"] = music.get("lyricist", "")
        info["arranger"] = music.get("arranger", "")
        print(f"\nCommissioned song: {music['title']}")
        print(f"  Composer: {music.get('composer', 'N/A')}")
        print(f"  Lyricist: {music.get('lyricist', 'N/A')}")
        print(f"  Arranger: {music.get('arranger', 'N/A')}")

    episodes = story.get("eventStoryEpisodes", [])
    episodes.sort(key=lambda e: e["episodeNo"])
    info["episodes"] = []
    print(f"\nEpisodes ({len(episodes)}):")
    for ep in episodes:
        ep_info = {
            "number": ep["episodeNo"],
            "title": ep["title"],
            "scenario_id": ep["scenarioId"],
        }
        info["episodes"].append(ep_info)
        print(f"  {ep['episodeNo']}. {ep['title']}  ({ep['scenarioId']})")

    return info


def print_transcript(event_id: int, episode_nums: list[int] | None = None):
    story = fetch_event_stories(event_id)
    asset_bundle = story["assetbundleName"]
    episodes = sorted(story.get("eventStoryEpisodes", []), key=lambda e: e["episodeNo"])

    if episode_nums:
        episodes = [e for e in episodes if e["episodeNo"] in episode_nums]

    for ep in episodes:
        print(f"\n{'='*60}")
        print(f"Episode {ep['episodeNo']}: {ep['title']}")
        print(f"{'='*60}\n")

        lines = fetch_scenario(asset_bundle, ep["scenarioId"])
        for line in lines:
            speaker = line["speaker"]
            text = line["text"].replace("\n", " ")
            if speaker:
                print(f"{speaker}: {text}")
            else:
                print(f"  {text}")


def main():
    parser = argparse.ArgumentParser(description="Fetch Project Sekai event story data")
    parser.add_argument(
        "event", nargs="?", help="Event name (fuzzy match) or ID (e.g. 'grow glorious', 151)"
    )
    parser.add_argument(
        "--episodes", type=int, nargs="+", help="Specific episode numbers to fetch"
    )
    parser.add_argument(
        "--transcript", action="store_true", help="Print full episode transcripts"
    )
    parser.add_argument(
        "--json", action="store_true", help="Output summary as JSON"
    )
    parser.add_argument(
        "--list", action="store_true", help="List all events (optionally filtered by query)"
    )
    args = parser.parse_args()

    if args.list:
        list_events(args.event)
        return

    if not args.event:
        parser.error("event name or ID required (or use --list)")

    event = resolve_event(args.event)
    info = print_summary(event["id"])

    if args.json:
        print(f"\n{json.dumps(info, ensure_ascii=False, indent=2)}")

    if args.transcript:
        print_transcript(event["id"], args.episodes)


if __name__ == "__main__":
    main()
