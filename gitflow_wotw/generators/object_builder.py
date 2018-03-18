# pylint:disable=W,C,R

from __future__ import print_function

from collections import Callable, OrderedDict
from logging import getLogger

from coloredlogs import install as colored_install
from verboselogs import install as verbose_install

from gitflow_wotw.components import Action, Argument, ArgumentGroup, Command
from gitflow_wotw.generators import ConfigLoader

verbose_install()
colored_install()
LOGGER = getLogger(__name__)

UNIVERSAL_ARGUMENTS = ['UniversalArgumentGroup']


def action_init(self):
    Action.__init__(self, self.identifier, self.help_string)


def action_process(self, parent_commands=None, parsed=None, args=None):
    if self.processed_class:
        return self.processed_class(args, parent_commands)
    return None


def argument_init(self):
    Argument.__init__(self, *self.args, **self.kwargs)


def argument_group_init(self):
    ArgumentGroup.__init__(
        self,
        self.seed,
        self.title,
        self.description,
        self.exclusive
    )


def command_init(self, args=None):
    Command.__init__(self, args, self.identifier, self.help_string)
    for action in self.action_seeds:
        action_instance = action()
        self[action_instance.identifier] = action_instance
    for argument in self.argument_seeds:
        self.arguments.append(argument)
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

    def delayed_command_build(self, object_name):
        def build_new(owner, args=None, parent_commands=None):
            return self[object_name](args, parent_commands)
        return build_new

    def build_argument(self, argument_name):
        LOGGER.debug("Building argument %s", argument_name)
        config = self.loader(argument_name)
        LOGGER.spam(config)
        return type(
            argument_name,
            (Argument,),
            {
                '__init__': argument_init,
                'args': config['args'],
                'kwargs': config['kwargs']
            }
        )

    def build_argument_group(self, argument_group_name):
        LOGGER.debug("Building ArgumentGroup %s", argument_group_name)
        config = self.loader(argument_group_name)
        LOGGER.spam(config)
        seed = OrderedDict()
        for element in config['seed']:
            if isinstance(element, list):
                new_seed = OrderedDict()
                name = ''
                for child in element:
                    name += child
                    new_seed[child] = self[child]()
                seed[name] = ArgumentGroup(seed=new_seed, exclusive=True)
            else:
                seed[element] = self[element]()
        return type(
            argument_group_name,
            (ArgumentGroup,),
            {
                'seed': seed,
                'title': config['title'],
                'description': config['description'],
                'exclusive': config['exclusive'],
                '__init__': argument_group_init
            }
        )

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
            class_dict['processed_class'] = self.delayed_command_build(process)
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
        arguments = []
        for argument in UNIVERSAL_ARGUMENTS:
            arguments.append(self[argument]())
        class_dict = {
            'identifier': identifier,
            'help_string': help_string,
            '__init__': command_init,
            'action_seeds': actions,
            'argument_seeds': arguments
        }
        return type(
            command_name,
            (Command,),
            class_dict
        )

    def build_object(self, object_name):
        LOGGER.debug("Attempting to create %s", object_name)
        if object_name.endswith('Argument'):
            return self.build_argument(object_name)
        elif object_name.endswith('ArgumentGroup'):
            return self.build_argument_group(object_name)
        elif object_name.endswith('Action'):
            return self.build_action(object_name)
        elif object_name.endswith('Command'):
            return self.build_command(object_name)
        raise NotImplementedError("No builder found for %s" % object_name)

    def __call__(self, object_name):
        return self.build_object(object_name)
