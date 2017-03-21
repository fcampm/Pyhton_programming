#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problem 3.
# Fecha: Enero 15, 2017.

def primos(n):
    a = 2
    while n > a:
        if n % a == 0:
            n = n // a
            a = 2
        else:
            a += 1
            
    return a
    
def main():
    print(primos(600851475143))
    
main()