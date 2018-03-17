# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Action
from gitflow_wotw.arguments import GetArgument, SetArgument


class BaseAction(Action):
    ACTION = 'base'
    HELP_STRING = 'Set base config'

    def __init__(self):
        super(BaseAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['get'] = GetArgument()
        self.arguments['set'] = SetArgument()

    def execute(self, parsed):
        print('Firing base!')
        print(parsed)
