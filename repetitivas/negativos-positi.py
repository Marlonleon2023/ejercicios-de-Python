"""Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
números"""

sumaNumero=0     # contador acumula numero positivo
for x in range(1,5):    # dados un rago  
    numero = int(input("Ingrese un número negativo: "))   # ingresamos numero negativo 
    numeroPositivo = abs(numero)  # Convertir el número a positivo
    print("Número positivo :", numeroPositivo) # imprimirmos el numero positivo
    sumaNumero+=numeroPositivo   #  aca hacemos que numero positivo pase los numeros a suma numero
    total=sumaNumero    # aca suma numero lo definimos como total 
    
print("La suma de los números positivos  ingresados es:",total )  # aqui imprimimos total 