# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:33:49 2021

@author: santi
"""

def superficie(lado1,lado2):
    superficie1=lado1*lado2
    return superficie1
print("    ")
print("Primer rectangulo")
lado1=int(input("Ingrese el valor de la base: "))
lado2=int(input("Ingrese el valor de la altura: "))
print("    ")
print("Segundo rectangulo")
lado3=int(input("Ingrese el valor de la base: "))
lado4=int(input("Ingrese el valor de la altura: "))

if superficie(lado1,lado2) == superficie(lado3, lado4):
    print ("Los dos rectangulos tienen la misma supericie")
else:
    if superficie(lado1, lado2) > superficie(lado3,lado4):
        print ("El primer rectangulo tiene una superficie mayor")
    else:
        print("El segundo rectangulo tiene una superficie mayor")

