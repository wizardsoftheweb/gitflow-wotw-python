# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import (
    LocalArgument,
    GlobalArgument,
    SystemArgument,
    FileArgument,
    ShowCommandsArgument
)
from gitflow_wotw.components import Action


class SetAction(Action):
    ACTION = 'set'
    HELP_STRING = 'Sets a specific config value'

    def __init__(self):
        super(SetAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.exclusive_groups.append([
            GlobalArgument(),
            SystemArgument(),
            LocalArgument(),
            FileArgument()
        ])
        self.arguments['show_commands'] = ShowCommandsArgument()

    def execute(self, parsed):
        print('Firing set!')
        print(parsed)
