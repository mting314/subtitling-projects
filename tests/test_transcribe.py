"""Tests for transcribe.transcript_to_json, parse_normalization_entries, and ASS integration."""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from google.cloud.speech_v2.types import cloud_speech

from transcribe import transcript_to_json, parse_normalization_entries, transcribe_batch
from json_to_ass import (
    extract_dialogue_lines,
    snap_gaps,
    enforce_min_duration,
    lines_to_ass,
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
        transcript = _make_transcript(
            [
                [("hello", 1.0, 2.0), ("world", 2.5, 3.0)],
            ]
        )
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
        transcript = _make_transcript(
            [
                [("word", 5.0, 0.0)],
            ]
        )
        results = transcript_to_json(transcript, time_offset=0.0)
        words = results[0]["alternatives"][0]["words"]
        # end=0 -> end<=0 -> end=start=5.0
        self.assertEqual(words[0]["endOffset"], "5.00s")
        self.assertEqual(words[0]["startOffset"], "5.00s")

    def test_end_exceeds_chunk_duration(self):
        """endOffset exceeding chunk_duration should be clamped."""
        transcript = _make_transcript(
            [
                [("word", 5.0, 9999.0)],
            ]
        )
        results = transcript_to_json(transcript, time_offset=0.0, chunk_duration=1080.0)
        words = results[0]["alternatives"][0]["words"]
        # end=9999 > chunk_duration=1080 -> end=start=5.0
        self.assertEqual(words[0]["endOffset"], "5.00s")

    def test_start_exceeds_chunk_duration(self):
        """startOffset exceeding chunk_duration should fall back."""
        transcript = _make_transcript(
            [
                [("word", 9999.0, 10.0)],
            ]
        )
        results = transcript_to_json(transcript, time_offset=0.0, chunk_duration=1080.0)
        words = results[0]["alternatives"][0]["words"]
        # start=9999 > chunk_duration -> start = end if end<=chunk, else 0
        # end=10 <= 1080, so start=10
        self.assertEqual(words[0]["startOffset"], "10.00s")
        self.assertEqual(words[0]["endOffset"], "10.00s")

    def test_both_exceed_chunk_duration(self):
        """Both start and end exceeding chunk_duration -> both clamped to 0."""
        transcript = _make_transcript(
            [
                [("word", 9999.0, 9999.0)],
            ]
        )
        results = transcript_to_json(
            transcript, time_offset=100.0, chunk_duration=1080.0
        )
        words = results[0]["alternatives"][0]["words"]
        # start=9999 > 1080 -> start = end if end<=chunk, else 0 -> end=9999>1080 -> start=0
        # end=9999 > 1080 -> end=start=0
        # then end<=0 -> end=start=0
        # offset applied: 0+100=100
        self.assertEqual(words[0]["startOffset"], "100.00s")
        self.assertEqual(words[0]["endOffset"], "100.00s")

    def test_negative_end_offset(self):
        """Negative endOffset should be clamped."""
        transcript = _make_transcript(
            [
                [("word", 5.0, -1.0)],
            ]
        )
        results = transcript_to_json(transcript, time_offset=0.0)
        words = results[0]["alternatives"][0]["words"]
        # end=-1 <= 0 -> end=start=5.0
        self.assertEqual(words[0]["endOffset"], "5.00s")

    def test_language_code_preserved(self):
        transcript = _make_transcript(
            [
                [("テスト", 1.0, 2.0)],
            ],
            lang="ja-jp",
        )
        results = transcript_to_json(transcript)
        self.assertEqual(results[0]["languageCode"], "ja-jp")

    def test_result_end_offset_includes_time_offset(self):
        transcript = _make_transcript(
            [
                [("word", 1.0, 10.0)],
            ]
        )
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
        transcript = _make_transcript(
            [
                [
                    ("こんにちは。", 1.0, 2.0),
                    ("今日は", 2.5, 3.0),
                    ("いい天気ですね。", 3.2, 4.5),
                ],
                [("はい、", 5.0, 5.5), ("そうですね。", 5.8, 6.5)],
            ]
        )
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


class TestParseNormalizationEntries(unittest.TestCase):
    def _write_temp_md(self, content):
        f = tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        )
        f.write(content)
        f.close()
        self.addCleanup(os.unlink, f.name)
        return f.name

    def test_valid_table(self):
        md = self._write_temp_md(
            "## Transcript Normalization\n\n"
            "| Search | Replace | Case Sensitive |\n"
            "|--------|---------|----------------|\n"
            "| foo | bar | yes |\n"
            "| baz | qux | no |\n"
        )
        entries = parse_normalization_entries(md)
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0].search, "foo")
        self.assertEqual(entries[0].replace, "bar")
        self.assertTrue(entries[0].case_sensitive)
        self.assertEqual(entries[1].search, "baz")
        self.assertEqual(entries[1].replace, "qux")
        self.assertFalse(entries[1].case_sensitive)

    def test_empty_table(self):
        md = self._write_temp_md(
            "## Transcript Normalization\n\n"
            "| Search | Replace | Case Sensitive |\n"
            "|--------|---------|----------------|\n"
        )
        entries = parse_normalization_entries(md)
        self.assertEqual(entries, [])

    def test_missing_section(self):
        md = self._write_temp_md("## Some Other Section\n\nContent here\n")
        entries = parse_normalization_entries(md)
        self.assertEqual(entries, [])

    def test_nonexistent_file(self):
        entries = parse_normalization_entries("/nonexistent/path.md")
        self.assertEqual(entries, [])

    def test_too_many_entries(self):
        rows = "\n".join(f"| search{i} | replace{i} | yes |" for i in range(101))
        md = self._write_temp_md(
            "## Transcript Normalization\n\n"
            "| Search | Replace | Case Sensitive |\n"
            "|--------|---------|----------------|\n" + rows + "\n"
        )
        with self.assertRaises(ValueError, msg="Too many normalization entries"):
            parse_normalization_entries(md)

    def test_search_too_long(self):
        md = self._write_temp_md(
            "## Transcript Normalization\n\n"
            "| Search | Replace | Case Sensitive |\n"
            "|--------|---------|----------------|\n"
            f"| {'x' * 101} | bar | yes |\n"
        )
        with self.assertRaises(ValueError, msg="search term exceeds"):
            parse_normalization_entries(md)

    def test_replace_too_long(self):
        md = self._write_temp_md(
            "## Transcript Normalization\n\n"
            "| Search | Replace | Case Sensitive |\n"
            "|--------|---------|----------------|\n"
            f"| foo | {'y' * 101} | yes |\n"
        )
        with self.assertRaises(ValueError, msg="replace term exceeds"):
            parse_normalization_entries(md)

    def test_case_sensitive_defaults_true(self):
        md = self._write_temp_md(
            "## Transcript Normalization\n\n"
            "| Search | Replace |\n"
            "|--------|--------|\n"
            "| foo | bar |\n"
        )
        entries = parse_normalization_entries(md)
        self.assertEqual(len(entries), 1)
        self.assertTrue(entries[0].case_sensitive)

    def test_section_among_other_content(self):
        md = self._write_temp_md(
            "## Fixed Translations\n\nSome content\n\n"
            "## Transcript Normalization\n\n"
            "Description text\n\n"
            "| Search | Replace | Case Sensitive |\n"
            "|--------|---------|----------------|\n"
            "| alpha | beta | yes |\n\n"
            "## Another Section\n\nMore content\n"
        )
        entries = parse_normalization_entries(md)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].search, "alpha")


