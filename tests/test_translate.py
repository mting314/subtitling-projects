"""Tests for translate.py."""

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from post_processing import merge_absorbed_lines
from translate import (
    build_system_prompt,
    format_batch_input,
    load_checkpoint,
    parse_structured_response,
    save_checkpoint,
    translate_batch,
)


SAMPLE_ASS = """\
[Script Info]
Title: Test
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,48,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:05.00,0:00:08.00,Default,,0,0,0,,こんにちは
Comment: 0,0:00:08.00,0:00:09.00,Default,,0,0,0,,This is a comment
Dialogue: 0,0:00:09.00,0:00:12.00,Default,,0,0,0,,ありがとう
Dialogue: 0,0:00:12.00,0:00:15.00,Default,,0,0,0,,さようなら
"""


class TestBuildSystemPrompt(unittest.TestCase):
    def test_with_instructions_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write("# Test Instructions\nBe accurate.")
            f.flush()
            try:
                prompt = build_system_prompt(f.name, None)
                self.assertIn("Test Instructions", prompt)
            finally:
                os.unlink(f.name)

    def test_missing_instructions_still_works(self):
        prompt = build_system_prompt("nonexistent.md", None)
        self.assertIn("professional Japanese-to-English subtitle translator", prompt)

    def test_preamble_always_present(self):
        prompt = build_system_prompt("nonexistent.md", None)
        self.assertIn("JSON array", prompt)
        self.assertIn("translated", prompt)

    def test_with_project_ref(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as inst:
            inst.write("Instructions")
            inst.flush()
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".md", delete=False
            ) as ref:
                ref.write("# Project Reference\nMailbox!")
                ref.flush()
                try:
                    prompt = build_system_prompt(inst.name, ref.name)
                    self.assertIn("Project Reference", prompt)
                    self.assertIn("Mailbox!", prompt)
                finally:
                    os.unlink(inst.name)
                    os.unlink(ref.name)


class TestFormatBatchInput(unittest.TestCase):
    def test_basic_formatting(self):
        events = [
            {"style": "Default", "text": "こんにちは"},
            {"style": "Speaker1", "text": "ありがとう"},
        ]
        result = json.loads(format_batch_input(events, 0))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["style"], "Default")
        self.assertEqual(result[0]["text"], "こんにちは")
        self.assertEqual(result[1]["id"], 2)

    def test_offset_numbering(self):
        events = [{"style": "Default", "text": "テスト"}]
        result = json.loads(format_batch_input(events, 10))
        self.assertEqual(result[0]["id"], 11)

    def test_empty_style(self):
        events = [{"style": "", "text": "テスト"}]
        result = json.loads(format_batch_input(events, 0))
        self.assertEqual(result[0]["style"], "")
        self.assertEqual(result[0]["text"], "テスト")

    def test_output_is_valid_json(self):
        events = [
            {"style": "Default", "text": 'Text with "quotes" and {tags}'},
        ]
        result_str = format_batch_input(events, 0)
        parsed = json.loads(result_str)
        self.assertEqual(parsed[0]["text"], 'Text with "quotes" and {tags}')


