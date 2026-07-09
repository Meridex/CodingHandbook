# Chapter 12 — Documentation Policy

## Overview

Documentation is not optional — it is part of the research output.
A function that implements an equation from a paper but has no reference
to that equation is scientifically incomplete. Code that runs but cannot
be understood is not reproducible.

This chapter defines the minimum documentation standards for all group repositories.

---

## What Must Be Documented

### 1. Every Public Function and Class

Every function or class that other code calls must have a docstring.
The docstring must include:
- **Purpose:** what the function does in one sentence
- **Parameters:** name, type, meaning, and expected range for each parameter
- **Return value:** type and meaning
- **Reference:** the equation number or paper if implementing a specific formula

**Python (NumPy-style docstrings):**

```python
def thermal_correction(phi, T, g_squared):
    """
    Compute the one-loop thermal correction to the effective potential.

    Implements Eq. 3.7 of Quiros (1999), arXiv:hep-ph/9901312.
    Active only when T > 0.

    Parameters
    ----------
    phi : float or ndarray
        Field value in GeV.
    T : float
        Temperature in GeV. Must be >= 0.
    g_squared : float
        Squared gauge coupling constant. Must be > 0.

    Returns
    -------
    float or ndarray
        Thermal correction to V_eff in GeV^4. Zero if T == 0.

    Raises
    ------
    ValueError
        If g_squared <= 0 or T < 0.
    """
```

**C++ (Doxygen-style comments):**

```cpp
/**
 * @brief Compute the one-loop thermal correction to the effective potential.
 *
 * Implements Eq. 3.7 of Quiros (1999), arXiv:hep-ph/9901312.
 *
 * @param phi Field value in GeV.
 * @param T   Temperature in GeV. Must be >= 0.
 * @param g2  Squared gauge coupling constant. Must be > 0.
 * @return    Thermal correction in GeV^4.
 */
double thermal_correction(double phi, double T, double g2);
```

### 2. Every Non-Obvious Algorithm

Any non-trivial numerical method must include:
- A citation to the source paper or textbook
- The equation number being implemented
- Any assumptions or approximations made

```python
# Implements the Arnold-McLerran resummation scheme.
# See Arnold & McLerran, Phys. Rev. D 36, 581 (1987), Eq. (2.14).
# Approximation: valid only for T >> phi (high-temperature expansion).
```

### 3. Every Script

Analysis scripts and run scripts must begin with a header comment:

```python
#!/usr/bin/env python3
"""
generate_phase_diagram.py — Generate the phase diagram for Fig. 2 of arXiv:2601.12345.

Usage:
    python generate_phase_diagram.py --output figs/phase_diagram.pdf

Arguments:
    --output : Path to save the output figure (PDF).
    --T-min  : Minimum temperature in GeV (default: 0.0).
    --T-max  : Maximum temperature in GeV (default: 300.0).

Requirements:
    Python >= 3.10, numpy, matplotlib, scipy.
    Run `pip install -r requirements.txt` to install dependencies.
"""
```

### 4. Every Configuration File

Configuration files (`.yaml`, `.toml`, `.json`, `.ini`) must include inline comments:

```yaml
# Numerical solver configuration
solver:
  tolerance: 1.0e-8    # Convergence criterion for the iterative solver
  max_iterations: 1000  # Maximum iterations before declaring non-convergence
  grid_points: 512      # Number of field-space grid points (power of 2 recommended)
```

---

## The README Must Stay Current

The README is the first thing a new user reads. It must accurately reflect the
current state of the code.

Review the README when:
- A new feature significantly changes usage
- Installation instructions change
- Dependencies are updated
- A paper is published (add citation)

Apply the [README template](../templates/README-template.md).

---

## MkDocs: The Handbook Site

The `docs/` folder in this handbook is built into the MkDocs site.
All Markdown files in `docs/` are part of the documentation site.

When adding a significant new feature or module, add a corresponding page
to `docs/` describing its physics motivation, API, and example usage.
Update `mkdocs.yml` to include the new page in the navigation.

---

## Deprecation Policy

When removing or changing a public interface:

1. In the release **before** removal, mark it as deprecated:

   ```python
   import warnings

   def old_function(args):
       warnings.warn(
           "old_function is deprecated and will be removed in v2.0.0. "
           "Use new_function instead.",
           DeprecationWarning,
           stacklevel=2
       )
       return new_function(args)
   ```

2. Document the deprecation in release notes.
3. Remove in the next MAJOR version bump.

---

## Documentation Review in PRs

Documentation is part of the review checklist (Chapter 8).
A PR that adds a function without a docstring should not be approved.

Specifically check:
- [ ] New public functions have docstrings with parameter and return docs
- [ ] Non-obvious algorithms reference their source equation/paper
- [ ] New scripts have header comments with usage
- [ ] README updated if user-facing behaviour changed

---

## Checklist

- [ ] All public functions have docstrings (purpose, parameters, returns, reference)
- [ ] All non-trivial algorithms cite the source equation/paper inline
- [ ] All scripts have usage header comments
- [ ] All configuration files have inline comments
- [ ] README reflects the current code state
- [ ] New significant features have a corresponding page in `docs/`
- [ ] Documentation reviewed as part of every PR
