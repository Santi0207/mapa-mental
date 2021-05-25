# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:55:31 2021

@author: santi
"""

def calcular_menor():
    valor1=int(input("Ingrese primer valor 1: "))
    valor2=int(input("Ingrese primer valor 2: "))
    valor3=int(input("Ingrese primer valor 3: "))
    if valor1<valor2 and valor1<valor3:
        print ("El menor es:", valor1)
    else:
        if valor2<valor3:
            print ("El menor es:", valor2)
        else:
            print("El menor es:", valor3)
    

calcular_menor()
calcular_menor()
