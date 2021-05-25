# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:34:49 2021

@author: santi
"""

#Nick alejandro villa_82202118163
#Santiago lopez_82202117875
#Mariana grand_101202114369

import math #Importacion de la libreria 

def area_triangulo(a): # nombre de la primera funcion o encabezado
    raiz= math.sqrt(3) # Solucion de la raiz 
    area= (raiz/4)*(a**2) # Solcion para hallar el area del triangulo
    print("El area del triangulo es:", area) # impresion del resultado del area del triangulo

def perimetro_triangulo(p): #Nombre de la segunda funcion o encabezado
    perimetro= p+p+p # Formula y solucion del perimetro del triangulo
    print("El perimetro del triangulo es:", perimetro) # Impresion del resultado del perimetro del triangulo
    
#BLOQUE PRINCIPAL
lado= float(input("Ingrese los valores del triangulo:")) # El usuario ingresa valores deseados
area_triangulo(lado) #llamado a la primera funcion
perimetro_triangulo(lado)#llamado a la segunda funcion


