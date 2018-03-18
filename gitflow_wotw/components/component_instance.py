# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict
from gitflow_wotw.repo import FlowWrangler


class ComponentInstance(OrderedDict):
    args = []
    identifier = ''
    help_string = ''
    responsibilities_seed = []
    arguments_seed = []
    arguments = OrderedDict()
    handlers = OrderedDict()

    def __init__(self):
        OrderedDict.__init__(self)
        self.flow = FlowWrangler()
        self.populate()
        self.handlers['tidy_branches'] = ComponentInstance.tidy_branches

    def populate(self):
        self.populate_dict(self.arguments, self.arguments_seed)
        if self.responsibilities_seed:
            self.populate_dict(self, self.responsibilities_seed)

    def populate_dict(self, target=None, elements=None):
        for element in elements:
            target[element.identifier] = element
            for key, handler in element.handlers.items():
                self.handlers[key] = handler

    @staticmethod
    def tidy_branches(runner, parsed):
        if hasattr(parsed, 'branch') and not parsed.branch:
            parsed.branch = runner.flow.branch.branch
            if parsed.branch:
                parsed.upstream = runner.flow.branch.upstream_from_branch(
                    parsed.branch
                )
        if hasattr(parsed, 'base') and not parsed.base:
            if parsed.branch:
                parsed.base = runner.flow.branch.base_from_branch(
                    parsed.branch
                )
