# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.actions import SetAction, BaseAction
from gitflow_wotw.components import SubcommandInstance


class ConfigSubcommand(SubcommandInstance):
    identifier = 'config'
    help_string = 'Manages config'

    def __init__(self):
        SubcommandInstance.__init__(self)
        self['set'] = SetAction()
        self['base'] = BaseAction()
