# pylint:disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    LocalArgument,
    GlobalArgument,
    SystemArgument,
    FileArgument,
)
from gitflow_wotw.components import ArgumentGroup


class ConfigLocationArgumentGroup(ArgumentGroup):

    def __init__(self):
        ArgumentGroup. __init__(
            self,
            OrderedDict({
                'system': SystemArgument(),
                'global': GlobalArgument(),
                'local': LocalArgument(),
                'file': FileArgument()
            }),
            'Configuration File',
            'Choose the configuration file to use',
            True
        )
