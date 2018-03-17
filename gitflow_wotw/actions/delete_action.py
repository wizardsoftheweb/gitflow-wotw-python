# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments.groups import BranchArgumentGroup
from gitflow_wotw.components import Action, ArgumentGroup


class DeleteAction(Action):
    ACTION = 'delete'
    HELP_STRING = 'Delete a specific branch'

    def __init__(self):
        super(DeleteAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['branches'] = BranchArgumentGroup()

    def execute(self, parsed):
        print('Firing delete!')
        print(parsed)
