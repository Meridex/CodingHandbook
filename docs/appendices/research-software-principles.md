# Research Software Principles

This appendix articulates the principles that underlie the group's development practices.
Understanding **why** the practices exist makes them easier to follow and helps you apply
good judgment in situations the handbook does not explicitly cover.

---

## 1. Reproducibility Is Non-Negotiable

A computational result that cannot be reproduced is not science.

In experimental physics, reproducibility means another lab can repeat the experiment
with the same equipment and method. In computational physics, reproducibility means:

- The exact code that produced a figure or result can be identified (via tags)
- The exact input parameters are recorded (in configuration files, not hardcoded)
- The code can be run again to produce the same output (deterministic by default)
- The environment (Python version, library versions) is documented

**Practical implication:** Tag every published figure. Archive every paper submission.
Never overwrite results without preserving the code state that produced them.

---

## 2. Code Is a Scientific Artifact

Code that implements a physical model is as much a scientific artifact as the
paper that describes it. It deserves the same level of care, documentation,
and peer review.

Consequences:

- Code review is peer review, not gatekeeping.
- A function without a citation to its source equation is incomplete.
- "It works on my machine" is not scientific validation.
- Code that no one else understands cannot be continued or verified by the group.

---

## 3. Clarity Over Cleverness

Research code is read far more often than it is written — by colleagues,
by your future self, and potentially by the scientific community after publication.

Write code that communicates intent:

```python
# Unclear:
V = phi**4 / 4 + mu2 * phi**2 / 2 + g2 * T**2 * phi**2 / 24

# Clear:
tree_level_potential = phi**4 / 4 + (mu_squared / 2) * phi**2
thermal_mass_term = (g_squared * T**2 / 24) * phi**2
V = tree_level_potential + thermal_mass_term
```

Variable names, function names, and comments are part of the documentation.
They should reflect the physics, not the implementation.

---

## 4. Version Control Is a Research Tool

Version control is not for programmers — it is for anyone who produces
files that change over time and whose history matters.

In this group, version control applies to:

- Simulation code
- Analysis scripts
- Figure-generation scripts
- Parameter configuration files
- LaTeX manuscripts (in some cases)
- This handbook

**Not** managed by the group's repositories:

- Raw experimental data (managed separately)
- Large simulation outputs (referenced by path, not stored in Git)
- Binary assets and generated figures (regenerated from code)

---

## 5. The Group Uses One Workflow

Consistency across the group matters more than any individual's preferred workflow.

The canonical workflow in this handbook is not the only valid approach to Git.
There are many legitimate alternatives. We use one because:

- Onboarding is faster when everyone does the same thing
- Code review is easier when history has a predictable structure
- Debugging is faster when `git log` is clean and squashed
- The workflow can be improved collectively over time

If you believe a convention should change, propose it via a PR to this handbook.
Do not silently deviate.

---

## 6. Write Tests for Things That Go in Papers

The minimum testing bar for research code is not code coverage percentage —
it is: *can you trust the results enough to put them in a paper?*

Practically, this means:

- Every numerical result that appears in a figure must have a test
- Every equation implementation must be validated against a known special case
- Every bug fix must be accompanied by a regression test

A test that catches a wrong sign before the paper is submitted saves months.

---

## 7. Documentation Is Respect

Undocumented code is a burden placed on every future reader, including your
future self. Documenting your work is an act of respect for your collaborators
and the scientific community.

Minimum documentation standards:

- Every function explains what it does and what its parameters mean
- Every non-trivial algorithm cites its source
- Every repository has a README that a newcomer can follow

---

## 8. Small, Focused Changes

Large, unfocused changes are hard to review, hard to debug, and risky to merge.

- One PR per logical change
- One commit per atomic unit of work
- One branch per task

When a change requires touching many parts of the codebase, consider whether
it should be split across multiple sequential PRs.

---

## 9. Fail Loudly, Fix Clearly

When code encounters an unexpected state (negative temperature, singular matrix,
out-of-bounds index), it should:

1. **Fail explicitly** — raise an exception with a clear message
2. **Not silently produce wrong results**

```python
# Silently wrong:
if T < 0:
    T = 0  # "fix" without telling anyone

# Explicit:
if T < 0:
    raise ValueError(f"Temperature must be >= 0, got T={T}")
```

A visible failure is always easier to debug than a silent one that propagates
into a published figure.

---

## 10. The Handbook Is a Living Document

This handbook describes current best practices. It will need to change as:

- The group grows
- New tools become available
- Current practices are found to be ineffective

Suggestions for improvement are welcome via Pull Request.
The handbook is itself maintained using the workflow it describes.
