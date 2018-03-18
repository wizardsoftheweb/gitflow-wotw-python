# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class PushMasterArgument(ArgumentInstance):
    args = ['--push-master', '--push-production']
    kwargs = {
        'action': 'append_const',
        'dest': 'push',
        'help': 'Push production after operation finishes'
    }

    def __init__(self):
        ArgumentInstance.__init__(self)
        self.kwargs['const'] = self.flow_branch.master
