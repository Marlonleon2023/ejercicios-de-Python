"""En un supermercado, se ha implementado la     ..
estrategia de descuento, según el valor de la compra y la balota que el cliente 
saque de una bolsa secreta. Las condiciones se listan a continuación:
- si el valor de la compra es superior igual a 50.000 pesos y saca:
a. balota roja el descuento será del 10%
b. balota verde el descuento será del 15%
c. balota azul el descuento será del 20%
d. balota amarilla el descuento será del 50%
e. balota negra el descuento será del 100%
-Si la compra es inferior a 50.000 pesos no participará 
del sorteo, para este caso se muestra un mensaje y se  imprimirá solo el valor a pagar.
elabore un algoritmo que permita leer la compra, evaluar 
las condiciones e imprimir el valor de la compra, e color de la balota 
el  valor del descuento y el valor a pagar."""


# compra desea segir en la aplicacion

import random

while True:
    compra = int(input("Ingresa el valor de la compra (o ingresa 0 para salir): "))
    
    if compra == 0:
        print("¡Hasta luego!")
        break

    balota = random.choice(["roja", "verde", "azul", "amarillo", "negra"])

    if compra >= 50000 and balota == "roja":
        descuento = 0.10
        total = compra - (descuento * compra)
    elif compra >= 50000 and balota == "verde":
        descuento = 0.15
        total = compra - (descuento * compra)
    elif compra >= 50000 and balota == "azul":
        descuento = 0.20
        total = compra - (descuento * compra)
    elif compra >= 50000 and balota == "amarillo":
        descuento = 0.50
        total = compra - (descuento * compra)
    elif compra >= 50000 and balota == "negra":
        descuento = 100
        total = compra - descuento
    elif compra < 50000:
        print("No participas")
        continue

    print("Compra:", compra, "Descuento:", descuento,
        "Valor total es:", total, "Balota:", balota)




