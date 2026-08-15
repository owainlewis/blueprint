from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "node_modules"}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def repository_files(suffix: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(f"*{suffix}")
        if not IGNORED_PARTS.intersection(path.parts)
    )


def check_skills(errors: list[str]) -> None:
    for skill_dir in sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir()):
        skill = skill_dir / "SKILL.md"
        if not skill.is_file():
            errors.append(f"Missing skill file: {skill.relative_to(ROOT)}")
            continue
        text = skill.read_text()
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not frontmatter:
            errors.append(f"Missing YAML frontmatter: {skill.relative_to(ROOT)}")
            continue
        name = re.search(r'^name:\s*["\']?([^"\'\n]+)', frontmatter.group(1), re.MULTILINE)
        description = re.search(r"^description:\s*.+", frontmatter.group(1), re.MULTILINE)
        if not name or name.group(1).strip() != skill_dir.name:
            errors.append(f"Skill name does not match directory: {skill.relative_to(ROOT)}")
        if not description:
            errors.append(f"Missing skill description: {skill.relative_to(ROOT)}")


def check_markdown(errors: list[str]) -> None:
    for path in repository_files(".md"):
        text = path.read_text()
        if sum(1 for line in text.splitlines() if line.startswith("```")) % 2:
            errors.append(f"Unbalanced fenced code block: {path.relative_to(ROOT)}")

        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not file_target:
                continue
            resolved = (
                ROOT / file_target.lstrip("/")
                if file_target.startswith("/")
                else path.parent / file_target
            ).resolve()
            if not resolved.exists():
                errors.append(
                    f"Missing local link in {path.relative_to(ROOT)}: {raw_target}"
                )


def main() -> int:
    errors: list[str] = []
    check_skills(errors)
    check_markdown(errors)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Repository structure and Markdown links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
