# Chapter 18 — Exercises

## Overview

This chapter contains structured exercises that cover the entire Student Guide workflow.
Complete them in order — each exercise builds on the previous.

You will use the group's **example repository** for these exercises.
The example repository is a small, intentionally simple physics code
designed for practice without the risk of affecting real research code.

!!! note "Before starting"
    Confirm with the maintainer that you have been added as a collaborator
    on the example repository, and obtain its GitHub URL.

---

## Part 1: Setup (Chapters 4–6)

### Exercise 1.1 — Verify Your Environment

Confirm your development environment is correctly configured:

```bash
git --version
git config --global user.name
git config --global user.email
git config --global core.editor
git config --global init.defaultBranch
ssh -T git@github.com
```

**Expected output for SSH:** `Hi your-username! You've successfully authenticated...`

Record any configuration that is wrong and fix it before proceeding.

---

### Exercise 1.2 — Clone the Example Repository

Clone the group's example repository:

```bash
git clone git@github.com:ORG/example-repository.git
cd example-repository
git remote -v
git log --oneline -5
```

Verify:

- The remote URL starts with `git@github.com:`
- The log shows at least one commit

---

### Exercise 1.3 — Explore the Structure

```bash
ls -la
cat README.md
```

Answer these questions in your notes:

1. What files are at the top level?
2. Is there a `src/` directory? A `tests/` directory?
3. What is this code supposed to do (from the README)?

---

## Part 2: Branches and Commits (Chapters 7–9)

### Exercise 2.1 — Your First Branch

Create a feature branch for your first contribution.
The task: add your name and a one-line description to the `CONTRIBUTORS.md` file.

```bash
git checkout main
git pull origin main
git checkout -b docs/add-your-name
```

Edit `CONTRIBUTORS.md` and add one line:
```
- Your Name (Year) — Brief description of your research area
```

Stage and commit:

```bash
git status
git diff
git add CONTRIBUTORS.md
git diff --staged
git commit -m "Add [Your Name] to contributors list"
```

---

### Exercise 2.2 — Atomic Commits

The task: add a new Python function to the example code.

1. Create a branch: `feature/add-your-function`
2. Write a simple mathematical function (e.g., a Gaussian or step function) in `src/`
3. Commit the function: `"Add [function name] function to src/"`
4. Write a test for the function in `tests/`
5. Commit the test separately: `"Add unit test for [function name]"`

Result: two separate, atomic commits. Verify with:

```bash
git log --oneline
```

---

### Exercise 2.3 — Interactive Staging

In the file you created for Exercise 2.2, make two unrelated changes:

- Fix a typo in a comment
- Add a second function

Use `git add -p` to stage only the typo fix and commit it.
Then stage the second function and commit it separately.

Verify you have three commits (original function, typo fix, second function).

---

## Part 3: Push and Pull Request (Chapters 10–11)

### Exercise 3.1 — Push Your Branch

Push your `docs/add-your-name` branch to GitHub:

```bash
git push -u origin docs/add-your-name
```

Verify the branch appears in the GitHub repository.

---

### Exercise 3.2 — Open a Pull Request

Open a Pull Request for your `docs/add-your-name` branch:

1. Go to the repository on GitHub.
2. Click **"Compare & pull request"**.
3. Fill in the PR template:
   - **Title:** `Add [Your Name] to contributors list` (imperative)
   - **Motivation:** Why are you adding yourself?
   - **Summary of changes:** What file was modified?
   - **Testing:** What verification did you perform?
   - **Related issue:** `None` or an actual issue if one exists
4. Assign the maintainer as reviewer.
5. Apply the label `type: docs`.
6. Create the PR.

---

### Exercise 3.3 — Draft PR

Push your `feature/add-your-function` branch and open a **Draft PR**:

```bash
git push -u origin feature/add-your-function
```

On GitHub, open a draft PR with:

- Title: `Add [function name] function`
- Mark it as a draft (click the arrow next to "Create pull request")

This exercises the concept of using draft PRs for work in progress.

---

## Part 4: Review (Chapter 12)

### Exercise 4.1 — Receive a Review

