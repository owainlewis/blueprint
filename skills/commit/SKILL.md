---
name: commit
description: "Stage and commit changes with a well-crafted commit message. Use when you're ready to commit your current work."
user-invocable: true
argument-hint: "[optional: commit message override]"
---

# Git Commit

Create a clean, well-structured git commit for the current changes.

## Process

1. Run `git status` to see what has changed (staged and unstaged).
2. Run `git diff` and `git diff --cached` to understand the actual changes.
3. Run `git log --oneline -10` to understand the commit message style of the repo.

If there are no changes to commit, tell the user and stop.

4. Stage the relevant files. Prefer staging specific files over `git add -A`. Never stage files that look like secrets (`.env`, credentials, keys).

5. If the user provided a message via `$ARGUMENTS`, use that as the commit message.

   Otherwise, write a commit message following **Conventional Commits** format:

   ```
   type(scope): short description

   Optional body explaining why, not what.
   ```

   Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `perf`, `style`, `build`

   Rules:
   - Subject line under 72 characters
   - Use imperative mood ("add feature" not "added feature")
   - The body should explain **why** the change was made, not repeat the diff
   - Do not include "Co-Authored-By" lines

6. Create the commit.
7. Run `git status` to confirm success.
8. Print the commit hash and message.
