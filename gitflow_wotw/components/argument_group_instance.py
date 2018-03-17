# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.components import ArgumentGroup, ComponentInstance


class ArgumentGroupInstance(ComponentInstance, ArgumentGroup):
    seed = OrderedDict()
    title = None
    help_string = None
    exclusive = False

    def __init__(self):
        ComponentInstance.__init__(self)
        super(ArgumentGroupInstance, self).__init__(
            seed=self.seed,
            title=self.title,
            description=self.help_string,
            exclusive=self.exclusive
        )
