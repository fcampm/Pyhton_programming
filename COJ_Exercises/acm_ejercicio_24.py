#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Topic: Problem number 2769.
# Date: June 21, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int (x) for x in stdin.read().split()])

N = next(nums)

for i in range(N):
    print (str(i+1)+":", "I am participating in the Engineer's day.")
