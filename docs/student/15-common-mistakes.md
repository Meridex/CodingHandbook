# Chapter 15 — Common Mistakes and Recovery

## Overview: Things Go Wrong — Here Is How to Fix Them

This chapter is a reference. You do not need to read it linearly.
Bookmark it and return when something breaks.

Each section covers one mistake: what happened, what it looks like, and how to recover.

---

## Mistake 1: Committed to `main` Instead of a Branch

**What happened:** You forgot to create a branch and committed directly to `main`.

**How to recover:**

```bash
# 1. Create the branch you should have been on (it will contain your commits)
git branch feature/my-task

# 2. Reset main back to the remote state (undo your local commits on main)
git reset --hard origin/main

# 3. Switch to your new branch
git checkout feature/my-task
```

Your commits are now only on `feature/my-task`, and `main` is restored.

!!! warning "This only works if you have not pushed to `main` yet"
    If you pushed to `main`, the push was rejected by branch protection. Good.
    If you somehow bypassed protection and pushed, contact the maintainer immediately.

---

## Mistake 2: Committed the Wrong Files

**What happened:** You committed files you did not intend to commit
(generated outputs, a debug script, `.DS_Store`, etc.).

**Option A: If the commit is not yet pushed:**

```bash
# Undo the commit but keep the changes staged
git reset --soft HEAD~1

# Unstage the unwanted file
git reset HEAD unwanted-file.txt

# Re-commit without it
git commit -m "Your original message"
```

**Option B: If the commit is already pushed (on your feature branch only):**

```bash
# Remove the file from tracking (but keep it locally)
git rm --cached unwanted-file.txt

# Add it to .gitignore
echo "unwanted-file.txt" >> .gitignore

# Commit the fix
git add .gitignore
git commit -m "Remove accidentally committed file and update .gitignore"
git push
```

Also add the file to `.gitignore` to prevent future accidents.

---

## Mistake 3: Wrote a Bad Commit Message (Not Yet Pushed)

**What happened:** Your last commit has a typo, wrong tense, or vague message.

```bash
git commit --amend
```

This opens your editor with the current message. Fix it and save.

!!! warning "Only amend unpushed commits"
    If the commit is already on GitHub, amending changes the commit hash and requires
    a force push. Only do this on your own feature branch with no one else reviewing.

---

## Mistake 4: Forgot to Stage a File (Last Commit)

**What happened:** You committed but forgot to include one file.

```bash
git add forgotten-file.py
git commit --amend --no-edit
```

`--no-edit` keeps the existing commit message unchanged.

---

## Mistake 5: Accidentally Deleted a File

**What happened:** You deleted a tracked file (with `rm` or accidentally in your editor).

```bash
# Restore the file from the last commit
git checkout HEAD -- src/thermal.py
```

---

## Mistake 6: Staged Files You Did Not Mean to Stage

**What happened:** You ran `git add .` and accidentally staged files you are not
ready to commit.

```bash
# Unstage a specific file (keeps your local changes)
git restore --staged src/thermal.py

# Unstage everything
git restore --staged .
```

---

## Mistake 7: Need to Undo the Last Commit (Soft)

**What happened:** You want to undo the commit but keep the changes as staged.

```bash
git reset --soft HEAD~1
```

Your files are unchanged; the commit is removed; the changes are staged.

---

## Mistake 8: Need to Undo the Last Commit (Hard) — Discard Changes

**What happened:** You want to completely undo the last commit and discard the changes.

```bash
git reset --hard HEAD~1
```

!!! danger "This is destructive"
    `git reset --hard` permanently discards uncommitted changes.
    There is no undo for this operation (beyond `git reflog` within a short window).
    Use it only when you are certain you want to discard the changes.

---

## Mistake 9: You Need to Temporarily Set Aside Uncommitted Changes

**What happened:** You are in the middle of work, but need to switch branches
(e.g., to fix an urgent bug). You cannot commit the in-progress work yet.

```bash
# Save (stash) your current changes
git stash

# Switch to the other branch, do your work, commit
git checkout bugfix/urgent-fix
# ... work ...
git checkout feature/my-task

# Restore your stashed work
git stash pop
```

