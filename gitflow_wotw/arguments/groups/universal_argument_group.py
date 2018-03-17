# pylint: disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    ForceArgument,
    HelpArgument,
    ShowCommandsArgument,
    VerboseArgument
)
from gitflow_wotw.components import ArgumentGroup


class UniversalArgumentGroup(ArgumentGroup):

    def __init__(self):
        ArgumentGroup. __init__(
            self,
            OrderedDict({
                'help': HelpArgument(),
                'force': ForceArgument(),
                'show_commands': ShowCommandsArgument(),
                'verbose': VerboseArgument()
            }),
            'Universal Arguments',
            'Arguments that can be used anywhere',
            False
        )
