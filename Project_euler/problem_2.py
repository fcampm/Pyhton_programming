#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: Problem 2.
# Fecha: Enero 14, 2017.
def fibo(n):
    suma = []
    total = 0
    i = 0
    j = 1
    for k in range(1, n + 1):
        t = i + j
        j = i
        i = t
        if j <= 4000000 and j % 2 == 0:
            suma.append(j)
          
    for c in suma:
        total += c
    return total

def main():
    print(fibo(400))

main()