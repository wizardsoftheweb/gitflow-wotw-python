# pylint:disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    LocalArgument,
    GlobalArgument,
    SystemArgument,
    FileArgument,
)
from gitflow_wotw.components import ArgumentGroupInstance


class ConfigLocationArgumentGroup(ArgumentGroupInstance):
    seed = OrderedDict()
    seed['system'] = SystemArgument()
    seed['global'] = GlobalArgument()
    seed['local'] = LocalArgument()
    seed['file'] = FileArgument()
    title = 'Configuration File'
    help_string = 'Choose the configuration file to use'
    exclusive = True
