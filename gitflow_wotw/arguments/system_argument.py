# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class SystemArgument(ArgumentInstance):
    args = ['--system']
    kwargs = {
        'action': 'store_const',
        'const': 'system',
        'dest': 'config_location',
        'help': 'Use the system config file'
    }
