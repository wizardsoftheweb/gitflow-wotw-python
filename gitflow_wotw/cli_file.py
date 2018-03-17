# pylint: disable=W,C,R

from gitflow_wotw.components import Command

from gitflow_wotw.actions import InitAction, VersionAction, LogAction
from gitflow_wotw.subcommands import (
    FeatureSubcommand,
    BugfixSubcommand,
    ReleaseSubcommand,
    HotfixSubcommand,
    SupportSubcommand,
    ConfigSubcommand
)


def cli():
    demo = Command()
    demo['init'] = InitAction()
    demo['feature'] = FeatureSubcommand()
    demo['bugfix'] = BugfixSubcommand()
    demo['release'] = ReleaseSubcommand()
    demo['hotfix'] = HotfixSubcommand()
    demo['support'] = SupportSubcommand()
    demo['version'] = VersionAction()
    demo['config'] = ConfigSubcommand()
    demo['log'] = LogAction()
    demo.bootstrap()
