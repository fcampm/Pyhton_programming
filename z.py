#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: 
# Fecha: 

def fibo():
    n = int(input("Teclea el numero para la sucesión de fibonacci: "))
    suma = []
    i = 0
    j = 1
    for k in range(1, n + 1):
        t = i + j
        j = i
        i = t
        suma.append(j)
    print(suma)