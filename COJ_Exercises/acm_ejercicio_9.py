#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1004
# Fecha: Febrero 24, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int (x) for x in stdin.read().split()])

T = next(nums)
for c in range(T):
    M = next(nums)
    N = next(nums)
    if M == N and N % 2 == 0:
        print('L')
    elif M == N and N % 2 != 0:
        print('R')
    elif M > N and N % 2 != 0:
        print('D')
    elif M > N and N % 2 == 0:
        print('U')
    elif N > M and M % 2 == 0:
        print('L')
    elif N > M and M % 2 != 0:
        print('R')