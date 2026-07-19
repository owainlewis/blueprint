---
name: test
description: "Tests a code change against its acceptance criteria using focused automated checks and real-browser verification for browser-facing work. Use when the user asks to test, verify, validate, QA, check acceptance criteria, browser-test, or prove a diff, branch, PR, URL, or user flow works."
user-invocable: true
argument-hint: "<task, acceptance criteria, diff, branch, PR, URL, or flow>"
---

# Test

## Workflow

1. Read the task, acceptance criteria, changed code, existing tests, and repository instructions.
2. Map every acceptance criterion and important failure path to proof. Add or update focused tests when proof is missing.
3. Run the narrowest relevant checks, then wider checks when shared behavior or interfaces changed.
4. For browser-rendered behavior, start the documented app and verify the main flow and important failure states in a real browser. Check desktop and mobile layout when relevant, keyboard use, console errors, and failed requests. Capture evidence. Source inspection is not browser proof.
5. Report each criterion as pass, fail, or unverified with the command, browser flow, or evidence that supports it.

## Boundaries

- Do not weaken assertions to make a change pass.
- Do not fix unrelated failures.
- If required browser tooling is unavailable, report the check as blocked unless the user explicitly accepts a manual exception.
