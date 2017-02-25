#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1318
# Fecha: Febrero 3, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = (stdin.read().split())
letras = entrada [-1]
nums = [int(x) for x in entrada[:3]]
nums.sort()
d = {}
#d["A"] = nums[0]
#d["B"] = nums[1]
#d["C"] = nums[2]
d = dict(zip("ABC", nums)) # Esta linea hace lo mismo que las líneas 19, 20 y 21 usando dict(zip)
r = []
for c in letras:
    r.append(d[c])

print(" ".join([str(x) for x in r]))