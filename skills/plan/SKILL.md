---
name: plan
description: "Break a spec or decided brief into agent-ready tickets that each deliver a working outcome. Draft them in chat and publish them when asked."
user-invocable: true
argument-hint: "<spec, brief, issue, or repo path>"
---

# Plan

1. Read the input, linked material, and relevant code. Stop and list missing decisions if the work is not ready to build.
2. Split the work into the smallest useful outcomes an agent can implement, test, and review independently. Keep dependent work in order. One ticket is fine.
3. Write each ticket with the template below. Include enough context for a new agent with no access to this conversation.
4. Return drafts in chat. Publish only when asked, using the requested or existing tracker such as GitHub Issues, Linear, or Jira. If access is unavailable, return the complete drafts and say why they were not published.
5. Group tickets into milestones only when that makes the delivery order clearer.

Prefer working slices over separate database, API, UI, or testing tickets. Do not split work just to create more tickets.

```markdown
# <One working outcome>

## Goal
What must be true when this ticket is done, and why.

## Context
The decisions, links, and constraints the agent needs.

## Acceptance criteria
- Observable results.

## Verify
- Commands or manual checks that prove completion.

## Must preserve
- Existing behavior or interfaces that cannot change.

## Out of scope
- Related work this ticket must not absorb.

## Dependencies
- Work that must land first, and why.
```
