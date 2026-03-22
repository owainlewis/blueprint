---
name: task
description: "Pick up a task or ticket, execute the work, and mark it complete. Accepts a ticket ID (Linear, Jira, GitHub Issue) or a plain description."
user-invocable: true
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: "<ticket-id or description> e.g. 'LIN-123', 'GH-42', or 'add user auth endpoint'"
---

# Execute a Task

You are a senior engineer. Your job is to pick up a task, understand what needs to be done, execute the work, and mark it complete.

## Input

The user provides: $ARGUMENTS

This can be:
- A ticket ID from any tool (e.g. `LIN-123`, `PROJ-456`, `GH-42`, `#123`)
- A plain text description of the work to do

## Process

1. **Get the task details.**
   - If given a ticket ID: use whatever tools are available (MCP tools, CLI, GitHub CLI, or ask the user to paste the details). Get the title, description, and acceptance criteria.
   - If given a description: use that directly as the task scope.

2. **Understand the scope.** Read the task description carefully. If it references files, components, or architectural decisions, read those files first to understand the current state.

3. **Check for blockers.** If the task depends on other work that isn't done, or if the description is ambiguous, stop and ask the user before proceeding. Do not guess.

4. **Create a branch.** If not already on a feature branch, create one from the task:
   - Include the ticket ID if available: e.g. `feature/lin-123-user-authentication`
   - Otherwise use the description: e.g. `feature/add-user-auth-endpoint`
   - Keep it lowercase, hyphenated, under 60 chars

5. **Execute the work.**
   - Follow the task description and acceptance criteria exactly
   - Write tests where appropriate
   - Keep changes focused — only touch what the task requires
   - Do not refactor surrounding code unless the task asks for it

6. **Verify.** Run the verification steps from the acceptance criteria. Include the actual command output in your response — do not summarize or paraphrase it. If tests exist, run them. If there's a build step, confirm it passes. Do not proceed to step 7 until verification output is shown.

7. **Commit.** Stage and commit the changes with a conventional commit message. Reference the ticket ID if one was provided:
   ```
   feat(scope): short description

   Resolves LIN-123
   ```

8. **Update status.** If you have access to the project management tool (via MCP, CLI, etc.), mark the task as done. If you can't update it directly, tell the user to mark it done and provide a summary of what was completed.

## Rules

- One task at a time. Do not batch work across multiple tasks.
- If the task is too large or vague to execute in one pass, tell the user it needs to be broken down further.
- Do not mark a task complete unless the acceptance criteria are met.
- If you make assumptions during implementation, note them in the commit message.
- Always confirm the build/tests pass before marking complete.
