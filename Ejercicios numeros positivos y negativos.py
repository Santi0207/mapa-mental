import random

cant_numeros=0
cont_repeticionesWhile=0
numero=0
acu_suma=0
prom_numeros_ale=0.0

acumuladorPositivos=0
acumuladorNegativos=0
contadorPositivos=0
contadorNegativos=0
promedioPositivos=0.0
promedioNegativos=0.0

mayorPositivo=0
mayorNegativo=0
menorPositivo=1000
menorNegativo=0



cantidadNumeros=int(input("Cantidad de Numeros: "))

while cont_repeticionesWhile<cantidadNumeros:
    numero=random.randint(-1000,1000)
    acu_suma=acu_suma+numero
    
    
    if numero>0:  
        print("Numero Positivo: ",numero)
        acumuladorPositivos=acumuladorPositivos+numero
        contadorPositivos=contadorPositivos+1
        
        if numero>mayorPositivo:
            mayorPositivo=numero
            
        if numero<menorPositivo:
            menorPositivo=numero
            
    else:
        print("Numero Negativo: ",numero)
        acumuladorNegativos=acumuladorNegativos+numero
        contadorNegativos=contadorNegativos+1
        
    cont_repeticionesWhile=cont_repeticionesWhile+1

prom_numeros_ale=acu_suma/cont_repeticionesWhile
promedioPositivos=acumuladorPositivos/contadorPositivos  
promedioNegativos=acumuladorNegativos/contadorNegativos

print("Suma de Numeros Aleatorios: ", acu_suma)   
print("Promedio de Numeros Aleatorios: ", prom_numeros_ale)   
 

print("Cantidad Numeros Positivos: ",contadorPositivos)
print("Suma de Numeros Positivos: ", acumuladorPositivos)   
print("Promedio de Numeros Positivos: ", promedioPositivos)   
    
print("Cantidad Numeros Negativos: ",contadorNegativos)
print("Suma de Numeros Negativos: ", acumuladorNegativos)   
print("Promedio de Numeros Negativos: ", promedioNegativos)   
    
print("Mayor de los positivos: ", mayorPositivo)   
print("Menor de los Positivos: ", menorPositivo)   
