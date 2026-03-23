"""Tests for utils.audio module."""

import unittest
from unittest.mock import patch, MagicMock

from utils.audio import (
    has_video_stream,
    get_audio_duration,
    extract_audio,
    trim_audio,
    split_audio,
)


class TestHasVideoStream(unittest.TestCase):
    @patch("utils.audio.subprocess.run")
    def test_video_present(self, mock_run):
        mock_run.return_value = MagicMock(stdout="video\n")
        self.assertTrue(has_video_stream("/path/to/file.mkv"))

    @patch("utils.audio.subprocess.run")
    def test_no_video(self, mock_run):
        mock_run.return_value = MagicMock(stdout="")
        self.assertFalse(has_video_stream("/path/to/file.opus"))


class TestGetAudioDuration(unittest.TestCase):
    @patch("utils.audio.subprocess.run")
    def test_normal_duration(self, mock_run):
        mock_run.return_value = MagicMock(stdout="1234.56\n")
        self.assertAlmostEqual(get_audio_duration("/path/to/file.opus"), 1234.56)


class TestExtractAudio(unittest.TestCase):
    @patch("utils.audio.subprocess.run")
    def test_extract(self, mock_run):
        result = extract_audio("/path/to/video.mkv", "/tmp/audio.opus")
        self.assertEqual(result, "/tmp/audio.opus")
        args = mock_run.call_args[0][0]
        self.assertEqual(args[0], "ffmpeg")
        self.assertIn("-vn", args)
        self.assertIn("-acodec", args)
        self.assertIn("/path/to/video.mkv", args)
        self.assertIn("/tmp/audio.opus", args)


class TestTrimAudio(unittest.TestCase):
    @patch("utils.audio.subprocess.run")
    def test_trim(self, mock_run):
        result = trim_audio("/path/to/audio.opus", 570.0, "/tmp/trimmed.opus")
        self.assertEqual(result, "/tmp/trimmed.opus")
        args = mock_run.call_args[0][0]
        self.assertIn("-ss", args)
        ss_idx = args.index("-ss")
        self.assertEqual(args[ss_idx + 1], "570.0")


class TestSplitAudio(unittest.TestCase):
    @patch("utils.audio.subprocess.run")
    @patch("utils.audio.get_audio_duration")
    def test_short_audio_no_split(self, mock_duration, mock_run):
        """Audio under 20 min should return the input file unchanged."""
        mock_duration.return_value = 600.0  # 10 min
        result = split_audio("/path/to/audio.opus", 1080.0, "/tmp")
        self.assertEqual(result, [("/path/to/audio.opus", 0.0)])
        mock_run.assert_not_called()

    @patch("utils.audio.subprocess.run")
    @patch("utils.audio.get_audio_duration")
    def test_long_audio_splits(self, mock_duration, mock_run):
        """40 min audio with 18 min chunks -> 3 chunks."""
        mock_duration.return_value = 2400.0  # 40 min
        result = split_audio("/path/to/audio.opus", 1080.0, "/tmp")

        self.assertEqual(len(result), 3)
        # Check chunk start offsets
        self.assertAlmostEqual(result[0][1], 0.0)
        self.assertAlmostEqual(result[1][1], 1080.0)
        self.assertAlmostEqual(result[2][1], 2160.0)
        # ffmpeg called once per chunk
        self.assertEqual(mock_run.call_count, 3)


if __name__ == "__main__":
    unittest.main()
