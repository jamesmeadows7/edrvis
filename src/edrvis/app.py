"""Textual application for visualising GROMACS EDR files."""

from pathlib import Path

from numpy import ndarray
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual_plot import HiResMode, PlotWidget


class EdrvisApp(App):
    """Textual application for visualising GROMACS EDR files."""

    TITLE = "edrvis"
    BINDINGS = [("q", "quit", "Quit")]

    def __init__(
        self,
        edr_path: Path,
        edr_data: dict[str, ndarray],
        edr_units: dict[str, str],
    ) -> None:
        """Initialise app with pre-loaded EDR data."""
        super().__init__()
        self._edr_path = edr_path
        self._data = edr_data
        self._units = edr_units

    def compose(self) -> ComposeResult:
        """Compose the widget layout."""
        yield Header()
        yield Footer()
        yield PlotWidget()

    def on_mount(self) -> None:
        """Populate plot once app is mounted."""
        self.sub_title = self._edr_path.name
        plot = self.query_one(PlotWidget)
        plot.plot(
            x=self._data["Time"],
            y=self._data["Bond"],
            hires_mode=HiResMode.BRAILLE,
        )
        plot.set_xlabel("Time")
        plot.set_ylabel("Temp.")
