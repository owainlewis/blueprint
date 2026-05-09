@AGENTS.md

## Claude Code

Blueprint is distributed as a Claude Code plugin. The active workflows live in `skills/<name>/SKILL.md`; thin mechanical commands live in `commands/`.

- Invoke plugin skills as `/blueprint:spec`, `/blueprint:plan`, `/blueprint:implement`, `/blueprint:tdd`, `/blueprint:review`, or `/blueprint:compress`.
- Use `/blueprint:branch` and `/blueprint:commit` for the thin git commands when available.
- Keep shared repo guidance in `AGENTS.md`; keep Claude-specific adapter notes here.
