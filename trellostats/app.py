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


from .board import TrelloStatsBoard


class TrelloStatsApp:
    """
    trelloStats App class.
    """

    def __init__(self, board=None):
        self.board = TrelloStatsBoard(board)
        self.numLabels = 0
        self.numLists = 0
        self.numOpenCards = 0
        if (not self.board.isBoardClosed()):
            print(self.board.getBoardLabels())
            self.numLabels = len(self.board.getBoardLabels())
            self.numLists = len(self.board.getBoardLists())
            self.numOpenCards = self._numOpenCard()

    def getStats(self):
        return {
            'numLabels': self.numLabels,
            'numLists': self.numLists,
            'numOpenCards': self.numOpenCards
        }

    def getNumLabels(self):
        return self.numLabels

    def getNumList(self):
        return self.numLists

    def getNumOpenCards(self):
        return self.numOpenCards

    def _numOpenCard(self):
        openCards = 0
        for list in self.board.getBoardLists():
            openCards += len(list.getListCards())
        return openCards


if __name__ == "__main__":
    print
