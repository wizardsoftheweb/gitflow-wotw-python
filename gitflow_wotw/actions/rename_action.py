# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import ShowCommandsArgument
from gitflow_wotw.components import Action


class RenameAction(Action):
    ACTION = 'rename'
    HELP_STRING = 'Renames a specific branch'

    def __init__(self):
        super(RenameAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['show_commands'] = ShowCommandsArgument()

    def execute(self, parsed):
        print('Firing rename!')
        print(parsed)
