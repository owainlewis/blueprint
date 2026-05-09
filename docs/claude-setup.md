# Claude Code Setup

Claude Code supports skills as directories containing `SKILL.md`. Project skills live at `.claude/skills/<skill-name>/SKILL.md`; plugin skills live at `skills/<skill-name>/SKILL.md` in the plugin root.

Blueprint is already shaped as a Claude Code plugin:

- `.claude-plugin/plugin.json`: plugin metadata.
- `skills/`: Blueprint workflows.
- `commands/`: thin branch and commit commands.

Install the plugin through Claude Code's plugin flow, or copy individual skills into a project or personal skills directory.

Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so this repo's `CLAUDE.md` imports `@AGENTS.md` and adds Claude-specific notes. Keep shared rules in `AGENTS.md`.

References:

- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/plugins
- https://docs.claude.com/en/docs/claude-code/memory
