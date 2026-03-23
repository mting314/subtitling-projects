"""Tests for json_to_ass module."""

import json
import os
import tempfile
import unittest

from json_to_ass import (
    _get_word_time,
    _emit_line,
    extract_dialogue_lines,
    load_transcript,
    lines_to_ass,
    pad_timing,
    snap_gaps,
    enforce_min_duration,
)
from quality_report import analyze_quality
from utils.time import seconds_to_timestamp


class TestSecondsToAss(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(seconds_to_timestamp(0.0), "0:00:00.00")

    def test_complex_time(self):
        self.assertEqual(seconds_to_timestamp(3723.5), "1:02:03.50")

    def test_sub_second(self):
        self.assertEqual(seconds_to_timestamp(0.75), "0:00:00.75")


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
            ("これは長いテキストです、", 1.0, 2.0),  # 12 chars, has comma
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
            "alternatives": [
                {
                    "transcript": "".join(w["word"] for w in words),
                    "words": words,
                }
            ],
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


class TestPadTiming(unittest.TestCase):
    def _line(self, start, end, style="JP"):
        return {"start": start, "end": end, "style": style, "text": "テスト"}

    def test_basic_padding(self):
        """Lead-in shifts start earlier, lead-out shifts end later."""
        lines = [self._line(5.0, 6.0)]
        count = pad_timing(lines, 0.125, 0.5)
        self.assertEqual(count, 1)
        self.assertAlmostEqual(lines[0]["start"], 4.875)
        self.assertAlmostEqual(lines[0]["end"], 6.5)

    def test_lead_in_pushes_past_previous_end(self):
        """Lead-in applies full amount even if it overlaps previous line's time."""
        lines = [self._line(1.0, 2.0), self._line(2.05, 3.0)]
        count = pad_timing(lines, 0.125, 0.5)
        self.assertEqual(count, 2)
        # Pass 1: line[1] start 2.05 - 0.125 = 1.925 (not capped at prev end)
        self.assertAlmostEqual(lines[1]["start"], 1.925)
        # Pass 2: line[0] end 2.0 + 0.5 = 2.5, shrunk to line[1] start (1.925)
        self.assertAlmostEqual(lines[0]["end"], 1.925)

    def test_connection_point_shifts_back(self):
        """When gap > lead-in, connection point shifts back by lead-in amount."""
        # Gap of 0.5s between lines — lead-in of 0.125 has room to fully apply
        lines = [self._line(1.0, 2.0), self._line(2.5, 3.0)]
        count = pad_timing(lines, 0.125, 0.5)
        self.assertEqual(count, 2)
        # Pass 1: line[1] start 2.5 - 0.125 = 2.375
        self.assertAlmostEqual(lines[1]["start"], 2.375)
        # Pass 2: line[0] end 2.0 + 0.5 = 2.5, capped at line[1] start (2.375) → 2.375
        self.assertAlmostEqual(lines[0]["end"], 2.375)

    def test_no_overlap_with_next(self):
        """Lead-out capped at next line's shifted start (after lead-in)."""
        lines = [self._line(1.0, 2.0), self._line(2.2, 3.0)]
        count = pad_timing(lines, 0.125, 0.5)
        self.assertEqual(count, 2)
        # Pass 1: line[1] start 2.2 - 0.125 = 2.075
        self.assertAlmostEqual(lines[1]["start"], 2.075)
        # Pass 2: line[0] end 2.0 + 0.5 = 2.5, capped at line[1] shifted start (2.075)
        self.assertAlmostEqual(lines[0]["end"], 2.075)

    def test_first_line_capped_at_zero(self):
        """First line's lead-in doesn't go below 0."""
        lines = [self._line(0.05, 1.0)]
        count = pad_timing(lines, 0.125, 0.5)
        self.assertEqual(count, 1)
        self.assertAlmostEqual(lines[0]["start"], 0.0)
        self.assertAlmostEqual(lines[0]["end"], 1.5)

    def test_last_line_lead_out_uncapped(self):
        """Last line's lead-out extends freely (no next line)."""
        lines = [self._line(1.0, 2.0)]
        count = pad_timing(lines, 0.0, 0.5)
        self.assertEqual(count, 1)
        self.assertAlmostEqual(lines[0]["end"], 2.5)

    def test_disabled_when_zero(self):
        """No changes when both lead-in and lead-out are 0."""
        lines = [self._line(1.0, 2.0), self._line(3.0, 4.0)]
        count = pad_timing(lines, 0.0, 0.0)
        self.assertEqual(count, 0)
        self.assertAlmostEqual(lines[0]["start"], 1.0)
        self.assertAlmostEqual(lines[0]["end"], 2.0)

    def test_lead_in_only(self):
        """Only lead-in applied when lead-out is 0."""
        lines = [self._line(5.0, 6.0)]
        count = pad_timing(lines, 0.125, 0.0)
        self.assertEqual(count, 1)
        self.assertAlmostEqual(lines[0]["start"], 4.875)
        self.assertAlmostEqual(lines[0]["end"], 6.0)

    def test_lead_out_only(self):
        """Only lead-out applied when lead-in is 0."""
        lines = [self._line(5.0, 6.0)]
        count = pad_timing(lines, 0.0, 0.5)
        self.assertEqual(count, 1)
        self.assertAlmostEqual(lines[0]["start"], 5.0)
        self.assertAlmostEqual(lines[0]["end"], 6.5)

    def test_returns_correct_count(self):
        """Count reflects only lines that were actually modified."""
        lines = [
            self._line(1.0, 2.0),
            self._line(5.0, 6.0),
            self._line(10.0, 11.0),
        ]
        count = pad_timing(lines, 0.125, 0.5)
        self.assertEqual(count, 3)

    def test_tight_lines_lead_in_wins(self):
        """Adjacent lines: lead-in pushes into previous line, shrinking its lead-out."""
        lines = [self._line(1.0, 2.0), self._line(2.0, 3.0)]
        pad_timing(lines, 0.125, 0.5)
        # First: lead-in shifts start to 0.875
        self.assertAlmostEqual(lines[0]["start"], 0.875)
        # Second: lead-in shifts start to 1.875 (full 125ms, into line 0's time)
        self.assertAlmostEqual(lines[1]["start"], 1.875)
        # First: lead-out shrunk from 2.0 to 1.875 (yields to line 1's lead-in)
        self.assertAlmostEqual(lines[0]["end"], 1.875)
        # Second: lead-out extends freely
        self.assertAlmostEqual(lines[1]["end"], 3.5)


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
            self._line(5.0, 6.0),  # not snapped (1.0s gap)
        ]
        count = snap_gaps(lines, 0.1)
        self.assertEqual(count, 2)


