# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import DefaultsArgument
from gitflow_wotw.arguments.groups import ConfigLocationArgumentGroup
from gitflow_wotw.components import ActionInstance


class InitAction(ActionInstance):
    identifier = 'init'
    help_string = 'Initialize git wotw'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['defaults'] = DefaultsArgument()
        self.arguments['location'] = ConfigLocationArgumentGroup()
