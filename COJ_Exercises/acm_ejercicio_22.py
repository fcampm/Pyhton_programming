#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Subject: Problem 1626
# Date: April 21, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int (x) for x in stdin.read().split()])

n = next(nums)

for i in range(n):
    reverse = ""
    res = 0
    case = str(next(nums))
    case2 = str(next(nums))
    case = case[::-1]
    case2 = case2[::-1]
    res += int(case) + int(case2)
    res = str(res)
    res = res[::-1]
    print(int(res))