class TestTranscribeBatchConfig(unittest.TestCase):
    @patch("transcribe.SpeechClient")
    def test_config_without_normalization(self, mock_client_cls):
        mock_client = MagicMock()
        mock_client_cls.return_value = mock_client
        mock_op = MagicMock()
        mock_client.batch_recognize.return_value = mock_op
        mock_response = MagicMock()
        mock_op.result.return_value = mock_response
        mock_response.results = {"gs://bucket/audio.opus": MagicMock()}

        transcribe_batch("gs://bucket/audio.opus", "my-project", "us")

        call_args = mock_client.batch_recognize.call_args
        request = (
            call_args[1]["request"] if "request" in call_args[1] else call_args[0][0]
        )
        config = request.config
        self.assertFalse(config.transcript_normalization.entries)

    @patch("transcribe.SpeechClient")
    def test_config_with_normalization(self, mock_client_cls):
        mock_client = MagicMock()
        mock_client_cls.return_value = mock_client
        mock_op = MagicMock()
        mock_client.batch_recognize.return_value = mock_op
        mock_response = MagicMock()
        mock_op.result.return_value = mock_response
        mock_response.results = {"gs://bucket/audio.opus": MagicMock()}

        entries = [
            cloud_speech.TranscriptNormalization.Entry(
                search="foo", replace="bar", case_sensitive=True
            )
        ]
        transcribe_batch("gs://bucket/audio.opus", "my-project", "us", entries)

        call_args = mock_client.batch_recognize.call_args
        request = (
            call_args[1]["request"] if "request" in call_args[1] else call_args[0][0]
        )
        config = request.config
        self.assertEqual(len(config.transcript_normalization.entries), 1)
        self.assertEqual(config.transcript_normalization.entries[0].search, "foo")


if __name__ == "__main__":
    unittest.main()
