# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import (
    LocalArgument,
    GlobalArgument,
    SystemArgument,
    FileArgument,
    ForceArgument,
    DefaultsArgument,
    ShowCommandsArgument
)
from gitflow_wotw.components import Action


class InitAction(Action):
    ACTION = 'init'
    HELP_STRING = 'List program version'

    def __init__(self):
        super(InitAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['defaults'] = DefaultsArgument()
        self.arguments['local'] = LocalArgument()
        self.arguments['global'] = GlobalArgument()
        self.arguments['system'] = SystemArgument()
        self.arguments['file'] = FileArgument()
        self.arguments['force'] = ForceArgument()
        self.arguments['show_commands'] = ShowCommandsArgument()

    def execute(self, parsed):
        print('Firing init!')
        print(parsed)
