#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problem 1484.
# Fecha: March 4, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = stdin.read().split()

N = int(entrada[0])
nums = iter([float(x) for x in entrada[1:]])

mayor = next(nums)
indice = 1

for x, i in zip(nums, range(2, N + 1)):
    if x >= mayor:
        mayor = x
        indice = i
print(indice)