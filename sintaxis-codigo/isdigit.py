"""cadena1 = "12345"--->True cadena2 = "abc123"--->false"""

# se solicida un dato o valor para la comprovacion de metodo isdigit 
cadena1=input("ingrea un dato o valor : ")
# para verificar si los carateres son correctos (numericos)
if cadena1.isdigit():
    print("el valor ingresado son digitos")
else: 
    print("los valores ingresados no son digitos")
    
"""Enunciado ------v2-----"""
listCarateres=[]
while True:
    
    cadena2=input("ingresa un dato numerico (salir) para terminar: ").lower()
    if cadena2=="salir":
        break
    if cadena2.isdigit():
        print("el caracter ingresado es valido")
        listCarateres.append(cadena2)
    else:
        print("el valor ingresdo solo puede tener caracteres numericos")
        continue
    print(f"Valores numéricos ingresados hasta ahora: {', '.join(listCarateres)}")

print("Valores numéricos finales ingresados:", ', '.join(listCarateres))