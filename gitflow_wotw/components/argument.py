# pylint: disable=W,C,R

from __future__ import print_function

from logging import getLogger

from coloredlogs import install as colored_install
from verboselogs import install as verbose_install

verbose_install()
colored_install()
LOGGER = getLogger(__name__)


class Argument(object):

    def __init__(self, *args, **kwargs):
        LOGGER.verbose('Initialized an Argument')
        LOGGER.spam(args)
        self.args = args
        self.kwargs = kwargs

    def attach_arguments(self, parser=None):
        LOGGER.debug('Attaching arguments')
        parser.add_argument(*self.args, **self.kwargs)

    def load_handlers(self, *args, **kwargs):
        """"""

    def assign_pre_tasks(self, *args, **kwargs):
        """"""

    def assign_post_tasks(self, *args, **kwargs):
        """"""
