# Getting Started

Blueprint is a set of plain Markdown agent skills. Install it once, then invoke the workflow from your agent by name or slash command.

## Install

```bash
npx skills add owainlewis/blueprint
```

Update later with:

```bash
npx skills update
```

## The Workflow

Use the full flow for non-trivial work:

```text
spec -> plan -> implement -> review
```

Use `tdd` instead of `implement` when you want test-first discipline. Use `compress` to tighten specs, plans, tickets, prompts, `AGENTS.md`, or skill files.

## Tool Setup

- Claude Code: [claude-setup.md](claude-setup.md)
- Cursor: [cursor-setup.md](cursor-setup.md)
- Windsurf: [windsurf-setup.md](windsurf-setup.md)
- GitHub Copilot: [copilot-setup.md](copilot-setup.md)
- Codex and other agents: [codex-setup.md](codex-setup.md)

Most tools need two things:

- A place to discover `skills/<name>/SKILL.md`.
- A repo instruction file such as `AGENTS.md`, `CLAUDE.md`, or `.github/copilot-instructions.md`.
