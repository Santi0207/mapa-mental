# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:21:03 2021

@author: santi
"""
# Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma,
#Repetir la carga e impresion de la suma 5 veces.
#Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.
def suma():
    valor1=int(input("Ingrese el valor 1:"))
    valor2=int(input("Ingrese el valor 2:"))
    suma=valor1+valor2
    print( valor1, "+", valor2, "=", suma)
    print ("El resultado es:", suma)



def separacion():
    print("                   ")    



for x in range(5):
    suma()
    separacion()
    