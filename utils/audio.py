"""FFmpeg/ffprobe audio processing helpers."""

import os
import subprocess
from pathlib import Path


MAX_WORD_TIMESTAMP_MINUTES = 20


def has_video_stream(local_path: str) -> bool:
    """Check if a file contains a video stream (i.e. is a video container, not pure audio)."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-select_streams", "v",
            "-show_entries", "stream=codec_type",
            "-of", "csv=p=0",
            local_path,
        ],
        capture_output=True, text=True,
    )
    return "video" in result.stdout


def extract_audio(local_path: str, output_path: str) -> str:
    """Extract audio from a video file, copying the audio stream without re-encoding."""
    subprocess.run(
        [
            "ffmpeg", "-y", "-i", local_path,
            "-vn", "-acodec", "copy",
            output_path,
        ],
        capture_output=True, check=True,
    )
    print(f"Extracted audio: {local_path} -> {output_path}")
    return output_path


def trim_audio(local_path: str, start_seconds: float, output_path: str) -> str:
    """Trim audio, removing everything before start_seconds. Stream copy, no re-encoding."""
    subprocess.run(
        ["ffmpeg", "-y", "-i", local_path,
         "-ss", str(start_seconds), "-vn", "-acodec", "copy", output_path],
        capture_output=True, check=True,
    )
    print(f"Trimmed audio: skipped first {start_seconds:.1f}s -> {output_path}")
    return output_path


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


def split_audio(local_path: str, chunk_seconds: float,
                output_dir: str) -> list[tuple[str, float]]:
    """Split audio into non-overlapping chunks.

    Returns list of (chunk_path, chunk_start_seconds) tuples.
    """
    duration = get_audio_duration(local_path)
    ext = Path(local_path).suffix

    if duration <= MAX_WORD_TIMESTAMP_MINUTES * 60:
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
