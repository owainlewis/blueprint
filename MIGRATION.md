# Migrate to the phase model

> **Breaking change:** Blueprint now ships five phase skills and one separate `/implement` workflow. Old skill directories must be removed manually.

## What changed

| Before | Now |
| --- | --- |
| `design-doc`, `spec` | `design` |
| `browser-verify` | Browser proof inside `test` |
| `refactor` | `improve` |
| `branch`, `commit`, `implement`, `pr`, `pr-to-ready`, `task-to-pr` | `/implement` workflow |
| `debug`, `tdd` | Techniques used while implementing |
| `goal-design`, `milestone`, `multitask` | Ordinary instructions or project-specific workflows |
| `code-reviewer` agent definition | A fresh generic subagent launched by `review` |

The public skill surface is now:

```text
design · plan · test · review · improve
```

## Clean upgrade

1. **Find the skill directory used by your coding tool.** Remove only the old Blueprint skill folders listed above. Do not delete the whole directory; it may contain unrelated skills.
2. **Reinstall the phase skills.**

   ```bash
   npx skills add owainlewis/blueprint
   ```

3. **Install `/implement` separately.** The Skills CLI does not install commands. For Claude Code at project scope:

   ```bash
   mkdir -p .claude/commands
   curl -fsSL https://raw.githubusercontent.com/owainlewis/blueprint/main/commands/implement.md \
     -o .claude/commands/implement.md
   ```

   For another tool, change the output path to its custom-command directory. Without custom commands, use the [raw workflow](https://raw.githubusercontent.com/owainlewis/blueprint/main/commands/implement.md) as an ordinary prompt.

4. **Remove copied reviewer agents.** Delete any old Blueprint `code-reviewer` definition. The `review` skill now launches a fresh generic subagent.
5. **Check the result.** Skill discovery should list exactly `design`, `plan`, `test`, `review`, and `improve` for Blueprint.

## Why cleanup is manual

Some noninteractive skill updaters add and replace skills but do not remove directories that disappeared upstream. Running `npx skills update` alone can therefore leave the old and new models installed together.

Blueprint intentionally provides no compatibility aliases. Duplicate entry points make routing ambiguous and defeat the smaller phase model.
