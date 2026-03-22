"""Tests for json_to_ass module."""

import json
import os
import tempfile
import unittest

from json_to_ass import (
    seconds_to_ass, _get_word_time, _emit_line,
    extract_dialogue_lines, load_transcript, lines_to_ass,
    snap_gaps,
)


class TestSecondsToAss(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(seconds_to_ass(0.0), "0:00:00.00")

    def test_complex_time(self):
        self.assertEqual(seconds_to_ass(3723.5), "1:02:03.50")

    def test_sub_second(self):
        self.assertEqual(seconds_to_ass(0.75), "0:00:00.75")


class TestGetWordTime(unittest.TestCase):
    def test_normal_value(self):
        word = {"startOffset": "10.5s", "endOffset": "11.0s"}
        self.assertAlmostEqual(_get_word_time(word, "startOffset", 0.0, 100.0), 10.5)

    def test_zero_returns_fallback(self):
        word = {"startOffset": "0s", "endOffset": "11.0s"}
        self.assertAlmostEqual(_get_word_time(word, "startOffset", 5.0, 100.0), 5.0)

    def test_exceeds_max_returns_fallback(self):
        word = {"startOffset": "999.0s", "endOffset": "11.0s"}
        self.assertAlmostEqual(_get_word_time(word, "startOffset", 5.0, 100.0), 5.0)

    def test_end_offset_zero_returns_fallback(self):
        word = {"endOffset": "0s"}
        self.assertAlmostEqual(_get_word_time(word, "endOffset", 10.0, 100.0), 10.0)

    def test_start_way_past_end_returns_fallback(self):
        """startOffset wildly inconsistent with endOffset -> fallback."""
        word = {"startOffset": "200.0s", "endOffset": "10.0s"}
        # start=200 > end=10 + 60 = 70, so should return fallback
        self.assertAlmostEqual(_get_word_time(word, "startOffset", 5.0, 500.0), 5.0)

    def test_start_near_end_accepted(self):
        """startOffset close to endOffset is accepted."""
        word = {"startOffset": "50.0s", "endOffset": "51.0s"}
        self.assertAlmostEqual(_get_word_time(word, "startOffset", 0.0, 100.0), 50.0)


class TestEmitLine(unittest.TestCase):
    def test_short_text_single_line(self):
        word_data = [("こんにちは", 1.0, 2.0)]
        lines = []
        _emit_line(word_data, "JP", 40, lines)
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0]["text"], "こんにちは")
        self.assertAlmostEqual(lines[0]["start"], 1.0)
        self.assertAlmostEqual(lines[0]["end"], 2.0)

    def test_empty_word_data(self):
        lines = []
        _emit_line([], "JP", 40, lines)
        self.assertEqual(len(lines), 0)

    def test_long_text_with_comma_splits(self):
        """Long text with commas should split at the comma with longest pause."""
        # Create words totaling >40 chars with a comma
        word_data = [
            ("これは長いテキストです、", 1.0, 2.0),   # 12 chars, has comma
            ("もっと長いテキストがここにあります、", 2.0, 3.0),  # 16 chars, has comma
            ("最後のテキストです。", 3.5, 4.0),  # big pause before this = 0.5s
        ]
        lines = []
        _emit_line(word_data, "JP", 20, lines)
        # Should have split at one of the commas
        self.assertGreater(len(lines), 1)

    def test_long_text_no_commas(self):
        """Long text without commas emits as single line."""
        word_data = [
            ("これは長いテキストですがコンマがありません。", 1.0, 2.0),
        ]
        lines = []
        _emit_line(word_data, "JP", 10, lines)
        self.assertEqual(len(lines), 1)

    def test_comma_split_disabled(self):
        """When comma_split_chars=0, no splitting occurs."""
        word_data = [
            ("長いテキスト、", 1.0, 2.0),
            ("もっとテキスト。", 2.5, 3.0),
        ]
        lines = []
        _emit_line(word_data, "JP", 0, lines)
        self.assertEqual(len(lines), 1)


class TestExtractDialogueLines(unittest.TestCase):
    def _make_result(self, words, lang="ja-jp"):
        """Helper to create a transcript result dict."""
        return {
            "languageCode": lang,
            "alternatives": [{
                "transcript": "".join(w["word"] for w in words),
                "words": words,
            }],
        }

    def _make_word(self, text, start, end):
        return {"word": text, "startOffset": f"{start}s", "endOffset": f"{end}s"}

    def test_sentence_ender_splits(self):
        words = [
            self._make_word("こんにちは。", 1.0, 2.0),
            self._make_word("さようなら。", 2.1, 3.0),
        ]
        result = self._make_result(words)
        lines = extract_dialogue_lines([result])
        self.assertEqual(len(lines), 2)

    def test_pause_forces_break(self):
        words = [
            self._make_word("テスト", 1.0, 2.0),
            self._make_word("テスト", 5.0, 6.0),  # 3s pause
        ]
        result = self._make_result(words)
        lines = extract_dialogue_lines([result], pause_threshold=1.0)
        self.assertEqual(len(lines), 2)

    def test_max_chars_forces_break(self):
        # First word is 70 chars (>= max_line_chars=60), so when the second
        # word arrives, the accumulated length triggers a break.
        words = [
            self._make_word("あ" * 70, 1.0, 2.0),
            self._make_word("い" * 10, 2.1, 3.0),
        ]
        result = self._make_result(words)
        lines = extract_dialogue_lines([result], max_line_chars=60)
        self.assertEqual(len(lines), 2)

    def test_punctuation_merged(self):
        words = [
            self._make_word("テスト", 1.0, 2.0),
            self._make_word("。", 2.0, 2.1),
            self._make_word("次の文", 3.0, 4.0),
        ]
        result = self._make_result(words)
        lines = extract_dialogue_lines([result])
        # The 。 should be merged into テスト
        self.assertTrue(lines[0]["text"].endswith("。"))

    def test_style_detection(self):
        words = [self._make_word("hello", 1.0, 2.0)]
        result = self._make_result(words, lang="en-us")
        lines = extract_dialogue_lines([result])
        self.assertEqual(lines[0]["style"], "Default")

        result_jp = self._make_result(words, lang="ja-jp")
        lines_jp = extract_dialogue_lines([result_jp])
        self.assertEqual(lines_jp[0]["style"], "JP")

    def test_empty_results(self):
        lines = extract_dialogue_lines([])
        self.assertEqual(lines, [])

    def test_no_alternatives_skipped(self):
        result = {"alternatives": []}
        lines = extract_dialogue_lines([result])
        self.assertEqual(lines, [])


