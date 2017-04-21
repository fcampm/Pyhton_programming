#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Subject: Problem 2634
# Date: April 21, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = iter(stdin.read().split())

n = int(next(entrada))

months_year = [0] * 13


for e in range(n):
    ID = next(entrada)
    date = next(entrada)
    day, month, year = date.split('/')
    month = int(month)
    months_year[month] += 1

for i in range (1, 13):
    print(i, months_year[i])
