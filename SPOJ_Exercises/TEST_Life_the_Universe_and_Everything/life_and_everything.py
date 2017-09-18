#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Topic: TEST - Life, the Universe, and Everything
# Date: September 18, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = [int (x) for x in stdin.read().split()]
for i in nums:
    if i != 42:
        print(i)
    else:
        break
