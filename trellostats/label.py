
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

from .conn import TrelloConn


class TrelloStatsLabel:
    """
    trelloStats Label class.
    """

    def __init__(self, idLabel):
        conn = TrelloConn()
        labelDict = json.loads(conn.get('/labels/%s/' % idLabel))
        if (labelDict):
            self.id = labelDict['id']
            self.name = labelDict['name']
            self.idBoard = labelDict['idBoard']
            self.color = labelDict['color']

    def getLabelName(self):
        return self.name

    def getLabelId(self):
        return self.id

    def getLabelBoard(self):
        return self.idBoard

    def getLabelColor(self):
        return self.color


if __name__ == "__main__":
    print
