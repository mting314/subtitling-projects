#!/usr/bin/env python3
"""GCP Speech-to-Text (Chirp 3) batch transcription with automatic chunking for long audio.

Handles audio longer than the 20-minute word-timestamp limit by splitting into chunks,
transcribing each via BatchRecognize, offsetting timestamps, and merging results into
a single ASS subtitle file.
"""

import argparse
import json
import os
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from google.api_core.client_options import ClientOptions
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
from google.cloud import storage


DEFAULT_REGION = "us"
DEFAULT_CHUNK_MINUTES = 18
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


def _storage_client(project_id: str) -> storage.Client:
    """Create a GCS client with the given project ID."""
    return storage.Client(project=project_id)


def download_from_gcs(uri: str, local_path: str, project_id: str):
    """Download a file from GCS to a local path."""
    bucket_name, blob_path = parse_gcs_uri(uri)
    client = _storage_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.download_to_filename(local_path)
    print(f"Downloaded {uri} -> {local_path}")


def upload_to_gcs(local_path: str, uri: str, project_id: str):
    """Upload a local file to GCS."""
    bucket_name, blob_path = parse_gcs_uri(uri)
    client = _storage_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} -> {uri}")


def delete_gcs_blobs(uris: list[str], project_id: str):
    """Delete a list of GCS URIs."""
    client = _storage_client(project_id)
    for uri in uris:
        bucket_name, blob_path = parse_gcs_uri(uri)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.delete()
        print(f"Deleted {uri}")


def split_audio(local_path: str, chunk_seconds: float,
                output_dir: str) -> list[tuple[str, float]]:
    """Split audio into non-overlapping chunks.

    Returns list of (chunk_path, chunk_start_seconds) tuples.
    """
    duration = get_audio_duration(local_path)
    ext = Path(local_path).suffix

    if duration <= MAX_WORD_TIMESTAMP_MINUTES * 60:
        # No splitting needed
        return [(local_path, 0.0)]

    chunks = []
    start = 0.0
    chunk_idx = 0

    while start < duration:
        chunk_path = os.path.join(output_dir, f"chunk_{chunk_idx:03d}{ext}")
        chunk_duration = min(chunk_seconds, duration - start)

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

        start += chunk_seconds
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


def _get_word_time(word, attr: str, fallback: float, max_time: float) -> float:
    """Get a word's start or end time, falling back if the API returns 0 or bogus values."""
    val = parse_offset(getattr(word, attr))
    # Chirp 3 sometimes returns 0 or absurdly large values for word offsets
    if val <= 0 or val > max_time:
        return fallback
    return val


