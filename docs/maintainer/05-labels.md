# Chapter 5 — Labels

## Overview

Labels categorise Issues and Pull Requests, making it easy to filter, sort,
and understand the state of work at a glance. Consistent labelling is a
low-effort, high-value practice.

---

## Default GitHub Labels

GitHub creates these labels automatically. Keep them or modify them:

| Label | Colour | Keep? |
|-------|--------|-------|
| `bug` | Red | Remove — use `type: bugfix` instead |
| `documentation` | Blue | Remove — use `type: docs` instead |
| `duplicate` | Grey | Keep |
| `enhancement` | Light blue | Remove — use `type: feature` instead |
| `good first issue` | Purple | Keep |
| `help wanted` | Green | Keep |
| `invalid` | Yellow | Keep |
| `question` | Pink | Keep |
| `wontfix` | White | Keep |

Delete the labels you are replacing to avoid confusion. Create the group-specific
labels below to standardise the language across all group repositories.

---

## Group-Specific Labels

Create these labels on every new repository. Use exactly these names and colours
for consistency across all group repositories.

### Type Labels

| Label | Hex Colour | Meaning |
|-------|-----------|---------|
| `type: feature` | `#0075ca` | New calculation, algorithm, or functionality |
| `type: bugfix` | `#d73a4a` | Incorrect result, crash, or unexpected behaviour |
| `type: docs` | `#cfd3d7` | Documentation only — no code change |
| `type: refactor` | `#e4e669` | Code restructuring without behaviour change |
| `type: experiment` | `#f9d0c4` | Exploratory work; may not be merged |
| `type: chore` | `#ededed` | Build system, CI, dependencies, tooling |

### Priority Labels

| Label | Hex Colour | Meaning |
|-------|-----------|---------|
| `priority: high` | `#b60205` | Urgent — blocking a paper deadline or CI |
| `priority: medium` | `#fbca04` | Normal priority |
| `priority: low` | `#0e8a16` | Can wait; not blocking anything |

### Status Labels

| Label | Hex Colour | Meaning |
|-------|-----------|---------|
| `status: needs-review` | `#fbca04` | Waiting for a reviewer to look at this |
| `status: in-progress` | `#0075ca` | Actively being worked on |
| `status: blocked` | `#e11d48` | Waiting on something external (data, decision, dependency) |
| `status: stale` | `#cccccc` | No activity for 30+ days; needs triage |

---

## Creating Labels

### Via GitHub UI

1. **Issues → Labels → New label**
2. Enter the name exactly as shown above.
3. Enter the hex colour code.
4. Click **Create label**.

Repeat for each label. This takes about 10 minutes per repository.

### Via GitHub CLI (faster for multiple repositories)

If you have the GitHub CLI (`gh`) installed:

```bash
gh label create "type: feature" --color "0075ca" --description "New calculation or functionality" --repo ORG/REPO
gh label create "type: bugfix" --color "d73a4a" --description "Incorrect result, crash, or bug" --repo ORG/REPO
gh label create "type: docs" --color "cfd3d7" --description "Documentation only" --repo ORG/REPO
gh label create "type: refactor" --color "e4e669" --description "Code restructuring, no behaviour change" --repo ORG/REPO
gh label create "type: experiment" --color "f9d0c4" --description "Exploratory; may not be merged" --repo ORG/REPO
gh label create "type: chore" --color "ededed" --description "Build, CI, tooling" --repo ORG/REPO
gh label create "priority: high" --color "b60205" --description "Urgent" --repo ORG/REPO
gh label create "priority: medium" --color "fbca04" --description "Normal priority" --repo ORG/REPO
gh label create "priority: low" --color "0e8a16" --description "Can wait" --repo ORG/REPO
gh label create "status: needs-review" --color "fbca04" --description "Waiting for reviewer" --repo ORG/REPO
gh label create "status: in-progress" --color "0075ca" --description "Actively being worked on" --repo ORG/REPO
gh label create "status: blocked" --color "e11d48" --description "Blocked on external dependency" --repo ORG/REPO
gh label create "status: stale" --color "cccccc" --description "No activity for 30+ days" --repo ORG/REPO
```

---

## Applying Labels Consistently

**Labels on Issues:**
- Apply `type:` label when creating the issue
- Apply `priority:` label if urgency is known
- Apply `status:` as work progresses

**Labels on Pull Requests:**
- Apply `type:` label to every PR (students should do this when opening the PR)
- Apply `priority: high` for urgent fixes
- Apply `status: needs-review` when the PR is ready for review
- Remove `status: needs-review` and add `status: stale` if the PR goes cold

**Periodic triage (recommended: weekly):**
- Review open issues and PRs without labels
- Apply `status: stale` to anything with no activity for 30+ days
- Prompt authors or close stale items

---

## Checklist

- [ ] Default GitHub labels reviewed and unnecessary ones deleted
- [ ] All `type:` labels created with correct colours
- [ ] All `priority:` labels created with correct colours
- [ ] All `status:` labels created with correct colours
- [ ] `good first issue` label kept and applied to suitable issues
- [ ] Students instructed to apply labels when opening PRs
