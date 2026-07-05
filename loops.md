# Goal Ideas For Blueprint

This document collects high-quality ways to use `/goal` to improve Blueprint itself.

It is intentionally short.

Most useful agent work should still be a normal prompt, a Blueprint skill, or a scheduled loop.

`/goal` is for the cases where Codex should keep checking a completion condition and continue without a new human prompt.

## Prompt, Goal, Or Loop

Use this rule before reaching for `/goal`.

| Primitive | Use When | Blueprint Example |
| --- | --- | --- |
| Prompt | One bounded pass is enough. | "Review the README and list unclear sections." |
| Goal | The agent should keep repairing and re-checking until a condition is true, blocked, or budget-limited. | "Make README, AGENTS, CLAUDE, guides, and skills agree on the installed skill set." |
| Scheduled loop | The trigger is time or external state. | "Every Friday, check for docs drift and report findings." |
| Issue-tracker loop | Labels, comments, PRs, and assignments are the state machine. | "Claim one `agent:ready` issue and run `task-to-pr`." |
| Skill invocation | Blueprint already has the workflow. | Use `review`, `task-to-pr`, `multitask`, `pr-to-ready`, or `goal-design` directly. |

A goal makes sense when the valuable part is the repeated self-check:

```text
Is the condition true yet?
If not, what is the next safe bounded action?
If continuing is unclear or unsafe, what proof should be reported?
```

If the task does not need that loop, it is probably just a prompt.

## Goal Template

```text
/goal
Use <skill or workflow> to <specific outcome>.

Do not stop until the outcome is proven or the work is genuinely blocked with proof.

Before changing anything, read <files, tools, and state>.

Keep the work scoped to <boundary>.

Run <specific checks> after each pass.

Fix valid failures and repeat until verification is clean.

Report <required proof>.

Stop and ask if <blocked condition>, repeated failure, or scope expansion occurs.

Do not <hard limits>.
```

Good goals include:

- a concrete end state
- a verifier the agent can actually run
- one bounded action per pass
- scope boundaries
- a human-decision stop
- a budget or repeated-failure stop

## Recommended Goals

These are tangible goals that should improve this repository.

They are written as prompts you can paste into Codex.

### 1. Documentation Consistency Repair

Use this when README, AGENTS, CLAUDE, guides, and skill files may describe different workflows.

This is a real goal because the agent must find a mismatch, patch it, re-scan, and continue until no unexplained contradictions remain.

```text
/goal
Make Blueprint's public workflow docs agree with each other.

Do not stop until the docs use the same skill names, workflow names, loop phases, and install guidance, or the work is blocked with proof.

Before changing anything, read README.md, AGENTS.md, CLAUDE.md, guides/*.md, skills/*/SKILL.md, and agents/code-reviewer.md.

Run targeted `rg` scans to find stale names or mismatched workflow descriptions.

Fix one real contradiction at a time.

Patch only the doc that owns the mistake.

Preserve current skill names and public workflow intent.

After each fix, re-run the relevant scan.

Stop and ask Owain if you have made 6 patches, the same mismatch repeats twice, or resolving a contradiction would change the intended product direction.

The final report must list changed files and scans run.

Do not edit generated files, examples, lockfiles, vendored files, or unrelated prose.

Do not rename skills or workflows.
```

Good verification scans:

```bash
rg "goal-skill|loop-design|task-to-pr|multitask|pr-to-ready|address-pr-feedback|codex-run-loop" README.md AGENTS.md CLAUDE.md guides skills
rg "agent:ready|agent:working|agent:complete|needs:spec|needs:human|blocked" AGENTS.md guides
```

### 2. Skill Quality Repair

Use this when the skill set has drifted from Blueprint's own quality bar.

This is a real goal because the agent works one skill at a time, patches only clear failures, and re-checks each changed skill before moving on.

```text
/goal
Check that every skill file meets Blueprint's review bar.

Do not stop until every skill is marked pass, patched, or needs-human.

Before changing anything, read REVIEW.md, AGENTS.md, and skills/*/SKILL.md.

For each skill, check trigger clarity, scope boundary, proof, failure behavior, and unnecessary ceremony.

Patch one skill only when the fix is clear and behavior-preserving.

Keep skills short and portable.

Re-read the changed skill before continuing.

Mark the inspected skill as pass, patched, or needs-human.

Stop and ask if you have made 5 skill patches, a skill's intended behavior is unclear, or making a skill shorter would weaken safety.

The final report must list checks run.

Do not change skill names, public workflow rules, generated files, or examples.
```

### 3. Skill Metadata Normalizer

Use this when installed skills need predictable frontmatter for discovery.

This is a good goal because the verifier is concrete and the agent can keep normalizing until every skill matches the schema or an intentional exception appears.

```text
/goal
Make every skill in skills/*/SKILL.md use the same required frontmatter fields.

Do not stop until a parser or explicit scan confirms every skill has the required fields in the expected order, or the work is blocked with proof.

Use skills/*/SKILL.md only.

Check for `name`, `description`, `user-invocable`, and `argument-hint`.

Fix one skill's frontmatter at a time.

Keep the fields consistently ordered.

After each fix, re-run the metadata check.

Stop and ask if you have made 10 skill patches or a skill intentionally needs a different schema.

The final report must list files changed and the command or scan used.

Do not rewrite skill bodies except where a field value needs a clearer description.

Do not change skill names or public trigger behavior.
```

Useful verification:

```bash
rg -n "^(name|description|user-invocable|argument-hint):" skills/*/SKILL.md
```

### 4. Markdown Link Repair

Use this when local docs have drifted after file renames or guide changes.

