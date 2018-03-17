# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class KeepLocalArgument(ArgumentInstance):
    args = ['--keep-local']
    kwargs = {
        'action': 'store_const',
        'const': 'both',
        'dest': 'local',
        'help': 'Keep the local branch after the operation finishes'
    }
