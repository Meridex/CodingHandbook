# 01 · Student Guide — Detailed Chapter Plan

Target audience: students with **zero** prior Git or GitHub knowledge.
Each chapter follows the standard page structure (Why / What / How / Mistakes / Checklist / Exercises).

---

## Chapter 1 — Introduction

**Goal:** Orient the student. Explain why version control matters for research.

### Sections
- Why does a physics research group need version control?
- What goes wrong without it? (story-style: "the nightmare of `final_v3_FINAL2.py`")
- What this handbook covers and what it does not.
- How to use this handbook.
- Glossary of terms used throughout (brief; full glossary in appendix).

### Key Points to Make
- Version control is a research tool, not just a programmer tool.
- Reproducibility of published results depends on it.
- The group uses one canonical workflow; there will be no "alternatives" presented.

---

## Chapter 2 — Git vs GitHub

**Goal:** Remove the common confusion between Git (the tool) and GitHub (the platform).

### Sections
- What is Git? (local version control system)
- What is GitHub? (remote hosting + collaboration platform)
- How they relate: local ↔ remote.
- Other platforms exist (GitLab, Bitbucket) but the group uses GitHub.
- Key vocabulary: repository, commit, branch, remote, clone, push, pull, fork.

### Diagrams
- Mermaid: local repo ↔ GitHub remote relationship.

---

## Chapter 3 — Development Workflow Overview

**Goal:** Show the big picture before diving into commands.

### Sections
- The canonical group workflow (full diagram).
- Protected `main` branch — why direct commits are forbidden.
- Feature branches — one branch per task.
- The Pull Request gate — peer review before merging.
- Squash merge — clean history on `main`.

### Diagrams
- Mermaid: full workflow flowchart (`main` → branch → PR → review → merge).
- Mermaid: branch graph showing feature branch lifetime.

---

## Chapter 4 — Initial Setup

**Goal:** Get the student's machine ready to work.

