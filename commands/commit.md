---
description: "Stage the intended changes and create a conventional commit."
argument-hint: "[optional commit message]"
---

# Commit

Create one clear commit for the intended current changes.

1. Inspect `git status`, `git diff`, and `git diff --cached`.
2. Read recent commit messages so the new one fits the repo.
3. Stage only intended files. Never stage secrets.
4. Use the user's message if provided. Otherwise write a Conventional Commit message.
5. Commit and report the hash and message.

Stop if there is nothing to commit or the diff is not understood.
