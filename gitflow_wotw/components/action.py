# pylint: disable=W,C,R

from __future__ import print_function

from argparse import ArgumentParser
from collections import OrderedDict
from sys import argv


class Action(object):

    def __init__(self, identifier=None, help_string=None):
        self.identifier = identifier
        self.help_string = help_string
        self.arguments = []

    def populate(self):
        """"""

    def attach_as_subcommand(self, subparsers):
        self.parser = subparsers.add_parser(
            self.identifier,
            add_help=False,
            description=self.help_string,
            help=self.help_string
        )

    def attach_arguments(self, subparsers):
        self.attach_as_subcommand(subparsers)
        for argument in self.arguments:
            argument.attach_arguments(self.parser)

    def process(self, parsed=None, args=None):
        print(parsed)
        print(args)
