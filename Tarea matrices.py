# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:17:30 2021

@author: santi
"""

#Matriz
MatrizNumeros= [[7,8,3],[1,9,2],[4,6,5]]
print(MatrizNumeros)

#Suma de todos los elementos de la matriz 
sumEle=0
for f in range (3):
    for c in range(3):
        sumEle=sumEle+MatrizNumeros[f][c]
print ("La resultado total de la suma es: ",sumEle)

#Imprimir la matriz 
for f in range (3):
    for c in range(3):
        print ("El dato: ", MatrizNumeros[f][c])
        
#Suma de la diagonal principal        
sumdiapri=0
for pos in range(3):
    sumdiapri=sumdiapri+MatrizNumeros[pos][pos]
print("La suma de la diagonal principal es: ",sumdiapri)



        