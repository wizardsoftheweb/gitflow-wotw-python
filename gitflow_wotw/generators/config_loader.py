# pylint:disable=W,C,R

from collections import Callable
from logging import getLogger
from os.path import abspath, dirname, join
from re import compile as re_compile, match, sub, VERBOSE

from verboselogs import install
from yaml import load

install()
LOGGER = getLogger(__name__)

DATA_DIR = join(abspath(dirname(__file__)), 'data')
LOGGER.debug("Object data directory: %s", DATA_DIR)
EXECUTORS_DIR = join(DATA_DIR, 'executors')
LOGGER.debug("Command and Action recipe directory: %s", DATA_DIR)
ARGUMENTS_DIR = join(DATA_DIR, 'arguments')
LOGGER.debug("Argument recipe directory: %s", DATA_DIR)


class ConfigLoader(Callable):
    DIRECTORIES = {
        'action': EXECUTORS_DIR,
        'argument': ARGUMENTS_DIR,
        'command': EXECUTORS_DIR
    }

    OBJECT_PATTERN = re_compile(
        r"""
        ^
        (?P<name>.*?)
        (?P<object_type>
            Action
            |
            Argument
            |
            Command
        )
        $
        """,
        VERBOSE
    )

    def load_object_config(self, unknown_object):
        LOGGER.debug("Attempting to load the config for %s", unknown_object)
        name, object_type = self.parse_info(unknown_object)
        LOGGER.spam("Discovered name: %s", name)
        LOGGER.spam("Discovered type: %s", object_type)
        config_file_path = join(self.DIRECTORIES[object_type], "%s.yml" % name)
        LOGGER.debug("Config file path is %s", config_file_path)
        with open(config_file_path, 'r') as config_file:
            config = load(config_file)
        return config

    @staticmethod
    def pascal_to_snake(pascal_case):
        snake_case = sub('(?!^)([A-Z][a-z]+)', r'_\1', pascal_case).lower()
        LOGGER.spam("Converted %s to %s", pascal_case, snake_case)
        return snake_case

    @staticmethod
    def parse_info(object_name):
        matched = match(ConfigLoader.OBJECT_PATTERN, object_name)
        if matched and matched.group('name') and matched.group('object_type'):
            return (
                ConfigLoader.pascal_to_snake(matched.group('name')),
                matched.group('object_type').lower()
            )
        else:
            raise KeyError(
                "%s was not found in %s or its subdirectories" % (
                    object_name,
                    DATA_DIR
                )
            )

    def __call__(self, unknown_object):
        return self.load_object_config(unknown_object)
