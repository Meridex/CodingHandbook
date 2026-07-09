# Chapter 18 — Student Onboarding

## Overview

A new student's first experience with the group's development process
shapes their habits for the rest of their time in the group.
Onboarding done well produces self-sufficient contributors within two weeks.
Onboarding done poorly produces students who are afraid of Git and work around it.

This chapter is a complete protocol for bringing a new student up to speed.

---

## Before the Student Arrives

Prepare the environment before the student's first day:

- [ ] Confirm the student's GitHub username (ask them to create one if needed)
- [ ] Create the student's collaborator invitation (Settings → Collaborators → Add people)
  - Permission level: **Write**
- [ ] Identify the first "good first issue" to assign them
- [ ] Have this handbook URL ready to share

---

## Day 1: Environment Setup (First 2 Hours)

Walk through these steps together or assign as self-study with a check-in:

1. **Share the handbook.** Direct the student to [Chapter 1](../student/01-introduction.md).
   Ask them to read Chapters 1–3 before the next step.

2. **Verify Git installation and configuration:**
   ```bash
   git --version        # should be 2.30+
   git config --global user.name
   git config --global user.email
   ```
   If not configured: work through [Chapter 4](../student/04-initial-setup.md) together.

3. **SSH key setup:**
   Walk through [Chapter 5](../student/05-ssh.md).
   Verify with: `ssh -T git@github.com`

4. **Accept collaborator invitation:**
   The student must accept the GitHub invitation email.
   Verify: Settings → Collaborators → confirm the student appears as "Active" (not "Pending").

5. **Clone the repository:**
   ```bash
   git clone git@github.com:ORG/REPO.git
   cd REPO
   git log --oneline -5
   ```

---

## Day 2–3: First Branch and Commit

Assign the first task: a "good first issue" labelled `good first issue`.

Walk through the daily workflow ([Chapter 7](../student/07-daily-workflow.md))
with the student. Have them:

1. `git pull origin main`
2. `git checkout -b docs/add-your-name` (or the actual first-issue branch)
3. Make a trivial change (add name to `CONTRIBUTORS.md`)
4. `git add`, `git diff --staged`, `git commit -m "..."`
5. `git push -u origin docs/add-your-name`
6. Open a Pull Request on GitHub using the template

---

## The First PR Review: A Teaching Moment

Review the student's first PR yourself, leaving **pedagogical comments**:
- Point out what they did well
- Explain (not just flag) any issues with commit message, PR description, etc.
- Approve and merge together so they see the full cycle

This first PR review sets the tone for the student's experience of code review.
Make it welcoming.

---

## Week 1–2: Completing the Exercises

Assign the handbook exercises ([Chapter 18 of the Student Guide](../student/18-exercises.md))
as structured onboarding work.

Track progress:

| Exercise | Status |
|----------|--------|
| 1.1 — Environment verified | |
| 1.2 — Repository cloned | |
| 2.1 — First branch and commit | |
| 2.2 — Atomic commits | |
| 3.2 — First PR opened | |
| 4.1 — Review received and responded to | |
| 5.1 — Branch rebased | |
| 6.1 — Conflict resolved | |

Check in daily during the first week. The expected timeline for a student to
become self-sufficient: **approximately 2 weeks**.

---

## Onboarding Checklist

- [ ] GitHub account created (use institute email)
- [ ] Collaborator invitation sent and accepted (Write permission)
- [ ] SSH key configured and tested (`ssh -T git@github.com`)
- [ ] Repository cloned successfully
- [ ] `git config user.name` and `user.email` set correctly
- [ ] First branch created
- [ ] First commit made (atomic, imperative message)
- [ ] First PR opened with complete template
- [ ] First PR reviewed and merged
- [ ] Student added to group communication channels (Slack/email)
- [ ] Student knows to check GitHub Issues for available tasks
- [ ] Handbook exercises assigned
- [ ] Student is aware of weekly group meeting / code review schedule

---

## Common Onboarding Failures

1. **"Just clone it and figure it out."**
   Students who are not walked through the first PR often develop incorrect habits
   that are hard to correct later.

2. **Assigning a complex first issue.**
   The first issue should be trivially easy — adding a name to a list,
   fixing a typo, updating a comment. The goal is to exercise the workflow,
   not the physics.

3. **Not reviewing the first PR carefully.**
   If the first PR is rubber-stamped without feedback, the student learns
   that the PR template is optional and commit messages do not matter.

4. **No follow-up check-in.**
   Schedule a 15-minute check-in on Day 3 to verify setup is working and
   answer questions. Students often run into SSH or Git config issues
   and do not ask for help.
