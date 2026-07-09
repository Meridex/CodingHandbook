# Chapter 17 — Cheat Sheet

Quick reference for the commands and conventions used daily.
Print this page and keep it at your desk until the commands are automatic.

---

## Setup (Once Per Machine)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@institute.edu"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
git config --global core.autocrlf input   # macOS/Linux
ssh-keygen -t ed25519 -C "you@institute.edu"
ssh -T git@github.com                      # test SSH connection
```

---

## Daily Workflow (Full Loop)

```bash
# 1. Sync with latest
git checkout main
git pull origin main

# 2. Create branch
git checkout -b feature/task-name

# 3. Work, then stage
git status
git diff
git add src/file.py
git diff --staged          # review before committing

# 4. Commit
git commit -m "Add descriptive imperative message"

# 5. Repeat steps 3–4 as needed

# 6. Push
git push -u origin feature/task-name    # first push
git push                                  # subsequent pushes

# 7. Open PR on GitHub

# 8. After merge: clean up
git checkout main
git pull origin main
git branch -d feature/task-name
```

---

## Branch Operations

```bash
git branch                          # list local branches
git branch -a                       # list all (local + remote)
git checkout -b feature/new-task    # create and switch
git checkout main                   # switch to existing branch
git branch -d feature/merged-task   # delete merged branch
git branch -D feature/unmerged      # force delete (loses unmerged commits)
git branch -m old-name new-name     # rename branch
```

---

## Staging and Committing

```bash
git status                    # what has changed
git diff                      # unstaged changes
git diff --staged             # staged changes (what will be committed)
git add src/file.py           # stage a specific file
git add .                     # stage everything
git add -p                    # interactive staging (hunk by hunk)
git restore --staged file.py  # unstage a file
git commit -m "Message"       # commit with inline message
git commit --amend            # edit last commit (unpushed only)
git commit --amend --no-edit  # amend without changing message
```

---

## Viewing History

```bash
git log --oneline              # compact history
git log --oneline -10          # last 10 commits
git log --oneline --graph      # branch graph
git show <hash>                # diff of one commit
git diff main feature/branch   # compare branches
git log --oneline HEAD..origin/main  # commits on remote not yet local
```

---

## Updating and Syncing

```bash
git fetch origin                  # fetch remote changes (does not modify local)
git pull origin main              # fetch + merge into current branch
git rebase origin/main            # rebase current branch onto latest main
git push --force-with-lease       # force push after rebase (never use --force)
git rebase --abort                # cancel a rebase in progress
git rebase --continue             # continue after resolving a conflict
```

---

## Undoing and Recovery

```bash
git restore --staged file.py      # unstage
git restore file.py               # discard unstaged changes (destructive)
git reset --soft HEAD~1           # undo last commit, keep changes staged
git reset --hard HEAD~1           # undo last commit, discard changes (destructive)
git stash                         # save uncommitted work temporarily
git stash pop                     # restore stashed work
git stash list                    # list all stashes
git reflog                        # full local HEAD history (recovery last resort)
git checkout HEAD -- file.py      # restore a deleted file from last commit
```

---

## Remote Operations

```bash
git remote -v                            # show remote URLs
git remote set-url origin git@...        # fix remote URL (e.g., HTTPS → SSH)
git push origin --delete feature/branch  # delete remote branch
git remote prune origin                  # clean up stale remote references
```

---

## Branch Naming Quick Reference

| Prefix | Use |
|--------|-----|
| `feature/` | New functionality |
| `bugfix/` | Fix a bug |
| `docs/` | Documentation only |
| `refactor/` | Restructure without behaviour change |
| `experiment/` | Exploratory work |
| `chore/` | Build, CI, tooling |

---

## Commit Message Rules

```
Add thermal correction to effective potential        ← Subject (imperative, ≤72 chars)
                                                     ← Blank line
Implements Eq. 3.7 of Quiros (1999). Active only     ← Body (optional, explains why)
when T > 0. Controlled by include_thermal flag.

Closes #42.                                          ← Issue reference
```

**Good verbs:** Add, Fix, Remove, Improve, Refactor, Update, Implement, Rename  
**Bad verbs:** update, fix, changes, final, temp, wip, misc

---

## Files to Never Commit

```
*.pyc  __pycache__/  .DS_Store  *.pdf  *.png  *.hdf5
*.dat  build/  dist/  .env  config.secret  *.swp
.ipynb_checkpoints/  *.o  *.so
```

These should already be in `.gitignore`. If not, add them and commit `.gitignore`.

---

## Emergency Recovery Checklist

1. **Don't panic.** Git history is almost always recoverable.
2. Run `git status` — understand your current state.
3. Run `git reflog` — find where you were before the problem.
4. If in a broken rebase: `git rebase --abort`.
5. If you need to reset to a known safe state: `git reset --hard origin/main` (on `main`).
6. If all else fails: ask the maintainer.
