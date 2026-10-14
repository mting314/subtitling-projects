#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "google-api-python-client>=2.0",
#   "google-auth-oauthlib>=1.0",
#   "google-auth-httplib2>=0.2",
#   "httplib2>=0.22",
#   "pysocks>=1.7",
# ]
# ///
"""
Upload a video file to Google Drive and configure public viewer access.

Usage:
    uv run --script scripts/gdrive_upload.py \\
      --video "projects/Project Sekai/Events/<event>/<name>_hardsubbed.mp4" \\
      --notes "projects/Project Sekai/Events/<event>/notes.md" \\
      --public --yes

Credentials:
    Reuses scripts/client_secret.json (Desktop OAuth Client).
    Saves auth token to scripts/.gdrive_token.json (gitignored).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

import httplib2
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_httplib2 import AuthorizedHttp
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive.file"]
DEFAULT_CLIENT_SECRETS = Path(__file__).parent / "client_secret.json"
DEFAULT_TOKEN = Path(__file__).parent / ".gdrive_token.json"


def parse_notes(notes_path: Path) -> tuple[str, str]:
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
    title = title_lines[0] if title_lines else ""

    blurb_lines = section(r"^##\s+YouTube Blurb")
    while blurb_lines and not blurb_lines[0].strip():
        blurb_lines.pop(0)
    while blurb_lines and not blurb_lines[-1].strip():
        blurb_lines.pop()
    description = "\n".join(blurb_lines).strip()
    return title, description


def build_http() -> httplib2.Http:
    proxy_url = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    proxy_info = None
    if proxy_url:
        import urllib.parse
        parsed = urllib.parse.urlsplit(proxy_url)
        proxy_info = httplib2.ProxyInfo(
            proxy_type=httplib2.socks.PROXY_TYPE_HTTP,
            proxy_host=parsed.hostname,
            proxy_port=parsed.port or 8080,
            proxy_user=parsed.username,
            proxy_pass=parsed.password,
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
        try:
            creds.refresh(Request())
        except RefreshError:
            print("Cached token was rejected (invalid_grant); re-running consent...")
            creds = None
    if not (creds and creds.valid):
        if not client_secrets.exists():
            sys.exit(
                f"ERROR: OAuth client secrets not found at {client_secrets}.\n"
                "Save your Google Cloud Desktop OAuth client JSON there."
            )
        flow = InstalledAppFlow.from_client_secrets_file(str(client_secrets), SCOPES)
        creds = flow.run_local_server(port=0, open_browser=open_browser)
    token.write_text(creds.to_json(), encoding="utf-8")
    try:
        token.chmod(0o600)
    except Exception:
        pass
    return creds


def main() -> None:
    ap = argparse.ArgumentParser(description="Upload video to Google Drive with public viewer link.")
    ap.add_argument("--video", required=True, type=Path, help="Path to the video file to upload.")
    ap.add_argument("--name", help="Display filename in Google Drive (defaults to video file name).")
    ap.add_argument("--notes", type=Path, help="Optional notes.md to pull title/description from.")
    ap.add_argument("--public", action="store_true", default=True, help="Make file viewable by anyone with link.")
    ap.add_argument("--client-secrets", type=Path, default=DEFAULT_CLIENT_SECRETS)
    ap.add_argument("--token", type=Path, default=DEFAULT_TOKEN)
    ap.add_argument("--yes", action="store_true", help="Skip confirmation prompt.")
    ap.add_argument("--no-browser", action="store_true", help="Print auth URL instead of opening browser.")
    args = ap.parse_args()

    if not args.video.is_file():
        sys.exit(f"ERROR: video not found: {args.video}")

    file_title = args.name
    description = ""
    if args.notes and args.notes.is_file():
        parsed_title, description = parse_notes(args.notes)
        if not file_title and parsed_title:
            file_title = f"{parsed_title}.mp4"

    if not file_title:
        file_title = args.video.name

    size_mb = args.video.stat().st_size / 1e6
    print("\n=== Google Drive Upload ===")
    print(f"File       : {args.video} ({size_mb:.1f} MB)")
    print(f"Drive Name : {file_title}")
    print(f"Access     : {'Anyone with the link (Viewer)' if args.public else 'Private'}")
    if description:
        preview_desc = description[:100] + ("..." if len(description) > 100 else "")
        print(f"Description: {preview_desc}")

    if not args.yes:
        resp = input("\nProceed with upload? [y/N] ").strip().lower()
        if resp not in ("y", "yes"):
            print("Aborted.")
            sys.exit(0)

    print("\nAuthenticating with Google Drive...")
    creds = get_credentials(args.client_secrets, args.token, open_browser=not args.no_browser)
    http = AuthorizedHttp(creds, http=build_http())
    drive_service = build("drive", "v3", http=http)

    file_metadata = {
        "name": file_title,
    }
    if description:
        file_metadata["description"] = description

    media = MediaFileUpload(
        str(args.video),
        mimetype="video/mp4",
        resumable=True,
        chunksize=10 * 1024 * 1024,  # 10 MB chunks
    )

    print("\nUploading (resumable)...")
    request = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id, name, webViewLink, webContentLink",
    )

    response = None
    last_pct = -1
    while response is None:
        status, response = request.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            if pct != last_pct and pct % 5 == 0:
                print(f"  {pct}%", flush=True)
                last_pct = pct

    file_id = response.get("id")
    print(f"\nUpload complete! File ID: {file_id}")

    if args.public:
        print("Setting public viewer permissions...")
        drive_service.permissions().create(
            fileId=file_id,
            body={"type": "anyone", "role": "reader"},
            fields="id",
        ).execute()

    file_info = drive_service.files().get(
        fileId=file_id,
        fields="id, name, webViewLink, webContentLink",
    ).execute()

    view_link = file_info.get("webViewLink")
    print("\nDone.")
    print(f"  File ID   : {file_id}")
    print(f"  View Link : {view_link}")

    # If notes.md was provided, append the drive link
    if args.notes and args.notes.is_file():
        notes_text = args.notes.read_text(encoding="utf-8")
        if "## Distribution" in notes_text:
            lines = notes_text.splitlines()
            new_lines = []
            for line in lines:
                new_lines.append(line)
                if line.strip().startswith("- **Target**: Google Drive"):
                    new_lines.append(f"- **Drive Link**: {view_link}")
                    new_lines.append(f"- **File ID**: `{file_id}`")
            args.notes.write_text("\n".join(new_lines), encoding="utf-8")
            print(f"Updated {args.notes} with Google Drive link.")


if __name__ == "__main__":
    main()
