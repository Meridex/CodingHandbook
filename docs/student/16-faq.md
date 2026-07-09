# Chapter 16 — FAQ

Frequently asked questions from students in the group.
Questions are grouped by topic.

---

## Getting Started

**Q: Do I need to know programming to use Git?**

No. Git tracks changes to any text files — Python scripts, C++ source code,
Markdown documentation, LaTeX manuscripts. The Git commands themselves are
independent of the programming language.

---

**Q: Can I use a GUI client instead of the command line?**

Yes — tools like GitHub Desktop, GitKraken, and VS Code's built-in Git panel
are valid. However, **learn the command line first**. GUI clients abstract away
important details, and when something goes wrong, you will need command-line
knowledge to diagnose and fix it. This handbook uses the command line throughout.

---

**Q: My colleague uses a different Git workflow. Why does the group use this one?**

Consistency matters more than optimality. Different workflows exist and all have
trade-offs. The group chose this workflow deliberately for a team of 3–10 people
working on research code. Deviating creates confusion when reviewing, onboarding
new students, and maintaining the repository over years.

---

## Daily Workflow

**Q: How often should I commit?**

Commit after completing each **logical unit of work** — a function, a test, a
documentation section. Do not commit every file save, but do not accumulate a
week of work into a single commit. A reasonable frequency is several times per day.

---

**Q: Do I have to pull every morning even if I am the only one working?**

Yes. Remote repositories can receive automated changes (CI results, tag pushes,
administrative commits). Pulling before branching is a low-cost habit that
prevents unexpected divergences.

---

**Q: How do I know if someone else is working on the same file as me?**

Check the open PRs on GitHub and communicate with your colleagues.
Git does not "lock" files — two people can edit the same file simultaneously.
If their PRs are merged first, you will encounter a conflict when you rebase.
This is normal; resolve it as described in Chapter 13.

---

**Q: Can I work on two features at the same time?**

Yes — create two separate branches: `feature/task-one` and `feature/task-two`.
Switch between them with `git checkout`. Changes on one branch are invisible on
the other (unless you cherry-pick). Keep each branch focused on one task.

---

## Commits

**Q: I forgot to add a file to my last commit. What do I do?**

If you have not pushed yet:
```bash
git add forgotten-file.py
git commit --amend --no-edit
```

If you have already pushed, add a follow-up commit:
```bash
git add forgotten-file.py
git commit -m "Add missing file for previous commit"
git push
```

---

**Q: My commit message is wrong. Can I fix it?**

If not yet pushed: `git commit --amend`.
If already pushed on your feature branch (and no one has reviewed it yet):
`git commit --amend` then `git push --force-with-lease`.
If the PR is under review: add a new commit rather than amending.

---

**Q: What is the difference between `git add .` and `git add -p`?**

`git add .` stages everything changed in the current directory and below.
`git add -p` stages changes interactively, hunk by hunk.

Use `git add -p` when a file contains multiple unrelated changes that you want
to split into separate commits. Use `git add .` only when you are certain
everything you changed belongs in the next commit.

---

## Branches

**Q: I deleted my branch by accident. How do I recover it?**

If the branch was not merged and had unique commits:

```bash
# Find the hash of the last commit on that branch
git reflog

# Recreate the branch
git checkout -b feature/recovered-branch <commit-hash>
```

If the branch was merged, its commits are part of `main`. No recovery needed.

---

**Q: My branch name has a typo. How do I rename it?**

```bash
# Rename locally
git branch -m old-name new-name

# Push the renamed branch to GitHub
git push origin new-name

# Delete the old remote branch
git push origin --delete old-name
```

---

**Q: How do I see what branches exist on GitHub?**

```bash
git fetch origin
git branch -r   # remote branches
git branch -a   # all branches (local + remote)
```

---

## Pull Requests

**Q: My PR has a conflict with `main`. What do I do?**

Rebase your branch onto the latest `main`:

```bash
git fetch origin
git rebase origin/main
# Resolve any conflicts
git push --force-with-lease
```

The conflict warning on the PR page will disappear.

---

**Q: The reviewer is taking a long time. What should I do?**

After 2–3 business days, send a polite message or mention the reviewer on the PR.
In a research group, people are busy. A short nudge is appropriate and expected.

---

**Q: Can I merge my own PR?**

No. The group policy requires at least one approval from another member before merging.
You must not approve your own PR.

---

**Q: I need to make a small fix to a merged PR. How?**

Create a new branch, make the fix, open a new (small) PR.
Do not reopen or edit the merged PR.

---

## Merge Conflicts

**Q: I see `<<<<<` markers in my file. What happened?**

A merge conflict was detected but left unresolved. Open the file,
find all `<<<<<<<`, `=======`, `>>>>>>>` markers, decide which version is correct,
remove the markers, stage the file with `git add`, and continue the operation
(`git rebase --continue` or `git commit`).

---

**Q: I cannot figure out which version is correct. What do I do?**

Ask the author of the conflicting change. Do not guess on scientific code.
It is always better to spend 10 minutes in conversation than to silently keep
a physically wrong version.

---

## SSH and Authentication

**Q: `git push` says "Permission denied (publickey)". What do I do?**

1. Check that your SSH key is added to GitHub: `ssh -T git@github.com`
2. Check that the SSH agent is running: `ssh-add -l`
3. Check the remote URL is SSH (not HTTPS): `git remote -v`
4. If all else fails, revisit Chapter 5 step by step.

---

**Q: I got a new computer. Do I need a new SSH key?**

Yes. Generate a new key pair on the new machine, add the public key to GitHub,
and test with `ssh -T git@github.com`. Do not copy your private key from the old machine.

---

## History and Recovery

**Q: I ran `git reset --hard` and lost my changes. Can I recover them?**

Possibly. Try `git reflog` to find the commit hash before the reset,
then `git checkout -b recovery <hash>`. This only works within approximately
90 days and only on your local machine.

---

**Q: I want to see what changed in a specific commit.**

```bash
git show <commit-hash>
git show a3f2c91   # shows the diff introduced by that commit
```

---

**Q: I want to see what changed between two commits.**

```bash
git diff <commit-hash-1> <commit-hash-2>
git diff main feature/my-branch   # compare branches
```

---

**Q: I accidentally committed a password. What do I do?**

1. Rotate/revoke the credential immediately — treat it as compromised.
2. Contact the maintainer — the commit must be removed from history (this is
   non-trivial for a public or shared repository).
3. Add the credentials file to `.gitignore` to prevent future accidents.

Never commit credentials. Use environment variables or a `.env` file that is gitignored.

---

## Tools and Environment

**Q: Which terminal / OS is recommended?**

The group does not mandate a specific OS. macOS and Linux work natively.
Windows users should use Git Bash or WSL2. All commands in this handbook
work identically on macOS and Linux; some may differ on Windows Git Bash.

---

**Q: Which text editor should I use with Git?**

Any editor works. VS Code is recommended because it has excellent built-in Git
integration, a visual merge editor, and syntax highlighting for all languages
used in the group. Configure it as your Git editor:

```bash
git config --global core.editor "code --wait"
```

---

**Q: What is `.gitignore`?**

A file at the root of the repository that tells Git which files to ignore.
Files listed in `.gitignore` are never staged by `git add .` and never shown
in `git status` as untracked. The repository's `.gitignore` is already
configured for the languages used in the group.

If you need to add a new ignored pattern, edit `.gitignore`, commit the change,
and open a PR.
