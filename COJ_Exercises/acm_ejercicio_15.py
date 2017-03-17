#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1300
# Fecha: March 17, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int(x) for x in stdin.read().split()])
s = set()

for i in range(10):
    n = next(nums)
    tot = n % 42
    s.add(tot)

print(len(s))