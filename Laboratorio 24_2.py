# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:36:26 2021

@author: santi
"""

def ordenar(v1, v2, v3):
    if v1<v2 and v1<v3:
        if v2<v3:
            print ("El orden es: ", v1, v2, v3)
        else: 
            print("El orden es: ",v1,v3,v2)
    else: 
        if v2<v3:
            if v1<v3:
                print ("El orden es: ",v2, v1, v3)
            else:
                print ("El orden es: ",v2, v3, v1)
        else:
            if v1<v2:
                print ("El orden es: ",v3, v1, v2)
            else:
                print ("El orden es: ",v3, v2, v1)
        
def menor_mayor():
    numero1=int(input("Ingrese numero 1: "))
    numero2=int(input("Ingrese numero 2: "))
    numero3=int(input("Ingrese numero 3: "))
    ordenar(numero1, numero2, numero3)
    
    
       
menor_mayor()
