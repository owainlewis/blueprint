from __future__ import annotations

import os
from pathlib import Path
import subprocess
import tempfile
import unittest


CHECK_DIFF = Path(__file__).resolve().parents[1] / "check_diff"


class CheckDiffTests(unittest.TestCase):
    def git(self, repository: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *arguments],
            cwd=repository,
            text=True,
            capture_output=True,
            check=True,
        )

    def repository(self, directory: str) -> tuple[Path, str]:
        repository = Path(directory)
        self.git(repository, "init", "--quiet")
        self.git(repository, "config", "user.name", "Repository check")
        self.git(repository, "config", "user.email", "check@example.com")
        (repository / "example.txt").write_text("clean\n")
        self.git(repository, "add", "example.txt")
        self.git(repository, "commit", "--quiet", "-m", "initial")
        base = self.git(repository, "rev-parse", "HEAD").stdout.strip()
        return repository, base

    def run_check(self, repository: Path, base: str) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment["CHECK_DIFF_BASE"] = base
        return subprocess.run(
            [str(CHECK_DIFF)],
            cwd=repository,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_push_base_checks_the_pushed_commit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository, base = self.repository(directory)

            (repository / "example.txt").write_text("trailing whitespace \n")
            self.git(repository, "add", "example.txt")
            self.git(repository, "commit", "--quiet", "-m", "introduce whitespace")

            result = self.run_check(repository, base)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("trailing whitespace", result.stdout)

    def test_unstaged_changes_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository, base = self.repository(directory)
            (repository / "example.txt").write_text("trailing whitespace \n")

            result = self.run_check(repository, base)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("trailing whitespace", result.stdout)

    def test_staged_changes_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository, base = self.repository(directory)
            (repository / "example.txt").write_text("trailing whitespace \n")
            self.git(repository, "add", "example.txt")

            result = self.run_check(repository, base)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("trailing whitespace", result.stdout)


if __name__ == "__main__":
    unittest.main()
