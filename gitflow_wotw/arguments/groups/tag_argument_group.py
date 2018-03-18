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
from gitflow_wotw.components import ArgumentGroup, ArgumentGroupInstance


class TagArgumentGroup(ArgumentGroupInstance):
    seed = OrderedDict()
    seed['sign'] = SignArgument()
    seed['signing_key'] = SigningKeyArgument()
    seed['tag'] = TagArgument()
    seed['tag_name'] = TagNameArgument()
    seed_message = OrderedDict()
    seed_message['message'] = MessageArgument()
    seed_message['message_file'] = MessageFileArgument()
    seed['message'] = ArgumentGroup(
        seed=seed_message,
        exclusive=True
    )
    title = 'Tag Options'
    help_string = 'Options related to tags'
    exclusive = False
