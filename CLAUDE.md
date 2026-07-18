@AGENTS.md

## Claude Code adapter

Install Blueprint skills with `npx skills add owainlewis/blueprint`. The public skills are `design`, `plan`, `test`, `review`, and `improve`.

Copy `commands/implement.md` to `.claude/commands/implement.md` for a project command or `~/.claude/commands/implement.md` for a user command. That file is the canonical workflow; `AGENTS.md` contains portable repository policy.

The `review` phase uses a fresh generic subagent. Blueprint does not require a separate reviewer agent definition.
