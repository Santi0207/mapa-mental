# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:27:38 2021

@author: santi
"""
def saludo():
    print("Bienvenido")
    
def calcular_cuadrado():
    valor1=int(input("Ingrese un valor:"))
    cuadrado=valor1*valor1
    print(" ")
    print ("El cuadrado del entero es:", cuadrado)
    
def calcular_producto():
    valor2=int(input("Ingrese entero 1:"))
    valor3=int(input("Ingrese entero 2:"))
    producto=valor2*valor3
    print ("     ")
    print ("El producto es:", producto)
    print ("     ")

def despedida():
    print("Hasta luego")
    

saludo()
calcular_cuadrado()
calcular_producto()
despedida()