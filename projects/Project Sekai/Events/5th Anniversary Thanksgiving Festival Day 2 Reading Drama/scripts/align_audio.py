"""Find where windows of reference audio land in target audio (offset = target - ref)."""

import subprocess
import sys

import numpy as np

SR = 4000
WIN = 20  # seconds


def load(path: str) -> np.ndarray:
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
        check=True, capture_output=True,
    ).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32)
    return x / (np.abs(x).max() + 1e-9)


def locate(needle: np.ndarray, hay: np.ndarray) -> tuple[int, float]:
    n = len(hay) + len(needle)
    size = 1 << (n - 1).bit_length()
    corr = np.fft.irfft(np.fft.rfft(hay, size) * np.conj(np.fft.rfft(needle, size)), size)
    corr = corr[: len(hay) - len(needle) + 1]
    # Normalise by the local energy of hay so loud passages don't win by default.
    csum = np.concatenate([[0], np.cumsum(hay**2)])
    energy = np.sqrt(csum[len(needle):] - csum[: -len(needle)]) + 1e-9
    score = corr / (energy * np.linalg.norm(needle))
    best = int(np.argmax(score))
    return best, float(score[best])


def main(ref: str, target: str) -> None:
    r, t = load(ref), load(target)
    dur = len(r) / SR
    for start in np.arange(10, dur - WIN, 60):
        seg = r[int(start * SR): int((start + WIN) * SR)]
        pos, score = locate(seg, t)
        print(f"ref {start:7.1f}s -> target {pos / SR:7.2f}s  offset {pos / SR - start:+7.2f}s  score {score:.2f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
