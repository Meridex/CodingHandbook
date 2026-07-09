# Chapter 7 — Project Board

## Overview

A GitHub Project board provides a visual overview of work in progress.
Where milestones answer *"What must be done by the deadline?"*, the project board
answers *"What is everyone working on right now?"*

---

## GitHub Projects (v2)

The group uses **GitHub Projects v2** (the table/board view, not the legacy
Projects v1 Kanban). Projects v2 is more flexible and supports filtering, grouping,
and custom fields.

Access: **Repository → Projects → Link a project** or create a new project
at the organisation level to span multiple repositories.

---

## Recommended Board Columns

Create a board with these four columns (status values):

| Column | Meaning |
|--------|---------|
| **Backlog** | Identified work; not yet started |
| **In Progress** | Currently being worked on (has an assignee and an open PR or branch) |
| **In Review** | PR is open and awaiting or under review |
| **Done** | Merged, closed, or resolved |

---

## Setting Up the Board

1. Navigate to the repository → **Projects → New project**
2. Select **Board** layout
3. Create the four columns listed above
4. Set the project title to match the repository or the current milestone

### Add Custom Fields

Add these fields to track status alongside the default title/assignee:

- **Milestone** (iteration field) — link to the GitHub milestone
- **Priority** — single select: High / Medium / Low
- **Type** — single select: Feature / Bugfix / Docs / Refactor / Chore

---

## Linking Issues and PRs to the Board

When creating an issue or PR:
- Right sidebar → **Projects** → select the board
- Set the **Status** field to the appropriate column

When work progresses, update the status:
- Created issue → **Backlog**
- Work started, branch created → **In Progress**
- PR opened → **In Review**
- PR merged or issue closed → **Done** (may be automated, see below)

---

## Automation

GitHub Projects v2 supports basic automation:

1. In the project, click **...** → **Settings → Workflows**
2. Enable:
   - **"Item added to project"** → set Status to **Backlog**
   - **"Item closed"** → set Status to **Done**
   - **"Pull request merged"** → set Status to **Done**

With these rules, closed issues and merged PRs move to **Done** automatically.
You only need to manually move items from Backlog → In Progress → In Review.

---

## Milestones vs Project Board: Working Together

| Use | Milestone | Board |
|-----|-----------|-------|
| Is this needed before the paper? | ✓ Assign to milestone | — |
| Is this being worked on this week? | — | ✓ Set to In Progress |
| Is this waiting for review? | — | ✓ Set to In Review |
| Is the deadline at risk? | ✓ Check milestone completion % | — |

In practice, every in-progress issue or PR should appear on the board
**and** be assigned to a milestone.

---

## Weekly Maintenance

Spend 10 minutes per week on board hygiene:

1. Review **In Progress** column: is everyone's status still accurate?
2. Review **In Review** column: are any PRs stale (open > 5 days without activity)?
3. Move newly merged PRs to **Done** if automation did not catch them.
4. Move new issues from the inbox to **Backlog** or assign them immediately.
5. Check milestone completion % against the remaining time.

---

## Checklist

- [ ] Project board created with four columns: Backlog / In Progress / In Review / Done
- [ ] Custom fields added: Milestone, Priority, Type
- [ ] Automation configured: item closed → Done, PR merged → Done
- [ ] All current open issues and PRs added to the board
- [ ] Board URL shared with all team members
- [ ] Weekly review habit established
