# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict


class ComponentInstance(OrderedDict):
    args = []
    kwargs = OrderedDict()
    identifier = ''
    help_string = ''
    responsibilities_seed = []
    arguments_seed = []
    arguments = OrderedDict()

    def __init__(self):
        super(ComponentInstance, self).__init__()
        self.populate()

    def populate(self):
        self.populate_dict(self.arguments, self.arguments_seed)
        if self.responsibilities_seed:
            self.populate_dict(self, self.responsibilities_seed)

    @staticmethod
    def populate_dict(target=None, elements=None):
        for element in elements:
            target[element.identifier] = element
