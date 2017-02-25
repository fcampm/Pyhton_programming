#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1059
# Fecha: Febrero 10

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = [int (x) for x in stdin.read().split()]

for i in nums[:-1]:
    b = bin(i)[2:]
    p = b.count("1")
    print ("The parity of", b, "is", p, "(mod 2).")