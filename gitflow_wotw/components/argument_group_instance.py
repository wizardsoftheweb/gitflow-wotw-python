# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.components import ArgumentGroup


class ArgumentGroupInstance(ArgumentGroup):
    SEED = OrderedDict()
    TITLE = None
    DESCRIPTION = None
    EXCLUSIVE = False

    def __init__(self):
        super(ArgumentGroupInstance, self).__init__(
            self.SEED,
            self.TITLE,
            self.DESCRIPTION,
            self.EXCLUSIVE
        )
