# Chapter 3 — Branch Protection Rules

## Overview

Branch protection rules are GitHub-level guardrails that enforce the group workflow
automatically. Even if a collaborator knows Git well enough to bypass the rules locally,
GitHub will reject the operation at the remote.

Branch protection on `main` is **mandatory** for all group repositories.
Configure it before adding any collaborators.

---

## Navigate to Branch Protection Settings

**Settings → Branches → Add branch protection rule**

(Or click **"Edit"** if a rule already exists for `main`.)

---

## Required Rules for `main`

Configure the rule for the branch name pattern: `main`

### 1. Require a pull request before merging

✓ **Enable:** "Require a pull request before merging"

Sub-options:
- **"Require approvals":** ✓ Enable — set to **1** (minimum; increase when group grows)
- **"Dismiss stale pull request approvals when new commits are pushed":** ✓ Enable

  *Why:* If a reviewer approves a PR and then the author pushes additional commits,
  the approval is automatically dismissed. The reviewer must re-approve the updated code.
  This prevents approval circumvention.

- **"Require review from Code Owners":** Disable (not used)
- **"Restrict who can dismiss pull request reviews":** Disable (keep simple for now)

### 2. Require status checks to pass before merging

✓ **Enable:** "Require status checks to pass before merging"

Sub-options:
- **"Require branches to be up to date before merging":** ✓ Enable

  *Why:* Prevents a PR from merging if `main` has advanced since the PR branch
  was created. This ensures the reviewer saw the final integrated state.

- **Status checks to require:** Leave empty for now. Add the CI job name here
  once GitHub Actions is configured (Chapter 14).

### 3. Require conversation resolution before merging

✓ **Enable:** "Require conversation resolution before merging"

*Why:* A reviewer's comment must be explicitly resolved before the PR can be merged.
This prevents PRs from being merged while open questions remain.

### 4. Restrict who can push to matching branches

✓ **Enable:** "Restrict who can push to matching branches"

- Add: all maintainers and the PI
- Do **not** add: students

*Why:* Even though branch protection prevents direct pushes, this rule adds an
explicit allowlist. Students cannot push to `main` even with force-push.

### 5. Do not allow bypassing the above settings

✓ **Enable:** "Do not allow bypassing the above settings"

*Why:* Without this, repository admins (including yourself) can bypass protection.
Enabling this means **no one** can bypass the rules — not even the maintainer or PI.
This is the correct setting for a research group where consistency matters.

---

## Summary of Rule Configuration

| Rule | Setting |
|------|---------|
| Require PR before merging | ✓ Enabled |
| Required approvals | 1 |
| Dismiss stale approvals | ✓ Enabled |
| Require status checks | ✓ Enabled (add CI job once available) |
| Require branch to be up to date | ✓ Enabled |
| Require conversation resolution | ✓ Enabled |
| Restrict push access | ✓ Enabled (maintainers only) |
| Allow bypassing | ✗ Disabled |

---

## Testing the Protection Rules

After saving, verify the rules work correctly:

```bash
# Attempt a direct push to main — should be rejected
echo "test" >> README.md
git add README.md
git commit -m "Test protection"
git push origin main
```

Expected error:
```
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: error: Changes must be made through a pull request.
To github.com:ORG/REPO.git
 ! [remote rejected] main -> main (protected branch hook declined)
```

This is correct. Delete the local test commit:

```bash
git reset --hard origin/main
```

---

## Rulesets (GitHub's Newer Interface)

GitHub has introduced **Rulesets** as a more powerful alternative to branch protection rules.
If the repository is in an organisation with Rulesets available:

- **Settings → Rules → Rulesets → New ruleset**
- Target: include `main`
- Rules to enable: the same set as above

Rulesets offer finer-grained control and inheritance across repositories.
For new repositories in 2024+, prefer Rulesets over the legacy branch protection UI.

---

## Common Mistakes

1. **Forgetting "Dismiss stale approvals".** Without this, an attacker could
   get approval on a clean version and then push malicious changes afterward.

2. **Not enabling "Require branch to be up to date".** This is how stale PRs
   slip in changes that conflict with `main`'s current state.

3. **Allowing bypassing.** The maintainer's own commits should also go through PRs.
   No one should be above the process.

4. **Configuring protection after adding collaborators.** Always set protection first.

---

## Checklist

- [ ] Branch protection rule created for `main`
- [ ] Require PR before merging: enabled
- [ ] Minimum 1 approval required
- [ ] Dismiss stale approvals: enabled
- [ ] Require status checks: enabled
- [ ] Require branch up to date: enabled
- [ ] Require conversation resolution: enabled
- [ ] Push restricted to maintainers/PI
- [ ] Bypassing disabled
- [ ] Tested: direct push to `main` is rejected
