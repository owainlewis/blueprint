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

Use the Linear MCP tools to list available teams, projects, and labels. You'll need these when creating the issue.

### Step 2: Understand What the User Wants

Ask clarifying questions about the problem or feature, type (bug/feature/improvement), and priority. For bugs, also ask about reproduction steps and current vs expected behavior. Gather enough context before writing anything.

### Step 3: Draft and Review

Write the issue using the appropriate structure below. Present it to the user. Iterate until approved.

### Step 4: Create in Linear

Create the issue via the Linear MCP tools with the appropriate team, project, priority, and labels. If the issue should be split, create a parent issue first, then child issues. Show the user the issue identifier when done.

---

## Issue Structure

**Features/Improvements:** Summary, Current vs Expected Behavior, Acceptance Criteria (max 3), Scope (in/out), Additional Context.

**Bugs:** Summary, Reproduction Steps, Current vs Expected Behavior, Root Cause Analysis (evidence + possible causes), Acceptance Criteria.

---

## Splitting Issues

If an issue has more than 3 acceptance criteria or covers multiple concerns, suggest splitting into parent + child issues. Ask the user before splitting.
