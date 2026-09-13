"""Tests for the EDR file reader."""

from pathlib import Path

import pytest
from numpy import ndarray

from edrvis.reader import read_edr

DATA_DIR = Path(__file__).parent / "data"


def test_read_edr_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        read_edr(tmp_path / "missing.edr")


def test_edr_assumptions():
    """edrvis assumes data/units keys line up and "Time" is always present."""
    data, units = read_edr(DATA_DIR / "test.edr")

    assert "Time" in data
    assert data.keys() == units.keys()
    assert all(isinstance(values, ndarray) for values in data.values())
    assert all(len(values) > 0 for values in data.values())
