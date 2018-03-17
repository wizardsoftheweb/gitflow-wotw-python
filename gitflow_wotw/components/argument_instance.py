# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.components import Argument


class ArgumentInstance(Argument):
    ARGS = []
    KWARGS = OrderedDict()

    def __init__(self):
        super(ArgumentInstance, self).__init__(
            *self.ARGS,
            **self.KWARGS
        )
