"""Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto."""


multiplicacion=int(input("ingresar numero: "))  # se  solicicta ingresar el numero  para multiplicar por ese numero
for f in range(1,11):    # se establece un rango 
	resultado=multiplicacion*f #hacemos la multiplicación
	print(multiplicacion,"x",f,"=",resultado) #mostramos el resultado y organizamos  
 
 
 