List all stashes: `git stash list`
Apply a specific stash: `git stash apply stash@{2}`

---

## Mistake 10: Pushed a Commit with a Mistake to Your Feature Branch

**What happened:** You pushed a commit that has a bug or wrong content
(on your feature branch, not `main`).

**Option A: Add a fix commit (simplest, preferred during active review):**

```bash
# Make the fix
git add src/thermal.py
git commit -m "Fix sign error introduced in previous commit"
git push
```

This preserves the history of your mistake and fix — which can be informative.

**Option B: Amend and force-push (if the PR review has not started yet):**

```bash
git add src/thermal.py
git commit --amend  # or rebase -i to squash/edit earlier commits
git push --force-with-lease
```

---

## Mistake 11: Rebased and Something Went Wrong

**What happened:** You started a `git rebase` and it went badly — conflicts
you cannot resolve, or you made it worse.

```bash
git rebase --abort
```

This cancels the rebase completely and returns your branch to its pre-rebase state.

---

## Mistake 12: You Accidentally Cloned via HTTPS Instead of SSH

**What happened:** Push attempts fail with "Permission denied" because you are
using HTTPS instead of SSH.

```bash
# Check current remote URL
git remote -v

# Fix it
git remote set-url origin git@github.com:ORG/REPO.git

# Verify
git remote -v
```

---

## Mistake 13: `git pull` Produced a Merge Commit on `main`

**What happened:** You ran `git pull` on `main` and it created an unwanted
merge commit because your local `main` had diverged.

**Prevention:** This should not happen if you follow the workflow (never commit directly to `main`).
If it happened, your local `main` must have commits. Reset to match the remote:

```bash
git fetch origin
git reset --hard origin/main
```

---

## The `git reflog`: Your Last Resort

`git reflog` records every move of `HEAD` in your local repository — including
commits that have been "undone" with reset.

If you accidentally discarded a commit with `git reset --hard`, it may still be
recoverable within a few days:

```bash
git reflog
```

Look for the commit hash of the state you want to recover. Then:

```bash
git checkout -b recovery-branch <commit-hash>
```

!!! warning "Reflog is local only"
    `git reflog` only exists on your local machine. It is not pushed to GitHub.
    It is erased by Git's garbage collection after approximately 90 days.

---

## Common Mistakes Summary Table

| Mistake | Command |
|---------|---------|
| Committed to `main` | `git branch new-branch && git reset --hard origin/main` |
| Bad commit message (unpushed) | `git commit --amend` |
| Forgot to stage a file (unpushed) | `git add file && git commit --amend --no-edit` |
| Staged wrong files | `git restore --staged file` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Undo last commit (discard changes) | `git reset --hard HEAD~1` |
| Temporarily save in-progress work | `git stash` / `git stash pop` |
| Rebase went wrong | `git rebase --abort` |
| Cloned via HTTPS | `git remote set-url origin git@...` |
| Recover deleted commit | `git reflog` |

---

## Best Practice Summary

- `--soft` keeps your changes; `--hard` discards them.
- Only amend commits that have not been pushed.
- `git rebase --abort` is always safe to run during a broken rebase.
- When in doubt, `git status` tells you what state you are in.
- If truly stuck, ask the maintainer — Git history is usually recoverable.

---

## Checklist

- [ ] I know how to move commits from `main` to a feature branch.
- [ ] I know the difference between `git reset --soft` and `git reset --hard`.
- [ ] I know when it is safe to use `git commit --amend`.
- [ ] I know how to use `git stash` to temporarily store changes.
- [ ] I know what `git reflog` is and when to use it as a last resort.

---

## Exercises

1. **Commit to `main` recovery.** Intentionally make a commit on `main` (locally, do not push).
   Practice the recovery procedure to move the commit to a feature branch.

2. **Stash practice.** Start making changes on a branch. Stash them, switch to another branch
   and make a different commit, come back, and pop the stash. Verify both sets of changes
   are present.

3. **Reflog exploration.** Run `git reflog` on your local clone. Identify the last three
   significant events in your HEAD history.
