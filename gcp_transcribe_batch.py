#!/usr/bin/env python3
"""GCP Speech-to-Text (Chirp 3) batch transcription with automatic chunking for long audio.

Handles audio longer than the 20-minute word-timestamp limit by splitting into chunks,
transcribing each via BatchRecognize, offsetting timestamps, and merging results into
a single ASS subtitle file.
"""

import argparse
import os
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from google.api_core.client_options import ClientOptions
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
from google.cloud import storage


DEFAULT_PROJECT_ID = "future-name-201021"
DEFAULT_REGION = "us"
DEFAULT_CHUNK_MINUTES = 18
OVERLAP_SECONDS = 30
MAX_WORD_TIMESTAMP_MINUTES = 20
MAX_BATCH_FILES = 15
MAX_AUDIO_LENGTH_SECS = 8 * 60 * 60

# ASS file template (matches json_to_ass.py output)
ASS_HEADER_TEMPLATE = """\
[Script Info]
; Generated from speech-to-text transcript
Title: {title}
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Lato ExtraBold,72,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,4,1.33,2,200,200,60,1
Style: JP,Lato ExtraBold,72,&H00FFFFFF,&H000000FF,&H006381A1,&H00000000,0,0,0,0,100,100,0,0,1,4,1.33,2,200,200,60,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def seconds_to_ass(seconds: float) -> str:
    """Convert seconds to ASS timestamp format 'H:MM:SS.CC'."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = round((seconds % 1) * 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def parse_gcs_uri(uri: str) -> tuple[str, str]:
    """Parse a gs:// URI into (bucket, blob_path)."""
    parsed = urlparse(uri)
    if parsed.scheme != "gs":
        raise ValueError(f"Expected gs:// URI, got: {uri}")
    return parsed.netloc, parsed.path.lstrip("/")


