---
name: review
description: "Review a code change for bugs, security problems, broken behavior, and missing tests."
user-invocable: true
argument-hint: "[optional: file path, diff, commit, or focus area]"
---

# Review

Do not edit files. Find the change from `$ARGUMENTS` or the conversation; ask if unclear. Follow `REVIEW.md` at the repo root if it exists. Flag pre-existing problems only if the change reaches or worsens them.

Try to prove the change wrong, not right. Trust code and tests, not confident explanations.

## Quality

Check behavior, edge cases, failure paths, security, interfaces and data shapes, and fit with existing patterns. Check whether tests prove the changed behavior. Flag dead code left by the change.

## Complexity

Flag new packages the project can already do without, custom code the standard library covers, abstractions with one implementation, config nobody sets, and wrappers that only forward. For each, name what to remove and what replaces it.

## Findings

List blockers, then important, then nits, each with location, severity, impact, and fix direction when it changes the next action.

- **blocker**: must fix before merge.
- **important**: should fix.
- **nit**: author can ignore.

End with one sentence on whether the tests actually run the changed code. Tests that don't run the changed branch, mock the function under test, or assert what the code did instead of what it should do are blockers.
