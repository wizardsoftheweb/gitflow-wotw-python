# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class SignArgument(ArgumentInstance):
    args = ['-s', '--sign']
    kwargs = {
        'action': 'store_true',
        'dest': 'sign',
        'help': 'Sign the operation'
    }
