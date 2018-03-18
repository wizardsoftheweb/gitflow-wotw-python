# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class FileArgument(ArgumentInstance):
    args = ['--file']
    kwargs = {
        'nargs': 1,
        'dest': 'config_file',
        'metavar': 'CONFIG_FILE',
        'help': 'Use the provided config file'
    }
