"""Tests for statistics module."""

from pathlib import Path

import numpy as np
import pytest

from edrvis.reader import read_edr
from edrvis.statistics import block_error_estimate, summarise, total_drift

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture(scope="session")
def edr_data():
    """Real quantity data loaded from the test.edr file."""
    data, _ = read_edr(DATA_DIR / "test.edr")
    return data


def test_block_error_estimate_changes_with_n_blocks():
    rng = np.random.default_rng(0)
    values = rng.normal(size=50)

    err_3 = block_error_estimate(values, n_blocks=3)
    err_5 = block_error_estimate(values, n_blocks=5)

    assert err_3 != err_5


def test_block_error_estimate_single_block_is_undefined():
    with pytest.warns(RuntimeWarning):
        result = block_error_estimate(np.arange(10.0), n_blocks=1)
    assert np.isnan(result)


def test_total_drift_needs_at_least_two_points():
    assert total_drift(np.array([1.0]), np.array([0.0])) == 0.0


def test_summarise_constant_series():
    """A constant series should have no spread, error, or drift."""
    values = np.full(20, 5.0)
    time = np.arange(20)
    stats = summarise(values, time, n_blocks=5)

    assert stats.std == 0.0
    assert stats.err_est == 0.0
    assert stats.tot_drift == pytest.approx(0.0)


def test_summarise_linear_ramp():
    time = np.arange(100.0)
    values = time.copy()

    stats = summarise(values, time, n_blocks=5)

    assert stats.tot_drift == pytest.approx(99.0)


def test_summarise_real_data_is_internally_consistent(edr_data):
    values = edr_data["Bond"]
    time = edr_data["Time"]
    stats = summarise(values, time, n_blocks=5)

    assert stats.min <= stats.mean <= stats.max
    assert stats.err_est >= 0


# Reference values from `gmx energy` (single precision).
# (quantity, Average, Err.Est., RMSD, Tot-Drift)
GMX_ENERGY_REFERENCE = [
    ("Bond", 60.5528, 1.1, 22.1144, 1.34608),
    ("Potential", 1057.49, 5.8, 68.4837, -23.3841),
    ("Kinetic En.", 209.63, 5.6, 61.3686, -15.238),
    ("Total Energy", 1267.11, 11, 123.873, -38.6221),
    ("Temperature", 471.262, 13, 137.961, -34.2562),
]


@pytest.mark.parametrize(
    ("quantity", "average", "err_est", "rmsd", "tot_drift"), GMX_ENERGY_REFERENCE
)
def test_summarise_matches_gmx_energy(
    edr_data, quantity, average, err_est, rmsd, tot_drift
):
    stats = summarise(edr_data[quantity], edr_data["Time"], n_blocks=5)

    assert stats.mean == pytest.approx(average, rel=1e-3)
    assert stats.std == pytest.approx(rmsd, rel=1e-3)
    # looser tolerance: different block-splitting algorithm
    assert stats.err_est == pytest.approx(err_est, rel=0.05)
    # looser tolerance: gmx energy ran in single precision
    assert stats.tot_drift == pytest.approx(tot_drift, rel=1e-2)
