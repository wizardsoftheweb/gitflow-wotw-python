# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import DefaultsArgument
from gitflow_wotw.arguments.groups import ConfigLocationArgumentGroup
from gitflow_wotw.components import Action


class InitAction(Action):
    ACTION = 'init'
    HELP_STRING = 'List program version'

    def __init__(self):
        super(InitAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['config_file'] = ConfigLocationArgumentGroup()
        self.arguments['defaults'] = DefaultsArgument()

    def execute(self, parsed):
        print('Firing init!')
        print(parsed)
