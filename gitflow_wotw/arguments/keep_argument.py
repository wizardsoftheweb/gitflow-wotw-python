# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class KeepArgument(ArgumentInstance):
    args = ['-k', '--keep']
    kwargs = {
        'action': 'store_const',
        'const': 'both',
        'dest': 'keep',
        'help': 'Keep local and remote branch after operation finishes'
    }
