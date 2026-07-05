---
name: review
description: "Review a code change for bugs, security problems, broken behavior, and missing tests."
user-invocable: true
argument-hint: "[optional: file path, diff, commit, or focus area]"
---
# Review

Goal: find the most important problems in a code change.

Do not edit files. Find the change from `$ARGUMENTS` or the conversation. Ask if unclear. If `REVIEW.md` exists at the repo root, follow it. Flag pre-existing problems only if the change reaches or worsens them.

Try to prove the change wrong, not right. Trust code and tests, not confident explanations.

## Quality

Check task behavior, edge cases, failure paths, security checks, function signatures, return values, data shapes, and existing patterns. Check whether tests prove the changed behavior. Flag dead code left by the change: unused variables, unused compatibility code, and comments that explain deleted code.

## Complexity And Over-Engineering

Flag new packages when the project already has a way to do the same thing, custom code covered by the standard library or platform, abstractions with one implementation, config nobody sets, and wrappers that only call another function.

For complexity findings, name what to remove and what replaces it: existing helper, standard library function, platform feature, simpler local code, or nothing.

## Findings

List findings: blockers, important, then nits. For each finding, include location, severity, bug, impact, and fix direction when it changes the next action.

- **blocker**: must fix before merge.
- **important**: should fix.
- **nit**: minor; the author can ignore it.

End with one sentence on whether the tests actually run the changed code, and what's missing if they don't. Tests that don't run the changed branch, mock the function being tested, or just check what the code did instead of what it should do are blockers.
