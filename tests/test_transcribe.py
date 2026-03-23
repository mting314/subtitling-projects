"""Tests for gcp_transcribe_batch.transcript_to_json and ASS integration."""

import unittest
from unittest.mock import MagicMock

from gcp_transcribe_batch import transcript_to_json
from json_to_ass import (
    extract_dialogue_lines, snap_gaps, enforce_min_duration, lines_to_ass,
)


def _make_word(text, start_seconds, end_seconds):
    """Create a mock protobuf word with start/end offsets."""
    word = MagicMock()
    word.word = text
    word.start_offset = MagicMock()
    word.start_offset.total_seconds.return_value = start_seconds
    word.end_offset = MagicMock()
    word.end_offset.total_seconds.return_value = end_seconds
    return word


def _make_transcript(word_groups, lang="ja-jp"):
    """Create a mock protobuf transcript.

    word_groups: list of lists of (text, start, end) tuples, one list per result.
    """
    transcript = MagicMock()
    results = []
    for words_data in word_groups:
        result = MagicMock()
        result.language_code = lang
        alt = MagicMock()
        alt.transcript = "".join(w[0] for w in words_data)
        alt.words = [_make_word(t, s, e) for t, s, e in words_data]
        result.alternatives = [alt]
        # result_end_offset = max end time
        max_end = max(w[2] for w in words_data) if words_data else 0
        result.result_end_offset = MagicMock()
        result.result_end_offset.total_seconds.return_value = max_end
        results.append(result)
    transcript.results = results
    return transcript


class TestTranscriptToJson(unittest.TestCase):
    def test_normal_words_with_offset(self):
        """Words should have time_offset added to their timestamps."""
        transcript = _make_transcript([
            [("hello", 1.0, 2.0), ("world", 2.5, 3.0)],
        ])
        results = transcript_to_json(transcript, time_offset=100.0)

        self.assertEqual(len(results), 1)
        words = results[0]["alternatives"][0]["words"]
        self.assertEqual(len(words), 2)
        self.assertEqual(words[0]["word"], "hello")
        self.assertEqual(words[0]["startOffset"], "101.00s")
        self.assertEqual(words[0]["endOffset"], "102.00s")
        self.assertEqual(words[1]["startOffset"], "102.50s")
        self.assertEqual(words[1]["endOffset"], "103.00s")

    def test_bogus_zero_end_offset(self):
        """Zero endOffset should be clamped to startOffset."""
        transcript = _make_transcript([
            [("word", 5.0, 0.0)],
        ])
        results = transcript_to_json(transcript, time_offset=0.0)
        words = results[0]["alternatives"][0]["words"]
        # end=0 -> end<=0 -> end=start=5.0
        self.assertEqual(words[0]["endOffset"], "5.00s")
        self.assertEqual(words[0]["startOffset"], "5.00s")

    def test_end_exceeds_chunk_duration(self):
        """endOffset exceeding chunk_duration should be clamped."""
        transcript = _make_transcript([
            [("word", 5.0, 9999.0)],
        ])
        results = transcript_to_json(transcript, time_offset=0.0, chunk_duration=1080.0)
        words = results[0]["alternatives"][0]["words"]
        # end=9999 > chunk_duration=1080 -> end=start=5.0
        self.assertEqual(words[0]["endOffset"], "5.00s")

    def test_start_exceeds_chunk_duration(self):
        """startOffset exceeding chunk_duration should fall back."""
        transcript = _make_transcript([
            [("word", 9999.0, 10.0)],
        ])
        results = transcript_to_json(transcript, time_offset=0.0, chunk_duration=1080.0)
        words = results[0]["alternatives"][0]["words"]
        # start=9999 > chunk_duration -> start = end if end<=chunk, else 0
        # end=10 <= 1080, so start=10
        self.assertEqual(words[0]["startOffset"], "10.00s")
        self.assertEqual(words[0]["endOffset"], "10.00s")

    def test_both_exceed_chunk_duration(self):
        """Both start and end exceeding chunk_duration -> both clamped to 0."""
        transcript = _make_transcript([
            [("word", 9999.0, 9999.0)],
        ])
        results = transcript_to_json(transcript, time_offset=100.0, chunk_duration=1080.0)
        words = results[0]["alternatives"][0]["words"]
        # start=9999 > 1080 -> start = end if end<=chunk, else 0 -> end=9999>1080 -> start=0
        # end=9999 > 1080 -> end=start=0
        # then end<=0 -> end=start=0
        # offset applied: 0+100=100
        self.assertEqual(words[0]["startOffset"], "100.00s")
        self.assertEqual(words[0]["endOffset"], "100.00s")

    def test_negative_end_offset(self):
        """Negative endOffset should be clamped."""
        transcript = _make_transcript([
            [("word", 5.0, -1.0)],
        ])
        results = transcript_to_json(transcript, time_offset=0.0)
        words = results[0]["alternatives"][0]["words"]
        # end=-1 <= 0 -> end=start=5.0
        self.assertEqual(words[0]["endOffset"], "5.00s")

    def test_language_code_preserved(self):
        transcript = _make_transcript([
            [("テスト", 1.0, 2.0)],
        ], lang="ja-jp")
        results = transcript_to_json(transcript)
        self.assertEqual(results[0]["languageCode"], "ja-jp")

    def test_result_end_offset_includes_time_offset(self):
        transcript = _make_transcript([
            [("word", 1.0, 10.0)],
        ])
        results = transcript_to_json(transcript, time_offset=500.0)
        self.assertEqual(results[0]["resultEndOffset"], "510.00s")

    def test_no_alternatives_skipped(self):
        transcript = MagicMock()
        result = MagicMock()
        result.alternatives = []
        transcript.results = [result]
        results = transcript_to_json(transcript)
        self.assertEqual(len(results), 0)


class TestAssOutputIntegration(unittest.TestCase):
    """Verify transcript_to_json output feeds through the full ASS pipeline."""

    def test_end_to_end_ass_generation(self):
        """transcript_to_json → extract_dialogue_lines → snap_gaps → enforce_min_duration → lines_to_ass."""
        transcript = _make_transcript([
            [("こんにちは。", 1.0, 2.0), ("今日は", 2.5, 3.0), ("いい天気ですね。", 3.2, 4.5)],
            [("はい、", 5.0, 5.5), ("そうですね。", 5.8, 6.5)],
        ])
        raw_results = transcript_to_json(transcript, time_offset=0.0)

        lines = extract_dialogue_lines(raw_results)
        self.assertGreater(len(lines), 0)

        lines.sort(key=lambda x: x["start"])
        snap_gaps(lines, 0.25)
        enforce_min_duration(lines, 0.5)

        ass_content = lines_to_ass(lines, "Test Title")
        self.assertIn("[Script Info]", ass_content)
        self.assertIn("Title: Test Title", ass_content)
        self.assertIn("[Events]", ass_content)
        self.assertIn("Dialogue:", ass_content)

        for line in lines:
            self.assertGreaterEqual(line["end"] - line["start"], 0)


if __name__ == "__main__":
    unittest.main()