class TestEnforceMinDuration(unittest.TestCase):
    def _line(self, start, end, style="JP"):
        return {"start": start, "end": end, "style": style, "text": "テスト"}

    def test_short_line_extended_via_lead_out(self):
        """Short line extends end when there's room after it."""
        lines = [self._line(1.0, 1.2), self._line(3.0, 4.0)]
        count = enforce_min_duration(lines, 0.5)
        self.assertEqual(count, 1)
        self.assertAlmostEqual(lines[0]["start"], 1.0)
        self.assertAlmostEqual(lines[0]["end"], 1.5)

    def test_short_line_extended_via_lead_in(self):
        """Short line extends start when end is blocked by next line."""
        lines = [self._line(1.0, 1.5), self._line(2.0, 2.1), self._line(2.1, 3.0)]
        count = enforce_min_duration(lines, 0.5)
        self.assertEqual(count, 1)
        # Lead-out blocked by next line at 2.1 (0 room), so lead-in extends back
        self.assertAlmostEqual(lines[1]["start"], 1.6)
        self.assertAlmostEqual(lines[1]["end"], 2.1)

    def test_both_lead_in_and_lead_out(self):
        """Short line sandwiched tightly uses both lead-out and lead-in."""
        lines = [self._line(0.0, 0.8), self._line(1.0, 1.1), self._line(1.2, 2.0)]
        count = enforce_min_duration(lines, 0.5)
        self.assertEqual(count, 1)
        # Lead-out: 1.1 -> 1.2 (+0.1), still need 0.3 more
        self.assertAlmostEqual(lines[1]["end"], 1.2)
        # Lead-in: 1.0 -> 0.8 (capped by prev end), gets +0.2
        self.assertAlmostEqual(lines[1]["start"], 0.8)

    def test_long_enough_line_unchanged(self):
        """Lines already meeting min duration are not touched."""
        lines = [self._line(1.0, 2.0), self._line(3.0, 4.0)]
        count = enforce_min_duration(lines, 0.5)
        self.assertEqual(count, 0)
        self.assertAlmostEqual(lines[0]["end"], 2.0)

    def test_no_overlap_with_next_line(self):
        """Extension never overlaps into the next line."""
        lines = [self._line(1.0, 1.1), self._line(1.2, 2.0)]
        count = enforce_min_duration(lines, 0.5)
        self.assertEqual(count, 1)
        # Lead-out capped at next start (1.2, +0.1), then lead-in fills the rest (-0.3)
        self.assertAlmostEqual(lines[0]["end"], 1.2)
        self.assertAlmostEqual(lines[0]["start"], 0.7)

    def test_no_overlap_with_previous_line(self):
        """Lead-in never overlaps into the previous line."""
        lines = [self._line(1.0, 1.95), self._line(2.0, 2.1), self._line(2.1, 3.0)]
        count = enforce_min_duration(lines, 0.5)
        self.assertEqual(count, 1)
        # Lead-out blocked (next at 2.1, 0 room), lead-in capped at prev end (1.95)
        self.assertAlmostEqual(lines[1]["start"], 1.95)

    def test_first_line_lead_in_stops_at_zero(self):
        """First line's lead-in doesn't go below 0."""
        lines = [self._line(0.1, 0.2)]
        count = enforce_min_duration(lines, 0.5)
        self.assertEqual(count, 1)
        # Lead-out: 0.2 -> 0.6 (+0.4, plenty of room), done
        self.assertAlmostEqual(lines[0]["start"], 0.1)
        self.assertAlmostEqual(lines[0]["end"], 0.6)

    def test_returns_correct_count(self):
        lines = [
            self._line(1.0, 1.1),  # extended
            self._line(3.0, 4.0),  # fine
            self._line(5.0, 5.2),  # extended
        ]
        count = enforce_min_duration(lines, 0.5)
        self.assertEqual(count, 2)


