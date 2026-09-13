"""Statistics widget for displaying useful metrics."""

from numpy import ndarray
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label

from edrvis.statistics import summarise


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
        yield Label(id="err_est")
        yield Label(id="tot_drift")
        yield Label(id="min")
        yield Label(id="max")

    def update(self, data: dict[str, ndarray], quantity: str, n_blocks: int) -> None:
        """Recompute statistics for the new quantity."""
        stats = summarise(data[quantity], data["Time"], n_blocks)
        self.query_one("#mean", Label).update(f"Mean: {stats.mean:.5g}")
        self.query_one("#std", Label).update(f"Std: {stats.std:.5g}")
        self.query_one("#err_est", Label).update(f"Err. Est.: {stats.err_est:.5g}")
        self.query_one("#tot_drift", Label).update(f"Tot. Drift: {stats.tot_drift:.5g}")
        self.query_one("#min", Label).update(f"Min: {stats.min:.5g}")
        self.query_one("#max", Label).update(f"Max: {stats.max:.5g}")
