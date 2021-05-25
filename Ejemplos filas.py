# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:24:52 2021

@author: santi
"""
# 1 matriz
matriz= [[3,5,7,12],[21,3,8,2],[4,7,2,9]]

# 2 Imprimir la matriz
print (matriz)

# 3 Imprimir una posicion fijo
print ("La posicion especifica es:", matriz[2][1])

# 4 Solucitar la posicion al usuario 
fila= int(input("Fila: "))
columna=int(input("Columna: "))
print("Posicion leida es: ", matriz[fila-1][columna-1])

# 5 Imprimir una fila determinada 
print ("Fila 0: ", matriz[0])
print ("Fila 1: ", matriz[1])
print ("Fila 2: ", matriz[2])

# 6 Imprimir una columna 
for f in range (3):
    print(matriz[f][1])
    
# 7 Imprimir columna que el usuario requiera 
columna=int(input("Columna que desea: "))
for f in range(3):
    print (matriz[f][columna])
    
# 8 Sumar elementos de la matriz 
sumaMatriz=0
for f in range (3):
    for c in range (4):
        sumaMatriz=sumaMatriz+matriz[f][c]
print("La suma de los  elementos: ", sumaMatriz)