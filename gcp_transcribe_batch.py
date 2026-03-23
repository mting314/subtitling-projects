#!/usr/bin/env python3
"""GCP Speech-to-Text (Chirp 3) batch transcription with automatic chunking for long audio.

Handles audio longer than the 20-minute word-timestamp limit by splitting into chunks,
transcribing each via BatchRecognize, and saving raw JSON transcripts.

Automatically generates an ASS subtitle file after transcription. Re-run json_to_ass.py
separately to tune splitting parameters without re-transcribing.
"""

import argparse
import json
import os
import subprocess
import tempfile
from pathlib import Path

from dotenv import load_dotenv
from google.api_core.client_options import ClientOptions
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

from utils.audio import (
    has_video_stream, extract_audio, trim_audio, get_audio_duration, split_audio,
    MAX_WORD_TIMESTAMP_MINUTES,
)
from utils.gcs import (
    is_gcs_uri, parse_gcs_uri, download_from_gcs, upload_to_gcs, delete_gcs_blobs,
)
from utils.time import parse_offset, seconds_to_timestamp
from json_to_ass import (
    extract_dialogue_lines, snap_gaps, enforce_min_duration,
    lines_to_ass, print_quality_report,
    DEFAULT_PAUSE_THRESHOLD, DEFAULT_MAX_LINE_CHARS,
    DEFAULT_COMMA_SPLIT_CHARS, DEFAULT_SNAP_GAP, DEFAULT_MIN_DURATION,
)


DEFAULT_REGION = "us"
DEFAULT_CHUNK_MINUTES = 18
DEFAULT_GCS_BUCKET = "subtitling-projects"
MAX_BATCH_FILES = 15
MAX_AUDIO_LENGTH_SECS = 8 * 60 * 60


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


