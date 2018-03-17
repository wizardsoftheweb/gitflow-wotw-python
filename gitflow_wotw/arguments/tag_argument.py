# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class TagArgument(ArgumentInstance):
    args = ['-t', '--tag']
    kwargs = {
        'action': 'store_true',
        'dest': 'tag',
        'help': 'Tag the repo after the operation finishes'
    }
