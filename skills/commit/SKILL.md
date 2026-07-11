---
name: commit
description: "Stage intended changes and create one Conventional Commit."
user-invocable: true
argument-hint: "[optional commit message]"
---

# Commit

1. Inspect the working tree and diffs. If there are no intended changes, or you cannot explain the diff, stop.
2. Stage only the intended files, not broad adds.
3. Use the user's message if provided. Otherwise write a Conventional Commit matching the repo's existing style: imperative subject, add a body only when the reason, checks, or risk matter.
4. Commit and report the hash and message.

## Rules

- Never commit `.env`, credentials, or keys.
- Never bypass hooks with `--no-verify`. If a hook fails, fix the cause or stop and report.
