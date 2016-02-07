#!/usr/bin/env python
from test_common import xpass

print("outside")


def bingo(value):
    print("inside")
    print(value)

bingo('boom')
bingo(xpass)
