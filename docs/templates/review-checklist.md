# Review Checklist

Use this checklist when reviewing a pull request. Leave a comment for each item
that needs attention. You do not need to block the PR for minor style issues —
use your judgment.

---

## Scientific Correctness

- [ ] The algorithm matches the described method
- [ ] Units and conventions are consistent
- [ ] Edge cases are handled (zero, negative, large values)
- [ ] Results validated against known limit or reference

## Code Quality

- [ ] Code is readable without needing to ask the author
- [ ] No dead code (commented-out blocks, unused variables)
- [ ] No debug print statements or hardcoded paths
- [ ] No generated or binary files committed

## Correctness

- [ ] Code compiles / runs without errors
- [ ] Tests pass (run locally if needed)
- [ ] No obvious bugs in logic

## Documentation

- [ ] Docstrings present for all new public functions
- [ ] Inline comments on non-obvious logic
- [ ] README updated if installation/usage changed
- [ ] CHANGELOG or release notes updated (if applicable)

## Style

- [ ] Naming is clear and consistent with the rest of the codebase
- [ ] Formatting follows group conventions

## Process

- [ ] PR description is complete (motivation, summary, testing)
- [ ] Branch is up to date with `main`
- [ ] Related issue is linked
