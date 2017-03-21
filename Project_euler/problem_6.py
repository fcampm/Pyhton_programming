#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problem 6.
# Fecha: Enero 14, 2017.

def suma1(n):
    r = 0
    for c in range (n + 1):
        r += c ** 2
    return r

def suma2(n):
    d = 0
    w = 0
    for c in range (n + 1):
        d += c
    w += d ** 2
    return w
    
def resta_sumas(n):
    q = 0
    q += suma2(n) - suma1(n)
    return q
    
def main():
    print(resta_sumas(100))

main()