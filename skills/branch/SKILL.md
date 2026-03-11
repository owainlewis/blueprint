---
name: branch
description: "Create and checkout a new git branch using conventional naming. Use when starting work on a new feature, bug fix, or task."
user-invocable: true
allowed-tools: Bash, Read
argument-hint: "<type> <short-description> e.g. 'feature user-auth' or 'fix login-redirect'"
---

# Git Branch

Create and checkout a new git branch following conventional naming conventions.

## Input

The user provides: `$ARGUMENTS`

This should be in the format: `<type> <description>`

## Branch Types

| Type | Prefix | Use for |
|------|--------|---------|
| feature | `feature/` | New functionality |
| feat | `feature/` | Alias for feature |
| fix | `fix/` | Bug fixes |
| bug | `fix/` | Alias for fix |
| hotfix | `hotfix/` | Urgent production fixes |
| docs | `docs/` | Documentation changes |
| refactor | `refactor/` | Code restructuring |
| chore | `chore/` | Maintenance, deps, config |
| ci | `ci/` | CI/CD changes |
| test | `test/` | Adding or fixing tests |
| perf | `perf/` | Performance improvements |

## Process

1. Parse the arguments. If no arguments provided, ask the user what type of branch and a short description.

2. Map the type to the correct prefix (handling aliases like `bug` -> `fix/`).

3. Format the description:
   - Lowercase
   - Replace spaces with hyphens
   - Remove special characters
   - Keep it concise (max 50 chars)

4. Construct the branch name: `<prefix><description>`
   Examples:
   - `feature/user-authentication`
   - `fix/login-redirect-loop`
   - `docs/api-reference`
   - `chore/update-dependencies`

5. Check that the branch doesn't already exist.

6. Create and checkout the branch from the current HEAD:
   ```
   git checkout -b <branch-name>
   ```

7. Confirm to the user: print the branch name and what it was created from.

## Rules

- If the type is not recognized, show the table above and ask the user to pick one.
- If already on a non-main/non-master branch, warn the user and ask if they want to branch from the current branch or from main/master.
- Never force-delete or overwrite existing branches.
