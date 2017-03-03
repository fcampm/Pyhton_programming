#  -*- coding: utf-8 -*-
# Authors:
#          Pon tu nombre aquí.
#
# Tema:Actividad 3, problema 2.
# Fecha: Establecer la fecha de entrega

def main():
    n = int(input("¿Cuántos usuarios quieres?\n")) # Pide al usuario el número de datos que el ususario va a meter.
    
    for c in range(n): # Se hace un ciclo for desde 0 hasta n; donde n es el input que el usuario metio arriba.
        w = float(input("¿Cuántos kilómetros viajarás?\n")) # Pide al usuario el la cantidad de kilómetros que va a viajar.
        q = input("¿Qué tipo de servicio requieres? (X, XL, BLACK, SUV)\n") # Pide al usuario el servicio que va a usar.
        if q.upper() == "X": # Se hace una validación; en caso de que el input q sea "X" asigna el valor de uber_costo con 7.00
            uber_costo = 7.00 
        elif q.upper() == "XL": # Si entra en esta validación asigna el valor de uber_costo con 12.26
            uber_costo = 12.26
        elif q.upper() == "BLACK": # Si entra en esta validación asigna el valor de uber_costo con 16.52
            uber_costo = 16.52
        else: # Si no entra en ninguna de las validaciones anteriores asigna el valor de uber_costo con 22.72
            uber_costo = 22.72
        tarifa_dinamica = input("¿Hay tarifa dinámica? (s = si, n = no)\n")# Pide al usuario si va a ver tarifa dinámica donde s es si y n no
        if tarifa_dinamica.lower() == "s": # Se hace la validación en caso de que tarifa_dinamica sea s entra en esta validación.
            tarifa_dinamica_o = float(input("¿Cuál es la tarifa dinámica?\n")) # Pide al usuario que proporcione el valor de tarifa dinámica
        else: # Si no entra en la validación de arriba asigna el a tarifa_dinmamica_o con 1.
            tarifa_dinamica_o = 1 
        res = w * uber_costo * tarifa_dinamica_o # Se hace la multiplicación de todos los datos pertinentes para sacar el resultado del costo.
        print("El costo aproximado de tu viaje es de ", res, "pesos") # Se hace un print con la salida espera.
        print() # Se hace un print vacio para que no se amontone con los datos de los usuarios siguientes (en caso de haber)
    print("El programa ha terminado") # Este print al estar afuera del ciclo for avisa al usuario que el programa ha terminado de correr.
main()