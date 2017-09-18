#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Topic: Problem CRDS - Cards.
# Date: August 21, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = (int (x) for x in stdin.read().split()) # Por comprensión existe una lista y un iterador (iter)
T = next(nums)

for i in range(T):
    N = next(nums)
    r = ((3 * N * (N + 1)) // 2 - N) % 1000007
    print (r)
