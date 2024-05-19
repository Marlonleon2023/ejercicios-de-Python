listas=["zapatos","ropa","abrigo","bolso","cortina","cortina","cortina"]
# se accede a un elemto de la lista
print(listas[1])
# se cambia un elmento de la lista por su indice
listas[2]="chaqueta"
# Se agrega un elemento a final de la lista
listas.append("chanclas")
# se agrega un elemento en una cession especifica de la lista
listas.insert(2,"comida")

#eliminar un valor de la lista
listas.remove("ropa")

#elimina un elemento por su indice

listas.pop(4)

# verificar la exitencia de un elemento 
print("comida" in listas)

# método index() de la lista para obtener el índice de la primera ocurrencia de un valor
print(listas.index("comida"))

#método count() de la lista para contar cuántas veces aparece un valor específico.

print(listas.count("cortina"))

#método sort() de la lista para ordenar los elementos en orden ascendente

print(listas.sort())


#método reverse() de la lista para invertir el orden de los elementos

print(listas.reverse())

#método extend() de la lista para agregar todos los elementos de otra lista al final de la lista actual.
nuevaLista=[]
nuevaLista.extend(listas)

print(nuevaLista)

# iterar sobre una lista 
print("Iteracion--------")
for productos in listas:
    print(productos)
    

#método clear() de la lista para eliminar todos los elementos de la lista.

nuevaLista.clear()

print("zapatos" in nuevaLista)