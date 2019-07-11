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

def setUpModule():
    global board, list
    board = TrelloStatsBoard('testAPI')
    list = board.getBoardLists()[1]     # get the second list (ble)


class TrelloStatsCardTests(unittest.TestCase):
    """
    Test the TrelloStatsCards and TrelloStatsCard classes.
    """
    def setUp(self):
        self.cards = list.getListCards()
        # get the second card of the list
        self.card = self.cards[1]

    def test_getCards(self):
        self.assertEqual(len(self.cards), 2)

    def test_getCardName(self):
        self.assertEqual(self.card.getCardName(), 'One more test')

    def test_getCardId(self):
        self.assertEqual(self.card.getCardId(), '5d11ef9284d894576abbbaf7')

    def test_getCardList(self):
        self.assertEqual(self.card.getCardList(), '5b3c6ee2e99fe70899b10376')

    def test_getCardLabels(self):
        labels = self.card.getCardLabels()
        self.assertEqual(len(labels), 2)


if __name__ == "__main__":
    unittest.main()
