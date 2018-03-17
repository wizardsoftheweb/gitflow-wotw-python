# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Action


class FinishAction(Action):
    ACTION = 'finish'
    HELP_STRING = 'Finish a specific something'

    def __init__(self):
        super(FinishAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        """"""

    def execute(self, parsed):
        print('Firing finish!')
        print(parsed)
