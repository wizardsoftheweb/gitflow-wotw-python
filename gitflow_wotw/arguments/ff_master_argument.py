# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class FfMasterArgument(ArgumentInstance):
    args = ['--ff-master']
    kwargs = {
        'action': 'store_true',
        'dest': 'ff_master',
        'help': 'Fast-forward master when applicable'
    }