def extract_dialogue_lines(transcript, time_offset: float, chunk_duration: float = 0) -> list[dict]:
    """Extract dialogue lines from a transcript, applying a time offset.

    Chirp 3 often returns a single result containing all text for a chunk.
    We use word-level timestamps to split into subtitle-sized lines at
    sentence boundaries (Japanese punctuation: 。？！) or when a pause
    between words exceeds a threshold.

    Punctuation marks (。、？！etc.) are often returned as separate word
    entries by Chirp 3 — these are appended to the current line rather
    than treated as standalone words.

    Returns list of dicts with keys: start, end, style, text
    """
    PAUSE_THRESHOLD = 1.0  # seconds of silence to force a line break
    MAX_LINE_CHARS = 200   # force a break if a line gets too long
    SENTENCE_ENDERS = "。？！?!"
    PUNCTUATION_ONLY = set("。、？！?!,.…──")
    # Max valid timestamp within this chunk (with some margin)
    max_valid_time = chunk_duration * 1.1 if chunk_duration > 0 else MAX_AUDIO_LENGTH_SECS

    lines = []
    for result in transcript.results:
        if not result.alternatives:
            continue
        alt = result.alternatives[0]
        if not alt.words:
            text = alt.transcript.strip()
            if text:
                style = "JP" if result.language_code == "ja-jp" else "Default"
                lines.append({
                    "start": time_offset,
                    "end": time_offset,
                    "style": style,
                    "text": text,
                })
            continue

        style = "JP" if result.language_code == "ja-jp" else "Default"

        # Pre-process: collect words with valid timestamps, merging punctuation-only
        # tokens into the preceding word
        processed = []  # list of (text, start, end)
        last_valid_time = 0.0

        for word in alt.words:
            w_start = _get_word_time(word, "start_offset", last_valid_time, max_valid_time)
            w_end = _get_word_time(word, "end_offset", w_start, max_valid_time)
            last_valid_time = max(last_valid_time, w_start, w_end)

            word_text = word.word
            # If this is punctuation-only, append to previous word
            if word_text.strip() in PUNCTUATION_ONLY and processed:
                prev_text, prev_start, prev_end = processed[-1]
                processed[-1] = (prev_text + word_text, prev_start, max(prev_end, w_end))
                continue

            processed.append((word_text, w_start, w_end))

        # Build lines from processed words
        current_words = []
        line_start = None
        line_end = 0.0

        for i, (word_text, w_start, w_end) in enumerate(processed):
            if line_start is None:
                line_start = w_start

            # Check if we should break BEFORE this word
            should_break = False
            if current_words:
                pause = w_start - line_end
                if pause >= PAUSE_THRESHOLD:
                    should_break = True

                # Check if previous word ended a sentence
                prev_text = current_words[-1]
                if prev_text and prev_text[-1] in SENTENCE_ENDERS:
                    should_break = True

                # Force break if line is getting too long
                if sum(len(w) for w in current_words) >= MAX_LINE_CHARS:
                    should_break = True

            if should_break and current_words:
                text = "".join(current_words).strip()
                if text:
                    lines.append({
                        "start": line_start + time_offset,
                        "end": line_end + time_offset,
                        "style": style,
                        "text": text,
                    })
                current_words = []
                line_start = w_start

            current_words.append(word_text)
            line_end = w_end

        # Flush remaining words
        if current_words:
            text = "".join(current_words).strip()
            if text:
                lines.append({
                    "start": line_start + time_offset,
                    "end": line_end + time_offset,
                    "style": style,
                    "text": text,
                })

    return lines


