# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:11:10 2021

@author: santi
"""

# Declaro de variables

nombre= "***"
fortran=0.0
pascal=0.0
basic=0.0
cont_est=0

media=0.0


nombre=input("Ingrese nombre del estudiante:")

while(nombre != "***"):
    basic=float(input("ingrese nota definitiva basic:"))
    pascal=float(input("ingrese nota definitiva pascal:"))
    fortran=float(input("ingrese nota definitiva fortran:"))
    media= (basic+pascal+fortran)/3
    print ("La media es:",media)
    nombre=input("Ingrese nombre del estudiante:")
    cont_est=cont_est+1
print("Total de estudiantes:",cont_est)
print ("HASTA PRONTO.")
    



