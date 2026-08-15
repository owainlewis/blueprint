from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "node_modules"}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_PATTERN = re.compile(
    r"^ {0,3}\[(?!\^)([^\]]+)\]:[ \t]*(?:<([^>]+)>|(\S+))",
    re.MULTILINE,
)
FENCE_PATTERN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def repository_files(suffix: str, root: Path = ROOT) -> list[Path]:
    return sorted(
        path
        for path in root.rglob(f"*{suffix}")
        if not IGNORED_PARTS.intersection(path.parts)
    )


def check_skills(errors: list[str], root: Path = ROOT) -> None:
    for skill_dir in sorted(path for path in (root / "skills").iterdir() if path.is_dir()):
        skill = skill_dir / "SKILL.md"
        if not skill.is_file():
            errors.append(f"Missing skill file: {skill.relative_to(root)}")
            continue
        text = skill.read_text()
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not frontmatter:
            errors.append(f"Missing YAML frontmatter: {skill.relative_to(root)}")
            continue
        try:
            metadata = yaml.safe_load(frontmatter.group(1))
        except yaml.YAMLError as error:
            errors.append(f"Invalid YAML frontmatter in {skill.relative_to(root)}: {error}")
            continue
        if not isinstance(metadata, dict):
            errors.append(f"YAML frontmatter must be a mapping: {skill.relative_to(root)}")
            continue
        name = metadata.get("name")
        description = metadata.get("description")
        if not isinstance(name, str) or name.strip() != skill_dir.name:
            errors.append(f"Skill name does not match directory: {skill.relative_to(root)}")
        if not isinstance(description, str) or not description.strip():
            errors.append(f"Missing skill description: {skill.relative_to(root)}")


def has_unbalanced_fence(text: str) -> bool:
    fence: tuple[str, int] | None = None
    for line in text.splitlines():
        match = FENCE_PATTERN.match(line)
        if not match:
            continue
        marker = match.group(1)
        if fence is None:
            fence = (marker[0], len(marker))
            continue
        character, minimum = fence
        if marker[0] == character and len(marker) >= minimum and not match.group(2).strip():
            fence = None
    return fence is not None


def local_targets(text: str) -> list[str]:
    targets = LINK_PATTERN.findall(text)
    targets.extend(match.group(2) or match.group(3) for match in REFERENCE_PATTERN.finditer(text))
    return targets


def check_markdown(errors: list[str], root: Path = ROOT) -> None:
    for path in repository_files(".md", root):
        text = path.read_text()
        if has_unbalanced_fence(text):
            errors.append(f"Unbalanced fenced code block: {path.relative_to(root)}")

        for raw_target in local_targets(text):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not file_target:
                continue
            resolved = (
                root / file_target.lstrip("/")
                if file_target.startswith("/")
                else path.parent / file_target
            ).resolve()
            if not resolved.exists():
                errors.append(
                    f"Missing local link in {path.relative_to(root)}: {raw_target}"
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
