---
name: branch
description: "Create a Git branch for the current task."
user-invocable: true
argument-hint: "<branch-name or task reference>"
---

# Branch

Goal: create or switch to a safe branch for this task.

## Workflow

1. Check the current branch, `git status`, and task details.
2. Look at existing branch names. Follow the repo's style for prefixes, ticket IDs, and casing.
3. Choose the name. A name from the user wins as given. Otherwise derive `<ticket-id>-<short-kebab-summary>` when the work has a ticket ID, or `<short-kebab-summary>` when it does not: lowercase summary of five words or fewer, ticket ID in its own casing, strip anything that is not a letter, digit, or hyphen. If a ticket exists but its ID is not visible, ask when a human is present; when no human is present, proceed without it and note that in the report.
4. Branch from the latest default branch: fetch, then create from `origin/<default>`. Branch from another branch only when the user explicitly asks.
5. If the branch already exists, switch to it and report whether it already has commits. Otherwise create it and switch to it.
6. Report the branch name, its base, and any uncommitted work that was already present.

## Rules

- Stop if local changes make switching branches unsafe.
- Do not overwrite or discard uncommitted work.
- Include the ticket ID for work from an issue tracker.
- Do not invent ticket IDs.
