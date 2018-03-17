# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.components import Argument, ComponentInstance


class ArgumentInstance(ComponentInstance, Argument):

    def __init__(self):
        ComponentInstance.__init__(self)
        Argument.__init__(
            self,
            *self.args,
            **self.kwargs
        )