class TestLoadTranscript(unittest.TestCase):
    def test_load_single_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"results": [{"test": 1}]}, f)
            f.flush()
            try:
                results = load_transcript(f.name)
                self.assertEqual(len(results), 1)
                self.assertEqual(results[0]["test"], 1)
            finally:
                os.unlink(f.name)

    def test_load_directory_with_merged(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            merged_path = os.path.join(tmp_dir, "merged.json")
            with open(merged_path, "w") as f:
                json.dump({"results": [{"merged": True}]}, f)
            results = load_transcript(tmp_dir)
            self.assertEqual(len(results), 1)
            self.assertTrue(results[0]["merged"])

    def test_load_directory_chunk_files(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            for i in range(3):
                path = os.path.join(tmp_dir, f"chunk_{i:03d}.json")
                with open(path, "w") as f:
                    json.dump({"results": [{"chunk": i}]}, f)
            results = load_transcript(tmp_dir)
            self.assertEqual(len(results), 3)
            self.assertEqual(results[0]["chunk"], 0)
            self.assertEqual(results[2]["chunk"], 2)


class TestLinesToAss(unittest.TestCase):
    def test_header_present(self):
        lines = [{"start": 1.0, "end": 2.0, "style": "JP", "text": "テスト"}]
        ass = lines_to_ass(lines, "Test Title")
        self.assertIn("[Script Info]", ass)
        self.assertIn("Title: Test Title", ass)
        self.assertIn("[V4+ Styles]", ass)
        self.assertIn("[Events]", ass)

    def test_dialogue_format(self):
        lines = [{"start": 1.0, "end": 2.5, "style": "JP", "text": "テスト"}]
        ass = lines_to_ass(lines, "Test")
        self.assertIn("Dialogue: 0,0:00:01.00,0:00:02.50,JP,,0,0,0,,テスト", ass)

    def test_empty_lines(self):
        ass = lines_to_ass([], "Empty")
        self.assertIn("[Script Info]", ass)
        self.assertNotIn("Dialogue:", ass)


class TestSnapGaps(unittest.TestCase):
    def _line(self, start, end, style="JP"):
        return {"start": start, "end": end, "style": style, "text": "テスト"}

    def test_small_gap_snapped(self):
        lines = [self._line(1.0, 2.0), self._line(2.05, 3.0)]
        count = snap_gaps(lines, 0.1)
        self.assertEqual(count, 1)
        self.assertAlmostEqual(lines[0]["end"], 2.05)

    def test_large_gap_preserved(self):
        lines = [self._line(1.0, 2.0), self._line(2.5, 3.0)]
        count = snap_gaps(lines, 0.1)
        self.assertEqual(count, 0)
        self.assertAlmostEqual(lines[0]["end"], 2.0)

    def test_zero_gap_no_change(self):
        lines = [self._line(1.0, 2.0), self._line(2.0, 3.0)]
        count = snap_gaps(lines, 0.1)
        self.assertEqual(count, 0)
        self.assertAlmostEqual(lines[0]["end"], 2.0)

    def test_negative_gap_no_change(self):
        lines = [self._line(1.0, 2.5), self._line(2.0, 3.0)]
        count = snap_gaps(lines, 0.1)
        self.assertEqual(count, 0)
        self.assertAlmostEqual(lines[0]["end"], 2.5)

    def test_different_styles_not_snapped(self):
        lines = [self._line(1.0, 2.0, "JP"), self._line(2.05, 3.0, "Default")]
        count = snap_gaps(lines, 0.1)
        self.assertEqual(count, 0)
        self.assertAlmostEqual(lines[0]["end"], 2.0)

    def test_same_style_snapped(self):
        lines = [self._line(1.0, 2.0, "Default"), self._line(2.08, 3.0, "Default")]
        count = snap_gaps(lines, 0.1)
        self.assertEqual(count, 1)
        self.assertAlmostEqual(lines[0]["end"], 2.08)

    def test_returns_correct_count(self):
        lines = [
            self._line(1.0, 2.0),
            self._line(2.03, 3.0),  # snapped
            self._line(3.05, 4.0),  # snapped
            self._line(5.0, 6.0),   # not snapped (1.0s gap)
        ]
        count = snap_gaps(lines, 0.1)
        self.assertEqual(count, 2)


if __name__ == "__main__":
    unittest.main()
