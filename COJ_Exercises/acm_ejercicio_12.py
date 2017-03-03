#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1288
# Fecha: Marzo 3, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int (x) for x in stdin.read().split()])
T = next(nums)

for i in range(T):
    
    N = next(nums)
    print("YES" if N % 6 == 0 else "NO") # Expresión if (consecuente if condicion else alternativa).