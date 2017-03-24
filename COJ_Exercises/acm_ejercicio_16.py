#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1842
# Fecha: Marzo 20, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int(x) for x in stdin.read().split()])
n = next(nums)

for i in range(n):
    x = next(nums)
    y = next(nums)
    x2 = next(nums)
    y2 = next(nums)
    res = 0
    res += abs(x - x2) + abs(y - y2)
    print(res)