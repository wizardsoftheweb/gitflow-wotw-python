# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class SigningKeyArgument(ArgumentInstance):
    args = ['-u', '--signing-key']
    kwargs = {
        'nargs': 1,
        'dest': 'signing_key',
        'metavar': 'KEY',
        'help': 'Sign with the provided key'
    }
