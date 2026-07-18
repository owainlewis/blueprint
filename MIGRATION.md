# Migration to the phase model

This release is intentionally breaking. Blueprint now contains five phase skills and one `/implement` workflow.

## New surface

- Skills: `design`, `plan`, `test`, `review`, `improve`
- Workflow command: `/implement`

## Removed skills

`branch`, `browser-verify`, `commit`, `debug`, `design-doc`, `goal-design`, `implement`, `milestone`, `multitask`, `pr`, `pr-to-ready`, `refactor`, `spec`, `task-to-pr`, and `tdd` are no longer shipped.

The behavior is not all lost. Design docs and specs became `design`. Browser verification moved into `test`. Refactoring became `improve`. Ticket-to-PR delivery, commits, CI, feedback handling, and PR feedback moved into the `/implement` workflow. Debugging and TDD remain techniques an agent can use while implementing.

## Clean upgrade

First remove only the old Blueprint skill directories from the skill location used by your agent. Then reinstall:

```bash
npx skills add owainlewis/blueprint
```

Do not delete the whole skills directory because it may contain unrelated skills. Some noninteractive skill updaters do not remove directories that disappeared upstream, so `npx skills update` alone can leave both models installed.

Copy `commands/implement.md` to your tool's custom-command directory if it supports slash commands. Otherwise invoke that file as an ordinary prompt and keep only a reference to it in your repository instructions.

Remove any copied `code-reviewer` agent definition. The `review` skill now asks the coding tool for a fresh generic subagent, which avoids a second source of review policy.

There are no compatibility aliases. Keeping old and new entry points together makes routing ambiguous and defeats the purpose of the smaller model.
