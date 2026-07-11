# Chapter 5 — SSH Authentication

## Overview: Why SSH?

To push and pull from GitHub, you need to authenticate.
GitHub supports two protocols: HTTPS and SSH.

**This group uses SSH exclusively.**

Why SSH over HTTPS?

| | SSH | HTTPS |
|--|-----|-------|
| Authentication | Key pair (no password typing) | Personal Access Token or password |
| Daily experience | Silent, automatic | Token required or password prompt |
| Security | Private key never leaves your machine | Token must be stored or re-entered |
| Group policy | **Required** | Not used |

Once SSH is configured, every `git push` and `git pull` works silently
without entering a password. This matters when running automated scripts
or long analysis pipelines.

---

## Step 1: Check for Existing SSH Keys

Before generating new keys, check if you already have one:

```bash
ls -la ~/.ssh
```

Look for files named:

- `id_ed25519` and `id_ed25519.pub` (recommended)
- `id_rsa` and `id_rsa.pub` (older, acceptable)

If these files exist, you may already have SSH keys configured.
Skip to Step 3 to check if they are already added to GitHub.

---

## Step 2: Generate a New SSH Key Pair

If you do not have an SSH key, generate one:

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Replace `your.email@example.com` with your institute email (same as in `git config`).

You will be prompted:

```
Enter file in which to save the key (/Users/you/.ssh/id_ed25519):
```

Press **Enter** to accept the default location.

```
Enter passphrase (empty for no passphrase):
```

!!! tip "Passphrase recommendation"
    Setting a passphrase adds an extra layer of security. If you use macOS Keychain
    (Step 4), you only need to enter the passphrase once per login session.
    For shared or less-secure machines, always use a passphrase.

Two files are created:

| File | Type | Contents |
|------|------|---------|
| `~/.ssh/id_ed25519` | **Private key** | Secret — never share, never upload |
| `~/.ssh/id_ed25519.pub` | **Public key** | Safe to share — this goes to GitHub |

!!! danger "Never upload your private key"
    The private key (`id_ed25519`, without `.pub`) must never be shared with anyone
    or uploaded anywhere. The public key (`.pub`) is what goes on GitHub.

---

## Step 3: Add the Public Key to GitHub

1. Copy your public key to the clipboard:

    === "macOS"
        ```bash
        pbcopy < ~/.ssh/id_ed25519.pub
        ```

    === "Linux"
        ```bash
        cat ~/.ssh/id_ed25519.pub
        # Then select and copy the output
        ```

    === "Windows (Git Bash)"
        ```bash
        clip < ~/.ssh/id_ed25519.pub
        ```

2. Go to [https://github.com/settings/keys](https://github.com/settings/keys)

3. Click **New SSH key**

4. Fill in:
   - **Title:** A descriptive name for this machine (e.g., `MacBook Pro Lab 2024`, `Cluster Login Node`)
   - **Key type:** Authentication Key
   - **Key:** Paste the public key (starts with `ssh-ed25519`)

5. Click **Add SSH key**

---

## Step 4: Start the SSH Agent and Add Your Key

The SSH agent manages your keys so you do not need to unlock the passphrase repeatedly.

=== "macOS"

    macOS integrates SSH keys with the system Keychain.
    Add these lines to your `~/.ssh/config` file (create it if it does not exist):

    ```
    Host github.com
        AddKeysToAgent yes
        UseKeychain yes
        IdentityFile ~/.ssh/id_ed25519
    ```

    Then add the key to the Keychain:

    ```bash
    ssh-add --apple-use-keychain ~/.ssh/id_ed25519
    ```

=== "Linux"

    Start the agent and add your key:

    ```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```

    To persist across sessions, add the `ssh-add` line to your `~/.bashrc` or `~/.zshrc`.

=== "Windows (Git Bash)"

    ```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```

---

## Step 5: Test the Connection

```bash
ssh -T git@github.com
```

Expected output:

```
Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see your GitHub username in this message, SSH is working correctly.

!!! warning "First connection fingerprint"
    On first connection, you may see:
    ```
    The authenticity of host 'github.com' can't be established.
    Are you sure you want to continue connecting (yes/no)?
    ```
    Type `yes`. This adds GitHub to your `~/.ssh/known_hosts`.

---

## Multiple Machines

Each machine needs its own SSH key. Repeat this process on every computer you use
to work with group repositories. Each machine's public key must be added to your
GitHub account separately.

There is no security benefit to sharing a key between machines — on the contrary,
if a machine is compromised, you want to be able to revoke only that machine's key.

---

## What to Do If SSH Fails

If `ssh -T git@github.com` does not return your username:

1. **Check that the public key is on GitHub:**
   Go to [https://github.com/settings/keys](https://github.com/settings/keys)
   and verify the key is listed.

2. **Check the SSH agent is running:**
   ```bash
   ssh-add -l
   ```
   If it says "no identities", run `ssh-add ~/.ssh/id_ed25519`.

3. **Verbose mode for diagnosis:**
   ```bash
   ssh -vT git@github.com
   ```
   Look for lines beginning with `debug1: Offering public key`.

4. **Ask the maintainer.** SSH issues are common on first setup.
   Do not spend more than 30 minutes troubleshooting alone.

---

## Common Mistakes

1. **Uploading the private key** (`id_ed25519` without `.pub`) to GitHub.
   This is a serious security error. Delete the key from GitHub immediately
   and generate a new key pair.

2. **Forgetting to start `ssh-agent`.** The key must be loaded into the agent.
3. **One key for multiple people.** Every person must have their own key.
4. **Copying only part of the public key.** The entire `.pub` file content
   (one long line starting with `ssh-ed25519`) must be copied.

---

## Best Practice Summary

- Use `ed25519` key type (more secure than RSA).
- Use a passphrase on machines others have physical access to.
- Add a descriptive title when adding keys to GitHub (machine name and year).
- Each machine gets its own key; revoke keys for machines you no longer use.
- Never share or upload the private key.

---

## Checklist

- [ ] SSH key pair generated (`~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub` exist).
- [ ] Public key added to GitHub under Settings → SSH keys.
- [ ] SSH agent configured for my OS.
- [ ] `ssh -T git@github.com` returns my username.

---

## Exercises

1. **Test SSH.** Run `ssh -T git@github.com` and confirm your username appears.

2. **Check multiple keys (if applicable).** Run `ssh-add -l` to list all keys
   currently loaded in the agent. Verify your key is listed.

3. **Review GitHub keys.** Go to GitHub → Settings → SSH and GPG keys.
   Verify the key for your current machine is listed with an appropriate title.
   Remove any keys for machines you no longer use.
