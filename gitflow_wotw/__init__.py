"""This file provides the full wotw module"""

# pylint:disable=W,C,R

from .components import (
    Argument,
    Action,
    Command
)
from .generators import (
    ConfigLoader,
    ObjectBuilder,
)
from .cli_file import cli

from logging import debug, info
from logging.config import dictConfig
from os.path import abspath, dirname, join

from verboselogs import install
from yaml import load

__location__ = abspath(dirname(__file__))

install()
with open(join(__location__, 'logging.yml'), 'r') as config_file:
    config = load(config_file)
dictConfig(config)