def get_audio_duration(local_path: str) -> float:
    """Get audio duration in seconds using ffprobe."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "csv=p=0",
            local_path,
        ],
        capture_output=True, text=True, check=True,
    )
    return float(result.stdout.strip())


def download_from_gcs(uri: str, local_path: str):
    """Download a file from GCS to a local path."""
    bucket_name, blob_path = parse_gcs_uri(uri)
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.download_to_filename(local_path)
    print(f"Downloaded {uri} -> {local_path}")


def upload_to_gcs(local_path: str, uri: str):
    """Upload a local file to GCS."""
    bucket_name, blob_path = parse_gcs_uri(uri)
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} -> {uri}")


def delete_gcs_blobs(uris: list[str]):
    """Delete a list of GCS URIs."""
    client = storage.Client()
    for uri in uris:
        bucket_name, blob_path = parse_gcs_uri(uri)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.delete()
        print(f"Deleted {uri}")


def split_audio(local_path: str, chunk_seconds: float, overlap_seconds: float,
                output_dir: str) -> list[tuple[str, float]]:
    """Split audio into chunks with overlap.

    Returns list of (chunk_path, chunk_start_seconds) tuples.
    """
    duration = get_audio_duration(local_path)
    ext = Path(local_path).suffix

    if duration <= MAX_WORD_TIMESTAMP_MINUTES * 60:
        # No splitting needed
        return [(local_path, 0.0)]

    chunks = []
    step = chunk_seconds - overlap_seconds
    start = 0.0
    chunk_idx = 0

    while start < duration:
        chunk_path = os.path.join(output_dir, f"chunk_{chunk_idx:03d}{ext}")
        chunk_duration = chunk_seconds if start + chunk_seconds < duration else duration - start

        subprocess.run(
            [
                "ffmpeg", "-y", "-i", local_path,
                "-ss", str(start),
                "-t", str(chunk_duration),
                "-vn", "-acodec", "copy",
                chunk_path,
            ],
            capture_output=True, check=True,
        )
        print(f"Split chunk {chunk_idx}: start={start:.1f}s, duration={chunk_duration:.1f}s")
        chunks.append((chunk_path, start))

        start += step
        chunk_idx += 1

    return chunks


def transcribe_batch(audio_uri: str, project_id: str, region: str) -> cloud_speech.BatchRecognizeResults:
    """Transcribe a single audio file via GCP BatchRecognize with Chirp 3."""
    client = SpeechClient(
        client_options=ClientOptions(
            api_endpoint=f"{region}-speech.googleapis.com",
        )
    )

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=["ja-JP", "en-US"],
        model="chirp_3",
        features=cloud_speech.RecognitionFeatures(
            enable_word_time_offsets=True,
            enable_automatic_punctuation=True,
        ),
    )

    file_metadata = cloud_speech.BatchRecognizeFileMetadata(uri=audio_uri)

    request = cloud_speech.BatchRecognizeRequest(
        recognizer=f"projects/{project_id}/locations/{region}/recognizers/_",
        config=config,
        files=[file_metadata],
        recognition_output_config=cloud_speech.RecognitionOutputConfig(
            inline_response_config=cloud_speech.InlineOutputConfig(),
        ),
    )

    operation = client.batch_recognize(request=request)
    print(f"Waiting for transcription of {audio_uri}...")
    response = operation.result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
    return response.results[audio_uri].transcript


def parse_offset(offset_str) -> float:
    """Parse a protobuf Duration or string like '123.456s' to float seconds."""
    if hasattr(offset_str, 'total_seconds'):
        return offset_str.total_seconds()
    if isinstance(offset_str, (int, float)):
        return float(offset_str)
    return float(str(offset_str).rstrip("s"))


def extract_dialogue_lines(transcript, time_offset: float) -> list[dict]:
    """Extract dialogue lines from a transcript, applying a time offset.

    Returns list of dicts with keys: start, end, style, text
    """
    lines = []
    for result in transcript.results:
        if not result.alternatives:
            continue
        alt = result.alternatives[0]
        text = alt.transcript.strip()
        if not text:
            continue

        # Start time from first word
        if alt.words:
            start_sec = parse_offset(alt.words[0].start_offset) + time_offset
        else:
            start_sec = time_offset

        end_sec = parse_offset(result.result_end_offset) + time_offset

        style = "JP" if result.language_code == "ja-jp" else "Default"
        lines.append({
            "start": start_sec,
            "end": end_sec,
            "style": style,
            "text": text,
        })
    return lines


def deduplicate_overlap(lines: list[dict], tolerance: float = 0.5) -> list[dict]:
    """Remove duplicate lines from overlapping chunk regions.

    When chunks overlap, the same speech segment may be transcribed twice.
    We detect duplicates by checking if two lines have similar start times
    (within tolerance) and keep the one from the earlier chunk (which appears
    first in the sorted list).
    """
    if not lines:
        return lines

    # Sort by start time
    lines.sort(key=lambda x: x["start"])

    deduped = [lines[0]]
    for line in lines[1:]:
        prev = deduped[-1]
        # If start times are very close and texts overlap, skip duplicate
        if abs(line["start"] - prev["start"]) < tolerance and (
            line["text"] == prev["text"]
            or line["text"] in prev["text"]
            or prev["text"] in line["text"]
        ):
            # Keep the longer text version
            if len(line["text"]) > len(prev["text"]):
                deduped[-1] = line
            continue
        deduped.append(line)

    return deduped


def lines_to_ass(lines: list[dict], title: str) -> str:
    """Convert dialogue lines to a complete ASS file string."""
    content = ASS_HEADER_TEMPLATE.format(title=title)
    for line in lines:
        start_ass = seconds_to_ass(line["start"])
        end_ass = seconds_to_ass(line["end"])
        content += f"Dialogue: 0,{start_ass},{end_ass},{line['style']},,0,0,0,,{line['text']}\n"
    return content


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio from GCS using GCP Speech-to-Text (Chirp 3) and output ASS subtitles. "
                    "Automatically splits audio longer than 20 minutes into chunks."
    )
    parser.add_argument("--input", required=True,
                        help="GCS URI for audio file (gs://bucket/path/file.opus)")
    parser.add_argument("--output", required=True,
                        help="Output path for ASS subtitle file")
    parser.add_argument("--title", default=None,
                        help="ASS file title (defaults to output filename)")
    parser.add_argument("--project-id", default=None,
                        help=f"GCP project ID (default: $GOOGLE_CLOUD_PROJECT or '{DEFAULT_PROJECT_ID}')")
    parser.add_argument("--region", default=DEFAULT_REGION,
                        help=f"GCP region (default: '{DEFAULT_REGION}')")
    parser.add_argument("--chunk-minutes", type=float, default=DEFAULT_CHUNK_MINUTES,
                        help=f"Chunk duration in minutes (default: {DEFAULT_CHUNK_MINUTES})")

    args = parser.parse_args()

    project_id = args.project_id or os.getenv("GOOGLE_CLOUD_PROJECT", DEFAULT_PROJECT_ID)
    chunk_seconds = args.chunk_minutes * 60
    title = args.title or Path(args.output).stem

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Download audio from GCS
        input_bucket, input_blob = parse_gcs_uri(args.input)
        ext = Path(input_blob).suffix
        local_audio = os.path.join(tmp_dir, f"input{ext}")
        download_from_gcs(args.input, local_audio)

        # Get duration and decide whether to split
        duration = get_audio_duration(local_audio)
        print(f"Audio duration: {duration:.1f}s ({duration/60:.1f} min)")

        if duration <= MAX_WORD_TIMESTAMP_MINUTES * 60:
            # Short audio — transcribe directly, no splitting needed
            print("Audio is under 20 minutes, transcribing directly...")
            transcript = transcribe_batch(args.input, project_id, args.region)
            all_lines = extract_dialogue_lines(transcript, time_offset=0.0)
        else:
            # Long audio — split into chunks
            print(f"Audio exceeds 20 minutes, splitting into ~{args.chunk_minutes}-min chunks "
                  f"with {OVERLAP_SECONDS}s overlap...")
            chunks = split_audio(local_audio, chunk_seconds, OVERLAP_SECONDS, tmp_dir)
            print(f"Created {len(chunks)} chunks")

            # Upload chunks to GCS
            chunk_uris = []
            tmp_gcs_prefix = f"gs://{input_bucket}/tmp/transcribe_chunks/"
            for chunk_path, _ in chunks:
                chunk_name = Path(chunk_path).name
                chunk_uri = f"{tmp_gcs_prefix}{chunk_name}"
                upload_to_gcs(chunk_path, chunk_uri)
                chunk_uris.append(chunk_uri)

            # Transcribe chunks (up to 15 per BatchRecognize request, but we do
            # one-per-request for simplicity since each chunk is independent)
            all_lines = []
            try:
                for i, ((chunk_path, chunk_start), chunk_uri) in enumerate(zip(chunks, chunk_uris)):
                    print(f"\nTranscribing chunk {i+1}/{len(chunks)} "
                          f"(start={chunk_start:.1f}s)...")
                    transcript = transcribe_batch(chunk_uri, project_id, args.region)
                    lines = extract_dialogue_lines(transcript, time_offset=chunk_start)
                    print(f"  Got {len(lines)} dialogue lines")
                    all_lines.extend(lines)
            finally:
                # Clean up temp GCS files
                print("\nCleaning up temporary GCS files...")
                try:
                    delete_gcs_blobs(chunk_uris)
                except Exception as e:
                    print(f"Warning: failed to clean up some GCS files: {e}")

            # Deduplicate overlap regions
            before = len(all_lines)
            all_lines = deduplicate_overlap(all_lines)
            after = len(all_lines)
            if before != after:
                print(f"Deduplication: {before} -> {after} lines ({before - after} duplicates removed)")

    # Sort by start time and generate ASS
    all_lines.sort(key=lambda x: x["start"])
    ass_content = lines_to_ass(all_lines, title)

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ass_content, encoding="utf-8")
    print(f"\nGenerated ASS file: {args.output}")
    print(f"Total dialogue lines: {len(all_lines)}")


if __name__ == "__main__":
    main()
