# pylint: disable=W,C,R

from __future__ import print_function

from argparse import ArgumentParser
from collections import OrderedDict
from logging import getLogger
from sys import argv

from coloredlogs import install as colored_install
from verboselogs import install as verbose_install

verbose_install()
colored_install()
LOGGER = getLogger(__name__)


class Command(OrderedDict):

    def __init__(
            self,
            args=None,
            parent_commands=None,
            identifier=None,
            help_string=None
    ):
        OrderedDict.__init__(self)
        LOGGER.verbose("Initialized a %s Command", identifier)
        if args is None:
            self.args = argv[1:]
        else:
            self.args = args
        LOGGER.debug("Received args %s", self.args)
        self.identifier = identifier
        self.help_string = help_string
        LOGGER.spam("help_string: %s", help_string)
        self.parser = None
        if parent_commands:
            self.prog = "%s %s" % (parent_commands, identifier)
        else:
            self.prog = identifier
        LOGGER.spam("PROG: %s", self.prog)
        self.subparsers = None
        self.arguments = []
        self.results = []
        self.pre_execution = OrderedDict()
        self.handlers = OrderedDict()
        self.post_execution = OrderedDict()

    def add_parser(self, subparsers=None):
        LOGGER.debug("Defining the root parser on %s", self.identifier)
        self.parser = ArgumentParser(
            prog="git %s" % self.prog,
            add_help=False,
            description=self.help_string,
            conflict_handler='resolve'
        )

    def add_subparsers(self):
        LOGGER.debug("Attaching a subparser on %s", self.identifier)
        self.subparsers = self.parser.add_subparsers(
            dest='next_command',
            metavar='Action',
            help='Available actions'
        )

    def attach_actions(self):
        if len(self.items()) > 0:
            LOGGER.verbose("Adding %s's Action arguments", self.identifier)
            self.add_subparsers()
        else:
            LOGGER.verbose("%s has no actions to add", self.identifier)
        for _, action in self.items():
            action.attach_arguments(self.subparsers)

    def attach_arguments(self):
        LOGGER.debug("Adding %s's own arguments", self.identifier)
        for argument in self.arguments:
            LOGGER.spam(argument)
            argument.attach_arguments(self.parser)

    def parse_args(self):
        LOGGER.debug('Attempting to parse args')
        return self.parser.parse_known_args(self.args)

    def parse(self, *args, **kwargs):
        self.add_parser()
        self.attach_actions()
        self.attach_arguments()
        self.results = self.parse_args()
        LOGGER.spam("%s parsed out %s", self.identifier, self.results[0])
        LOGGER.spam("%s left %s", self.identifier, self.results[0])

    def process(self, *args, **kwargs):
        if hasattr(self.results[0], 'next_command') and self.results[0].next_command:
            action = self.results[0].next_command
            LOGGER.info("%s triggered Action %s", self.identifier, action)
            return self[action].process(self.prog, *self.results)
        LOGGER.notice("%s.process() did not fire an action", self.identifier)

    def load_specific_handler(self, source=None, destination=None):
        LOGGER.debug('Loading specific handler')
        if source is None:
            return
        for key, args in source.items():
            destination[key] = args

    def load_handlers(self, *args, **kwargs):
        LOGGER.debug('Loading argument handlers')
        for argument in self.arguments:
            self.load_specific_handler(
                argument.load_handlers(),
                self.handlers
            )
            self.load_specific_handler(
                argument.assign_pre_tasks(),
                self.pre_execution
            )
            self.load_specific_handler(
                argument.assign_post_tasks(),
                self.post_execution
            )

    def run_handlers(self, handlers):
        LOGGER.debug('Running specific handler')
        for key, args in handlers.items():
            LOGGER.spam("Handler: %s", key)
            LOGGER.spam("Args: %s", args)
            self.handlers[key](self, self.results[0], *args)

    def __pre_execute(self, *args, **kwargs):
        LOGGER.debug("Running %s's pre_execute handlers", self.identifier)
        self.run_handlers(self.pre_execution)
        self.pre_execute(*args, **kwargs)

    def pre_execute(self, *args, **kwargs):
        """"""

    def execute(self, *args, **kwargs):
        """"""

    def __post_execute(self, *args, **kwargs):
        LOGGER.debug("Running %s's post_execution handlers", self.identifier)
        self.run_handlers(self.post_execution)
        self.post_execute(*args, **kwargs)

    def post_execute(self, *args, **kwargs):
        """"""

    def prosecute_command(self, *args, **kwargs):
        LOGGER.debug("Fully executing %s", self.identifier)
        self.__pre_execute(self, *args, **kwargs)
        self.execute(self, *args, **kwargs)
        self.__post_execute(self, *args, **kwargs)

    def complete(self, *args, **kwargs):
        self.parse(self, *args, **kwargs)
        self.process(self, *args, **kwargs)
        self.load_handlers(self, *args, **kwargs)
        self.prosecute_command(self, *args, **kwargs)
        LOGGER.info("%s has finished everything", self.identifier)
