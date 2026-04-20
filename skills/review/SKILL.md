---
name: review
description: "Review concrete code changes for correctness, security, simplicity, and robustness."
user-invocable: true
argument-hint: "[optional: file path or focus area]"
---

# Review

## When to use

- Reviewing current changes before commit or merge
- Reviewing a specific file or focus area
- Checking whether a change is safe to ship

## Process

1. Choose the target from `$ARGUMENTS`, the working tree, staged changes, or the latest commit.
2. Read the actual changes. If your environment offers an isolated review context, you may use it. If not, review directly.
3. Apply any repo-specific concerns from `REVIEW.md` if it exists.
4. Evaluate correctness, security, simplicity, and robustness.
5. Report findings as `Must fix`, `Should fix`, or `Observations`. A clean review is a valid outcome.

## Verification

- Every finding is tied to concrete code
- Findings are limited to the changes under review
- Pre-existing issues are not mixed in
- No finding is just a style preference

## Rules

- Flag changes that add unnecessary surface area.
- Flag silent contract changes.
- Flag missing or weak failure-path handling when it matters.
- If there is no concrete diff, file, or commit to review, say so.
- Findings only. Do not fix the code.
- Be direct and specific.
- Do not speculate without evidence.
- If you are unsure a problem is real, say so honestly.
