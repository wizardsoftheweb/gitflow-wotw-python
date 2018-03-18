# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class BranchArgument(ArgumentInstance):
    args = ['branch']
    kwargs = {
        'help': 'The branch to operate on'
    }

    def __init__(self, optional=True):
        ArgumentInstance.__init__(self)
        if optional:
            self.kwargs['nargs'] = '?'
