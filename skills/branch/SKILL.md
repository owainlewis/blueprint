---
name: branch
description: "Create a traceable Git branch for the current task."
user-invocable: true
argument-hint: "<branch-name or task reference>"
---

# Branch

Create a traceable Git branch for the current task.

## Workflow

1. Inspect the current Git branch, `git status`, and available task context.
2. Identify the ticket ID when the work is tracker-backed. If the task has a ticket but no visible ID, ask for it.
3. Use the user's branch name if provided; if tracker-backed work omits the ticket ID, ask before creating it.
4. Otherwise derive `<ticket-id>-<short-kebab-summary>` when there is a ticket ID, or `<short-kebab-summary>` when there is not.
5. Preserve an obvious repo prefix such as `feature/` only if the ticket ID remains visible.
6. If the branch already exists, switch to it. Otherwise, create and switch to it.
7. Report the branch name and any uncommitted work that was already present.

## Rules

- Stop if the working tree state makes switching branches unsafe.
- Do not overwrite or discard uncommitted work.
- Include the ticket ID for tracker-backed work.
- Do not invent ticket IDs.
