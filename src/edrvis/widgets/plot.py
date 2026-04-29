"""Plot widget for displaying EDR quantity timeseries."""

from numpy import ndarray
from textual.app import ComposeResult
from textual.widget import Widget
from textual_plotext import PlotextPlot


class EdrPlotWidget(Widget):
    """Displays a single EDR quantity vs time."""

    can_focus = False

    def compose(self) -> ComposeResult:
        """Compose the plot widget."""
        yield PlotextPlot()

    def show(
        self, data: dict[str, ndarray], units: dict[str, str], quantity: str
    ) -> None:
        """Replot the given quantity against time.

        Args:
            data: EDR data keyed by quantity name.
            units: Units for each quantity keyed by name.
            quantity: The quantity to plot on the y-axis.
        """
        plot_widget = self.query_one(PlotextPlot)
        plt = plot_widget.plt
        plt.clear_figure()
        plt.plot(list(data["Time"]), list(data[quantity]), marker="braille")
        plt.xlabel(f"Time ({units['Time']})")
        unit = "no units" if units[quantity] == "" else units[quantity]
        plt.ylabel(f"units: {unit}")
        plot_widget.refresh()
