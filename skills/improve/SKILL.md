---
name: improve
description: "Improve an existing change by fixing valid findings and simplifying the code without adding product scope."
user-invocable: true
argument-hint: "<diff, branch, PR, test failure, or review feedback>"
---

# Improve

1. Read the task, acceptance criteria, current diff, tests, and review or CI feedback.
2. Classify each finding. Fix valid in-scope problems. Explain why any rejected finding is incorrect, already addressed, or out of scope.
3. Simplify the changed code where deletion, clearer names, fewer branches, or smaller abstractions improve it without changing required behavior.
4. Do not add new product behavior, redesign public interfaces, or absorb unrelated cleanup.
5. Rerun the affected tests and checks. Return the change to review when correctness or behavior changed.
6. When working on PR feedback, reply to addressed comments with the fix and evidence. Do not claim a finding is resolved before the fix is pushed.

Prefer the smallest complete fix. If feedback exposes a wrong requirement or design, stop and update the source of truth before changing code.
