#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1166
# Fecha: Febrero 10, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = stdin.read().split()
num = [int (c) for c in entrada]
it = iter(num) # la función iter sirve como iterador y con la función next(it) va dando uno por uno los elementos de la lista

for i in range(next(it)):
    par = 0
    non = 0
    for j in range(next(it)):
        x = next(it)
        if x % 2 == 0:
            par += 1
        else:
            non += 1
    print (par, "even and", non, "odd.")