Métodos Diccionario Clave valor

Acceso directo con claves:
valor = diccionario[clave]
Método .get():
valor = diccionario.get(clave, valor_predeterminado)
Método .keys():
claves = diccionario.keys()
Método .values():
valores = diccionario.values()
Método .items():
items = diccionario.items()
Iteración con for:

Iterar sobre claves:
for clave in diccionario: print(clave, diccionario[clave])

Iterar sobre claves y valores:
for clave, valor in diccionario.items(): print(clave, valor)

Verificación de existencia de clave:
if clave in diccionario: # La clave existe






Eliminar valores de un diccionario

# Creación de un diccionario de ejemplo
mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}

# Uso de (del)
Elimina una clave y su valor asociado.
del mi_diccionario['edad']

# Uso de .pop()
Elimina una clave y devuelve su valor asociado. Si la clave no existe, puede devolver un valor predeterminado
ciudad = mi_diccionario.pop('ciudad', 'No disponible')

# Uso de .popitem()
Elimina y devuelve el último par clave-valor insertado en el diccionario.
ultima_clave_valor = mi_diccionario.popitem()

# Uso de .clear()
Elimina todos los elementos del diccionario, dejándolo vacío.
mi_diccionario.clear()
