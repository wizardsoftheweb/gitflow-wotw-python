# pylint: disable=W,C,R

from collections import OrderedDict


class ArgumentGroup(OrderedDict):

    def __init__(self, seed=None, title=None, description=None, exclusive=False):
        OrderedDict.__init__(self)
        self.title = title
        self.description = description
        self.exclusive = exclusive
        if seed:
            for key, value in seed.items():
                self[key] = value

    def attach_argument(self, parser=None):
        if self.title or self.description:
            group = parser.add_argument_group(self.title, self.description)
        else:
            group = parser
        if self.exclusive:
            group = group.add_mutually_exclusive_group()
        for _, argument in self.items():
            argument.attach_argument(group)
