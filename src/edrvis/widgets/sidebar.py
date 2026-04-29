"""Sidebar widget for navigating EDR energy quantities."""

from textual.message import Message
from textual.widgets import Label, ListItem, ListView


class QuantityChanged(Message):
    """Message when the selected quantity changes."""

    def __init__(self, quantity: str) -> None:
        super().__init__()
        self.quantity = quantity


class Sidebar(ListView):
    """Scrollable list of EDR quantity names."""

    def populate(self, quantities: list[str]) -> None:
        """Populate the list with quantity names."""
        for quantity in quantities:
            self.append(ListItem(Label(quantity)))

    def select_next(self) -> None:
        """Move selection down one item."""
        current = self.index or 0
        next_index = min(current + 1, len(self.children) - 1)
        self.index = next_index
        self._post_quantity_changed()

    def select_prev(self) -> None:
        """Move selection up one item."""
        current = self.index or 0
        prev_index = max(current - 1, 0)
        self.index = prev_index
        self._post_quantity_changed()

    def _post_quantity_changed(self) -> None:
        """Post a QuantityChanged message for the current selection."""
        assert self.index is not None
        item = self.children[self.index]
        quantity = str(item.query_one(Label).content)
        self.post_message(QuantityChanged(quantity))
