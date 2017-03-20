#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Power Digit Sum (Project Euler)
# Fecha: Marzo 20, 2017.

def powerSUM(n):
    w = []
    a = 2**n
    res = 0
    d = ""
    d += str(a)
    for c in d:
        w.append(int(c))
    for i in range(len(w)):
        res += w[i]
    print(res)
    
def main():
    powerSUM(1000)

main()