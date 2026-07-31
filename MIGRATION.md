# Migrate from older Blueprint skills

> **Breaking change:** Blueprint now ships nine skills. You must remove old Blueprint skill folders and copied commands by hand.

## What changed

| Before | Now |
| --- | --- |
| No previous equivalent | `/architecture` |
| Design review through `/review` | `/architecture-review` |
| `design-doc`, `spec` | `/design` |
| `browser-verify` | Browser proof inside `/test` |
| `refactor` | `/improve` |
| `branch`, `commit`, `implement`, `pr`, `pr-to-ready` | Steps inside `/task-to-pr` |
| `task-to-pr` | `/task-to-pr` |
| `debug`, `tdd` | Techniques used while implementing |
| `goal-design`, `multitask` | Ordinary instructions or project-specific workflows |
| `milestone` | `/milestone` skill, backed by `/task-to-pr` |
| `code-reviewer` agent definition | A fresh generic subagent launched by `/review` |

These are the nine skills you can call:

```text
/architecture · /design · /architecture-review · /plan · /test · /review · /improve · /task-to-pr · /milestone
```

## Clean upgrade

1. **Remove old Blueprint skills and commands.** In the skill directory used by your coding tool, remove only the old Blueprint skill folders listed above. Also remove copied Blueprint `implement.md` and `task-to-pr.md` command files. Do not delete whole skill or command directories because they may contain unrelated files.
2. **Install all nine skills.**

   ```bash
   npx skills add owainlewis/blueprint
   ```

3. **Remove copied reviewer agents.** Delete any old Blueprint `code-reviewer` definition. The `/review` skill now launches a fresh generic subagent.
4. **Check the result.** The `/architecture`, `/design`, `/architecture-review`, `/plan`, `/test`, `/review`, `/improve`, `/task-to-pr`, and `/milestone` skills should be available.

## Why cleanup is manual

Some update commands add or replace skills but do not remove folders from an older version. Running `npx skills update` alone can therefore leave both the old and new skills installed.

Use `/task-to-pr` to deliver one task. It keeps implementation, testing, review, publication, CI, and feedback in one place so a reader does not have to choose between overlapping workflow names.
