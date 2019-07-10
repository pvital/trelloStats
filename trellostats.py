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

import sys

from trellostats.app import TrelloStatsApp


def usage():
    print("""trelloStats - collect statistics from Trello boards.
Usage:
    trellostats <board>
    trellostats -h | --help
    trellostats --version
Options:
    -h --help       Show this message.
    --version       Show version.
""")

def main(argv):
    if len(argv) < 2:
        usage()
        sys.exit(2)

    if (argv[1] == "-h") or (argv[1] == "--help"):
        usage()
        sys.exit(0)
    elif (argv[1] == "--version"):
        print("trellostats v0.1")
        sys.exit(0)

    # Read the arguments to create the card
    stats = TrelloStatsApp(argv[1])

    # Print the stats for Board
    print("==> STATS: Number of lists: %d" % stats.getNumList())
    print("==> STATS: Number of open cards: %d" % stats.getNumOpenCards())
    print("==> STATS: Number of labels: %d" % stats.getNumLabels())

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
