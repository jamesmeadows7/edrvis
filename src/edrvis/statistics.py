from dataclasses import dataclass

import numpy as np
from numpy import ndarray


@dataclass(frozen=True, slots=True)
class SummaryStats:
    mean: float
    std: float
    min: float
    max: float


def summarise(values: ndarray) -> SummaryStats:
    return SummaryStats(
        mean=np.mean(values), std=np.std(values), min=np.min(values), max=np.max(values)
    )
