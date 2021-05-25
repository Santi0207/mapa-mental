# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:37:25 2021

@author: santi
"""

# Programa que calcula la nota de un estudiante 
# Entradas
# Pedir el nombre del estudiante y sus 3 notas de parciales

cantidad_est= int(input("Cantidad de estudiantes:"))

#Inicializar la variable que controla el ciclo
conRep=0

#Variable real para sumar las definitivas del grupo
sumaDefGru=0.0

#
notproDefGru=0.0

while(conRep < cantidad_est):
    #Instrucciones a repetir
    nombre_est=input("Nombre del estudiante:")
    nota_1= float(input("Parcial 1:"))
    nota_2= float(input("Parcial 2:"))
    nota_3= float(input("Parcial 3:"))

    # Calculos 
    notadef= (nota_1+nota_2+nota_3)/3
    
    #Acumulo las definitivas del grupo
    sumaDefGru=sumaDefGru+notadef

    # Imprimir resultados - salidas
    print (f"1.Su nota definitiva es:{notadef:.2f}")
    
    #Incrementar la variable que controla el ciclo 
    conRep= conRep+1
    
#Calcular el promedio del grupo
notProDefGru = sumaDefGru/cantidad_est

#  Imprimir la nota promedio del grupo
print(f"2.La nota promedio del grupo es :{notProDefGru:.2f}")

     
    