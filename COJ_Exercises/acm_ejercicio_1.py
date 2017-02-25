#  -*- coding: utf-8 -*-
# Authors:
#          Fabián Camp Mussa
#
# Problema: 1306
# Tema: Programa que imprima sí, si el número es divisible entre 4 y no si no lo es.
# Fecha: 27 enero, 2017.

from __future__ import print_function # Ambas lineas se importan para no tener problemas con la versión de python ya sea 2.7 o 3.x
from __future__ import division

from sys import stdin # Este import es para que la entrada sea de un archivo en lugar de que la entrada sea el teclado.

entrada = stdin.read().split()
enteros = [int(c) for c in entrada] # Checar documentación en la carpeta ACM, archivo ACM.1
t = enteros[0]
for n in enteros[1:]: # Se controla el ciclo for con un slide de la variable enteros
    if n % 4 == 0: # En esta parte pregunta si el residuo de n dividido entre 4 es igul a 0
        print("YES") # Otra forma de imprimir los documentos al archivo std es: stdout.write("YES\n") recordando tomar
    else:
        print("NO")
        
    