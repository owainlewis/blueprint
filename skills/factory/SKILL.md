---
name: factory
description: "Delivers a spec or decided task through the task-to-pr workflow and merges after all quality and approval gates pass. Explicit invocation grants merge authority for the supplied work."
user-invocable: true
argument-hint: "<spec, task, or GitHub issue>"
disable-model-invocation: true
---

# Factory

Use this skill only when the user explicitly selects it, or when an already selected Blueprint workflow requires its instructions. Do not select it from a general task match. For a required dependency, read its linked `SKILL.md` directly as part of the selected workflow; do not use a model-invoked skill command that the client blocks.

Deliver the supplied work through a verified merge.

Explicitly invoking `/factory` authorizes merging only the supplied work after
all gates pass. Automatic skill selection does not grant merge authority; leave
the PR open unless the user explicitly authorizes merging. Deployment and release
publication require separate authority.

## Process

1. Read the source and repository instructions. The spec is the ticket; reuse it rather than creating separate product and technical specs.
2. Follow [`/task-to-pr`](../task-to-pr/SKILL.md), including tests, fresh independent review, CI, and the full repair loop. Pass the scoped merge authority when it exists. Keep the same quality standard.
3. Use its merge gates. If a required approval, decision, or check is unavailable, report the blocker and leave the PR open. Never bypass a gate to finish unattended work.
4. Confirm the merge on GitHub and update the original issue when one exists. Follow `/task-to-pr` worktree cleanup rules.

## Return

Report the merged PR and proof, or the open PR and exact merge blocker.
