# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.action import Action


class StartAction(Action):
    ACTION = 'start'
    HELP_STRING = 'Start a new something'

    def __init__(self):
        super(StartAction, self).__init__(self.ACTION, self.HELP_STRING)

    def execute(self, parsed):
        print('Firing start!')
        print(parsed)
