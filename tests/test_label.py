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
list = None
card = None

def setUpModule():
    global board, list, card
    board = TrelloStatsBoard('testAPI')
    list = board.getBoardLists()[1]     # get the second list (ble)
    card = list.getListCards()[1]       # get the second card of the list


class TrelloStatsLabelTests(unittest.TestCase):
    """
    Test the TrelloStatsLabel class.
    """
    def setUp(self):
        self.labels = card.getCardLabels()
        # get the first label of the card
        self.label = self.labels[1]

    def test_getLabel(self):
        self.assertEqual(len(self.labels), 2)

    def test_getLabelName(self):
        self.assertEqual(self.label.getLabelName(), 'HAHAHA')

    def test_getLabelId(self):
        self.assertEqual(self.label.getLabelId(), '5b3a9c94ff9b616444c6cb7c')

    def test_getLabelBoard(self):
        self.assertEqual(self.label.getLabelBoard(), '5b3a9c9421794651e035bb22')

    def test_getLabelColor(self):
        self.assertEqual(self.label.getLabelColor(), 'yellow')

if __name__ == "__main__":
    unittest.main()
