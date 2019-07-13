
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


import json

from .card import TrelloStatsCards
from .conn import TrelloConn


class TrelloStatsLists:
    """
    Class to represent the trelloStats Lists of a given board.
    """

    def __init__(self, idBoard=None):
        self.idBoard = idBoard
        self.conn = TrelloConn()
        if (not idBoard):
            self.boardLists = []
        else:
            self.boardLists = self._getBoardLists()

    def getLists(self):
        return self.boardLists

    def _getBoardLists(self):
        lists = json.loads(self.conn.get('/boards/%s/lists/' % self.idBoard))
        return [TrelloStatsList(list) for list in lists if not list['closed']]


class TrelloStatsList:
    """
    trelloStats List class.
    """

    def __init__(self, listDict=None):
        if (not listDict):
            return None

        self.id = listDict['id']
        self.name = listDict['name']
        self.idBoard = listDict['idBoard']
        self.cards = TrelloStatsCards(listDict['id']).getCards()

    def getListName(self):
        return self.name

    def getListId(self):
        return self.id

    def getListBoard(self):
        return self.idBoard

    def getListCards(self):
        return self.cards


if __name__ == "__main__":
    print
