# pylint: disable=W,C,R

from __future__ import print_function

from copy import deepcopy


class Argument(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def attach_argument(self, parser=None):
        if 'opt_out' in self.kwargs and self.kwargs['opt_out']:
            del self.kwargs['opt_out']
        elif 'action' in self.kwargs and 'store_true' == self.kwargs['action']:
            if not 'default' in self.kwargs:
                self.kwargs['default'] = False
            parser = parser.add_mutually_exclusive_group()
            self.negate(parser)
        parser.add_argument(*self.args, **self.kwargs)

    def negate(self, parser=None):
        negated_args = []
        for arg in self.args:
            if arg.startswith('--'):
                negated_args.append(arg.replace('--', '--no-'))
        if negated_args:
            negated_kwargs = deepcopy(self.kwargs)
            negated_kwargs['help'] = (
                "Do not %s" % negated_kwargs['help'].lower()
            )
            negated_kwargs['action'] = 'store_false'
        parser.add_argument(*negated_args, **negated_kwargs)
