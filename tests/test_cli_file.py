# pylint: disable=missing-docstring

from gitflow_wotw import cli


def test_cli_callability():
    assert callable(cli)
