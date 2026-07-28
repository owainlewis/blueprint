---
name: test
description: "Tests a code change against its acceptance criteria using focused automated checks and real-browser verification for browser-facing work. Use when the user asks to test, verify, validate, QA, check acceptance criteria, browser-test, or prove a diff, branch, PR, URL, or user flow works."
user-invocable: true
argument-hint: "<task, acceptance criteria, diff, branch, PR, URL, or flow>"
---

# Test

## Workflow

1. Read the task, acceptance criteria, changed code, existing tests, and repository instructions.
2. Map every acceptance criterion and failure path affected by the change to proof. Test changed behavior, those failure paths, and behavior a refactor must preserve. If the change has no executable behavior, or the affected behavior cannot be exercised through available automated interfaces, state the concrete reason and substitute evidence.
3. Add or update focused tests where proof is missing. Check that assertions would fail when the changed behavior breaks and assert observable behavior rather than incidental implementation unless the internal contract is the target. Keep setup and assertions no more complex than the scenario requires.
4. Run the narrowest checks that exercise the changed behavior and affected interfaces, then wider checks when shared behavior or interfaces changed.
5. When browser-rendered behavior changes, start the documented app and verify the acceptance-criteria flows and affected failure states in a real browser. Check desktop and mobile when layout or responsive styles changed, and check keyboard use when interactions changed. Check console errors and failed requests during every browser flow. Capture evidence. Source inspection is not browser proof.
6. Report each criterion as pass, fail, or unverified with the command, browser flow, or evidence that supports it.

## Boundaries

- Do not weaken assertions to make a change pass.
- Do not fix unrelated failures.
- If required browser tooling is unavailable, report the check as blocked unless the user explicitly accepts a manual exception.
