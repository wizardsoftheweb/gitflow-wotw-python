# pylint:disable=W,C,R

from __future__ import print_function

from collections import Callable, OrderedDict
from logging import getLogger

from coloredlogs import install as colored_install
from verboselogs import install as verbose_install

from gitflow_wotw.components import Action, Command
from gitflow_wotw.generators import ConfigLoader

verbose_install()
colored_install()
LOGGER = getLogger(__name__)


def action_init(self):
    Action.__init__(self, self.identifier, self.help_string)


def action_process(self, parsed=None, args=None):
    if self.processed_class:
        return self.processed_class(args)
    return None


def command_init(self, args=None):
    Command.__init__(self, args, self.identifier, self.help_string)
    for action in self.action_seeds:
        action_instance = action()
        self[action_instance.identifier] = action_instance
    self.complete()


class ObjectBuilder(OrderedDict):

    __instance = None
    loader = ConfigLoader()

    def __new__(cls):
        if cls.__instance == None:
            LOGGER.verbose('Creating ObjectBuilder singleton')
            cls.__instance = OrderedDict.__new__(cls)
            cls.__instance.name = "ObjectStorage"
        return cls.__instance

    def __missing__(self, key):
        LOGGER.notice("%s not found; attempting to build", key)
        self[key] = self.build_object(key)
        return self[key]

    def build_action(self, action_name):
        LOGGER.debug("Building action %s", action_name)
        config = self.loader(action_name)
        LOGGER.spam(config)
        identifier = config['identifier']
        help_string = config['help_string']
        class_dict = {
            'identifier': identifier,
            'help_string': help_string,
            '__init__': action_init,
            'process': action_process,
            'processed_class': None
        }
        if (
                'action' in config
                and
                config['action']
                and
                'process' in config['action']
                and
                config['action']['process']
        ):
            process = config['action']['process']
            class_dict['processed_class'] = self[process]
            LOGGER.spam("Discovered call: %s", process)
        return type(
            action_name,
            (Action,),
            class_dict
        )

    def build_command(self, command_name):
        LOGGER.debug("Building action %s", command_name)
        config = self.loader(command_name)
        LOGGER.spam(config)
        identifier = config['identifier']
        help_string = config['help_string']
        if (
                'command' in config
                and
                config['command']
                and
                'actions' in config['command']
                and
                config['command']['actions']
        ):
            actions = [
                self[action]
                for action
                in config['command']['actions']
            ]
        else:
            actions = []
        LOGGER.spam("Discovered actions: %s", actions)
        class_dict = {
            'identifier': identifier,
            'help_string': help_string,
            '__init__': command_init,
            'action_seeds': actions
        }
        return type(
            command_name,
            (Command,),
            class_dict
        )

    def build_object(self, object_name):
        LOGGER.debug("Attempting to create %s", object_name)
        if object_name.endswith('Action'):
            return self.build_action(object_name)
        elif object_name.endswith('Command'):
            return self.build_command(object_name)
        raise NotImplementedError("No builder found for %s" % object_name)

    def __call__(self, object_name):
        return self.build_object(object_name)
