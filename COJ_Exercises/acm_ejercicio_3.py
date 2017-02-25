#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problema 1485
# Fecha: Febrero 3, 2017.

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada =list(stdin.read().strip())
entrada.sort()
entrada = "".join(entrada)
print(entrada)