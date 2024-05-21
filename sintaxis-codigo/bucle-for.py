#Imprime los numeros del 1 al 10
for i in range(1,10):
    print(i)
    
"""#Calcular la suma de los  100 numeros naturales
numerosNaturales=0
for l in range(1,101):
    print(l)
    numerosNaturales+=i
print(numerosNaturales)"""

#Generar una tabla de multiplicar para un número específico.
numero=int(input("ingresa numero deseado: "))
for x in range(1,11):
    resultado=numero*x
    print(numero,"X",x,"=",resultado)
    
    
"""Imprimir los elementos de una lista."""

numerosNaturales=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

for number in numerosNaturales:
    print("los numeros naturales son : ",number)
    
"""Calcular el factorial de un número."""
def factorial(n):
    if n < 0:
        return "Factorial no definido para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))  
print(factorial(0))  #   porque es 0
print(factorial(-3))

"""Contar la cantidad de vocales en una cadena de texto."""
#(contar) necesitas un -----> contador
vocales="marlon"
contarVocales=0
for letras in vocales:
    if letras  in "aeiou":
        contarVocales+=1
print(contarVocales)
    
"""Imprimir los elementos de una matriz bidimensional."""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos de la matriz
print(matriz[0][0])  # Imprime 1
print(matriz[1][2])  # Imprime 6
print(matriz[2][1])  # Imprime 8

# Recorrer todos los elementos de la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
    
"""Buscar un elemento específico en una lista."""

producto=["cafe","chocolate","arina","pasta","pan","huevos"]
product=input("¿Que productos buscas?: ")
for elemento in producto:
    if elemento == product.lower():
        print("Claro tenemos: ",elemento)
        break
else:
    print("producto se ha agotado o no lo tenemos")
    

"""Sumar los elementos de una lista."""
sumaNum=0
for elemeNumerico in numerosNaturales:
    sumaNum+=elemeNumerico
print(sumaNum)
