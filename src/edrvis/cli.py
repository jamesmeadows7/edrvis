"""Command-line entry point for `edrvis`."""

import argparse
from pathlib import Path

from edrvis.reader import read_edr


def main():
    """Entry point for the `edrvis` command."""
    parser = argparse.ArgumentParser(
        prog="edrvis", description="Visualise GROMACS edr files in the terminal."
    )
    parser.add_argument("edr_file", type=Path, help="edr file path")
    args = parser.parse_args()

    edr_path: Path = args.edr_file

    read_edr(edr_path)

    # from edrvis.app import BasicApp

    # app = BasicApp()
    # app.run()
