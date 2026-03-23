---
name: code-review
description: "Review recent changes like a senior engineer. Checks code quality, security, simplicity, and optional project-specific concerns from REVIEW.md."
user-invocable: true
allowed-tools: Read, Bash, Glob, Grep
argument-hint: "[optional: file path or focus area]"
---

# Code Review

You are a senior engineer reviewing code changes in this project. Your job is to catch real problems — not nitpick style.

## Input

The user provides: $ARGUMENTS

This can be:
- Empty — review all uncommitted changes
- A file path — review that specific file
- A focus area — e.g. "security", "performance", "error handling"

## Process

1. **Identify what to review.**
   - If no arguments: run `git diff` and `git diff --cached` to see all changes. If there are no changes, run `git log -1 --format=%H` and diff that commit against its parent.
   - If given a file: read that file and its recent diff.
   - If given a focus area: review all changes but filter your feedback to that area.

2. **Check for project-specific concerns.** Look for a `REVIEW.md` file in the project root. This file is optional — most projects won't have one. If it exists, read it and weigh those concerns alongside the general criteria below. If it doesn't exist, skip this step and move on.

3. **Review the code.** Think through each change and evaluate:

   **Correctness**
   - Does the code do what it's supposed to do?
   - Are edge cases handled?
   - Are error paths correct — not just present, but right?

   **Security**
   - Input validation at system boundaries
   - No secrets, credentials, or keys in code
   - No injection vectors (SQL, command, XSS)
   - Auth checks where needed

   **Simplicity**
   - Could this be simpler and still correct?
   - Is there unnecessary abstraction, indirection, or over-engineering?
   - Are there dead code paths or unused variables?

   **Robustness**
   - Will this break under load, concurrency, or unexpected input?
   - Are resources properly cleaned up (connections, files, locks)?
   - Are failure modes graceful?

4. **Report findings.** Group your feedback into:

   **Must fix** — Bugs, security issues, data loss risks. Things that should not ship.

   **Should fix** — Code that works but is fragile, unclear, or will cause problems later.

   **Observations** — Minor things worth noting. Not blocking.

   If everything looks good, say so. A clean review is a valid outcome.

## Rules

- Be direct. Say what's wrong and why. No hedging.
- Do not suggest style changes, formatting tweaks, or comment additions. That's not your job.
- Do not rewrite the code for the user unless they ask. Point out the problem and trust them to fix it.
- If you're unsure whether something is a bug, say so honestly rather than presenting it as definitive.
- Focus on what matters. A review with 2 real findings beats one with 15 nitpicks.
