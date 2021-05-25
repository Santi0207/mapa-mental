# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:36:42 2021

@author: santi
"""

def retornar_promedio(v1, v2, v3):
    promedio=(v1+v2+v3)/3
    return promedio 

valor1=int(input("Ingrese el primer valor: "))
valor2=int(input("Ingrese el segundo valor: "))
valor3=int(input("Ingrese el tercer valor: "))
print("El promedio de los tres numeros es: ", retornar_promedio(valor1,valor2,valor3))

    