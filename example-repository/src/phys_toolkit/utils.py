"""Unit conversion helpers for high-energy physics calculations.

.. note::
    Docstrings in this module are intentionally incomplete (Issue #3).
    A handbook exercise asks students to improve them.
"""

# Natural units: hbar * c = 197.3269804 MeV * fm
HBAR_C_MEV_FM = 197.3269804  # MeV·fm


def gev_to_natural(energy_gev: float) -> float:
    """Convert energy from GeV to natural units (hbar = c = 1).

    Parameters
    ----------
    energy_gev : float

    Returns
    -------
    float
    """
    return energy_gev * 1e3 / HBAR_C_MEV_FM


def natural_to_gev(energy_natural: float) -> float:
    """Convert energy from natural units back to GeV."""
    return energy_natural * HBAR_C_MEV_FM / 1e3


def mev_to_gev(energy_mev: float) -> float:
    """Convert MeV to GeV."""
    return energy_mev * 1e-3


def gev_to_mev(energy_gev: float) -> float:
    """Convert GeV to MeV."""
    return energy_gev * 1e3
