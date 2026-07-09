# Glossary

Complete glossary of terms used throughout this handbook.

---

## A

**Atomic commit**
A commit that contains exactly one logical change. Each commit should be independently
understandable and should not mix unrelated modifications.

**Author (commit)**
The person who originally wrote the code change. Recorded in every commit alongside
the timestamp.

---

## B

**Base branch**
The branch a Pull Request targets. In this group, the base branch is always `main`.

**Branch**
A movable pointer to a commit. Branches allow parallel lines of development.
Creating a branch is cheap and instant in Git.

**Branch protection**
GitHub settings that prevent direct pushes to a branch and require Pull Requests
and approvals before merging. Applied to `main` in all group repositories.

---

## C

**Checkout**
The act of switching to a different branch or restoring a file to a previous state.
`git checkout branch-name` switches your working directory to that branch.

**Clone**
A one-time operation that downloads a remote repository to your local machine,
including the full commit history.

**Commit**
A saved snapshot of staged changes. Contains the diff, author, timestamp, message,
and a reference to the parent commit.

**Commit hash (SHA)**
A unique 40-character hexadecimal identifier for each commit (e.g., `a3f2c91...`).
Usually abbreviated to the first 7–8 characters.

**Compare branch**
The feature branch being proposed in a Pull Request (the branch containing new changes).

**Conflict** → see *Merge conflict*

---

## D

**Default branch**
The branch that GitHub shows by default when visiting a repository. In this group,
always `main`.

**Diff**
A display of the exact lines changed between two states. `git diff` shows
unstaged changes; `git diff --staged` shows staged changes.

**Draft PR**
A Pull Request explicitly marked as not ready for final review. Used to share
work-in-progress and receive early feedback.

---

## F

**Fast-forward merge**
A merge where the target branch simply advances its pointer because no divergence
occurred. Results in no merge commit.

**Fetch**
Downloading new commits and branch information from the remote without modifying
your local branches. `git fetch origin`.

**Feature branch**
A branch created for a specific task. Named with a prefix like `feature/`,
`bugfix/`, `docs/`, etc. Deleted after the corresponding PR is merged.

**Force push**
Overwriting the remote branch history with your local history. Required after
rebasing. Always use `--force-with-lease`, never `--force`.

**Fork**
A copy of a repository under your own GitHub account. Not used in this group —
students clone directly.

---

## G

**Git**
A distributed version control system. Runs locally on your machine. Created by
Linus Torvalds in 2005.

**GitHub**
A web platform that hosts Git repositories and provides collaboration tools
(Pull Requests, Issues, code review). The group uses GitHub exclusively.

**`.gitignore`**
A file listing patterns of files that Git should not track. Located at the root
of the repository.

---

## H

**HEAD**
A special pointer that indicates your current position in the repository.
Usually points to the tip (latest commit) of your current branch.

**Hunk**
A contiguous section of changed lines in a diff. `git add -p` lets you stage
individual hunks.

---

## I

**Index** → see *Staging area*

---

## L

**Label (GitHub)**
A tag applied to Issues and Pull Requests to categorise them.
Examples: `type: feature`, `priority: high`, `status: needs-review`.

---

## M

**`main`**
The primary branch of a repository. Protected; all changes arrive via Pull Requests.
Represents the canonical, always-working state of the code.

**Merge**
The act of integrating one branch's commits into another.

**Merge commit**
A special commit created when merging two diverged branches. Has two parent commits.
The group avoids these on `main` by using squash merge.

**Merge conflict**
A situation where two branches have both modified the same lines in a file,
and Git cannot automatically decide which version is correct. Must be resolved manually.

**Milestone (GitHub)**
A group of Issues and Pull Requests associated with a deadline or goal
(e.g., "Paper Submission v2").

---

## O

**`origin`**
The conventional name for the default remote — the GitHub repository you cloned from.

---

## P

**PR** → see *Pull Request*

**Pull**
`git pull` fetches new commits from the remote and integrates them into your current
local branch. Equivalent to `git fetch` + `git merge`.

**Pull Request (PR)**
A proposal on GitHub to merge a feature branch into `main`. The venue for code review,
discussion, and approval before changes are accepted.

**Push**
Sending local commits to the remote (GitHub). `git push origin feature/task`.

---

## R

**Rebase**
Replaying commits from one branch on top of another. The group uses rebase to
update feature branches with the latest `main`. Produces a linear history.

**Remote**
A named reference to a repository hosted elsewhere (on GitHub).
The default remote is named `origin`.

**Repository (repo)**
A directory tracked by Git. Contains all project files and their complete history,
stored in the `.git/` subdirectory.

**Review (code review)**
The process of a colleague reading a Pull Request, leaving feedback, and
approving or requesting changes.

---

## S

**Squash merge**
A merge strategy that combines all commits on a feature branch into a single commit
on the target branch. The group uses squash merge for all PRs into `main`.

**SSH (Secure Shell)**
A cryptographic protocol used to authenticate with GitHub. The group uses SSH
key-based authentication exclusively.

**Staging area (index)**
A preparatory zone between your working directory and the repository.
`git add` moves changes here; `git commit` records them permanently.

**Stash**
Temporary storage for uncommitted changes. `git stash` saves changes;
`git stash pop` restores them.

---

## T

**Tag**
A permanent, named pointer to a specific commit. Used to mark releases and
paper-submission states. Tags are never deleted.

**Tracking branch**
A local branch linked to a remote branch. `git push -u` sets the upstream tracking.

---

## U

**Upstream**
The remote branch that a local branch tracks. Set with `git push -u origin branch-name`.

---

## W

**Working directory**
The actual files in your project folder, as you see them in your editor.
Distinct from the staging area and the repository.
