---
name: implement
description: "Finish one code task: understand it, make the smallest change, test it, review it, and report or open the requested PR."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'LIN-123' or 'Task 2 from user-auth'"
---

# Implement

1. Read the request, its sources, and the relevant code. Capture the goal, acceptance criteria, checks, and what not to change.
2. Ask only when requirements, safety, ownership, or product behavior are unclear. State low-risk assumptions and continue.
3. Make the smallest complete change in the right module. Don't change public interfaces or data shapes unless the task requires it.
4. Add or update tests for changed behavior. If a useful test isn't practical, say why and verify manually.
5. Run the most relevant checks first, wider checks when shared or user-facing behavior changed. Fix relevant failures without expanding the task.
6. Use a subagent to review the work. Fix any issues found. 
7. Open a pull request for human to review

## Rules

- One task at a time. Don't touch unrelated code.
- Don't hide unchecked work.
- Don't overwrite or discard user changes.
- If the task, spec, or plan is wrong, stop and update the source of truth before continuing.
