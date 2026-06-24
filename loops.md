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
| Skill invocation | Blueprint already has the workflow. | Use `review`, `task-to-pr`, `multitask`, `pr-to-ready`, or `loop-design` directly. |

A goal makes sense when the valuable part is the repeated self-check:

```text
Is the condition true yet?
If not, what is the next safe bounded action?
If continuing is unclear or unsafe, what evidence should be reported?
```

If the task does not need that loop, it is probably just a prompt.

## Goal Template

```text
/goal
Your job
<plain outcome>

Read first
<files, tools, and state to inspect before changing anything>

What you may do
<allowed actions and boundaries>
Preserve <constraints>.

After each pass
Run <specific checks>.
If the goal is not done, choose the next smallest safe action.

You are done when
<specific evidence> proves the outcome.

Stop and ask when
Blocked, repeated failures occur, or no valid paths remain.
Report <evidence gathered>, <blocker>, and <input needed>.

Do not
<hard limits>
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
Your job
Make Blueprint's public workflow docs agree with each other.
The docs should use the same skill names, workflow names, loop phases, and install guidance.

Read first
Read README.md, AGENTS.md, CLAUDE.md, guides/*.md, skills/*/SKILL.md, and agents/code-reviewer.md.
Run targeted `rg` scans to find stale names or mismatched workflow descriptions.

What you may do
Fix one real contradiction at a time.
Patch only the doc that owns the mistake.
Preserve current skill names and public workflow intent.

After each fix
Re-run the relevant scan.
Check whether the same mismatch still appears.
If another clear mismatch remains, fix the next smallest one.

You are done when
The scans show no unexplained mismatch in skill names, workflow names, loop phases, or install guidance.
The final report lists changed files and scans run.

Stop and ask Owain when
You have made 6 patches.
The same mismatch repeats twice.
Resolving a contradiction would change the intended product direction.

Do not
Do not edit generated files, examples, lockfiles, vendored files, or unrelated prose.
Do not rename skills or workflows.
Do not guess product direction.
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
Your job
Check that every skill file meets Blueprint's review bar.

Read first
Read REVIEW.md, AGENTS.md, and skills/*/SKILL.md.
For each skill, check trigger clarity, scope boundary, verification evidence, failure behavior, and unnecessary ceremony.

What you may do
Patch one skill only when the fix is clear and behavior-preserving.
Keep skills short and portable.

After each pass
Re-read the changed skill before continuing.
Mark the inspected skill as pass, patched, or needs-human.

You are done when
Every inspected skill has a pass, patched, or needs-human result.
The final report lists checks run.

Stop and ask when
You have made 5 skill patches.
A skill's intended contract is ambiguous.
Making a skill shorter would weaken safety.

Do not
Do not change skill names, public workflow contracts, generated files, or examples.
```

### 3. Skill Metadata Normalizer

Use this when installed skills need predictable frontmatter for discovery.

This is a good goal because the verifier is concrete and the agent can keep normalizing until every skill matches the schema or an intentional exception appears.

```text
/goal
Your job
Make every skill in skills/*/SKILL.md use the same required frontmatter fields.

Read first
Use skills/*/SKILL.md only.
Check for `name`, `description`, `user-invocable`, and `argument-hint`.

What you may do
Fix one skill's frontmatter at a time.
Keep the fields consistently ordered.

After each fix
Re-run the metadata check.

You are done when
A parser or explicit scan confirms every skill has the required fields in the expected order.
The final report lists files changed and the command or scan used.

Stop and ask when
You have made 10 skill patches.
A skill intentionally needs a different schema.

Do not
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
Your job
Make all local Markdown links resolve in Blueprint's repo-authored docs.

Read first
Use README.md, AGENTS.md, CLAUDE.md, REVIEW.md, guides/*.md, and skills/*/SKILL.md.
Use repo-authored Markdown only.

What you may do
Fix one broken local link or stale path at a time.
Patch the source that owns the broken link.

After each fix
Re-run the link check or documented fallback scan.

You are done when
All local Markdown links resolve.
The final report lists the checker used, fixed links, skipped links, and any needs-human target.

Stop and ask when
You have made 8 link fixes.
A target appears intentionally future-facing.

Do not
Do not validate external URLs unless network access and policy are explicit.
Do not edit generated files or examples unless the broken link is in the source of truth.
```

### 5. Example Artifact Boundary Repair

Use this when examples and docs are unclear about what is source material, generated output, or hand-editable guidance.

This is a real goal because the agent may need to inspect several files, patch one boundary explanation, and re-check that the docs no longer contradict each other.

```text
/goal
Your job
Make Blueprint's example artifact boundaries clear and consistent.

Read first
Use README.md, AGENTS.md, guides/*.md, examples/input.md, examples/regenerate.sh, examples/rag-chatbot/*.md, and examples/dispatch-control-plane/*.md.
Look for how docs describe source prompts, regeneration scripts, generated examples, and hand-edited examples.

What you may do
Fix one unclear or contradictory boundary at a time.
Patch the doc that owns the unclear wording.

After each fix
Re-scan for references to generated examples, regeneration scripts, and no-edit policy.

You are done when
The docs distinguish source prompts, regeneration scripts, generated examples, and hand-edited examples without contradiction.
The final report lists boundary rules, files changed, scans run, and any needs-human decision.

Stop and ask when
The intended source of truth cannot be inferred from the repo.

Do not
Do not regenerate examples.
Do not edit generated examples unless the repo already treats them as hand-edited sources.
```

### 6. Release Dry-Run Repair

Use this before tagging a Blueprint release.

This is a goal because release readiness often reveals a sequence of small blockers, and the agent should repair clear local blockers while stopping before publish authority.

```text
/goal
Your job
Check whether Blueprint is locally ready for a release dry run.

Read first
Use git status, git diff, README.md, AGENTS.md, CLAUDE.md, guides/*.md, skills/*/SKILL.md, agents/code-reviewer.md, and examples/.
Check changed skills, docs consistency, example boundaries, install manifest expectations, and unresolved risks.

What you may do
Fix one clear local release blocker at a time.
Keep the work local.

After each fix
Run the relevant check.
Update the release-readiness evidence.

You are done when
The final report says ready or not ready.
The report covers fixes made, checks run, unresolved risks, and the exact human decision needed before release.

Stop and ask when
You have made 5 fixes.
Publish tooling or network access is required.
Release policy needs human approval.

Do not
Do not tag, publish, push, edit lockfiles, or change generated files.
Do not invent a changelog if the repo prefers generated release notes.
```

### 7. Working Tree Reviewability Repair

Use this when the repo has several local changes and you want it made reviewable without losing human work.

This is a goal because the agent must inspect current state, group changes, fix only safe inconsistencies, and stop rather than discard unrelated work.

```text
/goal
Your job
Make the working tree reviewable without losing human work.

Read first
Use `git status --short`, git diff, repo instructions, and touched files only.

What you may do
Inspect one changed-file group at a time.
Fix only clear inconsistencies inside that group.

After each fix
Run `git status --short`.
Update the reviewability report.

You are done when
Every remaining changed file is explained as intended, unrelated, generated, blocked, or needs-human.
The final report lists groups, files touched, checks run, and what should happen next.

Stop and ask when
You have made 4 repair patches.
A change belongs to another human task.

Do not
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
- `loop-design` for designing a new loop

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

It also demonstrates the real value of `/goal`: repeated repair against evidence, not a long prompt with a slash command.
