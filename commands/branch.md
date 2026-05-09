---
description: "Create a feature branch for the current task."
argument-hint: "<branch-name or task reference>"
---

# Branch

Create a focused feature branch for `$ARGUMENTS`.

1. Inspect the current branch and `git status`.
2. Derive a short kebab-case branch name if the user did not provide one.
3. Use the repo or team's existing branch naming convention when one is obvious.
4. Create and switch to the branch.
5. Report the branch name and any uncommitted work that was already present.

Stop if the working tree state makes switching branches unsafe.
