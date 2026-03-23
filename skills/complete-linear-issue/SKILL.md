---
name: complete-linear-issue
description: "Pick up a Linear issue, implement it, and mark it done. Use when the user wants to work on, complete, close, or finish a Linear issue or ticket."
user-invocable: true
---

# Complete Linear Issue

Complete a Linear issue: $ARGUMENTS

## Goal

Pick up a Linear issue, implement the work described in it, and transition it to done — all in one flow.

## Workflow

### Step 1: Fetch the Issue

Use `mcp__linear-server__get_issue` to retrieve the issue details.

- `$ARGUMENTS` may be an issue identifier (e.g., TEAM-123), an issue title, or a description of what to work on
- If `$ARGUMENTS` is not a valid identifier, use `mcp__linear-server__list_issues` with `query` or `assignee: "me"` to find matching issues
- If multiple issues match, present them and ask the user to pick one

Read the full issue: title, description, acceptance criteria, labels, and any comments (`mcp__linear-server__list_comments`).

### Step 2: Confirm Understanding

Before writing any code, briefly summarize:
- **What** you're going to do (1-2 sentences)
- **Acceptance criteria** you'll satisfy
- **Approach** — high-level plan (files to touch, strategy)

Ask: "Does this look right, or should I adjust anything?"

Wait for confirmation before proceeding.

### Step 3: Move to In Progress

Update the issue state:
```
mcp__linear-server__save_issue(id: "TEAM-123", state: "In Progress")
```

### Step 4: Implement

Do the work described in the issue. Follow the acceptance criteria as your checklist.

- Write clean, minimal code that satisfies the requirements
- Add tests if the acceptance criteria call for them
- Do not over-engineer or add scope beyond what's specified

### Step 5: Verify

Before marking done, verify each acceptance criterion:

1. Run relevant tests
2. Check that the implementation matches the "Expected Behavior" from the issue
3. If anything is ambiguous or can't be satisfied, flag it to the user

### Step 6: Commit and Close

1. Stage and commit the changes with a message referencing the issue identifier (e.g., "TEAM-123: Add OAuth login to signup flow")
2. Update the issue state to done:

```
mcp__linear-server__save_issue(id: "TEAM-123", state: "Done")
```

3. Optionally add a comment summarizing what was done:

```
mcp__linear-server__save_comment(issueId: "TEAM-123", body: "Implemented in commit abc123. ...")
```

4. Report to the user: what was done, which acceptance criteria were met, and the issue identifier.

## Handling Problems

- **Issue is too vague** — Ask the user for clarification rather than guessing. Do not add a comment to the Linear issue asking for clarification unless the user asks you to.
- **Issue is too large** — Suggest splitting it. Offer to complete one piece and create follow-up issues for the rest.
- **Blocked by another issue** — Check if the blocking issue is linked. Tell the user what's blocking and suggest next steps.
- **Tests fail** — Fix the failing tests if the failure is related to your changes. If pre-existing failures, flag them and proceed.
