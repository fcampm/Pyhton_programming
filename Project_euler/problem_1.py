#  -*- coding: utf-8 -*-
# Authors:
#           Fabián Camp Mussa
#
# Tema: Problem 1
# Fecha: Octubre 21, 2016.

def multiples (n):
    a = 0
    for n in range (n):
        if n % 5 == 0:
            a += n
        elif n % 3 == 0:
            a += n
    return a
    

def main():
    print (multiples(1000))
    

main()
    