class TestAnalyzeQuality(unittest.TestCase):
    def _line(self, start, end, text="テスト", style="JP"):
        return {"start": start, "end": end, "style": style, "text": text}

    def test_empty_lines(self):
        report = analyze_quality([])
        self.assertEqual(report["stats"]["num_lines"], 0)
        self.assertIsNone(report["stats"]["time_range"])
        for v in report["issues"].values():
            self.assertEqual(len(v), 0)

    def test_return_structure(self):
        lines = [self._line(1.0, 2.0), self._line(3.0, 4.0)]
        report = analyze_quality(lines)
        self.assertIn("stats", report)
        self.assertIn("issues", report)
        self.assertEqual(report["stats"]["num_lines"], 2)
        self.assertIsNotNone(report["stats"]["time_range"])
        self.assertIsNotNone(report["stats"]["length_stats"])
        self.assertIsNotNone(report["stats"]["duration_stats"])
        for key in [
            "zero_duration",
            "long_lines",
            "short_lines",
            "long_duration",
            "inverted",
            "overlaps",
            "large_gaps",
        ]:
            self.assertIn(key, report["issues"])

    def test_stats_values(self):
        lines = [
            self._line(1.0, 3.0, "abc"),
            self._line(4.0, 5.0, "defgh"),
        ]
        report = analyze_quality(lines)
        self.assertEqual(report["stats"]["total_chars"], 8)
        self.assertEqual(report["stats"]["time_range"], (1.0, 5.0))
        self.assertEqual(report["stats"]["length_stats"]["min"], 3)
        self.assertEqual(report["stats"]["length_stats"]["max"], 5)
        self.assertAlmostEqual(report["stats"]["duration_stats"]["min"], 1.0)
        self.assertAlmostEqual(report["stats"]["duration_stats"]["max"], 2.0)

    def test_zero_duration_detected(self):
        lines = [self._line(1.0, 1.0)]
        report = analyze_quality(lines)
        self.assertEqual(report["issues"]["zero_duration"], [0])

    def test_inverted_detected(self):
        lines = [self._line(2.0, 1.0)]
        report = analyze_quality(lines)
        self.assertEqual(report["issues"]["inverted"], [0])

    def test_long_lines_detected(self):
        lines = [self._line(1.0, 2.0, "a" * 201)]
        report = analyze_quality(lines)
        self.assertEqual(len(report["issues"]["long_lines"]), 1)
        self.assertEqual(report["issues"]["long_lines"][0], (0, 201))

    def test_short_lines_detected(self):
        lines = [self._line(1.0, 2.0, "ab")]
        report = analyze_quality(lines)
        self.assertEqual(len(report["issues"]["short_lines"]), 1)
        self.assertEqual(report["issues"]["short_lines"][0], (0, "ab"))

    def test_long_duration_detected(self):
        lines = [self._line(1.0, 62.0)]
        report = analyze_quality(lines)
        self.assertEqual(len(report["issues"]["long_duration"]), 1)

    def test_overlaps_detected(self):
        lines = [self._line(1.0, 3.0), self._line(2.0, 4.0)]
        report = analyze_quality(lines)
        self.assertEqual(report["issues"]["overlaps"], [0])

    def test_large_gaps_detected(self):
        lines = [self._line(1.0, 2.0), self._line(33.0, 34.0)]
        report = analyze_quality(lines)
        self.assertEqual(len(report["issues"]["large_gaps"]), 1)
        self.assertAlmostEqual(report["issues"]["large_gaps"][0][1], 31.0)

    def test_clean_lines_no_issues(self):
        lines = [
            self._line(1.0, 2.0, "Hello"),
            self._line(2.5, 3.5, "World"),
        ]
        report = analyze_quality(lines)
        for v in report["issues"].values():
            self.assertEqual(len(v), 0)


if __name__ == "__main__":
    unittest.main()