class TestParseStructuredResponse(unittest.TestCase):
    def test_basic_parsing(self):
        response = json.dumps(
            [
                {"id": 1, "original": "こんにちは", "translated": "Hello!"},
                {"id": 2, "original": "ありがとう", "translated": "Thank you!"},
                {"id": 3, "original": "さようなら", "translated": "Goodbye!"},
            ]
        )
        result, missing = parse_structured_response(response, 3, 0)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])
        self.assertEqual(missing, 0)

    def test_with_offset(self):
        response = json.dumps(
            [
                {"id": 11, "original": "こんにちは", "translated": "Hello!"},
                {"id": 12, "original": "ありがとう", "translated": "Thank you!"},
            ]
        )
        result, missing = parse_structured_response(response, 2, 10)
        self.assertEqual(result, ["Hello!", "Thank you!"])
        self.assertEqual(missing, 0)

    def test_missing_line(self):
        response = json.dumps(
            [
                {"id": 1, "original": "こんにちは", "translated": "Hello!"},
                {"id": 3, "original": "さようなら", "translated": "Goodbye!"},
            ]
        )
        result, missing = parse_structured_response(response, 3, 0)
        self.assertEqual(result[0], "Hello!")
        self.assertEqual(result[1], "")
        self.assertEqual(result[2], "Goodbye!")
        self.assertEqual(missing, 1)

    def test_renumbered_from_one(self):
        """Gemini sometimes renumbers from 1 instead of using the offset."""
        response = json.dumps(
            [
                {"id": 1, "original": "a", "translated": "Hello!"},
                {"id": 2, "original": "b", "translated": "Thank you!"},
                {"id": 3, "original": "c", "translated": "Goodbye!"},
            ]
        )
        result, missing = parse_structured_response(response, 3, 100)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])
        self.assertEqual(missing, 0)

    def test_preserves_ass_tags(self):
        response = json.dumps(
            [
                {"id": 1, "original": "test", "translated": "{\\i1}Hello{\\i0} world!"},
            ]
        )
        result, _ = parse_structured_response(response, 1, 0)
        self.assertEqual(result[0], "{\\i1}Hello{\\i0} world!")

    def test_invalid_json(self):
        result, missing = parse_structured_response("not json at all", 3, 0)
        self.assertEqual(result, ["", "", ""])
        self.assertEqual(missing, 3)

    def test_not_array(self):
        result, missing = parse_structured_response('{"key": "value"}', 1, 0)
        self.assertEqual(result, [""])
        self.assertEqual(missing, 1)

    def test_empty_array(self):
        result, missing = parse_structured_response("[]", 2, 0)
        self.assertEqual(result, ["", ""])
        self.assertEqual(missing, 2)

    def test_items_without_required_fields(self):
        response = json.dumps(
            [
                {"id": 1, "translated": "Hello!"},
                {"id": 2, "text": "raw"},
            ]
        )
        result, missing = parse_structured_response(response, 2, 0)
        self.assertEqual(result[0], "Hello!")
        self.assertEqual(result[1], "")
        self.assertEqual(missing, 1)

    def test_empty_translation_not_counted_as_missing(self):
        """Intentionally empty translations (absorbed fillers) should not be missing."""
        response = json.dumps(
            [
                {"id": 1, "original": "こんにちは", "translated": "Hello!"},
                {"id": 2, "original": "えっと", "translated": ""},
                {"id": 3, "original": "さようなら", "translated": "Goodbye!"},
            ]
        )
        result, missing = parse_structured_response(response, 3, 0)
        self.assertEqual(result, ["Hello!", "", "Goodbye!"])
        self.assertEqual(missing, 0)


class TestTranslateIntegration(unittest.TestCase):
    """Integration test with mocked Gemini client."""

    def setUp(self):
        self.tmpfile = tempfile.NamedTemporaryFile(
            mode="w", suffix=".ass", delete=False, encoding="utf-8"
        )
        self.tmpfile.write(SAMPLE_ASS)
        self.tmpfile.close()

    def tearDown(self):
        os.unlink(self.tmpfile.name)
        out = self.tmpfile.name.replace(".ass", "_en.ass")
        if os.path.exists(out):
            os.unlink(out)

    def test_ass_parsing_preserves_comments(self):
        from utils.ass_parser import parse_ass

        data = parse_ass(self.tmpfile.name)
        types = [e["type"] for e in data["events"]]
        self.assertIn("Comment", types)
        self.assertEqual(types.count("Dialogue"), 3)
        self.assertEqual(types.count("Comment"), 1)


