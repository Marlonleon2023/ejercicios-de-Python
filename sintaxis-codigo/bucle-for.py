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