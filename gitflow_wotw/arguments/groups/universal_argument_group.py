# pylint: disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    ForceArgument,
    HelpArgument,
    ShowCommandsArgument,
    VerboseArgument
)
from gitflow_wotw.components import ArgumentGroupInstance


class UniversalArgumentGroup(ArgumentGroupInstance):
    seed = OrderedDict()
    seed['help'] = HelpArgument()
    seed['force'] = ForceArgument()
    seed['show_commands'] = ShowCommandsArgument()
    seed['verbose'] = VerboseArgument()
    title = 'Universal Arguments'
    help_string = 'Arguments that can be used anywhere'
    exclusive = False
