"""Plot widget for displaying EDR quantity timeseries."""

from numpy import ndarray
from textual.app import ComposeResult
from textual.widget import Widget
from textual_plot import HiResMode, PlotWidget


class EdrPlotWidget(Widget):
    """Displays a single EDR quantity vs time."""

    can_focus = False

    def compose(self) -> ComposeResult:
        """Compose the plot widget."""
        yield PlotWidget()

    def show(
        self, data: dict[str, ndarray], units: dict[str, str], quantity: str
    ) -> None:
        """Replot the given quantity against time.

        Args:
            data: EDR data keyed by quantity name.
            units: Units for each quantity keyed by name.
            quantity: The quantity to plot on the y-axis.
        """
        plot = self.query_one(PlotWidget)
        plot.clear()
        plot.plot(x=data["Time"], y=data[quantity], hires_mode=HiResMode.BRAILLE)
        plot.set_xlabel(f"Time ({units['Time']})")
        plot.set_ylabel(f"{quantity} ({units[quantity]})")
