# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import ParserSink


class ParserSinkTestCase(TestCase):

    def setUp(self):
        self.construct_parser_sink()
        self.addCleanup(self.wipe_parser_sink)

    def wipe_parser_sink(self):
        del self.parser_sink

    def construct_parser_sink(self):
        self.parser_sink = ParserSink()


class ConstructorUnitTests(ParserSinkTestCase):

    def setUp(self):
        ParserSinkTestCase.setUp(self)


class AddParserUnitTests(ParserSinkTestCase):

    def setUp(self):
        ParserSinkTestCase.setUp(self)


class AttachArgumentsUnitTests(ParserSinkTestCase):

    def setUp(self):
        ParserSinkTestCase.setUp(self)


class AttachUnitTests(ParserSinkTestCase):

    def setUp(self):
        ParserSinkTestCase.setUp(self)


class PrintHelpUnitTests(ParserSinkTestCase):

    def setUp(self):
        ParserSinkTestCase.setUp(self)
