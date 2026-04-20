---
name: commit
description: "Stage and commit the intended changes with a clear message."
user-invocable: true
argument-hint: "[optional: commit message override]"
---

# Commit

## When to use

- The current work is ready to record in git
- The diff is understood and intentionally scoped

## Process

1. Inspect `git status`, `git diff`, and `git diff --cached`.
2. Read recent commit messages so the new commit fits the repo.
3. If there is nothing worth committing, stop.
4. Stage only the intended files. Never stage secrets.
5. Use the user's message if provided. Otherwise write a Conventional Commit message.
6. Create the commit and report the hash and message.

## Verification

- The staged changes match the intended scope
- The commit exists
- `git status` confirms the expected result

## Rules

- If the change breaks a contract or requires migration, note it clearly in the commit message body.
- If there is nothing to commit or the diff is not understood, stop.
- Prefer staging specific files over broad adds.
- Do not commit `.env`, credentials, or keys.
- Keep the subject line short and in imperative mood.