This is a real goal because link repair is naturally iterative: check, fix one class of broken links, check again.

```text
/goal
Make all local Markdown links resolve in Blueprint's repo-authored docs.

Do not stop until all local Markdown links resolve, or blocked links are reported with proof.

Use repo-authored Markdown only.

Check README.md, AGENTS.md, CLAUDE.md, REVIEW.md, guides/*.md, and skills/*/SKILL.md.

Fix one broken local link or stale path at a time.

Patch the source that owns the broken link.

After each fix, re-run the link check or documented fallback scan.

Stop and ask if you have made 8 link fixes or a target appears intentionally future-facing.

The final report must list the checker used, fixed links, skipped links, and any needs-human target.

Do not validate external URLs unless network access and policy are explicit.

Do not edit generated files or examples unless the broken link is in the source of truth.
```

### 5. Example Artifact Boundary Repair

Use this when examples and docs are unclear about what is source material, generated output, or hand-editable guidance.

This is a real goal because the agent may need to inspect several files, patch one boundary explanation, and re-check that the docs no longer contradict each other.

```text
/goal
Make Blueprint's example artifact boundaries clear and consistent.

Do not stop until the docs distinguish source prompts, regeneration scripts, generated examples, and hand-edited examples without contradiction, or the work is blocked with proof.

Read README.md, AGENTS.md, guides/*.md, examples/input.md, examples/regenerate.sh, examples/rag-chatbot/*.md, and examples/dispatch-control-plane/*.md.

Look for how docs describe source prompts, regeneration scripts, generated examples, and hand-edited examples.

Fix one unclear or contradictory boundary at a time.

Patch the doc that owns the unclear wording.

After each fix, re-scan for references to generated examples, regeneration scripts, and no-edit policy.

Stop and ask if the intended source of truth cannot be inferred from the repo.

The final report must list boundary rules, files changed, scans run, and any needs-human decision.

Do not regenerate examples.

Do not edit generated examples unless the repo already treats them as hand-edited sources.
```

### 6. Release Dry-Run Repair

Use this before tagging a Blueprint release.

This is a goal because release readiness often reveals a sequence of small blockers, and the agent should repair clear local blockers while stopping before publish authority.

```text
/goal
Check whether Blueprint is locally ready for a release dry run.

Do not stop until the final report says ready or not ready.

Use git status, git diff, README.md, AGENTS.md, CLAUDE.md, guides/*.md, skills/*/SKILL.md, agents/code-reviewer.md, and examples/.

Check changed skills, docs consistency, example boundaries, install manifest expectations, and unresolved risks.

Fix one clear local release blocker at a time.

Keep the work local.

After each fix, run the relevant check and update the release-readiness proof.

Stop and ask if you have made 5 fixes, publish tooling or network access is required, or release policy needs human approval.

The final report must cover fixes made, checks run, unresolved risks, and the exact human decision needed before release.

Do not tag, publish, push, edit lockfiles, or change generated files.

Do not invent a changelog if the repo prefers generated release notes.
```

### 7. Working Tree Reviewability Repair

Use this when the repo has several local changes and you want it made reviewable without losing human work.

This is a goal because the agent must inspect current state, group changes, fix only safe inconsistencies, and stop rather than discard unrelated work.

```text
/goal
Make the working tree reviewable without losing human work.

Do not stop until every remaining changed file is explained as intended, unrelated, generated, blocked, or needs-human.

Use `git status --short`, git diff, repo instructions, and touched files only.

Inspect one changed-file group at a time.

Fix only clear inconsistencies inside that group.

After each fix, run `git status --short` and update the reviewability report.

Stop and ask if you have made 4 repair patches or a change belongs to another human task.

The final report must list groups, files touched, checks run, and what should happen next.

Never discard, revert, reset, checkout, or overwrite user changes.

Do not stage, commit, push, or edit unrelated files.
```

## Adjacent Non-Goals

These are useful, but they are not good `/goal` examples.

Keep them out of the goal demo set.

### Good Prompts

Use normal prompts for one-pass work:

- create a repo map
- write a release notes draft
- inventory runnable checks
- audit public claims
- write a quickstart
- compare Claude, Codex, and Hermes docs
- draft a video or blog outline

These can still be excellent prompts.

They just do not need persistent continuation.

### Good Scheduled Loops

Use Codex Automations, thread wakeups, GitHub Actions, cron, or another scheduler when time or external state is the trigger:

- weekly maintenance sweep
- PR feedback watcher
- stale claim recovery
- post-release verification
- daily low-risk fixer

The prompt inside the scheduled loop can call `pr-to-ready`, `task-to-pr`, or another skill.

The schedule owns the wakeup.

The goal should not sit there pretending to be a timer.

### Good Skill Invocations

Use the skill directly when Blueprint already has the workflow:

- `task-to-pr` for one ready ticket
- `multitask` for several independent tickets
- `pr-to-ready` for an open PR with feedback
- `review` for a release diff
- `goal-design` for writing a precise `/goal` prompt

Wrapping these in `/goal` is only useful when a coordinator must repeat the skill until a larger condition is true.

## Recommended Order

Start with goals that touch docs only.

1. Documentation Consistency Repair.
2. Skill Metadata Normalizer.
3. Skill Quality Repair.
4. Markdown Link Repair.
5. Example Artifact Boundary Repair.
6. Working Tree Reviewability Repair.
7. Release Dry-Run Repair.

That order moves from low-risk, mechanical cleanup toward broader release judgment.

It also demonstrates the real value of `/goal`: repeated repair against proof, not a long prompt with a slash command.
