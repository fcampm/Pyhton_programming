#  -*- coding: utf-8 -*-
# Authors:
#          Pon tu nombre aquí.
#
# Tema:Actividad 3, problema 1.
# Fecha: Establecer la fecha de entrega

def main():
    w = "n" # Se establece la variable para usar en el ciclo while.
    while w == "n": # Se establece el ciclo while que mientras w sea "n" se repitirá hasta que cambie ese valor.
        n = int(input("¿Qué tipo de gasolina desea (1 = Magna, 2 = Premium, 3 = Diesel)?\n")) # Se pregunta al usuario que tipo de gasolina quiere 1-Magna, 2-Premium y 3-Diesel.
        if n == 1: # Se valida si n es igual a 1 y si lo es entra en este apartado.
            costo_gasolina = 13.98 # Se asigna a costo_gasolina el valor de 13.98
            cantidad_litros = int(input("¿Cuántos litros quiere comprar de Magna?\n")) # Se pregunta al usuario la cantidad de litros.
            res = costo_gasolina * cantidad_litros # Se hace la matemática para calcular el total a pagar.
            print("Su compra costará ", res, "pesos") # Se imprime la salida esperada.
            print() # Se hace un print vacio para no amontonar los datos.
        elif n == 2: # Se valida si n es igual a 2 y si lo es entra en este apartado.
            costo_gasolina = 14.81 # Asigna el valor a costo_gasolina de 14.81
            cantidad_litros = int(input("¿Cuántos litros quiere comprar de Premium?\n")) # Se pregunta al usuario la cantidad de litros.
            res = costo_gasolina * cantidad_litros # Se hace la matemática para calcular el total a pagar.
            print("Su compra costará ", res, "pesos") # Se imprime la salida esperada.
            print() # Imprime un espacio vacio para no amontonar los datos.
        else: # En caso de no entrar en ninguna de las validaciones anteriores entra en esta.
            costo_gasolina = 14.45 # Se asigna a costo_gasolina con el valor de 14.45
            cantidad_litros = int(input("¿Cuántos litros quiere comprar de Diesel?\n")) # Se pregunta al usuario la cantidad de litros.
            res = costo_gasolina * cantidad_litros # Se hace la matemática para calcular el total a pagar.
            print("Su compra costará ", res, "pesos") # Se imprime la salida esperada.
            print() # Imprime un espacio vacio para no amontonar los datos.
            
        w = input("¿Ha terminado el día (s=si, n=no)?\n") # Se le asigna un nuevo valor a w en caso de que sea w = s se acaba el ciclo while.
    print("El programa ha terminado") # Imprime el mensaje de que el programa ha terminado de correr
    
main()
        