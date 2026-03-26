"""Tests for translate.py."""

import json
import os
import tempfile
import unittest
from pathlib import Path

from translate import (
    build_system_prompt,
    format_batch_input,
    format_yaml_reference,
    load_speaker_files,
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
        result = parse_structured_response(response, 3, 0)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])

    def test_with_offset(self):
        response = json.dumps(
            [
                {"id": 11, "original": "こんにちは", "translated": "Hello!"},
                {"id": 12, "original": "ありがとう", "translated": "Thank you!"},
            ]
        )
        result = parse_structured_response(response, 2, 10)
        self.assertEqual(result, ["Hello!", "Thank you!"])

    def test_missing_line(self):
        response = json.dumps(
            [
                {"id": 1, "original": "こんにちは", "translated": "Hello!"},
                {"id": 3, "original": "さようなら", "translated": "Goodbye!"},
            ]
        )
        result = parse_structured_response(response, 3, 0)
        self.assertEqual(result[0], "Hello!")
        self.assertEqual(result[1], "")
        self.assertEqual(result[2], "Goodbye!")

    def test_renumbered_from_one(self):
        """Gemini sometimes renumbers from 1 instead of using the offset."""
        response = json.dumps(
            [
                {"id": 1, "original": "a", "translated": "Hello!"},
                {"id": 2, "original": "b", "translated": "Thank you!"},
                {"id": 3, "original": "c", "translated": "Goodbye!"},
            ]
        )
        result = parse_structured_response(response, 3, 100)
        self.assertEqual(result, ["Hello!", "Thank you!", "Goodbye!"])

    def test_preserves_ass_tags(self):
        response = json.dumps(
            [
                {"id": 1, "original": "test", "translated": "{\\i1}Hello{\\i0} world!"},
            ]
        )
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
        response = json.dumps(
            [
                {"id": 1, "translated": "Hello!"},
                {"id": 2, "text": "raw"},
            ]
        )
        result = parse_structured_response(response, 2, 0)
        self.assertEqual(result[0], "Hello!")
        self.assertEqual(result[1], "")


class TestFormatYamlReference(unittest.TestCase):
    def test_glossary_section(self):
        data = {
            "glossary": [
                {"term": "プロセカ", "translation": "ProSeka", "notes": "Capital S"},
                {"term": "セカイ", "translation": "SEKAI"},
            ]
        }
        result = format_yaml_reference(data, [])
        self.assertIn("## Glossary", result)
        self.assertIn("プロセカ → ProSeka (Capital S)", result)
        self.assertIn("セカイ → SEKAI", result)

    def test_segments_section(self):
        data = {
            "segments": [
                {"term": "メールボックス", "translation": "Mailbox"},
            ]
        }
        result = format_yaml_reference(data, [])
        self.assertIn("## Segment Names", result)
        self.assertIn("メールボックス → Mailbox", result)

    def test_replacements_section(self):
        data = {
            "replacements": [
                {
                    "original": "皆さんこんばんは",
                    "translation": "Good evening, everyone!",
                    "context": "Standard greeting",
                },
            ]
        }
        result = format_yaml_reference(data, [])
        self.assertIn("## Fixed Translations", result)
        self.assertIn("皆さんこんばんは → Good evening, everyone!", result)
        self.assertIn("[Standard greeting]", result)

    def test_replacement_without_context(self):
        data = {
            "replacements": [
                {"original": "バイバーイ", "translation": "Bye bye!"},
            ]
        }
        result = format_yaml_reference(data, [])
        self.assertIn("バイバーイ → Bye bye!", result)
        self.assertNotIn("[", result.split("Bye bye!")[1].split("\n")[0])

    def test_speakers_from_files(self):
        speakers = [
            {
                "name": "Ruriko Noguchi",
                "name_jp": "野口瑠璃子",
                "roles": [
                    {
                        "character": "Ichika Hoshino",
                        "unit": "Leo/need",
                        "style": "Kind and caring",
                        "greeting": "Kon-needo",
                    }
                ],
            }
        ]
        result = format_yaml_reference({}, speakers)
        self.assertIn("## Speaker Profiles", result)
        self.assertIn("Ruriko Noguchi (野口瑠璃子)", result)
        self.assertIn("Ichika Hoshino", result)
        self.assertIn("Leo/need", result)
        self.assertIn("Kind and caring", result)
        self.assertIn("Kon-needo", result)

    def test_speaker_with_nickname(self):
        speakers = [
            {
                "name": "Sayuri Date",
                "nickname": "Sayu / Sayurin",
                "roles": [{"character": "Kanon Shibuya", "style": "Warm"}],
            }
        ]
        result = format_yaml_reference({}, speakers)
        self.assertIn("Sayuri Date — Sayu / Sayurin", result)

    def test_inline_speakers_merged_with_files(self):
        data = {
            "speakers": [{"name": "Inline Speaker", "roles": [{"character": "Char A"}]}]
        }
        file_speakers = [{"name": "File Speaker", "roles": [{"character": "Char B"}]}]
        result = format_yaml_reference(data, file_speakers)
        self.assertIn("Inline Speaker", result)
        self.assertIn("File Speaker", result)

    def test_project_section(self):
        data = {
            "project": {
                "name": "Test Project",
                "description": "A test project",
                "franchise": "Test Franchise",
            }
        }
        result = format_yaml_reference(data, [])
        self.assertIn("## Project: Test Project", result)
        self.assertIn("A test project", result)
        self.assertIn("Franchise: Test Franchise", result)

    def test_notes_section(self):
        data = {"notes": "Key relationships:\n- A and B are siblings"}
        result = format_yaml_reference(data, [])
        self.assertIn("## Additional Notes", result)
        self.assertIn("Key relationships:", result)

    def test_hosts_section(self):
        data = {
            "hosts": [
                {
                    "aftertalk": "Find the dream view",
                    "host": "Shiho",
                    "unit": "Leo/need",
                }
            ]
        }
        result = format_yaml_reference(data, [])
        self.assertIn("## Hosts", result)
        self.assertIn("Find the dream view", result)

    def test_empty_data(self):
        result = format_yaml_reference({}, [])
        self.assertEqual(result, "")

    def test_empty_glossary_omitted(self):
        data = {"glossary": [], "segments": []}
        result = format_yaml_reference(data, [])
        self.assertNotIn("## Glossary", result)
        self.assertNotIn("## Segment Names", result)


