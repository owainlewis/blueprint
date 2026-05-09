---
name: commit
description: "Stage the intended changes and create one clear conventional commit."
user-invocable: true
argument-hint: "[optional commit message]"
---

# Commit

Create one clear commit for the intended current changes.

## Workflow

1. Inspect `git status`, `git diff`, and `git diff --cached`.
2. Read recent commit messages so the new one fits the repo.
3. If there is nothing worth committing, stop.
4. Stage only intended files. Never stage secrets.
5. Use the user's message if provided. Otherwise write a Conventional Commit message.
6. Create the commit and report the hash and message.

## Rules

- Prefer staging specific files over broad adds.
- Do not commit `.env`, credentials, or keys.
- If the diff is not understood, stop.
- The subject should say what changed. The body should explain why when context matters.
