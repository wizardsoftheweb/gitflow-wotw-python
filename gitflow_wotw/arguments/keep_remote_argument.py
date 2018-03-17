# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class KeepRemoteArgument(ArgumentInstance):
    args = ['--keep-remote']
    kwargs = {
        'action': 'store_const',
        'const': 'remote',
        'dest': 'keep',
        'help': 'Keep the remote branch after the operation finishes'
    }
