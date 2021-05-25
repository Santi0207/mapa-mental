# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:27:23 2021

@author: santi
"""

#Nick alejandro villa_82202118163
#Santiago lopez_82202117875
#Mariana grand_101202114369

resultado1=(int(input("ingrese el valor:")))
def fibonacci(a): #nombre de la funcion
    
    if a== 0: #es el condicional y es el valor desde donde empieza el conteo
        serie_fibonacci=[]# es una lista la cual se inicializa en 0
        
    if a== 1: # es con el valor que sigue la secuencia
        serie_fibonacci=[1]# es el primer valor del listado o de la serie
        
    if a== 2:
        serie_fibonacci=[0,1] #se retorna para la lista de inicializacion
        
    if a > 2: #si a es mayor que 2 
        serie_fibonacci=[0,1] #son los valores cuando a es mayor a 2
        i = 1
        
    while i < a: # si i es menor que a se cumple la condicion y nos muestra los valores
        serie_fibonacci.append(serie_fibonacci[i] + serie_fibonacci[i-1])
        i += 1
    
    return serie_fibonacci #se retorna la variable serie_fibonacci

print("El numero de la secuencia es:", resultado1)
resultado= fibonacci(9) #un llamado a la funcion 
print(resultado) #imprime la lista que se le pide











