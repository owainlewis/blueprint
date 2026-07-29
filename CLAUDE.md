# Claude Code

@AGENTS.md

Blueprint keeps shared repository policy in `AGENTS.md` and only Claude-specific setup here.

Install Blueprint with `npx skills add owainlewis/blueprint`. Use `/architecture`, `/design`, `/plan`, `/test`, `/review`, and `/improve` for one kind of engineering work. Use `/task-to-pr` to deliver one code change and `/milestone` to deliver every issue in a GitHub milestone.

Everything you call in Blueprint is a skill. Use `/task-to-pr` to take one task from its source to a ready pull request. `/milestone` runs that workflow one issue at a time. `AGENTS.md` contains the repository rules.

The `/review` phase uses a fresh generic subagent. Blueprint does not require a separate reviewer agent definition.
