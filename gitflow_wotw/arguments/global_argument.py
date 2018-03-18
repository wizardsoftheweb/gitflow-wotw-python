# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class GlobalArgument(ArgumentInstance):
    args = ['--global']
    kwargs = {
        'action': 'store_const',
        'const': 'global',
        'dest': 'config_location',
        'help': 'Use the global config file'
    }
