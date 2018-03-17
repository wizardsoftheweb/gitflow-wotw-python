# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ComponentInstance, Subcommand


class SubcommandInstance(ComponentInstance, Subcommand):

    def __init__(self):
        ComponentInstance.__init__(self)
        Subcommand.__init__(
            self,
            self.identifier,
            self.help_string
        )
