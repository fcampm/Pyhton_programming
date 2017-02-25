#  -*- coding: utf-8 -*-
# Authors:
#          Pon tu nombre aquí.
#
# Tema:Actividad 3, problema 3.
# Fecha: Establecer la fecha de entrega

def main():
    w = "s" # Se declara la variable w para el ciclo while.
    while w == "s": # Se establece el ciclo while con la condición que mientras w sea "s" el programa seguirá corriendo.
        a = float(input("¿De cuántos kilómetros será su viaje?\n")) # Se le pide al usuario la cantidad de kilómetros que recorrerá en su viaje.
        if a >= 0 and a <= 12.8: # Se establece la condición que mientras a sea mayor o igual que 0 y a menor o igual que 12.8 entra en la condición
            costo = 7.00 # Se asigna el valor de costo con 7.00
            print ("Su viaje será considerado como corto y su costo es:", costo, "pesos") # Se imprime la salida esperada.
        if a >=12.9 and a <= 25.6: # Se establece la condición que mientras a sea mayor o igual que 12.9 y a sea menor o igual que 25.6 entra en la condición
            costo = 16.00 # Se asigna el valor de cosoto con 16.00
            print ("Su viaje será considerado como largo y su costo es:", costo, "pesos") # Se imprime la salida esperada.
        w = input("¿Desea introducir los datos de otro usuario (s/n)?\n") # Se pregunta si va a haber más usuarios en caso de que la respuesta sea n se sale del ciclo while
    print() # Imprime un espacio en blanco para no amontonar los datos.
    print("Ha terminado el programa") # Imprime un aviso de que el programa terminó de correr.
main()