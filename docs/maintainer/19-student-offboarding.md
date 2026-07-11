# Chapter 19 — Student Offboarding

## Overview

When a student leaves the group — through graduation, end of exchange,
or any other departure — their access must be cleanly revoked and their
in-progress work must be properly handed off.

An unmanaged departure creates orphaned branches, stale PRs, undocumented code,
and knowledge gaps that slow the group for months.

---

## Timeline: Start Two Weeks Before Departure

Offboarding should not happen on the last day. Begin two weeks before
the student's final date.

| Timeline | Action |
|----------|--------|
| 2 weeks before | Identify all open work; assign handoff tasks |
| 1 week before | Complete handoff documentation; close or transfer all items |
| Last day | Revoke access; final knowledge transfer conversation |
| After departure | Archive student branches; verify backup |

---

## Step 1: Inventory Open Work

Find everything the student has open:

```bash
# List branches the student has pushed
git branch -r | grep -v HEAD

# On GitHub: filter Issues and PRs by assignee
```

For each open item, decide:

| Item type | Action |
|-----------|--------|
| Merged PR | Nothing to do |
| Open PR (reviewable) | Merge before departure or transfer to another author |
| Open PR (unfinished work) | Close with explanation; archive branch (see below) |
| Open Issue assigned to student | Reassign to maintainer or another student |
| Branch with uncommitted work | Student must commit and push before leaving |

---

## Step 2: Handoff Documentation

For any significant in-progress work, the departing student must write a handoff note.
This can be a comment on the relevant Issue or PR, or a short document in `docs/`:

The note must include:

- Current state of the work
- What has been done and what remains
- Any non-obvious context (numerical subtleties, failed approaches, physics assumptions)
- Any relevant papers or derivations not yet referenced in the code

This documentation is the student's last scientific contribution to the project.
Treat it seriously.

---

## Step 3: Archive Unmerged Branches

Branches that contain useful but unfinished work should be archived as tags
before being deleted:

```bash
# Tag the branch state for preservation
git tag archive/student-LASTNAME/feature-xyz feature/feature-xyz
git push origin archive/student-LASTNAME/feature-xyz

# Delete the branch from GitHub
git push origin --delete feature/feature-xyz

# Delete locally
git branch -d feature/feature-xyz
```

The tag `archive/student-LASTNAME/feature-xyz` is a permanent record
that can be retrieved if the work is resumed later.

---

## Step 4: Verify All Work Is Pushed

Ensure no work exists only on the student's local machine:

```bash
# Student runs this on their machine:
git push --all origin
git push --tags origin
```

Verify on GitHub that all expected branches and tags are present.

---

## Step 5: Final Knowledge Transfer

Before access is revoked, have a 30-minute conversation covering:

- Status of all in-progress work
- Any domain knowledge not documented in the code
- Passwords or shared credentials that need to be rotated
- Any external collaborators the student was communicating with

Take notes. This conversation is the last opportunity to capture institutional knowledge.

---

## Step 6: Revoke Access

On the student's last day:

**For personal repository:**
Settings → Collaborators → [Student username] → Remove

**For organisation teams:**
Organisation Settings → Teams → [Team name] → Members → Remove [Student]

Revocation does not delete the student's commits, PRs, or issue comments.
Their contributions remain in the repository history permanently.
Their name will appear in `git log` forever — which is appropriate attribution.

---

## Step 7: Post-Departure

- Remove from GitHub repository collaborators (if not already done)
- Remove from group mailing lists and communication channels
- Optionally: add to an alumni list in the group README
- Rotate any shared credentials the student may have had access to

---

## Offboarding Checklist

### 2 Weeks Before

- [ ] All open PRs identified and action decided (merge, transfer, or close)
- [ ] All open Issues reassigned
- [ ] All active branches identified

### 1 Week Before

- [ ] In-progress branches committed and pushed
- [ ] Handoff documentation written for significant unfinished work
- [ ] Unmerged but valuable branches archived as tags

### Last Day

- [ ] All work pushed (`git push --all origin && git push --tags origin`)
- [ ] Knowledge transfer conversation completed and notes taken
- [ ] GitHub access revoked

### After Departure

- [ ] Student removed from communication channels
- [ ] Any shared credentials rotated
- [ ] Final backup created (git bundle)
- [ ] Repository reviewed for stale branches