def transcript_to_json(transcript, time_offset: float = 0.0,
                       chunk_duration: float = 0.0) -> list[dict]:
    """Convert a protobuf transcript to a JSON-serializable list of results.

    chunk_duration: if >0, used to detect absurdly large timestamps that
    exceed the chunk length (another Chirp 3 bug).
    """
    results = []
    for result in transcript.results:
        if not result.alternatives:
            continue
        alt = result.alternatives[0]
        words = []
        for w in alt.words:
            start = parse_offset(w.start_offset)
            end = parse_offset(w.end_offset)
            # Chirp 3 sometimes returns bogus word offsets: zero, negative,
            # the chunk duration, or absurdly large values for both start
            # and end. These must be clamped before adding time_offset,
            # otherwise the chunk start gets added to a zero value and
            # produces a plausible-looking but wrong timestamp
            # (e.g. 0 + 1080 = 1080s instead of ~1310s).
            if chunk_duration > 0:
                if start > chunk_duration:
                    start = end if end <= chunk_duration else 0
                if end > chunk_duration:
                    end = start
            if end <= 0 or end < start:
                end = start
            words.append({
                "word": w.word,
                "startOffset": f"{start + time_offset:.2f}s",
                "endOffset": f"{end + time_offset:.2f}s",
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


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Transcribe audio using GCP Speech-to-Text (Chirp 3) and generate ASS subtitles. "
                    "Accepts a local audio/video file or a GCS URI (gs://...). "
                    "Automatically splits audio longer than 20 minutes into chunks. "
                    "Raw JSON transcripts are saved for re-running json_to_ass.py with different parameters."
    )
    parser.add_argument("--input", required=True,
                        help="Local audio/video file or GCS URI (gs://bucket/path/file.opus)")
    parser.add_argument("--transcripts-dir", default=None,
                        help="Output directory for raw JSON transcript files (default: raw_transcripts/ next to input file)")
    parser.add_argument("--ass-output", default=None,
                        help="Override ASS output filename (default: input filename with .ass extension)")
    parser.add_argument("--project-id", default=None,
                        help="GCP project ID (default: $GOOGLE_CLOUD_PROJECT)")
    parser.add_argument("--region", default=DEFAULT_REGION,
                        help=f"GCP region (default: '{DEFAULT_REGION}')")
    parser.add_argument("--chunk-minutes", type=float, default=DEFAULT_CHUNK_MINUTES,
                        help=f"Chunk duration in minutes (default: {DEFAULT_CHUNK_MINUTES})")
    parser.add_argument("--gcs-bucket", default=DEFAULT_GCS_BUCKET,
                        help=f"GCS bucket for uploading local files (default: '{DEFAULT_GCS_BUCKET}')")
    parser.add_argument("--trim-start", type=float, default=0.0,
                        help="Skip this many seconds of audio before transcribing (default: 0, no trim)")

    args = parser.parse_args()

    project_id = args.project_id or os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        parser.error("GCP project ID required: set GOOGLE_CLOUD_PROJECT env var or pass --project-id")
    chunk_seconds = args.chunk_minutes * 60
    trim_offset = args.trim_start

    input_is_gcs = is_gcs_uri(args.input)
    input_label = "(GCS)" if input_is_gcs else "(local)"

    # Derive transcripts directory
    if args.transcripts_dir:
        transcripts_dir = Path(args.transcripts_dir)
    elif input_is_gcs:
        transcripts_dir = Path("raw_transcripts")
    else:
        transcripts_dir = Path(args.input).parent / "raw_transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    # Derive ASS output path
    if args.ass_output:
        ass_output = Path(args.ass_output)
    elif input_is_gcs:
        ass_output = transcripts_dir / (Path(args.input).stem + ".ass")
    else:
        ass_output = Path(args.input).with_suffix(".ass")

    print(f"\n{'='*60}")
    print(f"GCP Chirp 3 Batch Transcription")
    print(f"{'='*60}")
    print(f"  Input:      {args.input} {input_label}")
    print(f"  Transcripts: {transcripts_dir}")
    print(f"  ASS output: {ass_output}")
    print(f"  Project:    {project_id}")
    print(f"  Region:     {args.region}")
    print(f"  Chunk size: {args.chunk_minutes} min")
    if not input_is_gcs:
        print(f"  GCS bucket: {args.gcs_bucket}")
    if trim_offset > 0:
        print(f"  Trim start: {trim_offset:.1f}s ({trim_offset/60:.1f} min)")
    print(f"{'='*60}\n")

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Step 1: Get audio locally
        input_gcs_uri = None  # set if we already have a GCS URI for transcription
        if input_is_gcs:
            print("[1/4] Downloading audio from GCS...")
            _bucket, input_blob = parse_gcs_uri(args.input)
            ext = Path(input_blob).suffix
            local_audio = os.path.join(tmp_dir, f"input{ext}")
            download_from_gcs(args.input, local_audio, project_id)
            input_gcs_uri = args.input
        else:
            print("[1/4] Using local audio file...")
            local_path = Path(args.input)
            if not local_path.is_file():
                parser.error(f"Local file not found: {args.input}")
            local_audio = str(local_path)
            ext = local_path.suffix
            print(f"  File: {local_audio}")

        # Extract audio if input is a video container
        if has_video_stream(local_audio):
            print("  Detected video stream, extracting audio...")
            # Probe audio codec to pick the right container extension
            codec_result = subprocess.run(
                ["ffprobe", "-v", "error", "-select_streams", "a:0",
                 "-show_entries", "stream=codec_name", "-of", "csv=p=0",
                 local_audio],
                capture_output=True, text=True,
            )
            codec = codec_result.stdout.strip()
            codec_ext_map = {"opus": ".opus", "vorbis": ".ogg", "aac": ".m4a",
                             "mp3": ".mp3", "flac": ".flac", "pcm_s16le": ".wav"}
            ext = codec_ext_map.get(codec, ".ogg")
            print(f"  Audio codec: {codec} -> container: {ext}")
            audio_path = os.path.join(tmp_dir, f"extracted_audio{ext}")
            extract_audio(local_audio, audio_path)
            local_audio = audio_path
            # Invalidate any existing GCS URI since we now have a different file
            input_gcs_uri = None

        # Trim leading audio if requested
        if trim_offset > 0:
            trimmed_path = os.path.join(tmp_dir, f"trimmed{Path(local_audio).suffix}")
            trim_audio(local_audio, trim_offset, trimmed_path)
            local_audio = trimmed_path
            # Invalidate any existing GCS URI since we now have a different file
            input_gcs_uri = None

        # Step 2: Analyze audio duration
        print("\n[2/4] Analyzing audio duration...")
        duration = get_audio_duration(local_audio)
        print(f"  Duration: {duration:.1f}s ({duration/60:.1f} min)")
        print(f"  Word-timestamp limit: {MAX_WORD_TIMESTAMP_MINUTES} min")

        all_raw_results = []

        if duration <= MAX_WORD_TIMESTAMP_MINUTES * 60:
            # Short audio — transcribe directly
            print(f"  -> Under limit, no splitting needed")
            print("\n[3/4] Transcribing (single file)...")

            # Upload local file to GCS if needed
            uploaded_input = False
            if input_gcs_uri is None:
                filename = Path(local_audio).name
                input_gcs_uri = f"gs://{args.gcs_bucket}/tmp/transcribe_input/{filename}"
                print(f"  Uploading to {input_gcs_uri}...")
                upload_to_gcs(local_audio, input_gcs_uri, project_id)
                uploaded_input = True

            try:
                transcript = transcribe_batch(input_gcs_uri, project_id, args.region)
                num_results = len(transcript.results)
                num_words = sum(len(r.alternatives[0].words) for r in transcript.results if r.alternatives)
                print(f"  API returned {num_results} result(s), {num_words} total words")

                raw_data = transcript_to_json(transcript, time_offset=trim_offset,
                                                chunk_duration=duration)
                all_raw_results.extend(raw_data)
                chunk_path = transcripts_dir / "transcript.json"
                chunk_path.write_text(json.dumps({"results": raw_data}, indent=2, ensure_ascii=False),
                                      encoding="utf-8")
                print(f"  Saved to {chunk_path}")
            finally:
                if uploaded_input:
                    print(f"  Cleaning up temporary GCS file...")
                    try:
                        delete_gcs_blobs([input_gcs_uri], project_id)
                    except Exception as e:
                        print(f"  Warning: failed to clean up GCS file: {e}")
        else:
            # Long audio — split into chunks
            print(f"  -> Exceeds limit, splitting required")

            print(f"\n[3/4] Splitting and transcribing...")
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
            print(f"\n  Uploading chunks to GCS...")
            chunk_uris = []
            tmp_gcs_prefix = f"gs://{args.gcs_bucket}/tmp/transcribe_chunks/"
            for chunk_path, _ in chunks:
                chunk_name = Path(chunk_path).name
                chunk_uri = f"{tmp_gcs_prefix}{chunk_name}"
                upload_to_gcs(chunk_path, chunk_uri, project_id)
                chunk_uris.append(chunk_uri)
            print(f"  Uploaded {len(chunk_uris)} chunks to {tmp_gcs_prefix}")

            # Transcribe each chunk
            print(f"\n  Transcribing chunks...")
            try:
                for i, ((chunk_path, chunk_start), chunk_uri) in enumerate(zip(chunks, chunk_uris)):
                    chunk_dur = get_audio_duration(chunk_path)
                    print(f"\n  --- Chunk {i+1}/{len(chunks)} ---")
                    print(f"  Time range: {seconds_to_timestamp(chunk_start)} - "
                          f"{seconds_to_timestamp(chunk_start + chunk_dur)}")
                    print(f"  URI: {chunk_uri}")

                    transcript = transcribe_batch(chunk_uri, project_id, args.region)

                    num_results = len(transcript.results)
                    num_words = sum(len(r.alternatives[0].words)
                                    for r in transcript.results if r.alternatives)
                    print(f"  API returned {num_results} result(s), {num_words} total words")

                    raw_data = transcript_to_json(transcript, time_offset=chunk_start + trim_offset,
                                                    chunk_duration=chunk_dur)
                    all_raw_results.extend(raw_data)
                    raw_path = transcripts_dir / f"chunk_{i:03d}.json"
                    chunk_meta = {"results": raw_data, "chunk_start": chunk_start,
                                    "chunk_duration": chunk_dur}
                    if trim_offset > 0:
                        chunk_meta["trim_offset"] = trim_offset
                    raw_path.write_text(
                        json.dumps(chunk_meta, indent=2, ensure_ascii=False),
                        encoding="utf-8")
                    print(f"  Saved to {raw_path}")
            finally:
                print(f"\n  Cleaning up {len(chunk_uris)} temporary GCS files...")
                try:
                    delete_gcs_blobs(chunk_uris, project_id)
                except Exception as e:
                    print(f"  Warning: failed to clean up some GCS files: {e}")

    # Save merged transcript
    merged_path = transcripts_dir / "merged.json"
    merged_data = {"results": all_raw_results}
    if trim_offset > 0:
        merged_data["trim_offset"] = trim_offset
    merged_path.write_text(
        json.dumps(merged_data, indent=2, ensure_ascii=False),
        encoding="utf-8")

    # Summary
    total_words = sum(len(r["alternatives"][0]["words"]) for r in all_raw_results)
    print(f"\n{'='*60}")
    print(f"Transcription complete!")
    print(f"{'='*60}")
    print(f"  Transcripts dir:   {transcripts_dir}")
    print(f"  Merged transcript: {merged_path}")
    print(f"  Total results:     {len(all_raw_results)}")
    print(f"  Total words:       {total_words}")

    # Generate ASS subtitle file
    print(f"\n[4/4] Generating ASS subtitles...")
    title = ass_output.stem
    lines = extract_dialogue_lines(all_raw_results,
                                   pause_threshold=DEFAULT_PAUSE_THRESHOLD,
                                   max_line_chars=DEFAULT_MAX_LINE_CHARS,
                                   comma_split_chars=DEFAULT_COMMA_SPLIT_CHARS)
    lines.sort(key=lambda x: x["start"])
    snapped = snap_gaps(lines, DEFAULT_SNAP_GAP)
    print(f"  Snapped {snapped} gap(s) under {DEFAULT_SNAP_GAP}s")
    extended = enforce_min_duration(lines, DEFAULT_MIN_DURATION)
    print(f"  Extended {extended} line(s) to meet {DEFAULT_MIN_DURATION}s minimum duration")
    ass_content = lines_to_ass(lines, title)
    ass_output.parent.mkdir(parents=True, exist_ok=True)
    ass_output.write_text(ass_content, encoding="utf-8")
    print(f"  Generated: {ass_output}")
    print_quality_report(lines)
    print(f"\nTune splitting: uv run json_to_ass.py {merged_path} {ass_output}")


if __name__ == "__main__":
    main()
