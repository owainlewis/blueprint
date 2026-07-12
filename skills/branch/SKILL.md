---
name: branch
description: Create or switch to a Git branch for the current task. Use whenever starting work on a ticket, feature, or fix, whenever the user says "make a branch" or "new branch", and before committing work that would otherwise land on the default branch.
user-invocable: true
argument-hint: <branch-name or task reference>
---

# Branch

1. Check the current branch, `git status --short`, remotes, and task details.
2. Name it. A name from the user wins as given. Otherwise use `<ticket-id>-<short-kebab-summary>`, or just the summary if there is no ticket. Follow the repo's existing naming style.
3. Fetch, then branch from the latest default branch when a remote exists, unless the user says otherwise.
4. If the branch already exists, switch to it and report commits it has beyond the base.
5. Report the branch name, its base, and any uncommitted work that was present.

## Rules

- Never stash, discard, or force through uncommitted work. If switching is blocked, stop and ask.
- Never invent ticket IDs. If a ticket exists but its ID is not visible, ask; if no human is available, proceed without it and say so in the report.
