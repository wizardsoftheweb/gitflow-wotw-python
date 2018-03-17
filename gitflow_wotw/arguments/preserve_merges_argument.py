# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class PreserveMergesArgument(ArgumentInstance):
    args = ['-P', '--preserve-merges']
    kwargs = {
        'action': 'store_true',
        'dest': 'preserve_merges',
        'help': 'Preserve merges while rebasing'
    }
