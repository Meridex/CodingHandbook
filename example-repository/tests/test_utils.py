import pytest
from phys_toolkit.utils import (
    gev_to_natural,
    natural_to_gev,
    mev_to_gev,
    gev_to_mev,
    HBAR_C_MEV_FM,
)


def test_mev_gev_roundtrip():
    energy = 125.0  # GeV (Higgs mass)
    assert gev_to_mev(mev_to_gev(energy)) == pytest.approx(energy, rel=1e-12)


def test_gev_to_natural_positive():
    result = gev_to_natural(1.0)
    assert result > 0.0


def test_natural_roundtrip():
    energy_gev = 1.0
    assert natural_to_gev(gev_to_natural(energy_gev)) == pytest.approx(energy_gev, rel=1e-12)


def test_hbar_c_value():
    """hbar*c should be approximately 197.33 MeV·fm."""
    assert HBAR_C_MEV_FM == pytest.approx(197.3269804, rel=1e-6)
