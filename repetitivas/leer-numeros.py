"""Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos
neutros."""

positivos=0
negativos=0
neutros=0
for i in range(1,5):
    numero=int(input("ingresa numero: "))
    if numero>0:
        positivos+=1
    elif numero<0:
        negativos+=1
    else:
        neutros+=1
        

print("numeros positivos son:", positivos)
print("numeros negativos son:", negativos)
print("numeros neutros son:", neutros)







    



    
    
    
    


    