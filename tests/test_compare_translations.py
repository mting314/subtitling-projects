"""Tests for compare_translations.py."""

import os
import tempfile
import unittest

from compare_translations import generate_comparison_html


class TestGenerateComparisonHtml(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.html_path = os.path.join(self.tmpdir, "comparison.html")

    def tearDown(self):
        if os.path.exists(self.html_path):
            os.unlink(self.html_path)
        os.rmdir(self.tmpdir)

    def test_basic_generation(self):
        source = [
            {"start": 5.0, "end": 8.0, "style": "Default", "text": "こんにちは"},
            {"start": 9.0, "end": 12.0, "style": "Default", "text": "ありがとう"},
        ]
        translated = [
            {"start": 5.0, "end": 8.0, "style": "Default", "text": "Hello!"},
            {"start": 9.0, "end": 12.0, "style": "Default", "text": "Thank you!"},
        ]
        generate_comparison_html(source, translated, self.html_path)
        self.assertTrue(os.path.exists(self.html_path))
        content = open(self.html_path, encoding="utf-8").read()
        self.assertIn("Translation Comparison", content)
        self.assertIn("Hello!", content)
        self.assertIn("こんにちは", content)

    def test_with_title(self):
        source = [{"start": 0, "end": 1, "style": "Default", "text": "テスト"}]
        translated = [{"start": 0, "end": 1, "style": "Default", "text": "Test"}]
        generate_comparison_html(source, translated, self.html_path, title="Episode 1")
        content = open(self.html_path, encoding="utf-8").read()
        self.assertIn("Episode 1", content)

    def test_stats_cards(self):
        source = [
            {"start": 0, "end": 1, "style": "Default", "text": "あ" * 10},
        ]
        translated = [
            {"start": 0, "end": 1, "style": "Default", "text": "a" * 20},
        ]
        generate_comparison_html(source, translated, self.html_path)
        content = open(self.html_path, encoding="utf-8").read()
        self.assertIn("10", content)  # JP chars
        self.assertIn("20", content)  # EN chars

    def test_short_translation_highlighted(self):
        source = [
            {
                "start": 0,
                "end": 1,
                "style": "Default",
                "text": "これは長いテキストです",
            },
        ]
        translated = [
            {"start": 0, "end": 1, "style": "Default", "text": "X"},
        ]
        generate_comparison_html(source, translated, self.html_path)
        content = open(self.html_path, encoding="utf-8").read()
        self.assertIn("severity-orange", content)

    def test_empty_lines(self):
        source = []
        translated = []
        generate_comparison_html(source, translated, self.html_path)
        self.assertTrue(os.path.exists(self.html_path))

    def test_without_video(self):
        source = [{"start": 0, "end": 1, "style": "Default", "text": "テスト"}]
        translated = [{"start": 0, "end": 1, "style": "Default", "text": "Test"}]
        generate_comparison_html(source, translated, self.html_path, video_path=None)
        content = open(self.html_path, encoding="utf-8").read()
        self.assertNotIn("player-section", content)

    def test_special_chars_escaped(self):
        source = [{"start": 0, "end": 1, "style": "Default", "text": "A < B & C > D"}]
        translated = [
            {"start": 0, "end": 1, "style": "Default", "text": "A < B & C > D"}
        ]
        generate_comparison_html(source, translated, self.html_path)
        content = open(self.html_path, encoding="utf-8").read()
        self.assertIn("&amp;", content)
        self.assertIn("&lt;", content)
        self.assertIn("&gt;", content)


if __name__ == "__main__":
    unittest.main()
