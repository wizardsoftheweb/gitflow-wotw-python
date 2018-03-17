# pylint: disable=W,C,R

from gitflow_wotw.actions import InitAction, VersionAction, LogAction
from gitflow_wotw.components import Command
from gitflow_wotw.subcommands import (
    FeatureSubcommand,
    BugfixSubcommand,
    ReleaseSubcommand,
    HotfixSubcommand,
    SupportSubcommand,
    ConfigSubcommand
)


class WotwCommand(Command):
    IDENTIFIER = 'wotw'
    HELP_STRING = 'An ambitious attempt to duplicate gitflow-avh in Python'

    def __init__(self):
        Command.__init__(
            self,
            self.IDENTIFIER,
            self.HELP_STRING
        )
        self.populate()

    def populate(self):
        self['init'] = InitAction()
        self['feature'] = FeatureSubcommand()
        self['bugfix'] = BugfixSubcommand()
        self['release'] = ReleaseSubcommand()
        self['hotfix'] = HotfixSubcommand()
        self['support'] = SupportSubcommand()
        self['version'] = VersionAction()
        self['config'] = ConfigSubcommand()
        self['log'] = LogAction()
