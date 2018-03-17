# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ActionInstance


class LogAction(ActionInstance):
    identifier = 'log'
    help_string = 'Compare current log against dev'
