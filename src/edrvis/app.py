from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual_plot import PlotWidget


class BasicApp(App):
    """A basic app to learn how to use Textual."""

    TITLE = "edrvis"
    SUB_TITLE = "visualise gromacs edr files"
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield PlotWidget()

    def on_mount(self) -> None:
        plot = self.query_one(PlotWidget)
        plot.plot(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
