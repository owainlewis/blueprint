---
name: review
description: "Review a spec or concrete code changes and report evidence-backed bugs, regressions, and risks."
user-invocable: true
argument-hint: "[optional: file path or focus area]"
---

# Review

## When to use

- Reviewing a spec before execution
- Reviewing current changes before commit or merge
- Reviewing a specific file or focus area
- Checking whether a change is safe to ship

## Process

1. Choose the target from `$ARGUMENTS`, the working tree, staged changes, or the latest commit.
2. If the target is a spec, check whether decisions, invariants, requirements, error behavior, and tests are reviewable before code exists.
3. If the target is code, read the actual changes and any available context that explains intent, such as the spec, plan, commit message, or PR title and description.
4. Apply any repo-specific concerns from `REVIEW.md` if it exists.
5. Prioritize concrete bugs, regressions, contract breaks, failure-path gaps, missing decisions, broken invariants, and unnecessary complexity.
6. Report findings as `Must fix`, `Should fix`, or `Observations`, ordered highest risk first. A clean review is a valid outcome.

## Verification

- Every finding is tied to concrete evidence in the target
- Every finding explains why it matters
- Findings are limited to the changes under review
- Highest-risk findings come first
- Pre-existing issues are not mixed in
- No finding is just a style preference

## Rules

- Prioritize real bugs and regressions over style commentary.
- Flag changes that add unnecessary surface area.
- Flag silent contract changes.
- Flag decisions made in code that were not surfaced in the spec when they affect behavior or maintenance.
- Flag invariants that were omitted from a spec or quietly broken by an implementation.
- Flag missing or weak failure-path handling when it matters.
- Flag reviewer-facing context that is missing or misleading when it would make the change hard to review, such as a PR title or description that does not explain what changed and why.
- If there is no concrete diff, file, or commit to review, say so.
- Findings only. Do not fix the code.
- Be direct and specific.
- Tie each finding to evidence in the diff.
- Do not speculate without evidence.
- If you are unsure a problem is real, say so honestly.
