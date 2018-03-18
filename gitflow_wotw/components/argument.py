# pylint: disable=W,C,R

from __future__ import print_function

from logging import getLogger

from verboselogs import install

LOGGER = getLogger(__name__)


class Argument(object):

    def __init__(self, *args, **kwargs):
        LOGGER.debug('Initialized an Argument')
        LOGGER.debug(*args)
        self.args = args
        self.kwargs = kwargs

    def attach_arguments(self, parser=None):
        LOGGER.info('Attaching arguments')
        parser.add_argument(*self.args, **self.kwargs)
