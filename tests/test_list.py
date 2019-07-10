#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Paulo Vital
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import unittest

from trellostats.board import TrelloStatsBoard

board = None

def setUpModule():
    global board
    board = TrelloStatsBoard('testAPI')


class TrelloStatsListTests(unittest.TestCase):
    """
    Test the TrelloStatsLists and TrelloStatsList classes.
    """
    def setUp(self):
        self.lists = board.getBoardLists()
        # get the first list
        self.list = self.lists[0]

    def test_getLists(self):
        self.assertEqual(len(self.lists), 2)

    def test_getListName(self):
        self.assertEqual(self.list.getListName(), 'bla')

    def test_getListId(self):
        self.assertEqual(self.list.getListId(), '5b3cdd89f344cf2b812007cc')

    def test_getListBoard(self):
        self.assertEqual(self.list.getListBoard(), '5b3a9c9421794651e035bb22')

    def test_getListCards(self):
        cards = self.list.getListCards()
        self.assertEqual(len(cards), 2)


if __name__ == "__main__":
    unittest.main()
