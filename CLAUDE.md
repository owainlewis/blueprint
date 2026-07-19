# Claude Code

@AGENTS.md

Blueprint keeps shared repository policy in `AGENTS.md` and only Claude-specific setup here.

Install Blueprint skills with `npx skills add owainlewis/blueprint`. Invoke the public skills as `/design`, `/plan`, `/test`, `/review`, and `/improve`.

The Skills CLI does not install commands. Install `/implement` separately for a project:

```bash
mkdir -p .claude/commands
curl -fsSL https://raw.githubusercontent.com/owainlewis/blueprint/main/commands/implement.md \
  -o .claude/commands/implement.md
```

Use `~/.claude/commands/implement.md` instead for a user command. The downloaded file is the canonical workflow; `AGENTS.md` contains portable repository policy.

The `/review` phase uses a fresh generic subagent. Blueprint does not require a separate reviewer agent definition.
