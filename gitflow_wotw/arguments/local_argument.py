# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class LocalArgument(ArgumentInstance):
    args = ['--local']
    kwargs = {
        'action': 'store_const',
        'const': 'local',
        'dest': 'config_location',
        'help': "Use repository's config file"
    }
