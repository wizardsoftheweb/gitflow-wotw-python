# pylint:disable=W,C,R

from collections import Callable
from os.path import abspath, dirname, join
from re import compile as re_compile, match, sub, VERBOSE
from yaml import load

DATA_DIR = join(abspath(dirname(__file__)), 'data')
EXECUTORS_DIR = join(DATA_DIR, 'executors')
ARGUMENTS_DIR = join(DATA_DIR, 'arguments')


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
        name, object_type = self.parse_info(unknown_object)
        config_file_path = join(self.DIRECTORIES[object_type], "%s.yml" % name)
        with open(config_file_path, 'r') as config_file:
            config = load(config_file)
        return config

    @staticmethod
    def pascal_to_snake(camel_case):
        return sub('(?!^)([A-Z][a-z]+)', r'_\1', camel_case).lower()

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
