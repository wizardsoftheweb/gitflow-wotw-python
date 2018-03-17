# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class FetchArgument(ArgumentInstance):
    args = ['-F', '--fetch']
    kwargs = {
        'action': 'store_true',
        'dest': 'fetch',
        'help': 'Fetch before operation'
    }
