# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:15:36 2021

@author: santi
"""
import random

con_rep=0
numero=0
acu_sum_tds_num=0
acu_sum_tds_pos=0
acu_sum_tds_neg=0

while con_rep<100:
    numero=random.randint(-100, 100)
    acu_sum_tds_num=acu_sum_tds_num+numero 
    if numero > 0:
        acu_sum_tds_pos=acu_sum_tds_pos+numero 
    else:
        acu_sum_tds_neg=acu_sum_tds_neg+numero 
    con_rep=con_rep+1
    
print ("suma todos:", acu_sum_tds_num)
print ("suma positivos:", acu_sum_tds_pos)
print ("suma negativos:",acu_sum_tds_neg)
    