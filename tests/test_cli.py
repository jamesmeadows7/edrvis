"""Tests for command-line argument parsing."""

import argparse

import pytest

from edrvis.cli import build_parser, positive_int


def test_positive_int_accepts_positive_values():
    assert positive_int("3") == 3


@pytest.mark.parametrize("value", ["0", "-1"])
def test_positive_int_rejects_non_positive_values(value):
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int(value)


def test_defaults():
    args = build_parser().parse_args(["file.edr"])

    assert args.theme == "light"
    assert args.n_blocks == 5
    assert isinstance(args.n_blocks, int)


def test_n_blocks_is_parsed_as_int():
    args = build_parser().parse_args(["file.edr", "--n-blocks", "3"])

    assert args.n_blocks == 3
    assert isinstance(args.n_blocks, int)


def test_n_blocks_zero_exits():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["file.edr", "--n-blocks", "0"])


def test_invalid_theme_exits():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["file.edr", "--theme", "purple"])


def test_missing_edr_path_exits():
    with pytest.raises(SystemExit):
        build_parser().parse_args([])
