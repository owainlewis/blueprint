---
name: plan
description: "Turn a reviewed design, brief, or large request into ordered agent-ready tasks and optional milestones."
user-invocable: true
argument-hint: "<design, brief, issue, or request>"
---

# Plan

1. Read the source, repository instructions, and relevant code.
2. Stop and return to design if product or technical choices remain open.
3. Break the work into vertical, outcome-based tasks small enough for one agent run. Order them by dependency. Add milestones only when they create a useful delivery or review boundary.
4. Put the plan in one place: create tracker tickets when asked, write `docs/<feature-slug>/plan.md` when a feature directory exists, or return it in chat.
5. Stop after planning. Do not implement.

Each task must stand alone:

```markdown
## <Task title>

**Outcome**
The working result.

**Context**
What a new agent needs with no session history.

**Constraints**
Decisions and behavior that must not change.

**Acceptance criteria**
- Testable condition.

**Checks**
Exact commands and any required manual verification.

**Out of scope**
Related work this task must not absorb.
```

Do not split by file or technical layer when one vertical slice can deliver working behavior. Do not create scaffolding or cleanup tasks without a checked outcome.
