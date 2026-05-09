---
name: branch
description: "Create a focused Git branch for the current task."
user-invocable: true
argument-hint: "<branch-name or task reference>"
---

# Branch

Create a focused Git branch for the current task.

## Workflow

1. Inspect the current Git branch and `git status`.
2. Derive a short kebab-case Git branch name if the user did not provide one.
3. Use the repo or team's existing Git branch naming convention when one is obvious.
4. If the branch already exists, switch to it. Otherwise, create and switch to it.
5. Report the branch name and any uncommitted work that was already present.

## Rules

- Stop if the working tree state makes switching branches unsafe.
- Do not overwrite or discard uncommitted work.
- Do not invent a Git branch prefix when the repo has no obvious convention.