Ask a colleague (or the maintainer) to review your `docs/add-your-name` PR
and leave at least one comment.

Respond to the comment:

1. Make the requested change (if any).
2. Commit and push.
3. Reply to the comment explaining what you did.
4. Mark the conversation as resolved.
5. Request re-review.

---

### Exercise 4.2 — Give a Review

Find a colleague who has an open PR. Review it:

1. Click **"Files changed"**.
2. Leave at least:
   - One inline comment (click `+` next to a line)
   - One overall comment using **"Review changes"**
3. Mark it as either "Approve", "Comment", or "Request changes".

---

## Part 5: Updating Branches (Chapter 14)

### Exercise 5.1 — Simulate a Diverged Branch

1. Ask the maintainer to push one commit to `main` after you created your feature branch.
2. Run:
   ```bash
   git fetch origin
   git log --oneline HEAD..origin/main
   ```
   Confirm you are behind.

3. Rebase:
   ```bash
   git rebase origin/main
   ```

4. Force-push:
   ```bash
   git push --force-with-lease
   ```

5. Verify the PR shows "no conflicts" on GitHub.

---

## Part 6: Conflict Resolution (Chapter 13)

### Exercise 6.1 — Simulate a Merge Conflict

Work with a colleague:

1. Both of you branch from the same commit on `main`.
2. Both edit the same line in the same file (e.g., `CONTRIBUTORS.md` line 1).
3. Both commit and push your branches.
4. One person's PR is merged first.
5. The other person:
   ```bash
   git fetch origin
   git rebase origin/main
   # Conflict!
   ```

6. Resolve the conflict, stage the file, continue the rebase, and push.

---

## Part 7: Recovery (Chapter 15)

### Exercise 7.1 — Commit to `main` Recovery

1. Check out `main`.
2. Make a trivial commit directly to `main` (e.g., add a space to `README.md`).
3. Do **not** push.
4. Practice the recovery:
   ```bash
   git branch feature/recovered
   git reset --hard origin/main
   git checkout feature/recovered
   ```

5. Verify your commit is now only on `feature/recovered`.

---

### Exercise 7.2 — Stash Workflow

1. Start editing a file on `feature/add-your-function`.
2. Stash your changes:
   ```bash
   git stash
   ```

3. Switch to `main`, pull, switch back.
4. Pop the stash:
   ```bash
   git stash pop
   ```

5. Verify your changes are restored.

---

## Part 8: Full Cycle Completion

### Exercise 8.1 — Merge Your PR

After your `docs/add-your-name` PR is approved:

- The maintainer will squash-merge it.
- After the merge, clean up locally:
  ```bash
  git checkout main
  git pull origin main
  git branch -d docs/add-your-name
  ```

- Verify your name is now in `CONTRIBUTORS.md` on `main`.

---

## Completion Checklist

- [ ] Exercise 1.1 — Environment verified
- [ ] Exercise 1.2 — Repository cloned
- [ ] Exercise 1.3 — Structure explored
- [ ] Exercise 2.1 — First branch and commit created
- [ ] Exercise 2.2 — Atomic commits demonstrated
- [ ] Exercise 2.3 — Interactive staging used
- [ ] Exercise 3.1 — Branch pushed to GitHub
- [ ] Exercise 3.2 — Pull Request opened with complete template
- [ ] Exercise 3.3 — Draft PR created
- [ ] Exercise 4.1 — Responded to review comments
- [ ] Exercise 4.2 — Reviewed a colleague's PR
- [ ] Exercise 5.1 — Branch rebased onto updated `main`
- [ ] Exercise 6.1 — Merge conflict resolved
- [ ] Exercise 7.1 — Commit-to-main recovery practiced
- [ ] Exercise 7.2 — Stash workflow practiced
- [ ] Exercise 8.1 — PR merged and branch cleaned up

**When all boxes are checked, you have completed the Student Guide.**

Proceed to regular development work on group projects.
If you encounter a situation not covered here, consult the FAQ (Chapter 16),
the Cheat Sheet (Chapter 17), or ask the maintainer.
