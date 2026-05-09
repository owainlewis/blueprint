# Codex Setup

Codex and many other coding agents use `AGENTS.md` as repo-local instructions. Keep `AGENTS.md` at the repo root so agents can orient themselves before editing.

For Blueprint:

1. Install or copy the `skills/` directory where your agent or skill manager can discover it.
2. Keep shared repo guidance in `AGENTS.md`.
3. Invoke skills by name in natural language if the tool does not expose slash commands:

```text
Use Blueprint spec for this feature.
Use Blueprint implement for LIN-123.
Review the current diff with Blueprint review.
```

The skills are plain Markdown. If a tool has no native skill loader, paste or reference the relevant `skills/<name>/SKILL.md` file when invoking the workflow.

References:

- https://github.com/agentsmd/agents.md
- https://github.com/openai/codex/blob/main/docs/agents_md.md
