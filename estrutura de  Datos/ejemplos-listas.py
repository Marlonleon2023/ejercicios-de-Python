
"""ejemplos  guiados por la instructora"""

compras = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]   # se crea la lista 
print (compras[1:4])       # se imprime  la lista  y se establecen los indices que quire mostrar
compras[1:3] = ["Atún", "Pasta","azucar"]   # le decimos a la lista compras que del indice uno y el indice 3 agrege atun pasta aceite
print (compras[1:3])              # se imprime a compras para comprobar el resuldado que se arroja


compras = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]   #
print(compras.index("Sal"))  # se busca un elemento dentro de una lista 


"""zip iterear listas unir"""



compras = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
cadena_resultante = ' '.join(compras)  # convierte la lista a cadena de texto
print(cadena_resultante)  # se imprime 

