#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1188, Cow multiplicator
# Fecha: Febrero 3, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = stdin.read().split()

suma = 0
for a in entrada[0]:
    for b in entrada[1]:
        x= int(a)
        y= int(b)
        suma += x * y
print(suma)