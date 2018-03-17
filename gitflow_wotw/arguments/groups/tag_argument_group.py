# pylint:disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    SignArgument,
    SigningKeyArgument,
    TagArgument,
    TagNameArgument,
    MessageArgument,
    MessageFileArgument
)
from gitflow_wotw.components import ArgumentGroup


class TagArgumentGroup(ArgumentGroup):

    def __init__(self):
        ArgumentGroup. __init__(
            self,
            OrderedDict({
                'sign': SignArgument(),
                'signing_key': SigningKeyArgument(),
                'tag': TagArgument(),
                'tag_name': TagNameArgument(),
                'message': ArgumentGroup(
                    seed={
                        'message': MessageArgument(),
                        'message_file': MessageFileArgument()
                    },
                    exclusive=True
                )
            }),
            'Tag Options',
            'Options related to tags',
            False
        )
