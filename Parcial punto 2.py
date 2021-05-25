# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:04:26 2021

@author: santi
"""

#Nick alejandro villa_82202118163
#Santiago lopez_82202117875
#Mariana grand_101202114369

import math #importacion de la libreria

def heron_area(a,b,c): # encabezado donde se nombra 
    s = (a+b+c)/2 # hallar el semiperimetro
    area = s*(s-a)*(s-b)*(s-c) # formula para hallar el area
    raiz = math.sqrt(area) # sirve para hallar la raiz
    print("El area del triangulo es: ", raiz ) # imprime el area del triangulo
    
def heron_perimetro(a,b,c): # encabezado donde se nombra
    perimetro= a+b+c #operacion para hallar perimetro
    print("El perimetro del triangulo es: ", perimetro) #imprime el perimetro del triangulo
    
#BLOQUE PRINCIPAL
a=float(input("Ingrese el primer valor:")) # donde el usuario ingresa el primer valor 
b=float(input("Ingrese el segundo valor:")) # donde el usuario ingresa el segundo valor 
c=float(input("Ingrese el tercer valor: ")) # donde el usuario ingresa el tercer valor 
heron_area(a, b, c) #llamado de la funcion 
heron_perimetro(a, b, c) #llamado de la funcion 

