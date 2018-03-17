# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class SigningKeyArgument(Argument):
    ARGS = ['-u', '--signing-key']
    KWARGS = {
        'nargs': 1,
        'dest': 'signing_key',
        'metavar': 'KEY',
        'help': 'Sign with the provided key'
    }
    NEGATABLE = False

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
