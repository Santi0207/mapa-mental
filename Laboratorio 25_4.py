# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:19:58 2021

@author: santi
"""

def cantidad_A(palabra):
    cont=0
    for x in range (len(palabra)):
        if palabra [x] =="a" or palabra [x] =="A":
            cont+=1
    return cont
    
    
palabra=input("Ingrese una palabra: ")
print ("la palabra", palabra,"tiene", cantidad_A(palabra), "a")
