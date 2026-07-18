@AGENTS.md

## Claude Code

Blueprint installs as standalone skills via `npx skills add owainlewis/blueprint`. The active workflows live in `skills/<name>/SKILL.md`.

- Invoke core workflows by name: `design-doc`, `spec`, `plan`, `implement`, `tdd`, `debug`, `refactor`, `review`, `multitask`, `pr`, `pr-to-ready`, `browser-verify`.
- Helper entry points remain available for mechanical delivery steps: `branch`, `commit`.
- Agent definitions live in `agents/`. Copy them to `.claude/agents/` (project) or `~/.claude/agents/` (user) to make them spawnable; `npx skills add` installs skills only.
- `browser-verify` requires an available real-browser automation and inspection path, such as Chrome DevTools MCP.
- Keep shared repo guidance in `AGENTS.md`; keep Claude-specific adapter notes here.
