"""EDR file reading utilities."""

from pathlib import Path

import pyedr
from numpy import ndarray


def read_edr(edr_path: Path) -> tuple[dict[str, ndarray], dict[str, str]]:
    if not edr_path.exists():
        raise FileNotFoundError(f"EDR file not found at {edr_path}.")

    edr_data: dict[str, ndarray] = pyedr.edr_to_dict(str(edr_path))
    edr_units: dict[str, str] = pyedr.get_unit_dictionary(str(edr_path))

    return edr_data, edr_units
