---
name: review
description: "Uses a fresh agent to review an implementation change without editing it. Checks behavior, security, regressions, complexity, tests, docs, and missing proof. Use for code, PR, diff, security, second-opinion, or pre-merge reviews."
user-invocable: true
argument-hint: "[diff, branch, commit, PR, or file path]"
---

# Review

The reviewer must be a fresh subagent that did not implement the change. Do not edit files or post comments.

## Scope

Review the implementation target named by the user. It may be a file, diff, branch, commit, pull request, or other code change on GitHub. Use `/architecture-review` for a technical proposal that has not been implemented.

If the user does not name a target, review the current repository's complete local change set: commits on the current branch relative to the repository's default branch, staged changes, unstaged changes, and untracked files. Use the repository and immediate surrounding code as context. If there are no local changes, say so instead of substituting a whole-repository audit.

## Standard

Approve only when:

- The change matches its source and behaves as required.
- No known defect or unhandled risk could break the source or repository rules for security, data loss, compatibility, or operations.
- No simpler design has been identified that delivers the same outcome and proof with less state, indirection, duplication, or operational work.

Do not demand perfection or block on personal taste. Cite technical evidence or repository conventions.

The verdict is independent agent evidence. It is not GitHub approval or a replacement for human review.

## Review order

1. **Set the frame.** Give the reviewer the task, acceptance criteria, repository rules, complete diff or pull request, and test evidence. Name the user or developer affected by the change.
2. **Take the broad view.** Read the change summary and the relevant design or ticket. Confirm that the change belongs in the system, matches the intended behavior, and delivers one reviewable outcome. Report a mismatch before reviewing details.
3. **Review the main behavior.** Start with the files and flows that deliver the outcome. Check behavior, failures, security boundaries, interfaces, compatibility, migrations, concurrency, and operations.
4. **Review every human-written changed line in context.** Read enough surrounding code to judge correctness, regressions, complexity, names, comments, style, and docs. For generated files or large data, inspect the source and spot-check the output. Keep findings within the change's scope.
5. **Review the proof.** Check that tests:
   - Cover the changed behavior and affected failure paths.
   - Prove the acceptance criteria.
   - Assert behavior a user or caller can observe, or a documented internal contract.
   - Would fail under a broken implementation.
   - Do not copy implementation logic or hide the scenario in setup.
6. Run focused checks that can confirm or disprove a claim that could change a finding or verdict.
7. **Check specialist coverage.** Identify security, privacy, concurrency, accessibility, internationalization, or domain-specific work. Mark a risk unverified when the reviewer lacks the evidence or skill to judge it. Use `Blocked` when that gap could hide a problem that breaks a rule and no qualified reviewer covers it.
8. **Report findings.** Return actionable findings in priority order using the format below.

## Code review findings

For code, commit, branch, and pull request reviews, report only real bugs and customer-impacting issues introduced or exposed by the change. Check security, logic, behavior, reliability, compatibility, regressions, and affected failure paths. Inspect the immediate surrounding code needed to prove each finding.

Use this format for every finding:

```text
Priority: Must fix / Should fix / Could fix
Confidence: 0–5
What I found: Describe the technical problem.
Why it matters: Explain the impact on customers, callers, or the service.
ELI5: In one or two short sentences, state the exact condition that triggers the problem and what the customer or service experiences. Use no analogies, jargon, or acronyms.
Where: File and line.
Suggested fix: Give a short, practical direction.
```

Priority means:

- **Must fix:** Unsafe to merge. The change can cause a security failure, data loss, broken required behavior, or a serious service regression.
- **Should fix:** A real defect or reliability risk that should be corrected before merge.
- **Could fix:** A proven, limited problem that does not need to block merge. Do not use this for style preferences.

Confidence means:

- **5:** Confirmed by reproduction, test, or direct code evidence.
- **4:** Strong evidence with no credible alternative explanation.
- **3:** Probable, but some runtime evidence is unavailable.
- **0–2:** Do not report. Investigate further or mark the area unverified.

Write so the developer can quickly understand what is broken, who it affects, and why they should care. Be concise. Do not report style preferences, theoretical concerns, or problems outside the changed code and its immediate context.

## Verdict

If fresh subagents are unavailable, stop and report that independent review is blocked unless the user explicitly accepts a documented self-review.

If there are no findings, say so. End with `Approve`, `Request changes`, or `Blocked`, then state what remains unverified. A Must fix or Should fix finding requires `Request changes`. Could fix findings do not prevent `Approve`.

## Boundaries

- Keep findings within the change, but inspect enough surrounding code to judge each changed line and its system effect.
- Do not turn preferences into findings. Use technical evidence and repository conventions.
- Do not approve solely because checks pass.
