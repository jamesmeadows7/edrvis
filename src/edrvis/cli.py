"""Command-line entry point for ``edrvis``."""

import argparse
from pathlib import Path

from edrvis import __version__
from edrvis.reader import read_edr


def positive_int(value: str) -> int:
    """Parse an int and reject zero/negative values."""
    n = int(value)
    if n < 1:
        raise argparse.ArgumentTypeError(f"must be a positive integer, got {value!r}")
    return n


def build_parser() -> argparse.ArgumentParser:
    """Build the ``edrvis`` command-line argument parser."""
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
        "--n-blocks",
        type=positive_int,
        default=5,
        help="number of blocks for the error estimate (default: 5)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main() -> None:
    """Parse arguments, load EDR data, and launch the TUI."""
    args = build_parser().parse_args()

    edr_path: Path = args.edr_path
    edr_data, edr_units = read_edr(edr_path)

    from edrvis.app import EdrvisApp

    app = EdrvisApp(
        edr_path, edr_data, edr_units, theme=args.theme, n_blocks=args.n_blocks
    )
    app.run()
