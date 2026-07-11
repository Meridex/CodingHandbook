# Chapter 4 — Initial Setup

## Overview: Getting Your Machine Ready

This chapter covers everything you need to do **once** on each machine you use.
After completing this setup, your machine will be ready to work with the group's repositories.

Estimated time: 20–30 minutes.

---

## Step 1: Install Git

=== "macOS"

    Git is pre-installed on macOS via Xcode Command Line Tools. To verify:

    ```bash
    git --version
    ```

    If Git is not installed (or the version is old), install via Homebrew:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install git
    ```

    Recommended minimum version: **2.30** or later.

=== "Linux (Ubuntu/Debian)"

    ```bash
    sudo apt update
    sudo apt install git
    git --version
    ```

=== "Linux (Fedora/RHEL)"

    ```bash
    sudo dnf install git
    git --version
    ```

=== "Windows"

    Download and install [Git for Windows](https://git-scm.com/download/win).

    During installation:
    - Select **"Use Git from the Windows Command Prompt"**
    - Select **"Checkout Windows-style, commit Unix-style line endings"**
    - Select **"Use MinTTY"** as the terminal emulator

    After installation, use **Git Bash** for all commands in this handbook.

---

## Step 2: Configure Your Identity

Git records your name and email with every commit. This must match your GitHub account.

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

!!! warning "Use your institute email"
    Use your university or institute email — the same email registered on GitHub.
    Do not use a personal email. This ensures commits are attributed correctly
    on GitHub and in the audit log.

Verify:

```bash
git config --global user.name
git config --global user.email
```

---

## Step 3: Configure Your Default Editor

Git opens a text editor when you need to write a commit message (if you omit `-m`)
or resolve a rebase. Set this to your preferred editor.

=== "VS Code (recommended)"

    ```bash
    git config --global core.editor "code --wait"
    ```

=== "nano (simple terminal editor)"

    ```bash
    git config --global core.editor "nano"
    ```

=== "vim"

    ```bash
    git config --global core.editor "vim"
    ```

---

## Step 4: Set the Default Branch Name

Git historically used `master` as the default branch name.
This group uses `main`. Configure your Git to match:

```bash
git config --global init.defaultBranch main
```

---

## Step 5: Configure Line Endings

Line ending mismatches between macOS/Linux and Windows cause noise in diffs.

=== "macOS / Linux"

    ```bash
    git config --global core.autocrlf input
    ```

=== "Windows"

    ```bash
    git config --global core.autocrlf true
    ```

---

## Step 6: Verify Your Configuration

Review all your global settings:

```bash
git config --global --list
```

You should see at minimum:

```
user.name=Your Full Name
user.email=your.email@example.com
core.editor=code --wait
init.defaultbranch=main
core.autocrlf=input
```

---

## Step 7: Create a GitHub Account

If you do not already have a GitHub account:

1. Go to [https://github.com](https://github.com)
2. Click **Sign up**
3. Use your institute email
4. Choose a professional username (e.g., `firstname-lastname` or `flastname`)
5. Complete email verification

**Profile settings (recommended):**

- Add your full name under Settings → Profile
- Add a photo (helps reviewers identify who they are working with)
- Set your organisation affiliation

After creating your account, give your GitHub username to the group maintainer
so they can add you as a collaborator on the group repositories.

---

## Step 8: Verify Git Installation

```bash
git --version      # Should show 2.30 or later
git config --list  # Should show your name, email, editor
```

SSH setup is covered in the next chapter. You are not yet ready to push or pull.

---

## Common Mistakes

1. **Using a personal email instead of the institute email.** Commits will not be
   linked to your GitHub profile correctly, and the group's audit records will be incomplete.

2. **Skipping `user.email`.** Git will warn you on every commit.
3. **Not setting `init.defaultBranch main`.** New repositories will start on `master`
   instead of `main`, causing confusion.

4. **Configuring at repository level instead of global.** Without `--global`,
   settings only apply to the current repository. Use `--global` for all identity settings.

---

## Best Practice Summary

- Run these setup steps on every new machine you use.
- Use your institute email in all Git and GitHub configurations.
- Use VS Code as your Git editor if you already use VS Code for development.
- Verify your setup with `git config --global --list` before proceeding.

---

## Checklist

- [ ] Git is installed (version 2.30+).
- [ ] `user.name` is configured with my full name.
- [ ] `user.email` is configured with my institute email.
- [ ] Default editor is configured.
- [ ] `init.defaultBranch` is set to `main`.
- [ ] Line endings are configured for my OS.
- [ ] GitHub account exists and uses my institute email.
- [ ] I have given my GitHub username to the group maintainer.

---

## Exercises

1. **Verify identity.** Run `git config --global --list` and confirm your name
   and email are set correctly.

2. **Test the editor.** Run `git config --global core.editor` and confirm
   the output is what you set.

3. **GitHub profile.** Log into GitHub, go to Settings → Profile, and add your
   full name and institute affiliation if not already present.
