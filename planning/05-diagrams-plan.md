# 05 · Diagrams Plan

All diagrams use **Mermaid** so they render natively on GitHub and in MkDocs.
Source lives in `docs/assets/diagrams/`. Each diagram is also embedded inline
in the chapter where it first appears.

---

## Diagram Inventory

### D-01 — Git/GitHub Relationship
**Chapter:** Student Guide Ch. 2
**Type:** `graph LR`

```mermaid
graph LR
    L[Local Repository<br/>your machine] -->|git push| R[GitHub Remote<br/>origin]
    R -->|git pull / git fetch| L
    R -->|git clone| C[New Local Clone<br/>collaborator's machine]
```

**Purpose:** Show that Git is local; GitHub is just a remote host.

---

### D-02 — Full Group Workflow
**Chapter:** Student Guide Ch. 3, Maintainer Guide Ch. 9
**Type:** `flowchart TD`

```mermaid
flowchart TD
    A[Start: git pull origin main] --> B[Create feature branch]
    B --> C[Write code / run simulations]
    C --> D[git add + git commit]
    D --> E{More changes?}
    E -- Yes --> C
    E -- No --> F[git push origin feature/name]
    F --> G[Open Pull Request on GitHub]
    G --> H[Reviewer checks code]
    H --> I{Approved?}
    I -- Changes requested --> J[Address comments]
    J --> D
    I -- Approved --> K[Squash Merge → main]
    K --> L[Delete feature branch]
    L --> M[Done]
```

**Purpose:** The canonical workflow every student must internalise.

---

### D-03 — Branch Graph
**Chapter:** Student Guide Ch. 3, Ch. 8
**Type:** `gitGraph`

```mermaid
gitGraph
   commit id: "Initial setup"
   commit id: "Add base potential"
   branch feature/gw-spectrum
   checkout feature/gw-spectrum
   commit id: "Add GW integrand"
   commit id: "Add spectrum output"
   checkout main
   branch bugfix/interpolation
   checkout bugfix/interpolation
   commit id: "Fix interpolation off-by-one"
   checkout main
   merge bugfix/interpolation id: "Fix interpolation (#7)"
   checkout feature/gw-spectrum
   commit id: "Address review comments"
   checkout main
   merge feature/gw-spectrum id: "Add GW spectrum (#12)"
```

**Purpose:** Show parallel branches and squash merges on `main`.

---

### D-04 — Clone Operation
**Chapter:** Student Guide Ch. 6
**Type:** `sequenceDiagram`

```mermaid
sequenceDiagram
    participant Student
    participant Local as Local Machine
    participant GitHub

    Student->>GitHub: git clone git@github.com:ORG/REPO.git
    GitHub-->>Local: Copy full repository history
    Local-->>Student: Directory created with .git/
    Note over Local: origin/main is now tracking GitHub
```

**Purpose:** Demystify what `git clone` does under the hood.

---

### D-05 — Daily Workflow Loop
**Chapter:** Student Guide Ch. 7
**Type:** `flowchart TD`

```mermaid
flowchart TD
    A[Morning: git pull origin main] --> B[git checkout -b feature/task]
    B --> C[Edit files]
    C --> D[git add files]
    D --> E[git commit -m 'message']
    E --> F{Work session done?}
    F -- No --> C
    F -- Yes --> G[git push origin feature/task]
    G --> H[Open / Update Pull Request]
```

**Purpose:** The loop students repeat every working day.

---

### D-06 — Staging Area Model
**Chapter:** Student Guide Ch. 9
**Type:** `graph LR`

```mermaid
graph LR
    W[Working Directory<br/>files on disk]
    S[Staging Area<br/>git add]
    R[Repository<br/>git commit]
    W -->|git add| S
    S -->|git commit| R
    R -->|git checkout| W
    S -->|git restore --staged| W
```

**Purpose:** Show the three Git states (working / staged / committed).

---

### D-07 — Pull Request Lifecycle
**Chapter:** Student Guide Ch. 11
**Type:** `stateDiagram-v2`

