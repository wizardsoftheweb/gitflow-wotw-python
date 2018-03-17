# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import GetArgument, SetArgument
from gitflow_wotw.components import ActionInstance


class BaseAction(ActionInstance):
    identifier = 'base'
    help_string = 'Set base config'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['get'] = GetArgument()
        self.arguments['set'] = SetArgument()
