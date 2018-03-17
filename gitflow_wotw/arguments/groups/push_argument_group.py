# pylint: disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    PushArgument,
    PushDevelopArgument,
    PushProductionArgument,
    PushTagArgument,
)
from gitflow_wotw.components import ArgumentGroupInstance


class PushArgumentGroup(ArgumentGroupInstance):
    seed = OrderedDict()
    seed['push'] = PushArgument()
    seed['push_develop'] = PushDevelopArgument()
    seed['push_production'] = PushProductionArgument()
    seed['push_tag'] = PushTagArgument()
    title = 'Push Options'
    help_string = 'Options related to pushing branches'
    exclusive = False
