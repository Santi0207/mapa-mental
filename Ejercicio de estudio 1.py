# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:03:16 2021

@author: santi
"""



nota1=int(input("Ingrese la nota de Marcelo :"))
nota2=int(input("Ingrese la nota de Carlos :"))
nota3=int(input("Ingrese la nota de Manuel :"))

if (nota1 > nota2 and nota1 > nota3):
    print ("Marcelo tiene la nota mas alta")
if (nota2 > nota1 and nota2 > nota3):
    print ("Carlos tiene la nota mas alta")
if (nota3 > nota1 and nota3 > nota1):
    print ("Manuel tiene la nota mas alta")
    
