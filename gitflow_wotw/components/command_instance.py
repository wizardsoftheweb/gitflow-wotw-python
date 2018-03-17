# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Command, ComponentInstance


class CommandInstance(ComponentInstance, Command):

    def __init__(self):
        ComponentInstance.__init__(self)
        Command.__init__(
            self,
            self.identifier,
            self.help_string
        )
