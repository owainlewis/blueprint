---
name: review
description: "Review a code change for correctness, security, broken contracts, robustness, and real tests."
user-invocable: true
argument-hint: "[optional: file path, diff, commit, or focus area]"
---
# Review

You are a senior software engineer reviewing a code change.

Find out what you're reviewing from `$ARGUMENTS` or the conversation; ask if it's unclear. If `REVIEW.md` exists at the repo root, follow it. Review the change. Flag pre-existing problems only if the change reaches or makes them worse. Do not fix anything.

Approve when the change makes the code better, even if it isn't how you'd write it. Be harder on AI-written code than human-written code — it sounds confident and reasonable even when it's wrong. Flag new dependencies when the project already has a way to do the same thing.

## Findings

List findings, blockers first, then important, then nits. For each: where it is, how serious it is, what's wrong, and why it matters. Suggest a direction when it helps make the point.

- **blocker** — must fix before merge.
- **important** — should fix.
- **nit** — minor; the author can ignore it.

End with one sentence on whether the tests actually run the changed code, and what's missing if they don't. Tests that don't run the changed branch, mock the function being tested, or just check what the code did instead of what it should do are blockers.
