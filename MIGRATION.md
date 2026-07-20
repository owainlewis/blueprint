# Migrate to the phase model

> **Breaking change:** Blueprint now ships five phase skills, the `/milestone` coordination skill, and separate `/implement` and `/task-to-pr` workflow commands. Old skill directories must be removed manually.

## What changed

| Before | Now |
| --- | --- |
| `design-doc`, `spec` | `/design` |
| `browser-verify` | Browser proof inside `/test` |
| `refactor` | `/improve` |
| `branch`, `commit`, `implement`, `pr`, `pr-to-ready` | `/implement` workflow |
| `task-to-pr` | `/task-to-pr` workflow command, backed by `/implement` |
| `debug`, `tdd` | Techniques used while implementing |
| `goal-design`, `multitask` | Ordinary instructions or project-specific workflows |
| `milestone` | `/milestone`, updated to use `/task-to-pr` |
| `code-reviewer` agent definition | A fresh generic subagent launched by `/review` |

The public skill surface is now:

```text
/design · /plan · /test · /review · /improve · /milestone
```

## Clean upgrade

1. **Find the skill directory used by your coding tool.** Remove only the old Blueprint skill folders listed above. Do not delete the whole directory; it may contain unrelated skills.
2. **Reinstall the phase skills.**

   ```bash
   npx skills add owainlewis/blueprint
   ```

3. **Install `/implement` and `/task-to-pr` separately.** The Skills CLI does not install commands. For Claude Code at project scope:

   ```bash
   mkdir -p .claude/commands
   curl -fsSL https://raw.githubusercontent.com/owainlewis/blueprint/main/commands/implement.md \
     -o .claude/commands/implement.md
   curl -fsSL https://raw.githubusercontent.com/owainlewis/blueprint/main/commands/task-to-pr.md \
     -o .claude/commands/task-to-pr.md
   ```

   For another tool, change the output path to its custom-command directory. Without custom commands, use the [raw workflow](https://raw.githubusercontent.com/owainlewis/blueprint/main/commands/implement.md) as an ordinary prompt.

4. **Remove copied reviewer agents.** Delete any old Blueprint `code-reviewer` definition. The `/review` skill now launches a fresh generic subagent.
5. **Check the result.** The `/design`, `/plan`, `/test`, `/review`, `/improve`, and `/milestone` skills should be available.

## Why cleanup is manual

Some noninteractive skill updaters add and replace skills but do not remove directories that disappeared upstream. Running `npx skills update` alone can therefore leave the old and new models installed together.

Blueprint keeps `/task-to-pr` as the one compatibility workflow entry point because it names a common outcome and delegates to `/implement`. Other duplicate entry points remain removed so routing stays clear.
