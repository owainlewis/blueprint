# Claude Code

@AGENTS.md

Blueprint keeps shared repository policy in `AGENTS.md` and only Claude-specific setup here.

Install Blueprint skills with `npx skills add owainlewis/blueprint`. Invoke the phase skills as `/design`, `/plan`, `/test`, `/review`, and `/improve`. Use `/milestone` to deliver every issue in a GitHub milestone through `/task-to-pr`.

The Skills CLI does not install commands. Install `/implement` and `/task-to-pr` separately for a project:

```bash
mkdir -p .claude/commands
curl -fsSL https://raw.githubusercontent.com/owainlewis/blueprint/main/commands/implement.md \
  -o .claude/commands/implement.md
curl -fsSL https://raw.githubusercontent.com/owainlewis/blueprint/main/commands/task-to-pr.md \
  -o .claude/commands/task-to-pr.md
```

Use `~/.claude/commands/` instead for user commands. `/implement` remains the canonical workflow; `/task-to-pr` is its named ticket-to-PR entry point. `AGENTS.md` contains portable repository policy.

The `/review` phase uses a fresh generic subagent. Blueprint does not require a separate reviewer agent definition.
