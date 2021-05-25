# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:37:06 2021

@author: santi
"""

#Programa que lee una tabla y la imprime desde el 1 hasta el 20 y sumar los resultados

#Declarar variables
tabla=0
multiplicador=1
resultado=0
suma_resultados=0
con_rep_ciclo=1

#Leer l numero de la tabla para la cual vamos a realizar las operaciones
tabla= int(input("Tabla:"))

#Leer el multiplicador 
multiplicador=int(input("Multiplicador:"))

#Inicio del ciclo repetitivo for
for con_rep_ciclo in range(multiplicador+1):
    resultado=tabla*con_rep_ciclo
    suma_resultados= suma_resultados+resultado
    print(tabla, " * ", con_rep_ciclo," = ", resultado)
print("La suma de los resultados es:", suma_resultados)

