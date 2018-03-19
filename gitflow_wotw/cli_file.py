# pylint:disable=W,C,R

from argparse import ArgumentParser
from logging import getLogger, NOTSET, WARNING
from sys import argv

from coloredlogs import (
    decrease_verbosity,
    increase_verbosity,
    install as colored_install,
    set_level,
)
from verboselogs import install as verbose_install

from gitflow_wotw.generators import ObjectBuilder

colored_install()
verbose_install()
LOGGER = getLogger()
LOGGER.removeHandler(LOGGER.handlers[0])


def create_parser():
    parser = ArgumentParser(add_help=False)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-v', '--verbose',
        action='count',
        default=0
    )
    group.add_argument(
        '-q', '--quiet',
        action='count',
        default=0
    )
    return parser


def build_and_parse_args(args=None):
    parser = create_parser()
    if args is None:
        args = argv[1:]
    known, unknown = parser.parse_known_args(args)
    for _ in list(range(0, known.verbose)):
        increase_verbosity()
    for _ in list(range(0, known.quiet)):
        decrease_verbosity()
    return unknown


def build_and_run_command(args=None):
    builder = ObjectBuilder()
    WotwCommand = builder('WotwCommand')
    WotwCommand(args)


def cli(args=None):
    set_level(WARNING)
    unknown = build_and_parse_args(args)
    return build_and_run_command(unknown)
