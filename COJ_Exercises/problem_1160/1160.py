#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Topic: Problem number 2769.
# Date: August 21, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int (x) for x in stdin.read().split()])

n = next(nums)

for i in range(n):
    x = next(nums)
    y = next(nums)
    if x == y or y == x-2:
        v = 2 * x
        if x % 2 == 1:
            v -= 1
        if x != y:
            v -=2
        print(v)
    else:
        print("No Number")
