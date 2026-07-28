#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "google-api-python-client>=2.0",
#   "google-auth-oauthlib>=1.0",
#   "google-auth-httplib2>=0.2",
#   "httplib2>=0.22",
# ]
# ///
"""
Upload a finished (hardsubbed) video to YouTube, PRIVATE by default.

Title + description are pulled straight from a project's ``notes.md`` (the
``## YouTube Title`` and ``## YouTube Blurb`` sections), so what you QC'd is what
gets published. Override with ``--title`` / ``--description`` if needed.

Run it with uv (auto-installs deps from the inline metadata above):

    uv run scripts/youtube_upload.py \\
      --video "projects/Project Sekai/We Escape to Survive Aftertalk/We Escape to Survive Aftertalk_hardsubbed.mp4" \\
      --notes "projects/Project Sekai/We Escape to Survive Aftertalk/notes.md"

Privacy defaults to ``private``. Pass ``--privacy unlisted`` or ``--privacy public``
to change it (it prints the chosen privacy and asks for confirmation before uploading).

------------------------------------------------------------------------------
ONE-TIME OAUTH SETUP (required — the gcloud login does NOT grant youtube.upload)
------------------------------------------------------------------------------
1. In Google Cloud console, on a project owned by the channel's Google account:
     - Enable "YouTube Data API v3".
     - APIs & Services > Credentials > Create Credentials > OAuth client ID
       > Application type: "Desktop app".
     - Download the JSON, save it as:  scripts/client_secret.json  (gitignored)
2. First run opens a browser for consent (scope: youtube.upload). The resulting
   token is cached in scripts/.youtube_token.json (gitignored) and reused/refreshed
   after that — no browser needed on later runs.

Notes:
  - Each upload costs ~1600 units of the default 10,000/day YouTube API quota.
  - This runs on YOUR machine with YOUR OAuth client; no third party sees the token.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import httplib2
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_httplib2 import AuthorizedHttp
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
DEFAULT_CLIENT_SECRETS = Path(__file__).parent / "client_secret.json"
DEFAULT_TOKEN = Path(__file__).parent / ".youtube_token.json"
# YouTube categoryId 24 = "Entertainment". See videoCategories.list for others.
DEFAULT_CATEGORY = "24"

TITLE_MAX = 100      # YouTube hard limit
DESC_MAX = 5000      # YouTube hard limit


def parse_notes(notes_path: Path) -> tuple[str, str]:
    """Extract (title, description) from a project notes.md.

    Title  = first non-empty line under '## YouTube Title'.
    Desc   = everything under '## YouTube Blurb...' up to the next '## ' heading,
             with placeholder 'TBD'/'TODO' lines rejected.
    """
    text = notes_path.read_text(encoding="utf-8").splitlines()

    def section(header_re: str) -> list[str]:
        out, capturing = [], False
        for line in text:
            if re.match(header_re, line):
                capturing = True
                continue
            if capturing and line.startswith("## "):
                break
            if capturing:
                out.append(line)
        return out

    title_lines = [l.strip() for l in section(r"^##\s+YouTube Title") if l.strip()]
    if not title_lines:
        sys.exit(f"ERROR: no '## YouTube Title' content found in {notes_path}")
    title = title_lines[0]

    blurb_lines = section(r"^##\s+YouTube Blurb")
    # trim leading/trailing blank lines
    while blurb_lines and not blurb_lines[0].strip():
        blurb_lines.pop(0)
    while blurb_lines and not blurb_lines[-1].strip():
        blurb_lines.pop()
    description = "\n".join(blurb_lines).strip()
    if not description:
        sys.exit(f"ERROR: no '## YouTube Blurb' content found in {notes_path}")

    for label, val in (("title", title), ("description", description)):
        if val.strip().upper() in ("TBD", "TODO"):
            sys.exit(f"ERROR: {label} is still a placeholder ('{val}') in {notes_path}")
    return title, description


def build_http() -> httplib2.Http:
    """httplib2 transport that routes through an env HTTP proxy if one is set.

    google-api-python-client uploads over httplib2, which (unlike ``requests``)
    ignores HTTPS_PROXY. On networks that force egress through a proxy (e.g. the
    Meta OD env's localhost:10054), a direct socket is blocked, so we wire the
    proxy in explicitly. No proxy env -> plain direct Http (normal networks / VMs).
    """
    proxy_url = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    proxy_info = None
    if proxy_url:
        parsed = urlparse(proxy_url)
        proxy_info = httplib2.ProxyInfo(
            proxy_type=httplib2.socks.PROXY_TYPE_HTTP,
            proxy_host=parsed.hostname,
            proxy_port=parsed.port or 80,
        )
    h = httplib2.Http(proxy_info=proxy_info)
    h.follow_redirects = False
    return h


def get_credentials(client_secrets: Path, token: Path, open_browser: bool = True) -> Credentials:
    creds: Credentials | None = None
    if token.exists():
        creds = Credentials.from_authorized_user_file(str(token), SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        if not client_secrets.exists():
            sys.exit(
                f"ERROR: OAuth client secrets not found at {client_secrets}.\n"
                "Create a Desktop OAuth client (see this script's docstring) and save it there."
            )
        flow = InstalledAppFlow.from_client_secrets_file(str(client_secrets), SCOPES)
        # open_browser=False prints the auth URL instead of launching a browser —
        # needed for headless/sandboxed/remote runs. The loopback redirect still
        # comes back to this local server once you approve in any browser on this host.
        creds = flow.run_local_server(port=0, open_browser=open_browser)
    token.write_text(creds.to_json(), encoding="utf-8")
    token.chmod(0o600)
    return creds


def main() -> None:
    ap = argparse.ArgumentParser(description="Upload a video to YouTube (private by default).")
    ap.add_argument("--video", required=True, type=Path, help="Path to the .mp4 to upload.")
    ap.add_argument("--notes", type=Path, help="notes.md to pull title/description from.")
    ap.add_argument("--title", help="Override title (else from --notes).")
    ap.add_argument("--description", help="Override description (else from --notes).")
    ap.add_argument("--privacy", default="private", choices=["private", "unlisted", "public"])
    ap.add_argument("--category", default=DEFAULT_CATEGORY, help="YouTube categoryId (default 24=Entertainment).")
    ap.add_argument("--tags", default="", help="Comma-separated tags.")
    ap.add_argument("--client-secrets", type=Path, default=DEFAULT_CLIENT_SECRETS)
    ap.add_argument("--token", type=Path, default=DEFAULT_TOKEN)
    ap.add_argument("--yes", action="store_true", help="Skip the confirmation prompt.")
    ap.add_argument("--no-browser", action="store_true",
                    help="Print the auth URL instead of opening a browser (headless/remote consent).")
    args = ap.parse_args()

    if not args.video.is_file():
        sys.exit(f"ERROR: video not found: {args.video}")

    title, description = args.title, args.description
    if (title is None or description is None):
        if not args.notes:
            sys.exit("ERROR: provide --notes, or both --title and --description.")
        n_title, n_desc = parse_notes(args.notes)
        title = title or n_title
        description = description or n_desc

    if len(title) > TITLE_MAX:
        sys.exit(f"ERROR: title is {len(title)} chars (>{TITLE_MAX}). Shorten it.")
    if len(description) > DESC_MAX:
        sys.exit(f"ERROR: description is {len(description)} chars (>{DESC_MAX}). Shorten it.")

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    print("=== YouTube upload ===")
    print(f"Video    : {args.video}  ({args.video.stat().st_size / 1e6:.0f} MB)")
    print(f"Title    : {title}")
    print(f"Privacy  : {args.privacy.upper()}")
    print(f"Category : {args.category}")
    print(f"Tags     : {tags or '(none)'}")
    print("Description:\n" + "\n".join("  " + l for l in description.splitlines()))
    if not args.yes:
        if input("\nProceed with upload? [y/N] ").strip().lower() not in ("y", "yes"):
            sys.exit("Aborted.")

    creds = get_credentials(args.client_secrets, args.token, open_browser=not args.no_browser)
    proxy_url = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if proxy_url:
        youtube = build("youtube", "v3", http=AuthorizedHttp(creds, http=build_http()))
    else:
        youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": args.category,
        },
        "status": {
            "privacyStatus": args.privacy,
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(str(args.video), chunksize=8 * 1024 * 1024, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    print("\nUploading (resumable)...")
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  {int(status.progress() * 100)}%")
    vid = response["id"]
    print("\nDone.")
    print(f"  Video ID : {vid}")
    print(f"  Watch    : https://youtu.be/{vid}")
    print(f"  Studio   : https://studio.youtube.com/video/{vid}/edit")
    print(f"  Privacy  : {args.privacy.upper()}")


if __name__ == "__main__":
    main()
