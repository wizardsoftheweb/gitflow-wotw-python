# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import ParserNode


class ParserNodeTestCase(TestCase):

    def setUp(self):
        self.construct_parser_node()
        self.addCleanup(self.wipe_parser_node)

    def wipe_parser_node(self):
        del self.parser_node

    def construct_parser_node(self):
        self.parser_node = ParserNode()


class ConstructorUnitTests(ParserNodeTestCase):

    def setUp(self):
        ParserNodeTestCase.setUp(self)


class AddSubparsersUnitTests(ParserNodeTestCase):

    def setUp(self):
        ParserNodeTestCase.setUp(self)


class AttachBelowUnitTests(ParserNodeTestCase):

    def setUp(self):
        ParserNodeTestCase.setUp(self)


class AttachUnitTests(ParserNodeTestCase):

    def setUp(self):
        ParserNodeTestCase.setUp(self)


class PrintHelpBelowUnitTests(ParserNodeTestCase):

    def setUp(self):
        ParserNodeTestCase.setUp(self)


class PrintHelpUnitTests(ParserNodeTestCase):

    def setUp(self):
        ParserNodeTestCase.setUp(self)
