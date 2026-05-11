"""Statistics widget for displaying useful metrics."""

import numpy as np
from numpy import ndarray
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label


class StatsPanel(Widget):
    """Displays a summary of statistics for the selected quantity."""

    DEFAULT_CSS = """
    StatsPanel {
        background: $surface;
    }
    """

    can_focus = False

    def compose(self) -> ComposeResult:
        """Write the statistics labels."""
        yield Label(id="mean")
        yield Label(id="std")
        yield Label(id="min")
        yield Label(id="max")

    def update(self, data: dict[str, ndarray], quantity: str) -> None:
        """Recompute statistics for the new quantity."""
        values = data[quantity]
        mean = np.mean(values)
        std = np.std(values)
        min_ = np.min(values)
        max_ = np.max(values)

        self.query_one("#mean", Label).update(f"Mean: {mean:.5g}")
        self.query_one("#std", Label).update(f"Std: {std:.5g}")
        self.query_one("#min", Label).update(f"Min: {min_:.5g}")
        self.query_one("#max", Label).update(f"Max: {max_:.5g}")
