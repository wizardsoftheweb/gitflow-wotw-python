# pylint: disable=W,C,R

from __future__ import print_function

from argparse import ArgumentParser
from collections import OrderedDict
from logging import getLogger
from sys import argv

LOGGER = getLogger(__name__)


class Action(object):

    def __init__(self, identifier=None, help_string=None):
        LOGGER.debug("Initialized a %s Action", identifier)
        self.identifier = identifier
        self.help_string = help_string
        self.arguments = []

    def populate(self):
        """"""

    def attach_as_subcommand(self, subparsers):
        LOGGER.info("Attaching %s as a subcommand", self.identifier)
        self.parser = subparsers.add_parser(
            self.identifier,
            add_help=False,
            description=self.help_string,
            help=self.help_string
        )

    def attach_arguments(self, subparsers):
        LOGGER.info("Attaching arguments for %s", self.identifier)
        self.attach_as_subcommand(subparsers)
        for argument in self.arguments:
            argument.attach_arguments(self.parser)

    def process(self, parsed=None, args=None):
        LOGGER.warning("Base process used for %s Action", self.identifier)
        print(parsed)
        print(args)
