#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
#
# Tema: 
# Fecha: 

c = int(input("Introduce el tiempo en segundos: "))
d = 0
minut = 0
horas = 0
if c != 0:
    minut = c // 60
    s = minut % 60
    x = minut // 60
    horas = x % 60
    w = x // 60 
    f = w % 60
    seg = s + x + f
print(horas, ":", minut, ":", seg)
