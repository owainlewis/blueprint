---
name: tickets
description: "Break an approved spec into one or more agent-ready ticket drafts, each delivering a working outcome. Optionally group them into milestones or publish them when asked."
user-invocable: true
argument-hint: "<spec path or URL>"
---

# Tickets

Turn one approved spec into work units a fresh agent can complete without the planning conversation.

1. Require `Status: Approved` in the spec. Stop when approval is missing or an open question affects behavior, interfaces, data, errors, or scope.
2. Read the whole spec, its linked material, and enough of the codebase to understand boundaries, dependencies, and verification commands.
3. Identify the smallest working outcomes that can be implemented and reviewed independently. Order them by dependency and risk.
4. Draft one or more tickets with the template below. A small spec may need only one ticket.
5. Group tickets into milestones only when the groups have distinct outcomes. State the result of each milestone and preserve ticket dependency order.
6. Return drafts in chat by default. Create tracker issues only when the user explicitly asks. Before publishing, search for duplicates, use the existing tracker and labels, create dependency links, and return every issue URL.

## Definition of Ready

Every ticket must have:

- One outcome, stated as working behavior rather than an implementation step.
- Enough context for a new agent with no prior conversation.
- Testable acceptance criteria.
- Specific commands or manual steps that prove completion.
- No unresolved product, design, interface, or error-behavior decisions.
- Clear boundaries and dependencies.

## Breakdown Rules

- Prefer vertical slices. Good: "A user can invite a teammate by email." Bad: "Add table", "add API", and "add button" as separate tickets.
- Keep tests with the behavior they prove. Do not create a final testing ticket.
- Do not split work only to create more tickets.
- Use a foundation ticket only when it has an independently verifiable result and clearly unlocks later work.
- Repeat the spec decisions needed to execute the ticket. Link the spec, but do not make the agent reconstruct essential context.
- Do not prescribe files or functions unless their exact shape is a requirement.
- A dependency must name the ticket or decision that blocks progress and explain why.

## Ticket Template

```markdown
# <Imperative title describing one outcome>

## Outcome
What must be true when this ticket is complete.

## Why
Why this outcome matters.

## Context
Background, relevant decisions, links, and the source spec.

## Acceptance criteria
- Observable results, each checkable on its own.

## Verify
- Commands or manual steps that prove the acceptance criteria.

## Must preserve
- Existing behavior, interfaces, data, or compatibility that cannot change.

## Out of scope
- Related work this ticket must not absorb.

## Dependencies
- Tickets or decisions that must land first, and why.
```

## Milestone Format

```markdown
## <Milestone name>
Result: <working capability available when these tickets are complete>

1. <Ticket title> - <why it comes first>
2. <Ticket title> - depends on <ticket or decision>
```
