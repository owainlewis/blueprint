from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_repo  # noqa: E402


class MarkdownChecksTests(unittest.TestCase):
    def check(self, markdown: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(markdown)
            errors: list[str] = []
            check_repo.check_markdown(errors, root)
            return errors

    def test_missing_reference_style_link_is_reported(self) -> None:
        errors = self.check("Read the [guide][details].\n\n[details]: missing.md\n")
        self.assertTrue(any("missing.md" in error for error in errors))

    def test_indented_backtick_fence_must_close(self) -> None:
        errors = self.check("   ```python\nprint('hello')\n")
        self.assertTrue(any("Unbalanced fenced code block" in error for error in errors))

    def test_tilde_fence_must_close(self) -> None:
        errors = self.check("~~~text\nhello\n")
        self.assertTrue(any("Unbalanced fenced code block" in error for error in errors))

    def test_matching_longer_fence_closes(self) -> None:
        errors = self.check("~~~text\nhello\n~~~~\n")
        self.assertEqual(errors, [])


class SkillChecksTests(unittest.TestCase):
    def test_malformed_yaml_frontmatter_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill_dir = root / "skills" / "example"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                '---\nname: example\ndescription: "unterminated\n---\n\n# Example\n'
            )
            errors: list[str] = []

            check_repo.check_skills(errors, root)

            self.assertTrue(any("Invalid YAML frontmatter" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
