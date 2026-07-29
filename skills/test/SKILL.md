---
name: test
description: "Proves that a code change meets its acceptance criteria. Uses focused automated checks and a real browser for browser-facing work. Use to test or verify a diff, branch, PR, URL, or user flow."
user-invocable: true
argument-hint: "<task, acceptance criteria, diff, branch, PR, URL, or flow>"
---

# Test

## Workflow

1. Read the task, acceptance criteria, changed code, existing tests, and repository instructions.
2. Map every acceptance criterion and affected failure path to proof. Test changed behavior and behavior a refactor must preserve.
3. If automated tests cannot exercise the affected behavior, explain why and give other evidence.
4. Add or update focused tests where proof is missing. Assertions should fail when the changed behavior breaks.
5. Assert behavior a user or caller can observe unless the test targets a documented internal contract. Keep setup and assertions no more complex than the scenario.
6. Run the narrowest checks that exercise the changed behavior and affected interfaces. Run wider checks when shared behavior or interfaces changed.
7. When browser-rendered behavior changes, start the documented app and check the required flows and affected failures in a real browser.
   - Check desktop and mobile when layout or responsive styles changed.
   - Check keyboard use when interactions changed.
   - Check console errors and failed requests during every flow.
   - Capture evidence. Reading source is not browser proof.
8. Report each criterion as pass, fail, or unverified. Include the command, browser flow, or other evidence.

## Boundaries

- Do not weaken assertions to make a change pass.
- Do not fix unrelated failures.
- If required browser tooling is unavailable, report the check as blocked unless the user explicitly accepts a manual exception.
