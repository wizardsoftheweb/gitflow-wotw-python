# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Action


class LogAction(Action):
    ACTION = 'log'
    HELP_STRING = 'Compare current log against dev'

    def __init__(self):
        super(LogAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        """"""

    def execute(self, parsed):
        print('Firing log!')
        print(parsed)
