# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:23:58 2021

@author: santi
"""
def f_saludo():
    print("CALCULO DE VALOR DE PRODUCTOS")
def f_despedida():
    print("HASTA PRONTO")
def f_factura():
    nom_art=""
    can_art=0
    valor_uniart=0.0
    
    cons_iva=0.19
    
    net_pag=0.0
    iva_pag=0.0
    total_pag=0.0
    
    nom_art=input("Ingrese articulo :") 
    can_art=int(input("Ingrese cantidad:"))
    valor_uniart=int(input("Ingrese valor del articulo:"))
    
    net_pag= can_art*valor_uniart
    iva_pag=net_pag*cons_iva
    total_pag=net_pag+iva_pag
    print ("El precio neto: ", net_pag)
    print ("el valor del iva es: ", iva_pag)
    print ("El valor del articulo es: ", total_pag)

f_saludo()
f_factura()
f_despedida()

