"""Command-line entry point for ``edrvis``."""

import argparse
from pathlib import Path

from edrvis import __version__
from edrvis.reader import read_edr


def main() -> None:
    """Parse arguments, load EDR data, and launch the TUI."""
    parser = argparse.ArgumentParser(
        prog="edrvis",
        description="Visualise GROMACS EDR files in the terminal.",
    )
    parser.add_argument("edr_path", type=Path, help="edr file path")
    parser.add_argument(
        "--theme",
        choices=["dark", "light"],
        default="light",
        help="colour theme (default: dark)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    args = parser.parse_args()

    edr_path: Path = args.edr_path
    edr_data, edr_units = read_edr(edr_path)

    from edrvis.app import EdrvisApp

    app = EdrvisApp(edr_path, edr_data, edr_units, theme=args.theme)
    app.run()