class TestLoadSpeakerFiles(unittest.TestCase):
    def test_loads_yaml_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            speakers_dir = os.path.join(tmpdir, "speakers")
            os.makedirs(speakers_dir)
            with open(os.path.join(speakers_dir, "alice.yaml"), "w") as f:
                f.write("name: Alice\nroles:\n  - character: Char A\n")
            with open(os.path.join(speakers_dir, "bob.yaml"), "w") as f:
                f.write("name: Bob\nroles:\n  - character: Char B\n")
            ref_path = os.path.join(tmpdir, "ref.yaml")
            open(ref_path, "w").close()

            speakers = load_speaker_files(Path(ref_path))
            self.assertEqual(len(speakers), 2)
            names = {s["name"] for s in speakers}
            self.assertEqual(names, {"Alice", "Bob"})

    def test_no_speakers_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            ref_path = os.path.join(tmpdir, "ref.yaml")
            open(ref_path, "w").close()
            speakers = load_speaker_files(Path(ref_path))
            self.assertEqual(speakers, [])

    def test_empty_speakers_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            speakers_dir = os.path.join(tmpdir, "speakers")
            os.makedirs(speakers_dir)
            ref_path = os.path.join(tmpdir, "ref.yaml")
            open(ref_path, "w").close()
            speakers = load_speaker_files(Path(ref_path))
            self.assertEqual(speakers, [])

    def test_ignores_non_yaml_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            speakers_dir = os.path.join(tmpdir, "speakers")
            os.makedirs(speakers_dir)
            with open(os.path.join(speakers_dir, "alice.yaml"), "w") as f:
                f.write("name: Alice\n")
            with open(os.path.join(speakers_dir, "notes.txt"), "w") as f:
                f.write("not a speaker")
            ref_path = os.path.join(tmpdir, "ref.yaml")
            open(ref_path, "w").close()
            speakers = load_speaker_files(Path(ref_path))
            self.assertEqual(len(speakers), 1)


class TestBuildSystemPromptYaml(unittest.TestCase):
    def test_yaml_reference_parsed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            inst = os.path.join(tmpdir, "inst.md")
            with open(inst, "w") as f:
                f.write("Instructions here")

            ref = os.path.join(tmpdir, "ref.yaml")
            with open(ref, "w") as f:
                f.write("glossary:\n  - term: テスト\n    translation: Test\n")

            prompt = build_system_prompt(inst, ref)
            self.assertIn("## Glossary", prompt)
            self.assertIn("テスト → Test", prompt)

    def test_yaml_with_speakers_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            inst = os.path.join(tmpdir, "inst.md")
            with open(inst, "w") as f:
                f.write("Instructions")

            ref = os.path.join(tmpdir, "ref.yaml")
            with open(ref, "w") as f:
                f.write("project:\n  name: Test\n")

            speakers_dir = os.path.join(tmpdir, "speakers")
            os.makedirs(speakers_dir)
            with open(os.path.join(speakers_dir, "va.yaml"), "w") as f:
                f.write(
                    "name: Test VA\n"
                    "roles:\n"
                    "  - character: Test Char\n"
                    "    style: Cheerful\n"
                )

            prompt = build_system_prompt(inst, ref)
            self.assertIn("Test VA", prompt)
            self.assertIn("Test Char", prompt)
            self.assertIn("Cheerful", prompt)

    def test_md_reference_backward_compatible(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            inst = os.path.join(tmpdir, "inst.md")
            with open(inst, "w") as f:
                f.write("Instructions")

            ref = os.path.join(tmpdir, "ref.md")
            with open(ref, "w") as f:
                f.write("# Legacy Reference\nMailbox!")

            prompt = build_system_prompt(inst, ref)
            self.assertIn("Legacy Reference", prompt)
            self.assertIn("Mailbox!", prompt)

    def test_missing_yaml_reference(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            inst = os.path.join(tmpdir, "inst.md")
            with open(inst, "w") as f:
                f.write("Instructions")

            prompt = build_system_prompt(inst, os.path.join(tmpdir, "missing.yaml"))
            self.assertIn("Instructions", prompt)
            self.assertNotIn("Glossary", prompt)


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
