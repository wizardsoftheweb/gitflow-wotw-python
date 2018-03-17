# pylint: disable=W,C,R

from __future__ import print_function


class Argument(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def attach_argument(self, parser=None):
        parser.add_argument(*self.args, **self.kwargs)
        if 'action' in self.kwargs and 'store_true' == self.kwargs['action']:
            self.negate(parser)

    def negate(self, parser=None):
        negated_args = []
        for arg in self.args:
            if arg.startswith('--'):
                negated_args.append(arg.replace('--', '--no-'))
        if negated_args:
            negated_kwargs = self.kwargs
            negated_kwargs['help'] = (
                "Do not %s" % negated_kwargs['help'].lower()
            )
            negated_kwargs['action'] = 'store_false'
        parser.add_argument(*negated_args, **negated_kwargs)
