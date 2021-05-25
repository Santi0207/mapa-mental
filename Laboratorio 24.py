# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:26:57 2021

@author: santi
"""

def cantidad_vocales(cadena):
    cant=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u": 
            cant=cant+1
    print ("La cantidad de vocales en la palabra", cadena, "es:", cant)
        
cantidad_vocales("abecedario")
cantidad_vocales("alcadeno")
cantidad_vocales("murcielago")


