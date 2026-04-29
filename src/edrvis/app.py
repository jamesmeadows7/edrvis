"""Textual application for visualising GROMACS EDR files."""

from pathlib import Path

from numpy import ndarray
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from edrvis.widgets.plot import EdrPlotWidget
from edrvis.widgets.sidebar import QuantityChanged, Sidebar


class EdrvisApp(App):
    """Textual application for visualising GROMACS EDR files."""

    TITLE = "edrvis"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("j", "next_quantity", "Next"),
        ("k", "prev_quantity", "Previous"),
    ]
    CSS_PATH = "app.tcss"

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
        yield Sidebar()
        yield EdrPlotWidget()
        yield Footer()

    def on_mount(self) -> None:
        """Populate the sidebar and plot the first quantity."""
        self.sub_title = self._edr_path.name
        quantities = [k for k in self._data if k != "Time"]
        sidebar = self.query_one(Sidebar)
        sidebar.populate(quantities)
        self.query_one(EdrPlotWidget).show(self._data, self._units, quantities[0])

    def on_quantity_changed(self, message: QuantityChanged) -> None:
        """Replot when selected quantity changes."""
        self.query_one(EdrPlotWidget).show(self._data, self._units, message.quantity)

    def action_next_quantity(self) -> None:
        """Move sidebar selection down."""
        self.query_one(Sidebar).select_next()

    def action_prev_quantity(self) -> None:
        """Move sidebar selection up."""
        self.query_one(Sidebar).select_prev()
