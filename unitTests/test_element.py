from unittest import TestCase
from PBCore.PBCore import *
__author__ = 'lpsdesk'


class TestElement(TestCase):

    def setUp(self):
        self.testElement = Element(tag="pbCore")
    def test_getAttribute(self):
        self.fail()

    def test_addAttribute(self):
        self.fail()

    def test_deleteAttribute(self):
        self.fail()

    def test_getTag(self):
        self.assertEquals(self.testElement.getTag(), "pbCore")

    def test_setTag(self):
        self.fail()

    def test_getValue(self):
        self.fail()

    def test_setValue(self):
        self.fail()