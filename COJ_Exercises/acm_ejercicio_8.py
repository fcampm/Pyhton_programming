#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1078
# Fecha: Febrero 17, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int (x) for x in stdin.read().split()])

T = next(nums)
for i in range(T):
    N = next(nums)
    suma = 0
    for j in range(N):
        dulces = next(nums)
        suma += dulces
    if suma % N == 0:
        print("YES")
    else:
        print("NO")