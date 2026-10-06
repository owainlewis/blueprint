# Consulting CRM requirements

> Decision status: proposed teaching example. No CRM is implemented here.

## Product and users

A small consulting firm needs one place to track potential clients and the next
sales action. Consultants record leads and follow-ups. The firm owner reviews
open opportunities to see what needs attention.

A workspace is one firm's shared CRM. Members can read and change its sales
records. A person outside that workspace must never see those records.

## A typical journey

Maya meets a potential client at an event. She records Acme Ltd, its contact
Sam, and an opportunity called “Website refresh”. She assigns a follow-up to
herself for Friday. Another consultant can open the opportunity and understand
who the client is and what happens next. Maya later records a call, moves the
opportunity to proposal, and eventually marks it won or lost.

## Evidence and assumptions

This is an invented teaching brief, not customer research. It assumes a small
team needs shared ownership and reliable follow-ups more than automated sales
campaigns. Before building a real product, observe how consultants record leads
and prepare for weekly sales reviews. Confirm whether missed follow-ups are a
real problem and which information they need to act.

## Key features and scope

- Keep companies and their contacts together.
- Track opportunities through lead, qualified, proposal, won, and lost stages.
- Record notes and calls on an opportunity's activity history.
- Assign dated follow-ups and see which are due.
- Keep each firm's records private to its members.

The first feature captures a new lead, shows it in the pipeline, and schedules
its first follow-up. Later features add stage changes, manual activity notes,
and completing follow-ups. Email sync, notifications, imports, billing, AI
scoring, custom stages, and member administration screens are out of scope.

## Requirements

| ID | Required behavior |
|---|---|
| REQ-1 | A provisioned member signs in and sees only their workspace. Non-members cannot read or change its records. |
| REQ-2 | A member captures a company, contact, and opportunity together. They appear together or none are saved. The opportunity starts at lead and belongs to its creator. |
| REQ-3 | Members see opportunities grouped by stage, including company, contact, and owner. They can open one to see its details. |
| REQ-4 | A member assigns a follow-up to an active workspace member with a due date. Members see open follow-ups due today or earlier, using the workspace's time zone. |
| REQ-5 | Members can move opportunities between the five fixed stages and record notes or calls. The history identifies the actor and when the change happened. |
| REQ-6 | A member can complete an open follow-up. Repeating completion does not create another change. Completed items leave the due list. |
| REQ-7 | Invalid input, denied access, and failed writes leave records unchanged. Retrying a lead submission after a lost response must not create a second lead. |

Titles and names are plain text, trimmed, and must contain 1 to 120 characters.
Contact email is optional. Follow-up details and field-specific limits belong
in the feature spec. Similar company names are allowed; the system must not
silently merge records because two businesses share a name.

## Constraints and acceptance

Use the web app from a desktop or mobile browser. Personal contact information
must not appear in diagnostic logs. No public signup is needed: an operator
provisions workspace membership before access. A person has one active workspace
in this first version; workspace switching is outside scope.

Acceptance: Maya captures the lead, reloads, sees it in the pipeline, assigns a
Friday follow-up, and finds it on Friday's due list. A colleague can see the
same records; a member of another firm cannot access them even with their IDs.
Later features complete the journey through activity history and closing work.

## Success measures and open decisions

For a real pilot, assess whether the team can prepare its weekly pipeline review
from the CRM and whether fewer follow-ups are missed. Baselines and targets need
customer evidence. There is no invented adoption or revenue target here.

The teaching brief is settled. Production capacity, recovery targets, and budget
need agreement before a real deployment. They do not block designing the example.
