@AGENTS.md

## Claude Code adapter

Install Blueprint skills with `npx skills add owainlewis/blueprint`. The public skills are `design`, `plan`, `test`, `review`, and `improve`.

Copy `commands/implement.md` to `.claude/commands/implement.md` for a project command or `~/.claude/commands/implement.md` for a user command. The shared workflow remains in `AGENTS.md` for portability.

The `review` phase uses a fresh generic subagent. Blueprint does not require a separate reviewer agent definition.
