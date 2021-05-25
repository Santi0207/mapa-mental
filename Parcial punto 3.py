# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:23:26 2021

@author: santi
"""

#Nick alejandro villa_82202118163
#Santiago lopez_82202117875
#Mariana grand_101202114369

def uno(num_empleados,tarifa_hora):#encabezado de llamado 
    total_horas=0 #variable de total de horas
    horas_ext=0 #variable de horas extras 
    femenino=0 #varible de empleados femenino 
    hombres=0 #variable de empleados masculinos 
    seccion1=0#variable de seccion 1
    seccion2=0#variable de seccion 2
    seccion3=0#variable de seccion 3
    salario=0#variable de salario
    pago_extra=0#variable de pago extra 
    pago=0#variable de pago 
    salario_extra=0#salario extra 
    
    for x in range (num_empleados):#ciclo repetitivo con for 
        nombre_trabajador = input("Ingrese el nombre del trabajor:")#variable de nombre de trabajo 
        horas_totales = int(input("Ingrese las horas trabajadas:"))#viable de horas totales 
        salario = horas_totales*tarifa_hora#para hallar el salario con la multiplicacion de horas totales*tarifas de horas
        
        if horas_totales>35:# es la condicional para mirar si es mayor a 35 horas 
            horas = horas_totales-35#aca se mira si son maroyes a 35 entones se mir cuantas horas son extras 
            tarifa_hora_extra = tarifa_hora*2.5#esto es la tarifa de la horas extra a lo que se le saca en 2.5
            pago_total = horas*tarifa_hora_extra# con esto muestra lo que es el pago total 
            salario_extra = salario + pago_total#salrio extra es lo que seda co salirio y pago totaal 
            horas_ext = horas_ext + horas#horas extras si se suma horas extas con horas 
            pago_extra = pago_total + pago_extra#pago extra es cn el pago extra mas pago total 
            print ("Su salario neto es:", salario)#el primer print que es salario 
            print ("Las horas extras:", horas)#segundo print que es horas 
            print ("El salario total con horas extras es:", salario_extra)#tercer print que es horas extras 
            
            if (salario_extra < 2000000):#la condicional si es mayor a 2 mmillones el sueldo 
                salud = salario_extra*0.125#esta e la salud que se descent con el 0.125
                icbf = salario_extra*0.04#el icbf que se descuenta con el 0.04
                descuento = salario_extra-(icbf+salud)#decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuentos es de: ", descuento)#el print del descuento 
                
            if (salario_extra >= 2000000) and (salario_extra <= 3000000):#son condiciones que si es mayor o igual a 2 millones y a 3 millones hacer lo siguiente 
                salud = salario_extra*0.125#esta e la salud que se descent con el 0.125
                icbf = salario_extra*0.04#el icbf que se descuenta con el 0.04
                retencion1 = salario_extra*0.05 #es una retencion del 0.05 si se lleega a ganar 2 millones 
                descuento = salario_extra - (icbf+salud+retencion1)#decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento)#el print del descuento 
            
            if (salario_extra >= 3000001) and (salario_extra <= 4000000):#son condiciones que si es mayor o igual a 3 millones uno  y a 4 millones hacer lo siguiente
                salud = salario_extra*0.125#esta e la salud que se descent con el 0.125
                icbf = salario_extra*0.04#el icbf que se descuenta con el 0.04
                retencion2 = salario_extra*0.07  #es una retencion del 0.07 si se lleega a ganar 3 millones o 4 millones 
                descuento = salario_extra - (icbf+salud+retencion2)#decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento)#el print del descuento 
            
            if (salario_extra >=4000001) and (salario_extra <= 5000000):#son condiciones que si es mayor o igual a 4 millones uno  y a 5 millones hacer lo siguiente
                salud = salario_extra*0.125#esta e la salud que se descent con el 0.125
                icbf = salario_extra*0.04#el icbf que se descuenta con el 0.04
                retencion3 = salario_extra*0.09  #es una retencion del 0.09 si se lleega a ganar 3 millones o 4 millones 
                descuento = salario_extra - (icbf+salud+retencion3)#decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento) #el print del descuento 
            
            if (salario_extra >=5000001):#es condicional se llega a 5 millones para arriba 
                salud = salario_extra*0.125#esta e la salud que se descent con el 0.125
                icbf = salario_extra*0.04#el icbf que se descuenta con el 0.04
                retencion4 = salario_extra*0.11 #es una retencion del 0.11 si se lleega a ganar 3 millones o 4 millones 
                descuento = salario_extra - (icbf+salud+retencion4)#decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento)#el print del descuento 
                
        else:
            pago = salario + pago#pago si es salario mas pago
            print ("El salario del trabajador:", pago)#print de pago
            print ("Trabajo las horas normales:", horas_totales)#print de hoas totales 
            print ("No trabajo horas extras")#es un comentario en la consola 
            
            if (pago < 2000000): #la condicional si es mayor a 2 mmillones el sueldo 
                salud = pago*0.125 #esta e la salud que se descent con el 0.125
                icbf = pago*0.04 #el icbf que se descuenta con el 0.04
                descuento = pago - (icbf+salud) #decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento) #el print del descuento 
            
            if (pago >= 2000000) and (pago <=3000000):
                salud = pago*0.125 #esta e la salud que se descent con el 0.125
                icbf = pago*0.04 #el icbf que se descuenta con el 0.04
                retencion1 = pago*0.05 #es una retencion del 0.05 si se lleega a ganar 2 millones o 3 millones
                descuento = pago - (icbf+salud+retencion1) #decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento) #el print del descuento 
            
            if (pago >= 3000001) and (pago <=4000000):
                salud = pago*0.125 #esta e la salud que se descent con el 0.125
                icbf = pago*0.04 #el icbf que se descuenta con el 0.04
                retencion2 = pago*0.07 #es una retencion del 0.07 si se lleega a ganar 3 millones o 4 millones
                descuento = pago - (icbf+salud+retencion2) #decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento) #el print del descuento 
            
            if (pago >= 4000001) and (pago <= 5000000):
                salud = pago*0.125 #esta e la salud que se descent con el 0.125
                icbf = pago*0.04 #el icbf que se descuenta con el 0.04
                retencion3 = pago*0.09 #es una retencion del 0.09 si se lleega a ganar 4 millones o 5 millones 
                descuento = pago - (icbf+salud+retencion3) #decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento) #el print del descuento 
            
            if (pago >= 5000001):
                salud = pago*0.125 #esta e la salud que se descent con el 0.125
                icbf = pago*0.04 #el icbf que se descuenta con el 0.04
                retencion4 = pago*0.11 #es una retencion del 0.11 si se lleega a ganar 5 millones 
                descuento = pago - (icbf+salud+retencion4) #decuento que se da con salario extra y el icbf mas salud 
                print("El salario total con los descuento es de:", descuento) #el print del descuento 
                
        total_horas = total_horas +  horas_totales
        genero=input("Ingrese el genero del trabajor: ")#Ingresa el usuario si es de genero masculino o femenino
        if genero=="femenino": #estructura condicional
            femenino=femenino+1 # es el contador para saber cuantas mujeres han ingresado            
        else:
              if genero=="masculino": #estructura condicional
                  hombres=hombres+1 # es el contador para saber cuantos hombres han ingresado   
                  
        seccion=int(input("Ingrese la sección donde trabaja 1,2 o 3: "))
        if seccion==1: #estructura condicional
            seccion1=seccion1+1 #contador para saber a cuantas personas son de la seccion 1
        else: #estructura condicional
            if seccion==2: #estructura condicional
                seccion2=seccion2+1 #contador para saber a cuantas personas son de la seccion 2
            else:#estructura condicional
                if seccion==3:#estructura condicional
                    seccion3=seccion3+1 #contador para saber a cuantas personas son de la seccion 3
                    
    print("El total de horas extras trabajadas son: ", horas_ext)  #imprime las horas extras que se trabajo
    print("El total del pago de las horas extra de los empleados: ",pago_extra) #imprime el pago por las horas extras
    print("El total de horas trabajadas por todos los empleados es: ", total_horas) # imprime el total de horas trabajadas
    print("El total del pago de las horas normales de los empleados: ",pago) # imprime el total del pago de las horas
    print("La cantidad de mujeres que hay son: ", femenino) # imprime cuantas mujeres ingresaron
    print("La cantidad de hombres que hay son: ", hombres) #imprime cuantos hombres ingresaron
    print("La cantidad de empleados que trabajan en la sección 1 son:", seccion1)# imprime cuantas personas son de la seccion 1
    print("La cantidad de empleados que trabajan en la sección 2 son:", seccion2) # imprime cuantas personas son de la seccion 2
    print("La cantidad de empleados que trabajan en la sección 3 son:", seccion3)# imprime cuantas personas son de la seccion 3

        

num_empleados=int(input("Ingrese la cantidad de empleados: "))
tarifa_hora=float(input("Cual es valor por hora trabajada: "))
uno(num_empleados, tarifa_hora)
           
                
                
                
                