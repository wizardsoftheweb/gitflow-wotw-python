# pylint: disable=W,C,R

from __future__ import print_function

from argparse import ArgumentParser, Namespace
from collections import OrderedDict
from sys import argv


class Action(object):

    def __init__(self, action=None):
        self.identifier = action

    def add_parser(self, subparsers):
        print("Adding %s's parser" % self.identifier)

    def attach(self, subparsers):
        self.add_parser(subparsers)

    def execute(self, parsed_args):
        print("Executing Action %s" % self.identifier)


class Subcommand(Action):

    def __init__(self, subcommand=None):
        self.available_items = OrderedDict()
        self.identifier = subcommand
        self.child_item = 'action'

    def add_available_item(self, available_item):
        self.available_items[available_item.identifier] = available_item

    def add_subparsers(self):
        print("Adding %s's subparsers" % self.identifier)

    def attach(self, subparsers):
        self.add_parser(subparsers)
        self.add_subparsers()
        self.attach_available_items(subparsers)

    def attach_available_items(self, subparsers):
        for _, value in self.available_items.items():
            value.attach(subparsers)

    def execute(self, parsed_args):
        print("Executing %s %s" % (type(self).__name__, self.identifier))
        if self.child_item:
            if hasattr(parsed_args, self.child_item):
                desired_item = getattr(parsed_args, self.child_item)
                if desired_item in self.available_items:
                    self.available_items[desired_item].execute(parsed_args)
                else:
                    raise ValueError(
                        "Unable to find the %s %s"
                        % (
                            desired_item,
                            self.child_item
                        )
                    )
            else:
                raise ValueError(
                    "No %s received from CLI args" % self.child_item
                )


class Command(Subcommand):

    def __init__(self):
        self.available_items = OrderedDict()
        self.identifier = 'wotw'
        self.child_item = 'subcommand'

    def create_parser(self):
        print('Creating root parser')

    def attach(self, subparsers=None):
        self.create_parser()
        self.add_subparsers()
        self.attach_available_items(subparsers)

    def parse_args(self, args=None):
        print('Parsing the args')
        parsed = Namespace()
        if len(args) > 0:
            parsed.subcommand = args[0]
        if len(args) > 1:
            parsed.action = args[1]
        return parsed

    def bootstrap(self):
        self.attach()
        parsed = self.parse_args(argv[1:])
        self.execute(parsed)


def cli():
    start = Action('start')
    finish = Action('finish')
    delete = Action('delete')

    feature = Subcommand('feature')
    feature.add_available_item(start)
    feature.add_available_item(finish)

    hotfix = Subcommand('hotfix')
    hotfix.add_available_item(delete)

    app = Command()
    app.add_available_item(feature)
    app.add_available_item(hotfix)
    # print(app.available_items)
    app.bootstrap()

if '__main__' == __name__:
    cli()