class TestTranslateBatchRetry(unittest.TestCase):
    """Tests for translate_batch retry logic."""

    def _make_events(self, n=2):
        return [{"style": "Default", "text": f"テスト{i}"} for i in range(n)]

    def _make_response(self, events, start_idx=0):
        """Build a mock response with valid JSON text."""
        data = [
            {"id": start_idx + i + 1, "original": e["text"], "translated": f"Trans{i}"}
            for i, e in enumerate(events)
        ]
        mock = MagicMock()
        mock.text = json.dumps(data)
        return mock

    def _make_partial_response(self, events, start_idx=0, missing_indices=None):
        """Build a mock response with some lines missing."""
        missing_indices = missing_indices or set()
        data = [
            {"id": start_idx + i + 1, "original": e["text"], "translated": f"Trans{i}"}
            for i, e in enumerate(events)
            if i not in missing_indices
        ]
        mock = MagicMock()
        mock.text = json.dumps(data)
        return mock

    @patch("translate.time.sleep")
    def test_succeeds_on_first_try(self, mock_sleep):
        events = self._make_events()
        client = MagicMock()
        client.models.generate_content.return_value = self._make_response(events)

        result = translate_batch(client, "model", "prompt", events, 0)

        self.assertEqual(result, ["Trans0", "Trans1"])
        client.models.generate_content.assert_called_once()
        mock_sleep.assert_not_called()

    @patch("translate.time.sleep")
    def test_api_retry_on_connection_error(self, mock_sleep):
        events = self._make_events()
        client = MagicMock()
        client.models.generate_content.side_effect = [
            ConnectionError("disconnected"),
            ConnectionError("disconnected"),
            self._make_response(events),
        ]

        result = translate_batch(client, "model", "prompt", events, 0)

        self.assertEqual(result, ["Trans0", "Trans1"])
        self.assertEqual(client.models.generate_content.call_count, 3)
        # Exponential backoff: 2^1=2, 2^2=4
        mock_sleep.assert_any_call(2)
        mock_sleep.assert_any_call(4)

    @patch("translate.time.sleep")
    def test_api_retries_exhausted_raises(self, mock_sleep):
        events = self._make_events()
        client = MagicMock()
        client.models.generate_content.side_effect = ConnectionError("disconnected")

        with self.assertRaises(ConnectionError):
            translate_batch(client, "model", "prompt", events, 0)

        # 5 attempts total (MAX_API_RETRIES)
        self.assertEqual(client.models.generate_content.call_count, 5)

    @patch("translate.time.sleep")
    def test_content_retry_on_missing_lines(self, mock_sleep):
        events = self._make_events(3)
        client = MagicMock()
        # First call: missing line index 1. Second call: all lines present.
        client.models.generate_content.side_effect = [
            self._make_partial_response(events, missing_indices={1}),
            self._make_response(events),
        ]

        result = translate_batch(client, "model", "prompt", events, 0)

        self.assertEqual(result, ["Trans0", "Trans1", "Trans2"])
        self.assertEqual(client.models.generate_content.call_count, 2)

    @patch("translate.time.sleep")
    def test_content_retries_exhausted_returns_partial(self, mock_sleep):
        events = self._make_events(3)
        client = MagicMock()
        # All 3 content attempts return partial results
        partial = self._make_partial_response(events, missing_indices={1})
        client.models.generate_content.return_value = partial

        result = translate_batch(client, "model", "prompt", events, 0)

        # Returns partial result after MAX_CONTENT_RETRIES attempts
        self.assertEqual(result[0], "Trans0")
        self.assertEqual(result[1], "")  # missing
        self.assertEqual(result[2], "Trans2")
        self.assertEqual(client.models.generate_content.call_count, 3)

    @patch("translate.time.sleep")
    def test_api_error_then_content_retry(self, mock_sleep):
        """API error on first content attempt, then missing lines on second."""
        events = self._make_events(2)
        client = MagicMock()
        client.models.generate_content.side_effect = [
            ConnectionError("fail"),
            self._make_partial_response(events, missing_indices={0}),
            self._make_response(events),
        ]

        result = translate_batch(client, "model", "prompt", events, 0)

        self.assertEqual(result, ["Trans0", "Trans1"])
        self.assertEqual(client.models.generate_content.call_count, 3)

    @patch("translate.time.sleep")
    def test_empty_translation_does_not_trigger_retry(self, mock_sleep):
        """Intentionally empty translations (absorbed fillers) should not retry."""
        events = self._make_events(3)
        # All IDs present, but one has empty translated string
        data = [
            {"id": 1, "original": events[0]["text"], "translated": "Trans0"},
            {"id": 2, "original": events[1]["text"], "translated": ""},
            {"id": 3, "original": events[2]["text"], "translated": "Trans2"},
        ]
        mock_resp = MagicMock()
        mock_resp.text = json.dumps(data)
        client = MagicMock()
        client.models.generate_content.return_value = mock_resp

        result = translate_batch(client, "model", "prompt", events, 0)

        self.assertEqual(result, ["Trans0", "", "Trans2"])
        client.models.generate_content.assert_called_once()
        mock_sleep.assert_not_called()


