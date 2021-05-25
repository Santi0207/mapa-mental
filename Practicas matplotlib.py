# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:09:15 2021

@author: santi
"""
import matplotlib
import matplotlib.pyplot as plt

nombreProductos=['Arroz','Azucar','Vino','Leche']
ventaProductos=[100,50,30,20]

def totalVentas():
    sumTotal=0
    for pos in range (4):
        sumTotal=sumTotal+ventaProductos[pos]
    return (sumTotal)
    
    
def promventas():
    promven=0.0
    promven=totalVentas()/len(ventaProductos)
    return(promven)

print("Total de las ventas: ",totalVentas())
print("Promedio de ventas: ",promventas())

fig, ax=plt.subplots()
ax.set_title('Ventas empresa')
ax.set_ylabel('Valor')
ax.set_xlabel('Nombre del producto')

plt.bar(nombreProductos,ventaProductos)
plt.show()
