---
name: test
description: "Proves that a code change meets its acceptance criteria. Uses focused automated checks and a real browser for browser-facing work. Use to test or verify a diff, branch, PR, URL, or user flow."
user-invocable: true
argument-hint: "<task, acceptance criteria, diff, branch, PR, URL, or flow>"
---

# Test

Prove that a change meets its acceptance criteria.

## Workflow

1. **Read**
   - Read the task, acceptance criteria, changed code, existing tests, and repository instructions.

2. **Map the proof**
   - Map every acceptance criterion and affected failure path to a check.
   - Include changed behavior and behavior a refactor must preserve.
   - If automated tests cannot cover something, explain why and name other evidence.

3. **Add missing tests**
   - Add or update focused tests where proof is missing.
   - Assert behavior a user or caller can observe, or a documented internal contract.
   - Make each assertion fail when the changed behavior breaks.
   - Keep setup and assertions no more complex than the scenario.

4. **Run the checks**
   - Start with the narrowest checks that exercise the changed behavior and affected interfaces.
   - Run wider checks when shared behavior or interfaces changed.
   - When browser-rendered behavior changes, start the documented app and check the required flows and affected failures in a real browser.
   - Check desktop and mobile when layout or responsive styles changed.
   - Check keyboard use when interactions changed.
   - Check console errors and failed requests during every flow.
   - Capture evidence. Reading source is not browser proof.

5. **Report**
   - Mark every criterion as pass, fail, or unverified.
   - Include the command, browser flow, or other evidence.

## Rules

- Do not weaken assertions to make a change pass.
- Do not fix unrelated failures.
- If required browser tooling is unavailable, report the check as blocked unless the user explicitly accepts a manual exception.
