"""Tests for translate.py."""

import json
import os
import tempfile
import unittest

from translate import (
    build_system_prompt,
    format_batch_input,
    parse_structured_response,
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
            with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as ref:
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
        response = json.dumps([
            {"id": 1, "original": "こんにちは", "translated": "Hello!"},
            {"id": 2, "original": "ありがとう", "translated": "Thank you!"},
            {"id": 3, "original": "さようなら", "translated": "Goodbye!"},
        ])
        result = parse_structured_response(response, 3, 0)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])

    def test_with_offset(self):
        response = json.dumps([
            {"id": 11, "original": "こんにちは", "translated": "Hello!"},
            {"id": 12, "original": "ありがとう", "translated": "Thank you!"},
        ])
        result = parse_structured_response(response, 2, 10)
        self.assertEqual(result, ["Hello!", "Thank you!"])

    def test_missing_line(self):
        response = json.dumps([
            {"id": 1, "original": "こんにちは", "translated": "Hello!"},
            {"id": 3, "original": "さようなら", "translated": "Goodbye!"},
        ])
        result = parse_structured_response(response, 3, 0)
        self.assertEqual(result[0], "Hello!")
        self.assertEqual(result[1], "")
        self.assertEqual(result[2], "Goodbye!")

    def test_renumbered_from_one(self):
        """Gemini sometimes renumbers from 1 instead of using the offset."""
        response = json.dumps([
            {"id": 1, "original": "a", "translated": "Hello!"},
            {"id": 2, "original": "b", "translated": "Thank you!"},
            {"id": 3, "original": "c", "translated": "Goodbye!"},
        ])
        result = parse_structured_response(response, 3, 100)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])

    def test_preserves_ass_tags(self):
        response = json.dumps([
            {"id": 1, "original": "test", "translated": "{\\i1}Hello{\\i0} world!"},
        ])
        result = parse_structured_response(response, 1, 0)
        self.assertEqual(result[0], "{\\i1}Hello{\\i0} world!")

    def test_invalid_json(self):
        result = parse_structured_response("not json at all", 3, 0)
        self.assertEqual(result, ["", "", ""])

    def test_not_array(self):
        result = parse_structured_response('{"key": "value"}', 1, 0)
        self.assertEqual(result, [""])

    def test_empty_array(self):
        result = parse_structured_response("[]", 2, 0)
        self.assertEqual(result, ["", ""])

    def test_items_without_required_fields(self):
        response = json.dumps([
            {"id": 1, "translated": "Hello!"},
            {"id": 2, "text": "raw"},
        ])
        result = parse_structured_response(response, 2, 0)
        self.assertEqual(result[0], "Hello!")
        self.assertEqual(result[1], "")


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


if __name__ == "__main__":
    unittest.main()
