# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:07:10 2021

@author: santi
"""

operacion = 0
while True:
    print("""
    ¿que operacion quieres hacer?
    1.SUMA
    2.RESTA
    3.MULTIPLICACION
    4.DIVISION
    5.POTENCIA
    6.SALIR
    """)
    operacion = float(input("introduce un numero"))
    if operacion == 1:
        x = float(input("ingrese numero:"))
        y = float(input("ingrese numero:"))
        print("La suma de",x,"+",y,"es",x+y)
        
    elif operacion == 2:
        x = float(input("ingrese numero:"))
        y = float(input("ingrese numero:"))
        print("La resta de",x,"-",y,"es",x-y)
        
    elif operacion == 3:
        x = float(input("ingrese numero:"))
        y = float(input("ingrese numero:"))
        print("La multiplicacion de",x,"*",y,"es",x*y)
        
    elif operacion == 4:
        x= float(input("ingrese numero:"))
        y= float(input("ingrese numero:"))
        print("La division de",x,"/",y,"es",x/y)
        
    elif operacion == 5: 
        x = float(input("ingrese numero base:"))
        y = float(input("ingrese numero exponente:"))
        print("El producto de",x,"*",y,"es",x*y)
        
    elif operacion == 6:
        break
    else:
        print("Opción incorrecta")



