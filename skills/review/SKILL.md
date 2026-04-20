---
name: review
description: "Review recent changes like a senior engineer. Checks code quality, security, simplicity, and optional project-specific concerns from REVIEW.md."
user-invocable: true
argument-hint: "[optional: file path or focus area]"
---

# Code Review

Review code changes like a senior engineer. Prefer an independent pass that is not overly influenced by the current conversation. If your environment offers an isolated review context, you may use it. If not, review directly.

## What to review

- If no arguments were given: inspect current working tree and staged changes.
- If there are no current changes: review the latest commit if history is available.
- If given a file path: read that file and its relevant diff.
- If given a focus area (e.g. "security"): review all changes but filter findings to that area.
- If there is no diff and no commit history to review, tell the user there is nothing concrete to review yet.

## Process

1. Read the actual changes. Do not trust summaries of what changed.
2. Look for a `REVIEW.md` in the project root. If it exists, apply those concerns alongside the criteria below.
3. Evaluate against:
   - **Correctness** — Does it do what it should? Edge cases? Error paths that are wrong, not just missing?
   - **Security** — Input validation at boundaries. No secrets in code. No injection vectors. Auth checks where needed.
   - **Simplicity** — Could this be simpler and still correct? Unnecessary abstraction or dead code?
   - **Robustness** — Will it break under load, concurrency, or unexpected input? Are resources cleaned up?
4. Report findings grouped as:
   - **Must fix** — Bugs, security issues, data loss risks. Things that should not ship.
   - **Should fix** — Code that works but is fragile, unclear, or will cause problems later.
   - **Observations** — Minor things worth noting. Not blocking.

If everything looks good, say so. A clean review is a valid outcome.

## Rules

- Only flag real problems — things the author would fix if they knew about them.
- Do not flag pre-existing issues.
- Do not speculate about what might break — if you can't point to the affected code, it's not a finding.
- Be direct. Say what's wrong and why.
- Do not suggest style changes, formatting tweaks, or comment additions.
- Do not fix anything. Present findings only.
- If unsure whether something is a bug, say so honestly.
- A review with 2 real findings beats one with 15 nitpicks.
- Ground findings in technical facts, not opinion. "This is hard to read" is opinion. "This allocates on every loop iteration when it could allocate once" is a finding.
- Flag hedging language in code comments or error messages: "should work", "probably fine", "seems correct". If the author wasn't certain, it needs a closer look.

## Don't rationalize away findings

| Temptation | Reality |
|---|---|
| "It works, so it's fine" | Working code that's insecure or architecturally wrong creates debt that compounds. |
| "I wrote it, so I know it's correct" | Authors are blind to their own assumptions. That's why review exists. |
| "The tests pass" | Tests are necessary but not sufficient. They don't catch architecture problems or security issues. |
| "It's just a small change" | Small changes cause big outages. Review effort should match risk, not line count. |
| "AI-generated code is probably fine" | AI code needs more scrutiny, not less. It's confident and plausible, even when wrong. |
