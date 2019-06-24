
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

from .conn import trelloConn
from .label import trelloStatsLabel


class trelloStatsCards:
    """
    Class to represent the trelloStats Cards of a given list.
    """

    def __init__(self, idList=None):
        self.idList = idList
        self.conn = trelloConn()
        if (not idList):
            self.listCards = []
        else:
            self.listCards = self._getlistCards()

    def getCards(self):
        return self.listCards

    def _getlistCards(self):
        cards = []
        for card in json.loads(self.conn.get('/lists/%s/cards/' % self.idList)):
            if (not card['closed']):
                cards.append(trelloStatsCard(card))
        return cards


class trelloStatsCard:
    """
    trelloStats Card class.
    """

    def __init__(self, cardDict=None):
        if (not cardDict):
            return None

        self.id = cardDict['id']
        self.name = cardDict['name']
        self.idList = cardDict['idList']
        self.labels = []
        for idLabel in cardDict['idLabels']:
            self.labels.append(trelloStatsLabel(idLabel))

    def getCardName(self):
        return self.name

    def getCardId(self):
        return self.id

    def getCardList(self):
        return self.idList

    def getCardLabels(self):
        return self.labels


if __name__ == "__main__":
    print
