# Claude Code

@AGENTS.md

Blueprint keeps shared repository policy in `AGENTS.md` and only Claude-specific setup here.

Install Blueprint with `npx skills add owainlewis/blueprint`. Use `/architecture`, `/design`, `/architecture-review`, `/plan`, `/test`, `/review`, and `/improve` for one kind of engineering work. Use `/task-to-pr` to deliver one or more code changes.

Everything you call in Blueprint is a skill. `/task-to-pr` accepts tasks, tickets, pull requests, or a milestone and creates one pull request for each task. `AGENTS.md` contains the repository rules.

The `/architecture-review` and `/review` phases use a fresh generic subagent. Blueprint does not require a separate reviewer agent definition.
