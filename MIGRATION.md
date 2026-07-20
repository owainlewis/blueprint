# Migrate to the phase model

> **Breaking change:** Blueprint now ships five phase skills and two delivery skills. Old skill directories and copied workflow commands must be removed manually.

## What changed

| Before | Now |
| --- | --- |
| `design-doc`, `spec` | `/design` |
| `browser-verify` | Browser proof inside `/test` |
| `refactor` | `/improve` |
| `branch`, `commit`, `implement`, `pr`, `pr-to-ready` | Steps inside `/task-to-pr` |
| `task-to-pr` | Canonical `/task-to-pr` delivery skill |
| `debug`, `tdd` | Techniques used while implementing |
| `goal-design`, `multitask` | Ordinary instructions or project-specific workflows |
| `milestone` | `/milestone` skill, backed by `/task-to-pr` |
| `code-reviewer` agent definition | A fresh generic subagent launched by `/review` |

The public skill surface is now:

```text
/design · /plan · /test · /review · /improve · /task-to-pr · /milestone
```

## Clean upgrade

1. **Remove old Blueprint entry points.** In the skill directory used by your coding tool, remove only the old Blueprint skill folders listed above. Also remove copied Blueprint `implement.md` and `task-to-pr.md` command files. Do not delete whole skill or command directories; they may contain unrelated files.
2. **Install all seven skills.**

   ```bash
   npx skills add owainlewis/blueprint
   ```

3. **Remove copied reviewer agents.** Delete any old Blueprint `code-reviewer` definition. The `/review` skill now launches a fresh generic subagent.
4. **Check the result.** The `/design`, `/plan`, `/test`, `/review`, `/improve`, `/task-to-pr`, and `/milestone` skills should be available.

## Why cleanup is manual

Some noninteractive skill updaters add and replace skills but do not remove directories that disappeared upstream. Running `npx skills update` alone can therefore leave the old and new models installed together.

`/task-to-pr` is the only one-task delivery entry point. Keeping implementation, testing, review, publication, CI, and feedback in that skill avoids duplicate workflow names and routing ambiguity.
