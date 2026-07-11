# Chapter 13 — Testing Policy

## Overview

Testing in research code serves a different purpose than in production software.
The goal is not 100% line coverage — it is **confidence in scientific correctness**.
The tests that matter most are the ones that would catch a wrong equation,
an incorrect numerical method, or a broken algorithm.

This chapter defines the minimum testing requirements for all group repositories.

---

## Philosophy

**Not every line needs a test. Every result that gets published does.**

The following must always have tests:

- Numerical solvers (regression tests with known outputs)
- Any function whose output appears in a paper figure
- Parser and file-loading functions (edge cases and malformed inputs)
- Any function that is non-trivial to inspect visually

The following does not need automated tests:

- Plotting and visualisation functions
- One-time utility scripts
- Simple file path manipulation

---

## What "Tested" Means for Research Code

### Regression Tests

The most important test type for numerical code.
Given a fixed, known input, verify that the output is the expected value.

```python
def test_thermal_correction_known_value():
    """Regression test against Table 1 of Quiros (1999)."""
    phi = 100.0  # GeV
    T = 150.0    # GeV
    g2 = 0.5
    result = thermal_correction(phi, T, g2)
    expected = 3421.7  # From Table 1, Quiros (1999)
    assert abs(result - expected) / expected < 1.0e-4  # 0.01% tolerance
```

Record the source of the expected value in the test docstring.

### Edge Case Tests

Test the boundaries of the valid input domain:

```python
def test_thermal_correction_zero_temperature():
    """Thermal correction must be zero at T=0."""
    result = thermal_correction(phi=100.0, T=0.0, g2=0.5)
    assert result == 0.0

def test_thermal_correction_negative_temperature():
    """Negative temperature must raise ValueError."""
    with pytest.raises(ValueError):
        thermal_correction(phi=100.0, T=-1.0, g2=0.5)
```

### Symmetry and Conservation Tests

Test physical symmetries that must be preserved:

```python
def test_potential_symmetry():
    """Effective potential must be symmetric in phi for Z2-symmetric models."""
    phi = 100.0
    T = 50.0
    assert abs(effective_potential(phi, T) - effective_potential(-phi, T)) < 1.0e-10
```

---

## Testing Framework

**Python:** use `pytest`

```bash
pip install pytest
python -m pytest                    # run all tests
python -m pytest tests/             # run tests directory
python -m pytest tests/test_thermal.py  # run one file
python -m pytest -v                 # verbose output
python -m pytest -k "thermal"       # run tests matching "thermal"
```

**C++:** use [Catch2](https://github.com/catchorg/Catch2)

See `docs/appendices/` for language-specific guidance.

---

## Test Organisation

Tests mirror the `src/` directory structure:

```
src/
    thermal.py
    potential.py
    solver.py
tests/
    test_thermal.py
    test_potential.py
    test_solver.py
```

**File naming:** `test_<module_name>.py` (Python) / `test_<module_name>.cpp` (C++)

**Test function naming:** `test_<what_is_being_tested>_<condition>()`

Examples:

- `test_thermal_correction_known_value()`
- `test_thermal_correction_zero_temperature()`
- `test_potential_minimum_location_at_T0()`

---

## Running Tests Before Opening a PR

**Required:** all tests must pass locally before opening a PR.

```bash
python -m pytest
```

If any test fails, fix it before pushing. A PR that breaks existing tests
will not be approved.

---

## Writing Tests for Review

When reviewing a PR that adds new functionality, check:

- [ ] New functionality has at least one test
- [ ] At least one edge case is tested
- [ ] The test docstring names the source of expected values
- [ ] Tests are in the correct file (`tests/test_<module>.py`)
- [ ] Tests follow the naming convention

If a PR adds a function with no test, request a test as a required change.

---

## CI Integration

Once GitHub Actions is configured (Chapter 14), tests will run automatically
on every PR. Until then, tests run manually.

The manual requirement: **the PR author runs `pytest` before opening the PR**
and reports the result in the PR description ("Testing Performed" section).

---

## Checklist

- [ ] Tests exist for all numerical solvers and critical algorithms
- [ ] Tests exist for all functions referenced in papers
- [ ] Edge cases are covered (zero values, negative inputs, boundary conditions)
- [ ] Tests are in `tests/` directory, mirroring `src/` structure
- [ ] Test functions follow naming convention `test_<what>_<condition>()`
- [ ] Test docstrings cite the source of expected values
- [ ] All tests pass locally before opening a PR
- [ ] PR description reports test results in "Testing Performed" section
