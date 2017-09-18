#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Topic: MUL - Fast Multiplication.
# Date: September 18, 2017.

from __future__ import print_function
from __future__ import division


from sys import stdin

nums = (int (x) for x in stdin.read().split())
n = next(nums)

for i in range(n):
    a = next(nums)
    b = next(nums)
    print (a*b)
