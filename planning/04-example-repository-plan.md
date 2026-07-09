# 04 · Example Repository Plan

The example repository is a self-contained practice environment for students to
complete handbook exercises. It must be realistic enough to feel like a real
research project but simple enough that students can focus on Git workflow rather
than physics.

---

## Purpose

- Provide a safe sandbox where mistakes have no consequences.
- Mirror the structure of a real group repository.
- Support all 10 exercises in Student Guide Chapter 18.
- Demonstrate good README, docstring, and commit style.

---

## Repository Structure

```text
example-repository/
├── README.md
├── .gitignore              ← Python + C++ + common editors
├── requirements.txt        ← Minimal Python deps (numpy, pytest)
├── setup.cfg               ← Minimal package definition
├── src/
│   └── phys_toolkit/
│       ├── __init__.py
│       ├── potential.py    ← Simple 1D potential energy function
│       ├── solver.py       ← Simple numerical integrator
│       └── utils.py        ← Unit conversion helpers
├── tests/
│   ├── test_potential.py
│   ├── test_solver.py
│   └── test_utils.py
├── docs/
│   └── index.md            ← Mini-handbook for the example project
├── examples/
│   ├── basic_usage.py      ← Minimal working example
│   └── plot_potential.py   ← Visualise the potential (requires matplotlib)
├── scripts/
│   └── run_scan.py         ← Example parameter scan script
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.yml
    │   └── feature_request.yml
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
        └── tests.yml       ← Run pytest on every push/PR
```

---

## Physics Content (intentionally simple)

To keep the focus on Git, the physics is deliberately minimal:

- **`potential.py`**: A quartic polynomial $V(\phi) = -\mu^2 \phi^2 + \lambda \phi^4$.
  - Parameters: `mu`, `lambda_`.
  - Methods: `evaluate(phi)`, `minimum()`, `barrier_height()`.
- **`solver.py`**: Simple bisection root-finder.
  - Finds the non-trivial minimum of `V`.
- **`utils.py`**: Conversion helpers (e.g., GeV ↔ natural units).

This is enough to have meaningful commits, tests, and PR descriptions without
requiring physics knowledge to understand the code.

---

## Pre-populated Git History

The example repository should be initialised with a realistic commit history:

```
* a1b2c3d  (main) Add parameter scan script
* d4e5f6a  Add unit tests for solver module
* 7g8h9i0  Implement bisection solver
* b1c2d3e  Add quartic potential class
* f4a5b6c  Add unit conversion utilities
* 0d1e2f3  Initial project structure
```

This history serves as a reference for what "good commits" look like.

---

## Seeded Issues (for exercises)

Create these issues in the example repository so students have real tasks:

| # | Title | Label | Description |
|---|-------|-------|-------------|
| 1 | Fix sign error in `barrier_height()` | `type: bugfix` | Returns negative value when it should be positive |
| 2 | Add `second_derivative()` method to potential | `type: feature` | Needed for stability analysis |
| 3 | Improve docstrings in `utils.py` | `type: docs` | Currently missing parameter descriptions |
| 4 | Add test for zero-barrier case | `type: feature` | Edge case not covered |
| 5 | Rename `lambda_` to `lam` for PEP8 style | `type: refactor` | Cosmetic change only |

---

## Seeded Conflicts (for conflict-resolution exercise)

Create a branch `conflict-branch` that modifies the same lines in `potential.py`
as a change already on `main`. Students must resolve the conflict as part of
Exercise 7.

---

## `.gitignore` Content

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.eggs/
.pytest_cache/
.mypy_cache/
venv/
.venv/

# C++
*.o
*.so
*.a
*.out

# Jupyter
.ipynb_checkpoints/

# Data and outputs
*.dat
*.hdf5
*.h5
*.csv
data/
output/
results/

# OS
.DS_Store
Thumbs.db

# Editors
.idea/
.vscode/
*.swp
```

---

## README for Example Repository

The README should:
1. Explain this is a practice repository for handbook exercises.
2. Show the physics context in one sentence.
3. Give install instructions (`pip install -e .`).
4. Show a quick-start example.
5. List the exercises and link to the handbook.
6. Explicitly state: "Make mistakes here — that is the point."

---

## CI Workflow (`tests.yml`)

```yaml
name: Tests
on:
  push:
    branches: ["**"]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -e ".[test]"
      - name: Run tests
        run: pytest --tb=short
```

This gives students immediate feedback on whether their changes break anything.
