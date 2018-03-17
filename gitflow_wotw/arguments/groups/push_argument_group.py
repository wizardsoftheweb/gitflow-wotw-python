# pylint: disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    PushArgument,
    PushDevelopArgument,
    PushProductionArgument,
    PushTagArgument,
)
from gitflow_wotw.components import ArgumentGroup


class PushArgumentGroup(ArgumentGroup):

    def __init__(self):
        ArgumentGroup. __init__(
            self,
            OrderedDict({
                'push': PushArgument(),
                'push_develop': PushDevelopArgument(),
                'push_production': PushProductionArgument(),
                'push_tag': PushTagArgument(),
            }),
            'Push Options',
            'Options related to pushing branches',
            False
        )