def transcript_to_json(transcript, time_offset: float = 0.0) -> list[dict]:
    """Convert a protobuf transcript to a JSON-serializable list of results."""
    results = []
    for result in transcript.results:
        if not result.alternatives:
            continue
        alt = result.alternatives[0]
        words = []
        for w in alt.words:
            words.append({
                "word": w.word,
                "startOffset": f"{parse_offset(w.start_offset) + time_offset:.2f}s",
                "endOffset": f"{parse_offset(w.end_offset) + time_offset:.2f}s",
            })
        results.append({
            "languageCode": result.language_code,
            "resultEndOffset": f"{parse_offset(result.result_end_offset) + time_offset:.2f}s",
            "alternatives": [{
                "transcript": alt.transcript,
                "words": words,
            }],
        })
    return results


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
                        help="GCP project ID (default: $GOOGLE_CLOUD_PROJECT)")
    parser.add_argument("--region", default=DEFAULT_REGION,
                        help=f"GCP region (default: '{DEFAULT_REGION}')")
    parser.add_argument("--chunk-minutes", type=float, default=DEFAULT_CHUNK_MINUTES,
                        help=f"Chunk duration in minutes (default: {DEFAULT_CHUNK_MINUTES})")
    parser.add_argument("--save-raw", default=None, metavar="DIR",
                        help="Save raw transcript JSON files to this directory for inspection. "
                             "Each chunk gets a separate JSON file, plus a merged file.")

    args = parser.parse_args()

    project_id = args.project_id or os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        parser.error("GCP project ID required: set GOOGLE_CLOUD_PROJECT env var or pass --project-id")
    chunk_seconds = args.chunk_minutes * 60
    title = args.title or Path(args.output).stem

    # Prepare raw output directory if requested
    raw_dir = None
    if args.save_raw:
        raw_dir = Path(args.save_raw)
        raw_dir.mkdir(parents=True, exist_ok=True)
        print(f"[save-raw] Raw transcripts will be saved to: {raw_dir}")

    print(f"\n{'='*60}")
    print(f"GCP Chirp 3 Batch Transcription")
    print(f"{'='*60}")
    print(f"  Input:      {args.input}")
    print(f"  Output:     {args.output}")
    print(f"  Project:    {project_id}")
    print(f"  Region:     {args.region}")
    print(f"  Chunk size: {args.chunk_minutes} min")
    print(f"{'='*60}\n")

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Step 1: Download audio from GCS
        print("[1/5] Downloading audio from GCS...")
        input_bucket, input_blob = parse_gcs_uri(args.input)
        ext = Path(input_blob).suffix
        local_audio = os.path.join(tmp_dir, f"input{ext}")
        download_from_gcs(args.input, local_audio, project_id)

        # Step 2: Analyze audio duration
        print("\n[2/5] Analyzing audio duration...")
        duration = get_audio_duration(local_audio)
        print(f"  Duration: {duration:.1f}s ({duration/60:.1f} min)")
        print(f"  Word-timestamp limit: {MAX_WORD_TIMESTAMP_MINUTES} min")

        all_raw_results = []

        if duration <= MAX_WORD_TIMESTAMP_MINUTES * 60:
            # Short audio — transcribe directly, no splitting needed
            print(f"  -> Under limit, no splitting needed")
            print("\n[3/5] Transcribing (single file)...")
            transcript = transcribe_batch(args.input, project_id, args.region)
            num_results = len(transcript.results)
            num_words = sum(len(r.alternatives[0].words) for r in transcript.results if r.alternatives)
            print(f"  API returned {num_results} result(s), {num_words} total words")
            all_lines = extract_dialogue_lines(transcript, time_offset=0.0, chunk_duration=duration)
            print(f"  Split into {len(all_lines)} dialogue lines")

            if raw_dir:
                raw_data = transcript_to_json(transcript)
                all_raw_results.extend(raw_data)
                raw_path = raw_dir / "transcript.json"
                raw_path.write_text(json.dumps({"results": raw_data}, indent=2, ensure_ascii=False),
                                    encoding="utf-8")
                print(f"  [save-raw] Saved to {raw_path}")
        else:
            # Long audio — split into chunks
            print(f"  -> Exceeds limit, splitting required")

            print(f"\n[3/5] Splitting audio into chunks...")
            num_chunks_est = int((duration + chunk_seconds - 1) / chunk_seconds)
            print(f"  Chunk duration: {args.chunk_minutes} min (non-overlapping)")
            print(f"  Estimated chunks: {num_chunks_est}")

            chunks = split_audio(local_audio, chunk_seconds, tmp_dir)
            print(f"  Created {len(chunks)} chunks:")
            for idx, (cp, cs) in enumerate(chunks):
                chunk_dur = get_audio_duration(cp)
                print(f"    chunk {idx}: {cs:.0f}s - {cs + chunk_dur:.0f}s "
                      f"({chunk_dur:.0f}s / {chunk_dur/60:.1f} min)")

            # Upload chunks to GCS
            print(f"\n[4/5] Uploading chunks to GCS...")
            chunk_uris = []
            tmp_gcs_prefix = f"gs://{input_bucket}/tmp/transcribe_chunks/"
            for chunk_path, _ in chunks:
                chunk_name = Path(chunk_path).name
                chunk_uri = f"{tmp_gcs_prefix}{chunk_name}"
                upload_to_gcs(chunk_path, chunk_uri, project_id)
                chunk_uris.append(chunk_uri)
            print(f"  Uploaded {len(chunk_uris)} chunks to {tmp_gcs_prefix}")

            # Transcribe each chunk
            print(f"\n[5/5] Transcribing chunks...")
            all_lines = []
            try:
                for i, ((chunk_path, chunk_start), chunk_uri) in enumerate(zip(chunks, chunk_uris)):
                    chunk_dur = get_audio_duration(chunk_path)
                    print(f"\n  --- Chunk {i+1}/{len(chunks)} ---")
                    print(f"  Time range: {seconds_to_ass(chunk_start)} - {seconds_to_ass(chunk_start + chunk_dur)}")
                    print(f"  URI: {chunk_uri}")

                    transcript = transcribe_batch(chunk_uri, project_id, args.region)

                    num_results = len(transcript.results)
                    num_words = sum(len(r.alternatives[0].words)
                                    for r in transcript.results if r.alternatives)
                    print(f"  API returned {num_results} result(s), {num_words} total words")

                    lines = extract_dialogue_lines(transcript, time_offset=chunk_start,
                                                   chunk_duration=chunk_seconds)
                    print(f"  Split into {len(lines)} dialogue lines")
                    if lines:
                        print(f"  Time range: {seconds_to_ass(lines[0]['start'])} - "
                              f"{seconds_to_ass(lines[-1]['end'])}")

                    all_lines.extend(lines)

                    if raw_dir:
                        raw_data = transcript_to_json(transcript, time_offset=chunk_start)
                        all_raw_results.extend(raw_data)
                        raw_path = raw_dir / f"chunk_{i:03d}.json"
                        raw_path.write_text(
                            json.dumps({"results": raw_data, "chunk_start": chunk_start,
                                        "chunk_duration": chunk_dur},
                                       indent=2, ensure_ascii=False),
                            encoding="utf-8")
                        print(f"  [save-raw] Saved to {raw_path}")
            finally:
                # Clean up temp GCS files
                print(f"\n  Cleaning up {len(chunk_uris)} temporary GCS files...")
                try:
                    delete_gcs_blobs(chunk_uris, project_id)
                except Exception as e:
                    print(f"  Warning: failed to clean up some GCS files: {e}")

        # Save merged raw transcript
        if raw_dir and all_raw_results:
            merged_path = raw_dir / "merged.json"
            merged_path.write_text(
                json.dumps({"results": all_raw_results}, indent=2, ensure_ascii=False),
                encoding="utf-8")
            print(f"  [save-raw] Merged transcript saved to {merged_path}")

    # Sort by start time and generate ASS
    all_lines.sort(key=lambda x: x["start"])
    ass_content = lines_to_ass(all_lines, title)

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ass_content, encoding="utf-8")

    # Summary and quality report
    print(f"\n{'='*60}")
    print(f"Transcription complete!")
    print(f"{'='*60}")
    print(f"  Output:         {args.output}")
    if raw_dir:
        print(f"  Raw transcripts: {raw_dir}")

    if not all_lines:
        print(f"  Dialogue lines: 0")
        print(f"\n  WARNING: No dialogue lines generated!")
    else:
        # ASS file stats
        text_lengths = [len(line["text"]) for line in all_lines]
        durations = [line["end"] - line["start"] for line in all_lines]
        total_chars = sum(text_lengths)

        print(f"\n  --- ASS File Stats ---")
        print(f"  Dialogue lines:  {len(all_lines)}")
        print(f"  Total characters: {total_chars}")
        print(f"  Time range:      {seconds_to_ass(all_lines[0]['start'])} - "
              f"{seconds_to_ass(all_lines[-1]['end'])}")

        print(f"\n  --- Line Length (characters) ---")
        print(f"  Min:     {min(text_lengths)}")
        print(f"  Max:     {max(text_lengths)}")
        print(f"  Mean:    {total_chars / len(all_lines):.1f}")
        print(f"  Median:  {sorted(text_lengths)[len(text_lengths) // 2]}")

        print(f"\n  --- Line Duration (seconds) ---")
        print(f"  Min:     {min(durations):.2f}s")
        print(f"  Max:     {max(durations):.2f}s")
        print(f"  Mean:    {sum(durations) / len(durations):.2f}s")
        print(f"  Median:  {sorted(durations)[len(durations) // 2]:.2f}s")

        # Quality warnings
        issues = []

        # Check for zero-duration lines
        zero_dur = [i for i, d in enumerate(durations) if d <= 0]
        if zero_dur:
            issues.append(f"  - {len(zero_dur)} line(s) with zero or negative duration "
                          f"(likely bogus timestamps)")
            for idx in zero_dur[:5]:
                line = all_lines[idx]
                issues.append(f"      line {idx+1}: {seconds_to_ass(line['start'])} -> "
                              f"{seconds_to_ass(line['end'])}  \"{line['text'][:50]}\"")
            if len(zero_dur) > 5:
                issues.append(f"      ... and {len(zero_dur) - 5} more")

        # Check for very long lines (>200 chars, might need manual splitting)
        long_lines = [(i, l) for i, l in enumerate(text_lengths) if l > 200]
        if long_lines:
            issues.append(f"  - {len(long_lines)} line(s) over 200 characters "
                          f"(may need manual splitting in Aegisub)")
            for idx, length in long_lines[:3]:
                issues.append(f"      line {idx+1}: {length} chars")
            if len(long_lines) > 3:
                issues.append(f"      ... and {len(long_lines) - 3} more")

        # Check for very short lines (<3 chars, likely noise/artifacts)
        short_lines = [(i, all_lines[i]["text"]) for i, l in enumerate(text_lengths) if l < 3]
        if short_lines:
            issues.append(f"  - {len(short_lines)} line(s) under 3 characters "
                          f"(likely noise or artifacts)")
            for idx, text in short_lines[:5]:
                issues.append(f"      line {idx+1}: \"{text}\"")
            if len(short_lines) > 5:
                issues.append(f"      ... and {len(short_lines) - 5} more")

        # Check for very long duration lines (>60s, likely timestamp gap)
        long_dur = [(i, d) for i, d in enumerate(durations) if d > 60]
        if long_dur:
            issues.append(f"  - {len(long_dur)} line(s) spanning over 60 seconds "
                          f"(likely timestamp gaps from API)")
            for idx, dur in long_dur[:3]:
                line = all_lines[idx]
                issues.append(f"      line {idx+1}: {dur:.1f}s  "
                              f"{seconds_to_ass(line['start'])} -> {seconds_to_ass(line['end'])}")
            if len(long_dur) > 3:
                issues.append(f"      ... and {len(long_dur) - 3} more")

        # Check for lines with end < start (inverted timestamps)
        inverted = [i for i, d in enumerate(durations) if d < 0]
        if inverted:
            issues.append(f"  - {len(inverted)} line(s) with end time before start time "
                          f"(bogus timestamps)")
            for idx in inverted[:3]:
                line = all_lines[idx]
                issues.append(f"      line {idx+1}: {seconds_to_ass(line['start'])} -> "
                              f"{seconds_to_ass(line['end'])}")
            if len(inverted) > 3:
                issues.append(f"      ... and {len(inverted) - 3} more")

        # Check for overlapping lines (next line starts before current ends)
        overlaps = []
        for i in range(len(all_lines) - 1):
            if all_lines[i+1]["start"] < all_lines[i]["end"] - 0.1:
                overlaps.append(i)
        if overlaps:
            issues.append(f"  - {len(overlaps)} pair(s) of overlapping lines "
                          f"(next line starts before current ends)")
            for idx in overlaps[:3]:
                issues.append(f"      lines {idx+1}-{idx+2}: "
                              f"end={seconds_to_ass(all_lines[idx]['end'])} > "
                              f"start={seconds_to_ass(all_lines[idx+1]['start'])}")
            if len(overlaps) > 3:
                issues.append(f"      ... and {len(overlaps) - 3} more")

        # Check for large gaps (>30s of silence between lines)
        gaps = []
        for i in range(len(all_lines) - 1):
            gap = all_lines[i+1]["start"] - all_lines[i]["end"]
            if gap > 30:
                gaps.append((i, gap))
        if gaps:
            issues.append(f"  - {len(gaps)} gap(s) over 30 seconds between lines "
                          f"(silence, music, or missed speech)")
            for idx, gap in gaps[:3]:
                issues.append(f"      between lines {idx+1}-{idx+2}: "
                              f"{gap:.1f}s gap at {seconds_to_ass(all_lines[idx]['end'])}")
            if len(gaps) > 3:
                issues.append(f"      ... and {len(gaps) - 3} more")

        if issues:
            print(f"\n  --- Quality Warnings ({len(issues)} issues) ---")
            for issue in issues:
                print(issue)
        else:
            print(f"\n  --- Quality: No issues detected ---")


if __name__ == "__main__":
    main()
