compras = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
print (compras[1:4])
compras[1:3] = ["Atún", "Pasta","azucar"]
print (compras[1:3])



compras = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
print(compras.index("Sal"))


"""zip iterear listas unir"""



compras = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
cadena_resultante = ' '.join(compras)
print(cadena_resultante)
