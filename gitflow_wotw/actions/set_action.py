# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments.groups import ConfigLocationArgumentGroup
from gitflow_wotw.components import ActionInstance


class SetAction(ActionInstance):
    identifier = 'set'
    help_string = 'Sets a specific config value'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['config_file'] = ConfigLocationArgumentGroup()
