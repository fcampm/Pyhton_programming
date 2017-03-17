#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problem 1101
# Fecha: March 17, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int(x) for x in stdin.read().split()])
n = next(nums)
si = set() # la función set te crea un conjunto en donde se añadirán un elemento pero el set es más eficiente que una lista 
no = set() 

for i in range(n):    
    inicio = next(nums)
    fin = next(nums)
    r = []
    for j in range(inicio, fin + 1):
        if j in si:
            r.append(str(j))
        elif j not in no:
            b = bin(j)[2:]
            if b == b[::-1]:
                r.append(str(j))
                si.add(j)
            else:
                no.add(j)
                
    print (' '.join(r))