---
name: branch
description: "Create a traceable Git branch for the current task."
user-invocable: true
argument-hint: "<branch-name or task reference>"
---

# Branch

Create a traceable Git branch for the current task.

## Workflow

1. Inspect the current branch, `git status`, and available task context.
2. Learn the repo's branch convention from existing names: prefix, ticket placement, and casing. Follow it.
3. Choose the name. A user-provided name wins as given. Otherwise derive `<ticket-id>-<short-kebab-summary>` when the work has a ticket ID, or `<short-kebab-summary>` when it does not: lowercase summary of five words or fewer, ticket ID in its own casing, strip anything that is not a letter, digit, or hyphen. If a ticket exists but its ID is not visible, ask when a human is present; unattended, proceed without it and note that in the report.
4. Branch from the up-to-date default branch: fetch, then create from `origin/<default>`. Branch from anywhere else only when the user explicitly asks to stack.
5. If the branch already exists, switch to it and report how it relates to the default branch, including any commits it already carries. Otherwise create and switch.
6. Report the branch name, its base, and any uncommitted work that was already present.

## Rules

- Stop if the working tree state makes switching branches unsafe.
- Do not overwrite or discard uncommitted work.
- Include the ticket ID for work from an issue tracker.
- Do not invent ticket IDs.
