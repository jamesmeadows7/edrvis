"""Statistics dataclass and helper functions."""

from dataclasses import dataclass

import numpy as np
from numpy import ndarray


@dataclass(frozen=True, slots=True)
class SummaryStats:
    """Summary statistics for a single thermodynamic quantity."""

    mean: float
    std: float
    err_est: float
    tot_drift: float
    min: float
    max: float


def block_error_estimate(values: ndarray, n_blocks: int = 5) -> float:
    """Compute standard error of the mean, using `n_blocks`."""
    block_means = np.array([block.mean() for block in np.array_split(values, n_blocks)])
    return float(block_means.std(ddof=1) / np.sqrt(n_blocks))


def total_drift(values: ndarray, time: ndarray) -> float:
    """Compute total drift from a least-squares fit."""
    if len(values) < 2:
        return 0.0
    slope, intercept = np.polyfit(time, values, 1)
    return float((slope * time[-1] + intercept) - (slope * time[0] + intercept))


def summarise(values: ndarray, time: ndarray, n_blocks: int) -> SummaryStats:
    """Compute mean, std, error estimate, total drift, min and max for `values`."""
    return SummaryStats(
        mean=np.mean(values),
        std=np.std(values),
        err_est=block_error_estimate(values, n_blocks),
        tot_drift=total_drift(values, time),
        min=np.min(values),
        max=np.max(values),
    )
