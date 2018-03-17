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
        self.handlers['tidy_branches'] = self.tidy_branches
        self.handlers['change_to_base_branch'] = self.change_to_base_branch

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
            parsed.branch = runner.flow_branch.branch
        if hasattr(parsed, 'base') and not parsed.base:
            if parsed.branch:
                parsed.base = runner.flow_branch.base_branch(parsed.branch)
        if parsed.branch:
            parsed.upstream = runner.flow_branch.upstream_branch(parsed.branch)

    @staticmethod
    def change_to_base_branch(runner, parsed):
        runner.flow_branch.change_to_base_branch(parsed.branch)
