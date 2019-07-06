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

from trellostats.board import trelloStatsBoard


class TrelloStatsBoardTests(unittest.TestCase):
    """
    Test the trelloStatsBoard class.
    """

    def setUp(self):
        self.board = trelloStatsBoard('testAPI')

    def test_getBoardName(self):
        self.assertEqual(self.board.getBoardName(), 'testAPI')

    def test_getBoardId(self):
        self.assertEqual(self.board.getBoardId(), '5b3a9c9421794651e035bb22')

    def test_getBoardLists(self):
        lists = self.board.getBoardLists()
        self.assertEqual(len(lists), 2)

    def test_getBoardLabels(self):
        labels = self.board.getBoardLabels()
        self.assertIn('HEHEHE', labels)
        self.assertIn('HAHAHA', labels)

    def test_isBoardClosed(self):
        self.assertFalse(self.board.isBoardClosed())


if __name__ == "__main__":
    unittest.main()
