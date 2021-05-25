# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:01:41 2021

@author: santi
"""

def presentacion():
    print("Programa que permite cargar dos valores por teclado, efectua la suma de los valores, muestra el resultado de la suma")


def suma():
    valor1=int(input("Ingrese el valor 1:"))
    valor2=int(input("Ingrese el valor 2:"))
    suma=valor1+valor2
    print( valor1, "+", valor2, "=", suma)


presentacion()
suma()
