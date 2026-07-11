# Chapter 6 — Milestones

## Overview

A milestone groups related Issues and Pull Requests under a shared goal with a due date.
Milestones answer the question: *"What must be done before the paper is submitted?"*

They are the primary tool for deadline-driven planning in the group.

---

## What Is a Milestone?

A milestone has:

- A **title** (the goal)
- An optional **description** (what done looks like)
- A **due date**
- A **progress bar** that fills as issues and PRs in the milestone are closed

Unlike labels (which categorise individual items) or project boards (which visualise
current work state), milestones link work to **outcomes with deadlines**.

---

## When to Create a Milestone

Create a milestone for:

| Trigger | Example milestone title |
|---------|------------------------|
| Paper submission | `paper-PRD-2026` |
| Conference deadline | `conference-Lattice-2026` |
| Code release | `v1.0.0` |
| Major internal feature | `thermal-potential-module` |

Do **not** create milestones for vague goals without deadlines.
A milestone without a due date is just a label with extra steps.

---

## Naming Convention

| Context | Format | Example |
|---------|--------|---------|
| Paper submission | `paper-JOURNAL-YEAR` | `paper-PRD-2026` |
| Conference | `conference-NAME-YEAR` | `conference-Lattice-2026` |
| Version release | `vMAJOR.MINOR.PATCH` | `v1.0.0` |
| Major feature | descriptive phrase | `thermal-potential-module` |

---

## Creating a Milestone

1. **Issues → Milestones → New milestone**
2. Fill in:
   - **Title:** following the naming convention above
   - **Due date:** the actual deadline (paper submission date, conference deadline, etc.)
   - **Description:** what "done" looks like (optional but recommended)
3. Click **Create milestone**

---

## Assigning Issues and PRs to Milestones

When opening or editing an Issue or PR:

- Right sidebar → **Milestone** → select the appropriate milestone

For batch assignment:

- **Issues** → check multiple issues → **Milestone** dropdown

**Policy:** Every issue and PR that must be completed before a deadline
should be assigned to the corresponding milestone. If an item does not belong
to any current milestone, it goes in the backlog (no milestone assigned).

---

## Using the Milestone Progress Bar

Navigate to **Issues → Milestones** to see all milestones and their completion percentage.

The progress bar shows `X of Y issues/PRs closed`.

Use this in group meetings to communicate:

- How much remains before the deadline
- Which items are blocking progress
- Whether the deadline is realistic

---

## Closing a Milestone

When all issues in a milestone are closed (or the deadline has passed):

1. **Issues → Milestones → [Milestone name] → Close milestone**

Closed milestones are archived and remain visible for historical reference.
Do not delete them — they are part of the project record.

---

## Milestones vs Project Boards

| | Milestones | Project Boards |
|--|-----------|----------------|
| Purpose | Track progress toward a deadline | Visualise current work state |
| Dimension | Time (when must this be done?) | State (what is being done now?) |
| Best for | Paper submissions, releases | Sprint planning, daily work |
| Update frequency | When items open/close | Weekly or daily |

Use both together: assign items to a milestone *and* to the project board column.

---

## Checklist

- [ ] Milestones created for all upcoming deadlines (papers, conferences, releases)
- [ ] Due dates set accurately
- [ ] All relevant issues and PRs assigned to milestones
- [ ] Milestone progress reviewed in group meetings
- [ ] Completed milestones closed (not deleted)
