# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class BaseArgument(ArgumentInstance):
    args = ['base']
    kwargs = {
        'nargs': '?',
        'help': 'The base branch to use'
    }
