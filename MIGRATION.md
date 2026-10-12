# Migrate from older Blueprint skills

> **Breaking change:** Blueprint now ships twelve skills. You must remove old Blueprint skill folders and copied commands by hand.

## Opt-in invocation

Reinstall Blueprint to receive the invocation settings. Remove any copied repository rule that forces `/task-to-pr` for every code change. Keep your repository's scope, verification, review, and delivery rules. Explicitly selected workflows still load their required skills.

## What changed

| Before | Now |
| --- | --- |
| `multitask` | `/codex-issue-coordinator` for Codex issue batches |
| `/issue-coordinator` | `/codex-issue-coordinator` |
| Design review through `/review` | `/architecture-review` |
| `design-doc`, `/design`, old `spec` | `/spec` for feature changes |
| System product needs inside `/design` | `/requirements` |
| Existing-state-only `/architecture` | `/architecture` for intended system design and data model |
| Unattended `/factory` leaving PRs open | `/task-to-pr`; explicit `/factory` now adds gated merging |
| `browser-verify` | Browser proof inside `/test` |
| `refactor` | `/improve` |
| `branch`, `commit`, `implement`, `pr`, `pr-to-ready` | Steps inside `/task-to-pr` |
| `task-to-pr` | `/task-to-pr`, now for one or more tasks |
| `debug`, `tdd` | Techniques used while implementing |
| `goal-design` | Ordinary instructions or a project-specific workflow |
| `milestone` | `/task-to-pr` with the milestone as input |
| `code-reviewer` agent definition | A fresh generic subagent launched by `/review` |

Existing `design.md` documents remain valid sources. Rename or split them only when useful. Do not treat an old architecture document as a future design without reviewing its decisions.

**Authority change:** Explicit `/factory` use now grants scoped merge authority. Remove old automations or prompts that invoke it expecting an open PR; use `/task-to-pr` instead.

## Clean upgrade

1. **Remove old Blueprint skills and commands.** In the skill directory used by your coding tool, remove the old `/design` and `milestone` skills and the other old Blueprint skill folders listed above. Also remove copied Blueprint `implement.md` and `task-to-pr.md` command files. Do not delete whole skill or command directories because they may contain unrelated files.
2. **Install all twelve skills.**

   ```bash
   npx skills add owainlewis/blueprint
   ```

3. **Remove copied reviewer agents.** Delete any old Blueprint `code-reviewer` definition. The `/review` skill now launches a fresh generic subagent.
4. **Check the result.** Compare installed skills with the [current skill list](README.md#twelve-focused-skills).

## Why cleanup is manual

Some update commands add or replace skills but do not remove folders from an older version. Running `npx skills update` alone can therefore leave both the old and new skills installed.
