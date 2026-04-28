"""Command-line entry point for `edrvis`."""

import argparse
from pathlib import Path

from edrvis.reader import read_edr


def main():
    """Entry point for the `edrvis` command."""
    # parse arguments
    parser = argparse.ArgumentParser(
        prog="edrvis", description="Visualise GROMACS edr files in the terminal."
    )
    parser.add_argument("edr_path", type=Path, help="edr file path")
    args = parser.parse_args()

    # read edr file
    edr_path = args.edr_path
    edr_data, edr_units = read_edr(edr_path)

    # build app
    from edrvis.app import BasicApp

    app = BasicApp(edr_path, edr_data, edr_units)
    app.run()
