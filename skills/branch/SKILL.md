---
name: branch
description: "Create and checkout a new git branch using conventional naming. Use when starting work on a new feature, bug fix, or task."
user-invocable: true
argument-hint: "<type> <short-description> e.g. 'feature user-auth' or 'fix login-redirect'"
---

# Git Branch

Create and checkout a new git branch following conventional naming conventions.

## Input

The user provides: `$ARGUMENTS`

This should be in the format: `<type> <description>`

## Process

1. Parse the arguments. If no arguments provided, ask the user what type and a short description.
2. Map the type to a conventional branch prefix (`feature/`, `fix/`, `hotfix/`, `docs/`, `refactor/`, `chore/`, `ci/`, `test/`, `perf/`). Handle common aliases (`feat` → `feature/`, `bug` → `fix/`).
3. Format: lowercase, hyphens for spaces, no special characters, max 50 chars.
4. Check the branch doesn't already exist. Create and checkout: `git checkout -b <branch-name>`
5. Confirm: print the branch name and what it was created from.

## Rules

- If already on a non-main/non-master branch, warn the user and ask where to branch from.
- Never force-delete or overwrite existing branches.
