# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import SinkParser


class SinkParserTestCase(TestCase):

    def setUp(self):
        self.construct_sink_parser()
        self.addCleanup(self.wipe_sink_parser)

    def wipe_sink_parser(self):
        del self.sink_parser

    def construct_sink_parser(self):
        self.sink_parser = SinkParser()


class ConstructorUnitTests(SinkParserTestCase):

    def setUp(self):
        SinkParserTestCase.setUp(self)


class AddParserUnitTests(SinkParserTestCase):

    def setUp(self):
        SinkParserTestCase.setUp(self)


class AttachUnitTests(SinkParserTestCase):

    def setUp(self):
        SinkParserTestCase.setUp(self)


class PrintHelpUnitTests(SinkParserTestCase):

    def setUp(self):
        SinkParserTestCase.setUp(self)
