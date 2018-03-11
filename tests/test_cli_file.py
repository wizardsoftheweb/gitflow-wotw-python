# pylint: disable=missing-docstring

from __future__ import print_function


from mock import patch

from gitflow_wotw import cli


@patch('gitflow_wotw.cli_file.FeatureSubcommand')
@patch('gitflow_wotw.cli_file.Command')
def test_execution(mock_command, mock_feature):
    mock_command.assert_not_called()
    mock_feature.assert_not_called()
    cli()
    mock_command.assert_called_once()
    mock_feature.assert_called_once()
