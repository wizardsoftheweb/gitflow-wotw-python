# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import InteractiveArgument, PreserveMergesArgument
from gitflow_wotw.components import Action


class RebaseAction(Action):
    ACTION = 'rebase'
    HELP_STRING = 'Rebases a specific branch'

    def __init__(self):
        super(RebaseAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['interactive'] = InteractiveArgument()
        self.arguments['preserve_merges'] = PreserveMergesArgument()

    def execute(self, parsed):
        print('Firing rebase!')
        print(parsed)
