---
name: create-linear-issue
description: "Create a well-defined Linear issue through collaborative conversation. Use when the user wants to create, file, or write a Linear issue, ticket, or bug report."
user-invocable: true
---

# Create Linear Issue

Create a Linear issue for: $ARGUMENTS

## Goal

Create issues that an AI coding agent can pick up and implement without needing to ask clarifying questions. Focus on **what** needs to be done and **why**, not **how** to implement it.

## Principles

- **Describe intent, not implementation** — Let the implementing agent figure out which files to modify
- **Be specific about outcomes** — Vague requirements lead to misaligned implementations
- **Define boundaries clearly** — What's in scope matters as much as what's out of scope
- **Keep issues small** — If it needs >3 acceptance criteria, it should probably be split

## Workflow

### Step 1: Discover Workspace

Before anything else, use the Linear MCP tools to understand the workspace:

1. Call `mcp__linear-server__list_teams` to get available teams
2. Call `mcp__linear-server__list_projects` to get available projects
3. Call `mcp__linear-server__list_issue_labels` to get available labels

Cache these results — you'll need them when creating the issue.

### Step 2: Understand What the User Wants

Ask clarifying questions about:
- **The problem or feature** — What needs to change and why?
- **Type** — Is this a bug, feature, or improvement?
- **Priority** — Urgent / High / Medium / Low (default to Medium if unclear)

If the issue is a **bug**, also ask about:
- Steps to reproduce
- Current vs expected behavior
- Any error messages or logs

Do NOT write the issue yet. Gather enough context first.

### Step 3: Draft the Issue

Write the issue using the appropriate template below. Present it to the user for review.

### Step 4: Review and Adjust

Present the draft and ask if anything needs changing. Iterate until the user approves.

### Step 5: Create in Linear

Use `mcp__linear-server__save_issue` with:
- `title` — The issue title
- `description` — The full markdown body
- `team` — Team name from Step 1 (ask user which team if multiple)
- `project` — Project name (ask user which project, or omit)
- `priority` — 1=Urgent, 2=High, 3=Normal, 4=Low
- `labels` — Array of label names from Step 1
- `state` — "Backlog" (default) or ask user

If the issue should be split into sub-issues, create a parent issue first, then create child issues using the `parentId` field.

After creation, show the user the issue identifier (e.g., TEAM-123) and confirm it was created.

---

## Issue Templates

### Feature / Improvement

```markdown
## Summary
[1-2 sentences: what this accomplishes and why it matters]

## Current vs Expected Behavior
**Current:** [What happens now, or "N/A" for new features]
**Expected:** [What should happen after this is implemented]

## Acceptance Criteria
- [ ] [Specific, testable outcome 1]
- [ ] [Specific, testable outcome 2]
- [ ] [Specific, testable outcome 3]

## Scope
**In scope:** [What this issue covers]
**Out of scope:** [What this issue explicitly does NOT cover]

## Additional Context
[Optional: links to designs, related issues, or existing patterns to follow]
```

### Bug

```markdown
## Summary
[1-2 sentences: what's broken and the user impact]

## Reproduction Steps
1. [Specific step 1]
2. [Specific step 2]
3. [Specific step 3]

## Current vs Expected Behavior
**Current:** [What happens now]
**Expected:** [What should happen]

## Root Cause Analysis

### Evidence Gathered
[Summarize what was found in logs, error messages, code review]

### Possible Root Causes
1. **[Most likely cause]** — [Evidence supporting this]
2. **[Alternative cause]** — [Evidence supporting this]

## Acceptance Criteria
- [ ] [The bug is fixed: specific testable outcome]
- [ ] [Edge case is handled]
- [ ] [Regression test added]
```

---

## Splitting Issues

If an issue has more than 3 acceptance criteria or covers multiple concerns, suggest splitting it into parent + child issues. Ask the user before splitting.
