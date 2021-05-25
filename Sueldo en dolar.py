# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:20:38 2021

@author: santi
"""

horas_trabajadas= int (input ("ingrese las horas trabajadas:"))
valor_hora= int ( input ("ingrese valor por hora:"))
sueldo= horas_trabajadas*valor_hora 
seguridad= sueldo*0.08
sueldo_total= sueldo-seguridad
dolar= sueldo_total/3496
bonificacion= sueldo_total*0.02+sueldo_total
print ("Debe pagar de seguridad:", seguridad)
print ("su sueldo total es:", sueldo_total)
print ("su sueldo en dolares es:", dolar,"$")


if dolar > 300:
    print("No obtiene la bonificaion")
    
elif dolar < 300:
    print("Obtiene la bonificacion del 2%", bonificacion)
    
else:
    print(" Ingrese valores correctos")
    
