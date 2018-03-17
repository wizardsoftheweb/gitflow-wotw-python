# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class TagNameArgument(ArgumentInstance):
    args = ['-T', '--tag-name']
    kwargs = {
        'action': 'store_true',
        'dest': 'tag_name',
        'help': 'Use the provided tag name'
    }
