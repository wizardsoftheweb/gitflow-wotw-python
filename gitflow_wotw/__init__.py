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

from coloredlogs import ColoredFormatter, install as colored_install
from verboselogs import install as verbose_install
from yaml import load

__location__ = abspath(dirname(__file__))

verbose_install()
colored_install()
with open(join(__location__, 'logging.yml'), 'r') as config_file:
    config = load(config_file)
dictConfig(config)
