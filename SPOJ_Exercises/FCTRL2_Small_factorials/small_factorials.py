#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Topic: FCTRL2 - Small factorials.
# Date: September 18, 2017.

from __future__ import print_function
from __future__ import division
from math import factorial

from sys import stdin

nums = (int (x) for x in stdin.read().split())
n = next(nums)

for i in range(n):
    t = next(nums)
    res = factorial(t)
    print(res)
