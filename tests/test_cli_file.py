# pylint: disable=missing-docstring

from __future__ import print_function

from mock import patch

from gitflow_wotw import cli


@patch('gitflow_wotw.cli_file.WotwCommand')
def test_execution(mock_command):
    mock_command.assert_not_called()
    cli()
    mock_command.assert_called_once_with()
