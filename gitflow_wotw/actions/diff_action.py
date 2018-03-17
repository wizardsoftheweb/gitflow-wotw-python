# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Action


class DiffAction(Action):
    ACTION = 'diff'
    HELP_STRING = 'Compare the branch against its base'

    def __init__(self):
        super(DiffAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        """"""

    def execute(self, parsed):
        print('Firing diff!')
        print(parsed)
