# Consulting CRM requirements

Status: Proposed. This is a teaching example. No CRM is implemented here.

## Problem and users

A small consulting firm has no single place to track potential clients and the
next sales action, so follow-ups get missed and weekly sales reviews take
guesswork. This is an invented teaching brief, not customer research. Before
building a real product, observe how consultants record leads and prepare for
sales reviews, and confirm that missed follow-ups are a real problem.

- **Consultant:** records leads, calls, and follow-ups.
- **Firm owner:** reviews open opportunities to see what needs attention.
- **Operator:** provisions workspace membership. There is no public signup.

A workspace is one firm's shared CRM. Every member can read and change its
sales records.

A typical journey: Maya meets a potential client at an event. She records Acme
Ltd, its contact Sam, and an opportunity called "Website refresh", and assigns
herself a follow-up for Friday. A colleague can open the opportunity and see who
the client is and what happens next. Maya later records a call, moves the
opportunity to proposal, and eventually marks it won or lost.

## User stories

### REQ-1: Sign in to my firm's workspace

As a consultant, I want to sign in and see only my firm's records, so that our
clients stay private.

Done when:
- A provisioned member signs in and sees only their workspace.
- A non-member cannot read or change the workspace's records, even with their IDs.

### REQ-2: Capture a new lead

As a consultant, I want to record a company, its contact, and an opportunity in
one step, so that I can log a lead while the conversation is fresh.

Done when:
- The company, contact, and opportunity appear together, or none are saved.
- The opportunity starts at the lead stage and belongs to the consultant who created it.

### REQ-3: See the pipeline

As a firm owner, I want to see opportunities grouped by stage, so that I can run
the weekly sales review from one screen.

Done when:
- Each opportunity shows its company, contact, and owner under its stage.
- A member can open an opportunity to see its details.

### REQ-4: Schedule and see follow-ups

As a consultant, I want to assign a dated follow-up to a colleague or myself and
see what is due, so that no client is forgotten.

Done when:
- A follow-up can be assigned only to an active member of the same workspace.
- Members see open follow-ups due today or earlier, using the workspace's time zone.

### REQ-5: Move opportunities and record activity

As a consultant, I want to move an opportunity between stages and record notes
or calls, so that colleagues know where each deal stands.

Done when:
- Opportunities move between the five fixed stages: lead, qualified, proposal, won, and lost.
- The history shows who made each change and when.

### REQ-6: Complete a follow-up

As a consultant, I want to mark a follow-up done, so that the due list shows only
open work.

Done when:
- A completed follow-up leaves the due list.
- Completing it again does not create another change.

### REQ-7: Fail safely

As a consultant, I want a failed or repeated save to leave my records correct,
so that I can retry without creating a mess.

Done when:
- Invalid input, denied access, and failed writes leave records unchanged.
- Retrying a lead submission after a lost response does not create a second lead.

## Business rules

- A person outside a workspace never sees its records.
- Titles and names are plain text, trimmed, and 1 to 120 characters. Contact email is optional.
- Similar company names are allowed. The system never silently merges two businesses that share a name.
- A person has one active workspace in this first version.

## Constraints

- Works in desktop and mobile browsers.
- Personal contact information never appears in diagnostic logs.
- Production capacity, recovery targets, and budget need agreement before a real deployment.

## Out of scope

Email sync, notifications, imports, billing, AI scoring, custom stages, member
administration screens, and workspace switching.

## Success measures

For a real pilot: can the team prepare its weekly pipeline review from the CRM,
and are fewer follow-ups missed? Baselines and targets need customer evidence.
There is no invented adoption or revenue target here.

## Open decisions

None for the teaching example. Production operating targets are deployment
inputs and do not block the design.
