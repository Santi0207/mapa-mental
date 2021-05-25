# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:52:19 2021

@author: santi
"""

import pandas as pd

df_archivoExcel=pd.read_excel('ventas_productos_1.xlsx')
df_archivoExcel=df_archivoExcel[:10].copy()

print (df_archivoExcel)


#df_archivoExcel.plot(kind)
