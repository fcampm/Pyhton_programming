#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problem 48.
# Specification: Use the final 10 digits of that number.
# Fecha: Enero 14, 2017.

def suma_de_exponentes(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i ** i
    return suma

def main():
    print(suma_de_exponentes(1000))
    
main()