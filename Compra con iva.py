# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:38:30 2021

@author: santi
"""

compra= int (input("ingrese el valor de su compra:"))
iva_1=  float (input("ingrese el valor del iva en su pais:"))
iva_2= compra*iva_1
descuento= compra*0.05
valor_total= compra-descuento
print ("el valor del iva es:", iva_2)
print ("el total de su compra es:", valor_total)        

           