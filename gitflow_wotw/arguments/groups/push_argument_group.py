# pylint: disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    PushArgument,
    PushDevelopArgument,
    PushMasterArgument,
    PushTagArgument,
)
from gitflow_wotw.components import ArgumentGroupInstance


class PushArgumentGroup(ArgumentGroupInstance):
    seed = OrderedDict()
    seed['push'] = PushArgument()
    seed['push_develop'] = PushDevelopArgument()
    seed['push_master'] = PushMasterArgument()
    seed['push_tag'] = PushTagArgument()
    title = 'Push Options'
    help_string = 'Options related to pushing branches'
    exclusive = False

    def __init__(self):
        ArgumentGroupInstance.__init__(self)
        self.handlers['push_results'] = PushArgumentGroup.push_results

    @staticmethod
    def push_results(runner, parsed):
        for item in set(parsed.push):
            if parsed.force:
                options = ' --force'
            else:
                options = ''
            print("git push %s origin %s" % (options, item))
