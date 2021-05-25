# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:23:01 2021

@author: santi
"""

import pandas as pd

datosEstudiantes= pd.DataFrame({'Estudiantes':['Juan','Valentina','Santiago'],
                                'Apellido':['Arias','Idarraga','Lopez'],
                                'Edad':[18,17,18]})

datosEstudiantes['Vivo']='True'
datosEstudiantes['Genero']='Masculino'

datosEstudiantes.insert(3,'Genero correcto',['Masculino','Femenino','Masculino'])
datosEstudiantes.insert(4,'Semestre',['Primero','Quinto','Septimo'])

datosEstudiantes=datosEstudiantes.assign(Colegio=['Colseñora','Universitario','Universitario'])



print(datosEstudiantes)
