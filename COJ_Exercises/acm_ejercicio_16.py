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
    if x >= x2 and y >= y2:
        res += (x-x2) + (y-y2)
    if x >= x2 and y2 >= y:
        res += (x-x2) + (y2-y)
    if x2 >= x and y >= y2:
        res += (x2-x) + (y-y2)
    if x2 >= x and y2 >= y:
        res += (x2-x) + (y2-y)
    print(res)