### Sections
- Install Git (macOS / Linux / Windows).
- Configure `user.name` and `user.email`.
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```
- Configure default editor.
- Configure default branch name to `main`.
- Verify installation with `git --version`.
- Create a GitHub account (if needed).
- GitHub profile settings (name, avatar — optional but recommended).

### Common Mistakes
- Using a personal email instead of the institute email.
- Skipping `user.email` configuration.
- Not setting the default branch to `main`.

---

## Chapter 5 — SSH Authentication

**Goal:** Set up SSH keys so the student can push/pull without entering a password.

### Sections
- Why SSH instead of HTTPS for the group.
- Check for existing SSH keys.
- Generate a new SSH key pair:
  ```bash
  ssh-keygen -t ed25519 -C "you@example.com"
  ```
- Add the public key to GitHub (Settings → SSH and GPG keys).
- Test the connection:
  ```bash
  ssh -T git@github.com
  ```
- `ssh-agent` and `ssh-add` (macOS keychain integration).
- What to do if SSH fails.

### Common Mistakes
- Uploading the private key (`.id_ed25519`) instead of the public key (`.id_ed25519.pub`).
- Forgetting to start `ssh-agent`.
- Multiple machines: need one key per machine.

---

## Chapter 6 — Cloning the Repository

**Goal:** Get a local copy of the group repository.

### Sections
- What does `git clone` do?
- Find the SSH URL on GitHub.
- Clone command:
  ```bash
  git clone git@github.com:ORG/REPO.git
  ```
- What is created: directory structure, `.git/` folder, `origin` remote.
- Verify with `git remote -v` and `git log --oneline`.
- Understanding `origin/main`.

### Diagrams
- Mermaid: clone operation (GitHub → local).

---

## Chapter 7 — Daily Workflow

**Goal:** The core loop the student will use every single day.

### Sections
The full daily loop with commands at every step:

1. **Start of day**: `git pull origin main` (sync with latest).
2. **Create a branch**: `git checkout -b feature/my-task`.
3. **Work**: edit files, run simulations, write code.
4. **Stage changes**: `git add <files>` or `git add -p` (interactive).
5. **Commit**: `git commit -m "Add thermal correction to effective potential"`.
6. **Repeat** steps 3–5 as needed.
7. **Push**: `git push origin feature/my-task`.
8. **Open a Pull Request** on GitHub.
9. **Respond to review**, make changes, push again.
10. **Wait for approval and merge**.
11. **Delete local branch** after merge.

### Diagrams
- Mermaid: daily workflow loop.

### Subsections
- When to commit (logical units, not "every file save").
- Atomic commits — one concept per commit.
- What NOT to commit (binary outputs, large data, `.DS_Store`, `__pycache__`).

---

## Chapter 8 — Branches

**Goal:** Understand what branches are and how to use them correctly.

### Sections
- What is a branch? (pointer to a commit)
- Why branches? (isolation, parallel work)
- Branch naming convention:
  - `feature/` — new feature or calculation
  - `bugfix/` — fix a bug
  - `docs/` — documentation only
  - `refactor/` — restructure without behaviour change
  - `experiment/` — exploratory work, may be discarded
  - `chore/` — tooling, CI, configuration
- Examples: `feature/gw-spectrum`, `bugfix/interpolation`, `docs/install`
- Commands:
  ```bash
  git branch                        # list local branches
  git checkout -b feature/my-task   # create and switch
  git checkout main                 # switch to main
  git branch -d feature/my-task     # delete after merge
  ```
- Keeping the branch up to date with `main`.
- One branch per task — never reuse an old branch.

### Common Mistakes
- Working directly on `main`.
- Creating branches with spaces or uppercase letters.
- Accumulating stale branches.

---

## Chapter 9 — Commits

**Goal:** Write good commit messages and understand the commit model.

### Sections
- What is a commit? (snapshot + metadata)
- The staging area (`git add` → index → commit).
- Anatomy of a good commit message:
  ```
  Add thermal correction to effective potential

  Implements the one-loop thermal correction following Eq. 3.7 of
  Quiros (1999). Only active for T > 0.
  ```
- The imperative rule: "Add …", "Fix …", "Improve …", "Refactor …"
- What to avoid: `update`, `fix`, `final`, `temp`, `wip`, `test`
- Commit granularity — logical units.
- `git diff --staged` before committing.
- Amending the most recent commit (before push only):
  ```bash
  git commit --amend
  ```

### Common Mistakes
- Committing generated files or data.
- Vague messages.
- Commits that mix unrelated changes.
- Committing broken code to a shared branch.

---

## Chapter 10 — Pushing

**Goal:** Understand how to push a branch to GitHub safely.

### Sections
- What does `git push` do?
- Upstream tracking: `git push -u origin feature/my-task`.
- Subsequent pushes on the same branch: `git push`.
- What happens on GitHub after a push (notification, PR button).
- Force push — when it is appropriate (only your own unreviewed branch) and why
  it is dangerous.
- Never force-push to `main` or a branch that others are reviewing.

---

## Chapter 11 — Pull Requests

**Goal:** Open, write, and manage a Pull Request.

### Sections
- What is a Pull Request?
- When to open a PR (branch is ready for review, not necessarily "finished").
- Draft PRs for work in progress.
- PR anatomy:
  - Title (imperative, matches branch intent)
  - Description using the group PR template:
    - Motivation
    - Summary of changes
    - Files affected
    - Testing performed
    - Screenshots (if applicable)
    - Related issue (closes #N)
- Assigning reviewers.
- Labels.
- Linking to an issue.
- Responding to reviewer comments:
  - Make changes locally → commit → push (PR updates automatically).
  - Reply to each comment.
  - Mark resolved when done.
- Small PRs — one feature per PR.

### Diagrams
- Mermaid: PR lifecycle (open → review → revision → approval → merge).

---

## Chapter 12 — Reviews

**Goal:** Understand how to receive and interpret a code review.

### Sections
- Purpose of review (correctness, quality, knowledge sharing — not criticism).
- Types of reviewer feedback: required change vs suggestion vs question.
- How to respond constructively.
- The review checklist (what the reviewer checks):
  - Scientific correctness
  - Builds successfully
  - Tests pass
  - Documentation updated
  - Style consistent
  - No dead code
  - No debug output
  - No generated files
- Requesting a re-review after changes.
- Review etiquette for both author and reviewer.

---

## Chapter 13 — Merge Conflicts

**Goal:** Understand why conflicts happen and how to resolve them calmly.

### Sections
- What is a merge conflict? (two branches modified the same lines)
- Why conflicts happen (and they are normal, not a sign of error).
- Conflict markers in files:
  ```
  <<<<<<< HEAD
  your change
  =======
  their change
  >>>>>>> feature/other-task
  ```
- Resolving conflicts:
  1. Open the file.
  2. Decide which version is correct (or combine them).
  3. Remove conflict markers.
  4. Stage the resolved file.
  5. Continue the rebase or merge.
- Using VS Code's merge editor (recommended).
- Testing after resolution.
- When to ask for help (complex conflicts in scientific code — ask the maintainer).

### Common Mistakes
- Accidentally deleting the other person's changes.
- Leaving conflict markers in the file.
- Not testing after resolution.

---

## Chapter 14 — Updating Branches

**Goal:** Keep a feature branch up to date with `main`.

### Sections
- Why update a branch? (avoid large divergence; easier review).
- The group's preferred strategy: **rebase**.
  ```bash
  git fetch origin
  git rebase origin/main
  ```
- Rebase vs merge — conceptual difference (keep history linear).
- Force-pushing after rebase (only your own branch, never `main`):
  ```bash
  git push --force-with-lease
  ```
- `--force-with-lease` vs `--force` (safer).
- When to update: before opening a PR, when `main` has changed significantly.

### Diagrams
- Mermaid: before and after rebase on `main`.

---

## Chapter 15 — Common Mistakes and Recovery

**Goal:** Provide a reference for the most frequent errors and how to fix them.

### Mistakes Covered

| Mistake | How to Recover |
|---------|---------------|
| Committed to `main` directly | `git reset HEAD~1`, create branch, push |
| Pushed wrong commit | `git revert`, open PR to fix |
| Committed large data file | Remove from history (ask maintainer) |
| Forgot to pull before branching | Rebase onto latest `main` |
| Deleted a branch by mistake | `git checkout -b name origin/name` if still on GitHub |
| Accidentally staged wrong files | `git restore --staged <file>` |
| Commit message typo (before push) | `git commit --amend` |
| Merge conflict panic | `git merge --abort` or `git rebase --abort` |

### Golden Rules
- `git status` is always safe.
- `git log --oneline` is always safe.
- When in doubt: do NOT run `git reset --hard` without understanding it.
- Ask before running anything with `--force`.

---

## Chapter 16 — FAQ

**Goal:** Answer the 15–20 most common questions.

### Questions to Include
- "I can't push — permission denied."
- "My branch is behind `main` — what do I do?"
- "I accidentally committed my data file."
- "What do I do when my PR has conflicts?"
- "Can I have multiple feature branches at once?"
- "My co-author made a change — how do I get it?"
- "How do I undo a commit I already pushed?"
- "What is `HEAD`?"
- "What is `origin`?"
- "Why does Git ask for my passphrase every time?"
- "The reviewer asked me to squash my commits — how?"
- "I need to work on two features at once — what do I do?"

---

## Chapter 17 — Cheat Sheet

**Goal:** Single-page quick reference for daily commands.

### Sections
- Setup (one-time)
- Start of day
- Branching
- Staging & committing
- Pushing & PRs
- Updating from main
- Conflict resolution
- Recovery commands
- Viewing history & status

Format: tables with command + short description. Designed to be printable.

---

## Chapter 18 — Exercises

**Goal:** Practise the full workflow in the example repository.

### Exercise List

| # | Title | Skills Practised |
|---|-------|-----------------|
| 1 | Fork and clone the example repo | Clone, SSH, basic navigation |
| 2 | Set up your environment | Config, SSH test |
| 3 | Create your first branch | Branch naming, checkout |
| 4 | Make a commit | Stage, commit, good message |
| 5 | Push and open a PR | Push, PR template, GitHub UI |
| 6 | Respond to a review comment | Commit, push, reply |
| 7 | Resolve a merge conflict | Conflict markers, resolution |
| 8 | Rebase onto main | Fetch, rebase, force-with-lease |
| 9 | Write a commit for a bug fix | `bugfix/` branch, message style |
| 10 | Complete the full loop end-to-end | All of the above |

Each exercise includes: setup instructions, task description, expected result,
and hints.
