# pylint: disable=W,C,R

from gitflow_wotw import Command

from gitflow_wotw.subcommand import FeatureSubcommand


def cli():
    demo = Command()
    demo['feature'] = FeatureSubcommand()
    demo.bootstrap()