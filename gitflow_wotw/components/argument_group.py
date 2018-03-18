# pylint: disable=W,C,R

from collections import OrderedDict
from logging import getLogger

from coloredlogs import install as colored_install
from verboselogs import install as verbose_install

verbose_install()
colored_install()
LOGGER = getLogger(__name__)


class ArgumentGroup(OrderedDict):

    def __init__(self, seed=None, title=None, description=None, exclusive=False):
        LOGGER.verbose("Initialized an ArgumentGroup (%s)", title)
        OrderedDict.__init__(self)
        self.title = title
        self.description = description
        self.exclusive = exclusive
        LOGGER.spam(seed)
        if seed:
            for key, value in seed.items():
                self[key] = value

    def attach_argument(self, parser=None):
        LOGGER.debug('Attaching arguments from ArgumentGroup')
        if self.title or self.description:
            LOGGER.spam('Creating a new argument group')
            group = parser.add_argument_group(self.title, self.description)
        else:
            LOGGER.spam('Using the existing parser')
            group = parser
        if self.exclusive:
            LOGGER.spam('Creating a mutually exclusive group')
            group = group.add_mutually_exclusive_group()
        for _, argument in self.items():
            argument.attach_argument(group)
