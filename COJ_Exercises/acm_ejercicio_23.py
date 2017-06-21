#  -*- coding: utf-8 -*-
# Authors:
#           Fabián Camp Mussa
#
# Subject: Problem 1023.
# Date: April 26, 2017.
from __future__ import print_function
from __future__ import division

from sys import stdin

finances = [stdin.read().split()]
res = 0

for i in range(12):
    flo= str(finances[i])
    for j in range(12):
        flo2 = float(j)
        res += flo2

print(res)
