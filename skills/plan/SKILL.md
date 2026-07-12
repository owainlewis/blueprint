---
name: plan
description: "Break an approved spec or decided brief into one or more agent-ready tickets, each delivering a working outcome. Optionally group or publish them when asked."
user-invocable: true
argument-hint: "<approved spec, decided brief, issue, or repo path>"
---

# Plan

Turn decided work into tickets a fresh agent can complete without the planning conversation.

1. Confirm the input is approved and decision-complete. If it is a spec, require `Status: Approved`. Stop when an open question affects behavior, interfaces, data, errors, or scope.
2. Read the whole input, linked material, and enough code to understand boundaries, dependencies, and verification commands.
3. Identify the smallest working outcomes that can be implemented and reviewed independently. Order them by dependency and risk.
4. Draft one or more tickets with the template below. Small work may need only one.
5. Group tickets into milestones only when each group has a distinct working result.
6. Return drafts in chat by default. Publish only when the user asks. Use the requested tracker or the tracker the project already uses, including GitHub Issues, Linear, or Jira. Ask which tracker when none is identifiable. Before publishing, check for duplicates, follow existing templates and labels, create dependency links when supported, and return every ticket URL. If access or publication fails, keep the complete drafts in chat and report the exact limitation.

## Definition Of Ready

Every ticket must have:

- One outcome, stated as working behavior rather than an implementation step.
- Enough context for a new agent with no prior conversation.
- Testable acceptance criteria.
- Specific commands or manual steps that prove completion.
- No unresolved product, design, interface, or error-behavior decisions.
- Clear boundaries and dependencies.

## Breakdown Rules

- Prefer vertical slices. Good: "A user can invite a teammate by email." Bad: separate database, API, and UI tickets for the same outcome.
- Keep tests with the behavior they prove. Do not create a final testing ticket.
- Do not split work only to create more tickets.
- Use a foundation ticket only when it has an independently verifiable result and clearly unlocks later work.
- Repeat the decisions needed to execute the ticket. Link the source, but do not make the agent reconstruct essential context.
- Do not prescribe files or functions unless their exact shape is a requirement.

## Ticket Template

```markdown
# <Imperative title describing one outcome>

## Outcome
What must be true when this ticket is complete.

## Why
Why this outcome matters.

## Context
Background, relevant decisions, links, and the source spec or brief.

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
