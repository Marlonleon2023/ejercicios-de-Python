#if , if else ,if elif

#condicionales




#desarrollar un algoritmo de compra calcular valor a pagar ,valor de descuento ,
#si la compra  es mayor 50000 descuento 10 %
#si es menor que 50000 desuento del 5 %
#si la compra es cero no tendra descuento





compra= int(input("dijite el valor de la compra:"))

if compra < 50000:
    descuento= 0.5
elif compra > 50000:
    descuento = 0.10
elif compra == 50000:
    descuento = 0.7
elif compra == 0:
    descuento = 0

print("compra es:", compra)
print("Descuento:", descuento, descuento*compra)


