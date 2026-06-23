---
name: implement
description: "Turn one scoped task into a verified diff: code, tests, verification, report. The inner build step of the delivery flow. Use directly when the workspace is prepared and no PR is expected; use task-to-pr when a ticket should become a PR."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'LIN-123' or 'Task 2 from user-auth'"
---

# Implement

Turn one task into a verified diff. Read the task, the spec when one exists, and the relevant code; fetch tracker details when the task references a ticket and mark it in progress. Ask when requirements are unclear, when the task is too large to be one change, or when anything affects behavior or safety. State low-risk assumptions and keep going.

## Contract

- One task at a time. Make the smallest complete change that fully does it.
- Before coding, identify the owning module and boundary. Put the change where the behavior belongs; keep I/O, persistence, rendering, and domain logic from bleeding into each other.
- Don't touch unrelated code. The task is not an excuse for cleanup elsewhere.
- Don't change function signatures, return shapes, or other contracts unless the task says to. If forced, call it out.
- Prefer boring, local code over new abstractions. Add an abstraction only when it removes real complexity, protects a boundary, or has a real second use.
- Make invalid states harder to represent. Prefer explicit types, enums, narrow constructors, and clear error paths over boolean flags, nullable state, or swallowed failures.
- Add or update tests whenever behavior changes, a bug is fixed, or a real edge case is introduced. Tests must prove the new behavior, not just exercise the code.
- If the behavior is hard to test without huge mocks, reconsider the boundary before forcing the test.
- When correctness depends on a framework's current behavior, check the docs for the version the project actually uses instead of trusting memory.
- Run the focused checks first, then the project's wider checks. Fix what they catch without growing scope.
- When used directly, run `review` on the final diff for non-trivial changes, with a fresh subagent when available. Ask it to check ownership, boundaries, invalid states, unnecessary abstraction, and whether tests prove the changed behavior. Fix valid in-scope findings and rerun the checks.
- When run inside `task-to-pr`, skip the direct-use review step. `task-to-pr` owns fresh review and acceptance verification for the PR loop.
- Report what changed, the checks run with results, acceptance criteria status, review findings fixed when reviewed directly, and anything not verified. If the task came from a tracker, comment the evidence and mark it ready for review.
