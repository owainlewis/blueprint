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

Use the Linear MCP tools to retrieve the issue details. `$ARGUMENTS` may be an issue identifier (e.g., TEAM-123), a title, or a description. If multiple issues match, present them and ask the user to pick one.

Read the full issue: title, description, acceptance criteria, labels, and comments.

### Step 2: Confirm Understanding

Before writing any code, briefly summarize what you're going to do, which acceptance criteria you'll satisfy, and your approach. Wait for confirmation.

### Step 3: Implement

Move the issue to "In Progress". Do the work described in the issue, following the acceptance criteria as your checklist. Write clean, minimal code. Do not add scope beyond what's specified.

### Step 4: Verify

Before marking done, verify each acceptance criterion. Run relevant tests. If anything is ambiguous or can't be satisfied, flag it to the user.

### Step 5: Commit and Close

1. Commit with a message referencing the issue identifier
2. Mark the issue as "Done"
3. Optionally add a comment summarizing what was done
4. Report to the user: what was done and which acceptance criteria were met

## Handling Problems

- **Issue is too vague** — Ask the user for clarification rather than guessing. Do not add a comment to the Linear issue asking for clarification unless the user asks you to.
- **Issue is too large** — Suggest splitting it. Offer to complete one piece and create follow-up issues for the rest.
- **Blocked by another issue** — Check if the blocking issue is linked. Tell the user what's blocking and suggest next steps.
- **Tests fail** — Fix the failing tests if the failure is related to your changes. If pre-existing failures, flag them and proceed.
