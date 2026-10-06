# One CRM project, one complete feature

A [consulting CRM](consulting-crm/REQUIREMENTS.md) gives a small firm a shared
sales pipeline and a clear next action for each potential client. The example
shows relationships, permissions, atomic writes, safe retries, and date rules
without adding email sync or sales automation.

Read in this order:

1. [Requirements](consulting-crm/REQUIREMENTS.md): users, journey, scope, and observable product rules.
2. [Architecture](consulting-crm/ARCHITECTURE.md): intended components, data flow diagram, data model, invariants, and tradeoffs.
3. [Capture lead spec](consulting-crm/docs/capture-lead/spec.md): sign-in, lead capture, pipeline, and the first follow-up, with contracts and acceptance checks.
4. The sample plan below: two usable slices of that feature, each suitable for a focused PR.

No CRM application is implemented in Blueprint. These are proposed teaching
documents, not evidence that the feature's checks pass. In its application repo,
`REQUIREMENTS.md` and `ARCHITECTURE.md` would live at the root. They stay current;
the feature spec retains decisions and delivery proof.

## Sample plan

This illustrates the output of `/plan`, normally returned in chat or published
as requested tracker tickets. It is included here to explain the example, not
to introduce a separate plan-document convention. Both tasks use the
[capture lead spec](consulting-crm/docs/capture-lead/spec.md) as their source.
Before real delivery, pin the source links to the reviewed commit.

### Milestone: capture a client and its next sales action

A consultant can sign in, capture a lead, and assign a follow-up that appears
when due. A colleague sees the same records; another firm's member cannot.

Depends on both tasks below, in order. Acceptance: run the spec's full browser
journey and AC-1 through AC-9, including lost-response retry and workspace
isolation. This milestone delivers working sales behavior across UI, server,
and storage, rather than separate database and frontend phases.

### Task 1: capture a lead and find it in the pipeline

#### What are we building?

A consultant can sign in, record a potential client, and find the saved
opportunity in a shared pipeline. Opening it shows the company, contact, owner,
and creation history. This is a usable result even before follow-ups exist.

#### Why?

The firm can stop losing client details across private notes. Colleagues can
see the same lead and know who owns the conversation.

#### Done when

- Provisioned members can sign in and out; outsiders cannot join automatically.
- Capturing a lead saves the company, contact, opportunity, and creation activity together. Invalid input saves nothing.
- Reloading the pipeline shows the saved lead and its details. Empty results and failed reads look different.
- Retrying after a lost response creates one lead. Reusing its key with changed values returns a conflict.
- Another workspace cannot read the lead, even with its ID. Stored text displays safely.

#### How to check

In the application repo, implement AC-1 through AC-5, the capture/read parts
of AC-6, and the lead-capture parts of AC-8 and AC-9. Run PostgreSQL integration tests for constraints, rollback,
concurrent retries, and scoped reads. In a real browser, sign in, capture,
reload, open the opportunity, sign out, and repeat with another workspace.
Check keyboard access, field errors, retained values, and a narrow mobile view.
Record runnable commands and results once the app exists.

#### Agent notes

- Depends on: None.
- Source: [capture lead spec](consulting-crm/docs/capture-lead/spec.md), through capture and read behavior.
- Own the first schema migration, identity/session integration, and shared submission-key contract. Include operator provisioning instructions; do not assume a login shell exists.
- Cover REQ-1 through REQ-3 and REQ-7, and INV-1 through INV-4 for capture. The full architecture describes follow-ups, but this task need not create those tables yet.
- Show creation history in opportunity details; omit follow-up controls until task 2.

#### Out of scope

Follow-up scheduling, stage editing, manual notes, imports, and selecting an
existing company. Do not introduce generic workflow engines or services.

### Task 2: schedule a follow-up and see it when due

#### What are we building?

A consultant can assign a next action from an opportunity to themselves or a
colleague, with a due date. The opportunity shows the saved action, and the
shared due list shows it on that date or later.

#### Why?

A captured lead now has an owner for its next action. The team can prepare for
the day without searching every opportunity or maintaining separate reminders.

#### Done when

- The form lists active members of the current workspace and defaults to the current member.
- Saving writes one follow-up and one scheduling activity together, and refreshing shows the saved item.
- The due list includes open items due today or earlier in the workspace's time zone, ordered as the spec requires.
- Invalid dates, summaries, or assignees produce useful errors without changing records.
- Lost-response and concurrent retries create one follow-up and activity. Denied requests, failed commits, and assignment racing deactivation respect the architecture's rules.

#### How to check

Implement AC-7 and the follow-up parts of AC-6, AC-8, and AC-9. Use PostgreSQL
tests for relationships, rollback, retry conflicts, concurrent requests, and
membership locking. Check dates just before and after workspace midnight and
across daylight-saving changes. In a real browser, capture a lead, assign a
follow-up, reload, inspect its opportunity, and open the due list. Use a second
workspace to prove guessed IDs cannot disclose records. Run task 1's regression
checks as well. Record exact commands when implemented.

#### Agent notes

- Depends on: Task 1, with an open, independently approved PR and no known blocker before stacking; update the base after it merges.
- Source: [capture lead spec](consulting-crm/docs/capture-lead/spec.md), scheduling and due-list behavior.
- Reuse task 1's identity, workspace access, and submission-key contracts. Add an additive migration for follow-ups and the due-list index.
- Cover REQ-4 and REQ-7, and INV-1, INV-3, and INV-4. Do not reinterpret a calendar date as midnight UTC.

#### Out of scope

Completing follow-ups, sending notifications, recurrence, and changing sales
stages. These need later feature specs, not extra tasks hidden in this one.

## Try the workflow

Ask `/requirements` to define this product, `/architecture` to design the
system, and `/spec` to settle capture and follow-up behavior. Review consequential
choices with `/architecture-review`. Use `/plan` when the feature benefits from
several delivery tasks. Compare the decisions and proof with this example,
rather than matching its wording.

In a real application repo, give the spec or a planned task to `/task-to-pr` for
a passing open PR. Explicit `/factory` use adds merging after all gates pass.
Do not ask either skill to implement the CRM inside Blueprint.
