---
name: review
description: "Review a code change for correctness, security, contracts, and tests."
user-invocable: true
argument-hint: "[optional: file path, diff, commit, or focus area]"
---
# Review

Find the change from `$ARGUMENTS` or the conversation. Ask if unclear. If `REVIEW.md` exists at the repo root, follow it. Flag pre-existing problems only if the change reaches or worsens them. Do not fix anything.

Review to disprove, not confirm. Treat confident prose as non-evidence; verify behavior from code and tests.

## Quality

Check task behavior, edge cases, failure paths, security boundaries, contracts, and existing patterns. Check whether tests prove changed behavior. Flag dead code left by the change: unused variables, compatibility shims with no consumers, and comments narrating removed code.

## Complexity And Over-Engineering

Flag new dependencies when the project already has a way to do the same thing, hand-rolled code covered by the standard library or platform, abstractions with one implementation, config nobody sets, and wrappers that only delegate.

For complexity findings, name what to cut and what replaces it: existing helper, standard library function, platform feature, simpler local code, or nothing.

## Findings

List findings: blockers, important, then nits. For each finding, include location, severity, bug, impact, and fix direction when it changes the next action.

- **blocker**: must fix before merge.
- **important**: should fix.
- **nit**: minor; the author can ignore it.

End with one sentence on whether the tests actually run the changed code, and what's missing if they don't. Tests that don't run the changed branch, mock the function being tested, or just check what the code did instead of what it should do are blockers.
