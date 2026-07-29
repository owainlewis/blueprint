---
name: milestone
description: "Completes every open issue in a GitHub milestone. Takes one issue at a time to a tested and reviewed pull request. Use when the user asks to finish or deliver a milestone."
user-invocable: true
argument-hint: "<GitHub milestone URL or name>"
---

# Milestone

Finish every open issue in a GitHub milestone.

## Workflow

1. **Read the milestone**
   - Resolve the repository and milestone.
   - Inspect its open issues, dependencies, linked pull requests, checks, and current project state.

2. **Order the work**
   - Order open issues by dependency, risk, and review cost.
   - Put blockers, bugs, and shared foundations before work that depends on them.

3. **Deliver one issue**
   - Use `/task-to-pr` to take one issue to a ready pull request.
   - Resume a matching pull request instead of creating another one.
   - Keep one branch and pull request per issue unless separate issues must ship together to work.

4. **Stop for merge**
   - Stop after each ready pull request unless the user allowed merging for this run.
   - When merging is allowed, merge only when the pull request is mergeable, required checks pass or are unconfigured, current comments are handled, no required change remains, and the description and checklist match the final commit.

5. **Refresh and repeat**
   - Sync the latest remote default branch.
   - Refresh the milestone before choosing the next issue.
   - Record pull request links, proof, blockers, and final state in the tracker when access permits.

6. **Report**
   - List completed issues, merged and open pull requests, blockers, checks, and anything not verified.

## Rules

- Work only on issues in the milestone.
- Do not batch unrelated issues.
- Explain why issues must be combined before starting combined work.
- Never merge without explicit permission.
- Do not merge with missing acceptance criteria.
- Do not merge with unverified acceptance criteria or affected failure paths unless the user accepts the evidence gap.
- Stop when an issue has unresolved product or technical decisions, requires missing secrets or permissions, already has conflicting work, or grows beyond its acceptance criteria.
