diccionary={"moto":50000,
            "avion":500000,
            "carro":36400}
print(diccionary["carro"])

#Cambiar el valor de un dicionario
diccionary["moto"]=40000

diccionary["cicla"]=20000
#eliminar el clave de un diccionario y devulve su valor
diccionary.pop("moto")

#con (del) se elimina su clave y su valor

del diccionary["carro"]
print(diccionary)

#si exite en el dicionario moto o cualquier clave
print("moto" in diccionary)


# método keys() del diccionario para obtener una vista de todas las claves
print(diccionary.keys())

#método values() del diccionario para obtener una vista de todos los valores.

print(diccionary.values())

#método items() del diccionario para obtener una vista de todos los pares clave-valor.

print(diccionary.items())

#método get(clave, valor_por_defecto) del diccionario 
# para obtener el valor asociado a una clave, o un valor por defecto si la clave no existe.
print("metodo get")
print(diccionary.get("carro","valor no encontrado"))

#el método update(otro_diccionario) 
# del diccionario para actualizar el diccionario con pares clave-valor de otro diccionario.

diciotar={"televisor":6000,
        "celular":40000,
        "computadora":50000}

diccionary.update(diciotar)

print(diccionary)


# se  itera solo el valor con .values
for dicionario in diccionary.values():
    print(dicionario)

# se itera la clave y el varlo en . items

for dicionario in diccionary.items():
    print(dicionario)