#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema número 1050.
# Fecha: Febrero 17, 2017.

from __future__ import print_function
from __future__ import division

from fractions import gcd

from sys import stdin

N = int (stdin.read())

c = 0
for x in range (1, N + 1):
    if gcd (N, x) == 1:
        c += 1
print(c)