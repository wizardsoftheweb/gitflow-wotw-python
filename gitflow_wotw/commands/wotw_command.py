# pylint: disable=W,C,R

from gitflow_wotw.actions import InitAction, VersionAction, LogAction
from gitflow_wotw.components import CommandInstance
from gitflow_wotw.subcommands import (
    FeatureSubcommand,
    BugfixSubcommand,
    ReleaseSubcommand,
    HotfixSubcommand,
    SupportSubcommand,
    ConfigSubcommand
)


class WotwCommand(CommandInstance):
    identifier = 'wotw'
    help_string = 'An ambitious attempt to duplicate gitflow-avh in Python'

    def __init__(self):
        CommandInstance.__init__(self)
        self['init'] = InitAction()
        self['feature'] = FeatureSubcommand()
        self['bugfix'] = BugfixSubcommand()
        self['release'] = ReleaseSubcommand()
        self['hotfix'] = HotfixSubcommand()
        self['support'] = SupportSubcommand()
        self['version'] = VersionAction()
        self['config'] = ConfigSubcommand()
        self['log'] = LogAction()
