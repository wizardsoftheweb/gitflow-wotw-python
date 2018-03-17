# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict
from gitflow_wotw.repo import FlowBranch


class ComponentInstance(OrderedDict):
    args = []
    kwargs = OrderedDict()
    identifier = ''
    help_string = ''
    responsibilities_seed = []
    arguments_seed = []
    arguments = OrderedDict()
    handlers = OrderedDict()

    def __init__(self):
        OrderedDict.__init__(self)
        self.flow_branch = FlowBranch()
        self.populate()

    def populate(self):
        self.populate_dict(self.arguments, self.arguments_seed)
        if self.responsibilities_seed:
            self.populate_dict(self, self.responsibilities_seed)

    def populate_dict(self, target=None, elements=None):
        for element in elements:
            target[element.identifier] = element
            for key, handler in element.handlers.items():
                self.handlers[key] = handler
