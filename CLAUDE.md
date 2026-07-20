# Claude Code

@AGENTS.md

Blueprint keeps shared repository policy in `AGENTS.md` and only Claude-specific setup here.

Install Blueprint with `npx skills add owainlewis/blueprint`. Invoke the phase skills as `/design`, `/plan`, `/test`, `/review`, and `/improve`. Use `/task-to-pr` for one end-to-end code change and `/milestone` for every issue in a GitHub milestone.

All Blueprint entry points are skills. `/task-to-pr` is the canonical delivery workflow, and `/milestone` runs it one issue at a time. `AGENTS.md` contains portable repository policy.

The `/review` phase uses a fresh generic subagent. Blueprint does not require a separate reviewer agent definition.
