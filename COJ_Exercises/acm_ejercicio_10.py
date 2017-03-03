#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1064.
# Fecha: Marzo 3, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums =iter([int(x) for x in stdin.read().split()])
while True:
    h1 = next(nums)
    m1 = next(nums)
    h2 = next(nums)
    m2 = next(nums)
    
    if h1 == m1 == h2 == m2 == 0:
        break
    
    mn1 = h1 * 60 + m1
    mn2 = h2 * 60 + m2
    
    if mn1 > mn2:
        mn2 += 24*60
    
    print(mn2 - mn1)