class TestCheckpoint(unittest.TestCase):
    """Tests for checkpoint save/load/resume."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.checkpoint_path = Path(self.tmpdir) / "output_en.ass.partial.json"

    def tearDown(self):
        if self.checkpoint_path.exists():
            self.checkpoint_path.unlink()
        os.rmdir(self.tmpdir)

    def test_save_and_load(self):
        translations = ["Hello", "World", "Test"]
        save_checkpoint(self.checkpoint_path, translations, 2)

        loaded_translations, next_batch = load_checkpoint(self.checkpoint_path)

        self.assertEqual(loaded_translations, translations)
        self.assertEqual(next_batch, 2)

    def test_load_no_file(self):
        translations, next_batch = load_checkpoint(self.checkpoint_path)

        self.assertEqual(translations, [])
        self.assertEqual(next_batch, 0)

    def test_load_invalid_json(self):
        self.checkpoint_path.write_text("not json", encoding="utf-8")

        translations, next_batch = load_checkpoint(self.checkpoint_path)

        self.assertEqual(translations, [])
        self.assertEqual(next_batch, 0)

    def test_load_missing_keys(self):
        self.checkpoint_path.write_text('{"foo": "bar"}', encoding="utf-8")

        translations, next_batch = load_checkpoint(self.checkpoint_path)

        self.assertEqual(translations, [])
        self.assertEqual(next_batch, 0)

    def test_save_overwrites(self):
        save_checkpoint(self.checkpoint_path, ["a"], 1)
        save_checkpoint(self.checkpoint_path, ["a", "b", "c"], 3)

        loaded_translations, next_batch = load_checkpoint(self.checkpoint_path)

        self.assertEqual(loaded_translations, ["a", "b", "c"])
        self.assertEqual(next_batch, 3)

    def test_unicode_preservation(self):
        translations = ["こんにちは", "ありがとう"]
        save_checkpoint(self.checkpoint_path, translations, 1)

        loaded_translations, _ = load_checkpoint(self.checkpoint_path)

        self.assertEqual(loaded_translations, translations)


class TestMergeAbsorbedLines(unittest.TestCase):
    """Tests for merge_absorbed_lines post-processing."""

    def _d(self, start, end, text, style="Default"):
        return {
            "type": "Dialogue",
            "start": start,
            "end": end,
            "style": style,
            "text": text,
        }

    def _c(self, start, end, text):
        return {"type": "Comment", "start": start, "end": end, "text": text}

    def test_no_empty_lines(self):
        events = [
            self._d("0:00:01.00", "0:00:03.00", "Hello"),
            self._d("0:00:03.00", "0:00:05.00", "World"),
        ]
        result = merge_absorbed_lines(events)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["text"], "Hello")
        self.assertEqual(result[1]["text"], "World")

    def test_merge_into_previous(self):
        events = [
            self._d("0:00:01.00", "0:00:03.00", "Hello world"),
            self._d("0:00:03.00", "0:00:05.00", ""),
        ]
        result = merge_absorbed_lines(events)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["text"], "Hello world")
        self.assertEqual(result[0]["start"], "0:00:01.00")
        self.assertEqual(result[0]["end"], "0:00:05.00")

    def test_merge_consecutive_empty(self):
        events = [
            self._d("0:00:01.00", "0:00:03.00", "Combined text"),
            self._d("0:00:03.00", "0:00:05.00", ""),
            self._d("0:00:05.00", "0:00:07.00", ""),
        ]
        result = merge_absorbed_lines(events)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["text"], "Combined text")
        self.assertEqual(result[0]["end"], "0:00:07.00")

    def test_merge_first_line_into_next(self):
        events = [
            self._d("0:00:01.00", "0:00:03.00", ""),
            self._d("0:00:03.00", "0:00:05.00", "Hello world"),
        ]
        result = merge_absorbed_lines(events)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["text"], "Hello world")
        self.assertEqual(result[0]["start"], "0:00:01.00")
        self.assertEqual(result[0]["end"], "0:00:05.00")

    def test_empty_between_non_empty(self):
        events = [
            self._d("0:00:01.00", "0:00:03.00", "First"),
            self._d("0:00:03.00", "0:00:05.00", ""),
            self._d("0:00:05.00", "0:00:07.00", "Third"),
        ]
        result = merge_absorbed_lines(events)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["text"], "First")
        self.assertEqual(result[0]["end"], "0:00:05.00")
        self.assertEqual(result[1]["text"], "Third")

    def test_comments_preserved(self):
        events = [
            self._d("0:00:01.00", "0:00:03.00", "Hello"),
            self._c("0:00:03.00", "0:00:04.00", "This is a comment"),
            self._d("0:00:04.00", "0:00:06.00", ""),
            self._d("0:00:06.00", "0:00:08.00", "World"),
        ]
        result = merge_absorbed_lines(events)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["type"], "Dialogue")
        self.assertEqual(result[0]["end"], "0:00:06.00")
        self.assertEqual(result[1]["type"], "Comment")
        self.assertEqual(result[2]["type"], "Dialogue")
        self.assertEqual(result[2]["text"], "World")

    def test_multiple_scattered_empty(self):
        events = [
            self._d("0:00:01.00", "0:00:03.00", "A"),
            self._d("0:00:03.00", "0:00:05.00", ""),
            self._d("0:00:05.00", "0:00:07.00", "B"),
            self._d("0:00:07.00", "0:00:09.00", "C"),
            self._d("0:00:09.00", "0:00:11.00", ""),
        ]
        result = merge_absorbed_lines(events)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["text"], "A")
        self.assertEqual(result[0]["end"], "0:00:05.00")
        self.assertEqual(result[1]["text"], "B")
        self.assertEqual(result[2]["text"], "C")
        self.assertEqual(result[2]["end"], "0:00:11.00")

    def test_empty_list(self):
        result = merge_absorbed_lines([])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
