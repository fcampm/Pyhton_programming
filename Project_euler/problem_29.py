#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problem 29
# Fecha: Marzo 20, 2017.

def distinctPOWERS(a, b):
    s = set()
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            y = i ** j
            s.add(y)
            w = sorted(s)
            res = len(w)
    print(res)

def main():
    distinctPOWERS(2, 100)
    
main()