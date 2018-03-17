# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class BranchArgument(ArgumentInstance):
    args = ['branch']
    kwargs = {
        'nargs': '?',
        'dest': 'branch',
        'help': 'The branch to operate on'
    }
