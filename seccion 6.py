#Muestra en la consola el mensaje 
print("ingrese 3 numeros enteros diferenetes") 

#Determina la opcion que debe escoger el usuario
opcion= int(input("Elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor:"))

#Determina el ingreseo de datos
n_1 = int(input("ingrese el numero a:"))

#Determina el ingreseo de datos
n_2 = int(input("ingrese el numero b:"))

#Determina el ingreseo de datos
n_3 = int(input("ingrese el numero c:"))


if (opcion == 1): 
#Es la primera condicion 

    if (n_1 > n_2):
#Aqui es el primer numero mayor y el segundo menor 
    
        if (n_1 > n_3):
#Aqui es el primer numero mayor y el tercero menor
        
            if(n_2 > n_3):
#Aqui es el segundo mayor y el tercero menor
            
               print(n_1, n_2, n_3)
#En este print se muestra el orden de mayor a menor n_1>n_2>n_3

            else:
               print(n_1, n_3, n_2)
#Este print es cuando no se cumple la condicion

    if (n_3 > n_1):
#Aqui es el tercer numero mayor y el primero menor

        if (n_3 > n_2):
#Aqui es el tercer numero mayor y el segundo menor

            if(n_2 > n_1):
#Aqui es el segundo numero mayor y el primero menor

               print(n_3, n_2, n_1)
#En este print se muestra el orden de mayor a menor n_3>n_1>n_2
            else:
               print(n_3, n_1, n_2)
#En este print no se cumple la condicion

    if (n_2 > n_1):
#Aqui es el segundo numero mayor y el primero menor

        if (n_2 > n_3):
#Aqui es el segundo numero mayor y el tercero menor

            if(n_1 > n_3):
#Aqui es el primer numero mayor y el tercero menor

               print(n_2, n_1, n_3)
#En este print se muestra el orden de mayor a menor n_2>n_1>n_3

            else:
               print(n_2, n_3, n_1)
#En este print no se cumple la condicion


if (opcion == 2):
#Es la primera condicion 

    if (n_1 < n_2):
#Aqui es el primer numero menor y el segundo mayor

        if (n_1 < n_3):
#Aqui es el primer numero menor y el tercero mayor

            if(n_2 < n_3):
#Aqui es el segundo numero menor y el tercero mayor

               print(n_1, n_2, n_3)
#En este print se muestra el orden de mayor a menor n_1>n_2>n_3

            else:
               print(n_1, n_3, n_2)
#En este print no se cumple la condicion

    if (n_3 < n_1):
#Aqui es el tercer numero menor y el primer mayor

        if (n_3 < n_2):
#Aqui es el tercer numero menor y el segundo mayor

            if(n_2 < n_1):
#Aqui es el segundo numero menor y el primero mayor

               print(n_3, n_2, n_1)
#En este print se muestra el orden de mayor a menor n_3>n_2>n_1

            else:
               print(n_3, n_1, n_2)
#En este print no se cumple la condicion

    if (n_2 < n_1):
#Aqui es el sguendo numero menor y el primer mayor

        if (n_2 < n_3):
#Aqui es el segundo numero menor y el tercer mayor

            if(n_1 < n_3):
#Aqui es el primer numero menor y el tercero mayor

               print(n_2, n_1, n_3)
#En este print se muestra el orden de mayor a menor n_2>n_1>n_3
            else:
               print(n_2, n_3, n_1)
#En este print no se cumple la condicion

if (n_1 == n_2):
#En esta nueva condicion es por si n_1 es igual a n_2 o viceversa

    print("n_2 y n_1 son iguales")
#En este print dependiendo la condicion imprime el enunciado.

    if (n_1 == n_3):
#En esta nueva condicion es por si n_1 es igual a n_3 o viceversa

        print("n_1 y n_3 son iguales")
#En este print dependiendo la condicion imprime el enunciado.

        if(n_2 == n_3):
#En esta nueva condicion es por si n_1 es igual a n_3 o viceversa

           print("n_2 y n_3 con iguales")
#En este print dependiendo la condicion imprime el enunciado.

           if(n_1 == n_2 == n_3):
#En esta nueva condicion es por si todos los numeros son iguales.

              print("todos son iguales")
#En este print dependiendo la condicion imprime el enunciado.