# -*- coding: utf-8 -*-
# Problema 20 de proyect Euler
# Authors: Fabián Camp Mussa

from math import factorial

def calculaFactorial(n):
    a = ""
    res_final = 0
    b = []
    res = 0
    res += factorial(n)
    r = str(res)
    for c in r:
        res_final += int(c)
    print (res_final)

def main():
    calculaFactorial(100)

main()