```mermaid
stateDiagram-v2
    [*] --> Draft : Open as draft
    [*] --> Open : Open for review
    Draft --> Open : Mark ready for review
    Open --> ChangesRequested : Reviewer requests changes
    ChangesRequested --> Open : Author pushes fixes
    Open --> Approved : Reviewer approves
    Approved --> Merged : Maintainer squash-merges
    Open --> Closed : Abandoned / rejected
    Merged --> [*]
    Closed --> [*]
```

**Purpose:** Show every possible state of a PR.

---

### D-08 — Conflict Marker Explanation
**Chapter:** Student Guide Ch. 13
**Type:** Text diagram (no Mermaid needed — use annotated code block)

Content: Annotated conflict block showing what `HEAD`, `=======`, and the
branch name mean, with labels indicating "your change" and "their change".

---

### D-09 — Rebase vs Merge
**Chapter:** Student Guide Ch. 14
**Type:** `gitGraph` (two separate diagrams — before/after)

**Before rebase:**
```mermaid
gitGraph
   commit id: "A"
   commit id: "B"
   branch feature/task
   checkout feature/task
   commit id: "X"
   commit id: "Y"
   checkout main
   commit id: "C"
   commit id: "D"
```

**After rebase:**
```mermaid
gitGraph
   commit id: "A"
   commit id: "B"
   commit id: "C"
   commit id: "D"
   branch feature/task
   checkout feature/task
   commit id: "X'"
   commit id: "Y'"
```

**Purpose:** Show why rebase produces a cleaner history.

---

### D-10 — Squash Merge Result
**Chapter:** Maintainer Guide Ch. 9
**Type:** `gitGraph` (before/after)

Show a feature branch with 4 noisy commits (wip, fix, fix2, cleanup) becoming
one clean commit on `main`.

---

### D-11 — Release Timeline
**Chapter:** Maintainer Guide Ch. 10, Ch. 11
**Type:** `timeline` (or `gitGraph` with tags)

```mermaid
gitGraph
   commit id: "Initial"
   commit id: "Feature A"
   commit id: "Feature B" tag: "v0.1.0"
   commit id: "Feature C"
   commit id: "Bug fix" tag: "v0.1.1"
   commit id: "Feature D"
   commit id: "Refactor" tag: "v1.0.0 (paper submission)"
```

**Purpose:** Connect releases and tags to the development timeline.

---

### D-12 — Repository Permission Levels
**Chapter:** Maintainer Guide Ch. 4
**Type:** `graph TD`

```mermaid
graph TD
    A[Admin<br/>PI] --> B[Maintain<br/>Senior Students / Postdocs]
    B --> C[Write<br/>Students]
    C --> D[Read<br/>External Collaborators]
```

**Purpose:** Show the access hierarchy clearly.

---

### D-13 — Repository Lifecycle
**Chapter:** Maintainer Guide Ch. 16, Ch. 17
**Type:** `stateDiagram-v2`

```mermaid
stateDiagram-v2
    [*] --> Private : Repository created
    Private --> ActiveDevelopment : Collaborators added
    ActiveDevelopment --> Private : (continues private)
    ActiveDevelopment --> ReadyForRelease : Paper accepted
    ReadyForRelease --> Public : Maintainer makes public
    Public --> Archived : Development complete
    Archived --> [*]
```

**Purpose:** Show the full lifecycle from creation to archival.

---

### D-14 — CI/CD Pipeline
**Chapter:** Maintainer Guide Ch. 14
**Type:** `flowchart LR`

```mermaid
flowchart LR
    PR[Pull Request / Push] --> CI[GitHub Actions triggered]
    CI --> T[Run pytest]
    T --> P{Pass?}
    P -- Yes --> G[Green checkmark on PR]
    P -- No --> R[Red ✗ — PR cannot merge]
```

**Purpose:** Explain CI visually before showing YAML.

---

## Diagram Production Notes

- All diagrams are written as raw Mermaid in the Markdown files.
- MkDocs + `mkdocs-material` theme renders Mermaid natively with the
  `pymdownx.superfences` extension.
- For GitHub rendering: Mermaid renders in `.md` files as of 2022.
- Export to SVG only if a diagram is needed in a printed document.
- Every diagram has a figure caption below it: `*Figure N: Description.*`
