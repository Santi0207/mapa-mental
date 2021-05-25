# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:38:33 2021

@author: santi
"""

numero=0
suma=0
media = 0
rep_ciclo=0


numero=int(input("Ingrese numero:"))

while(numero > 0):
    suma= suma+numero
    numero=int(input("Ingrese numero:"))
    rep_ciclo= rep_ciclo + 1
    media= suma / rep_ciclo
print("La media de la lista es:",media)

    

