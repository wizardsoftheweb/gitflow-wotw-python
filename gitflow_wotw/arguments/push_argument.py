# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class PushArgument(ArgumentInstance):
    args = ['-p', '--push']
    kwargs = {
        'action': 'store_const',
        'default': [],
        'dest': 'push',
        'help': 'Push to origin after operation completes'
    }

    def __init__(self):
        ArgumentInstance.__init__(self)
        self.kwargs['const'] = [
            self.flow_branch.master,
            self.flow_branch.develop,
            '--tags'
        ]
