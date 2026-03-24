"""Tests for translate.py."""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from translate import (
    build_system_prompt,
    format_lines_for_prompt,
    parse_translation_response,
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
                prompt = build_system_prompt(f.name, "nonexistent.md", None)
                self.assertIn("Test Instructions", prompt)
                self.assertIn("Output Format", prompt)
            finally:
                os.unlink(f.name)

    def test_missing_instructions_still_works(self):
        prompt = build_system_prompt("nonexistent.md", "nonexistent.md", None)
        self.assertIn("Output Format", prompt)

    def test_with_project_ref(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as inst:
            inst.write("Instructions")
            inst.flush()
            with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as ref:
                ref.write("# Project Reference\nMailbox!")
                ref.flush()
                try:
                    prompt = build_system_prompt(inst.name, "nonexistent.md", ref.name)
                    self.assertIn("Project Reference", prompt)
                    self.assertIn("Mailbox!", prompt)
                finally:
                    os.unlink(inst.name)
                    os.unlink(ref.name)


class TestFormatLinesForPrompt(unittest.TestCase):
    def test_basic_formatting(self):
        events = [
            {"style": "Default", "text": "こんにちは"},
            {"style": "Speaker1", "text": "ありがとう"},
        ]
        result = format_lines_for_prompt(events, 0)
        self.assertEqual(result, "1|[Default] こんにちは\n2|[Speaker1] ありがとう")

    def test_offset_numbering(self):
        events = [{"style": "Default", "text": "テスト"}]
        result = format_lines_for_prompt(events, 10)
        self.assertTrue(result.startswith("11|"))

    def test_empty_style(self):
        events = [{"style": "", "text": "テスト"}]
        result = format_lines_for_prompt(events, 0)
        self.assertEqual(result, "1|テスト")


class TestParseTranslationResponse(unittest.TestCase):
    def test_basic_parsing(self):
        response = "1|Hello!\n2|Thank you!\n3|Goodbye!"
        result = parse_translation_response(response, 3, 0)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])

    def test_with_offset(self):
        response = "11|Hello!\n12|Thank you!"
        result = parse_translation_response(response, 2, 10)
        self.assertEqual(result, ["Hello!", "Thank you!"])

    def test_missing_line(self):
        response = "1|Hello!\n3|Goodbye!"
        result = parse_translation_response(response, 3, 0)
        self.assertEqual(result[0], "Hello!")
        self.assertEqual(result[1], "")  # missing line 2
        self.assertEqual(result[2], "Goodbye!")

    def test_blank_lines_in_response(self):
        response = "\n1|Hello!\n\n2|Thank you!\n"
        result = parse_translation_response(response, 2, 0)
        self.assertEqual(result, ["Hello!", "Thank you!"])

    def test_preserves_ass_tags(self):
        response = "1|{\\i1}Hello{\\i0} world!"
        result = parse_translation_response(response, 1, 0)
        self.assertEqual(result[0], "{\\i1}Hello{\\i0} world!")

    def test_text_with_pipe(self):
        response = "1|Hello | world"
        result = parse_translation_response(response, 1, 0)
        self.assertEqual(result[0], "Hello | world")

    def test_numbered_list_format(self):
        response = "1. Hello!\n2. Thank you!\n3. Goodbye!"
        result = parse_translation_response(response, 3, 0)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])

    def test_colon_format(self):
        response = "1: Hello!\n2: Thank you!"
        result = parse_translation_response(response, 2, 0)
        self.assertEqual(result, ["Hello!", "Thank you!"])

    def test_code_fence_stripped(self):
        response = "```\n1|Hello!\n2|Thank you!\n```"
        result = parse_translation_response(response, 2, 0)
        self.assertEqual(result, ["Hello!", "Thank you!"])

    def test_style_tag_echo_stripped(self):
        response = "1|[Default] Hello!\n2|[Speaker1] Thank you!"
        result = parse_translation_response(response, 2, 0)
        self.assertEqual(result, ["Hello!", "Thank you!"])

    def test_renumbered_from_one(self):
        """Gemini sometimes renumbers from 1 instead of using the offset."""
        response = "1|Hello!\n2|Thank you!\n3|Goodbye!"
        result = parse_translation_response(response, 3, 100)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])


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
