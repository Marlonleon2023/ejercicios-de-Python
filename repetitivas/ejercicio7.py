"""Una persona debe realizar un muestreo con 50 personas para determinar el
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
Las categorías se determinar de acuerdo a la siguiente tabla:

joven=13-29
adulto=30-59
niños=0-12
ancianos=60
"""
#muestreo 50 personas 
# determinar el promedio
# determinar las categorias 

"Contadores "
pesoNinos = 0
pesoJovenes = 0
pesoAdultos = 0
pesoAncianos = 0

cantidadNinos = 0
cantidadJovenes = 0
cantidadAdultos = 0
cantidadAncianos = 0

for i in range(50):    # Se establece el rango solicitado por el enunciado 
    edad = int(input("Ingrese la edad: "))    # pedimos ingresar edad 
    peso = int(input("Ingrese el peso: "))    # solicita ingresar peso 

    #condiciones 
    # se verifica si estan dentro del rango de edad 
    if 0 <= edad <= 12:
        pesoNinos += peso
        cantidadNinos += 1
    elif 13 <= edad <= 29:
        pesoJovenes += peso
        cantidadJovenes += 1
    elif 30 <= edad <= 59:
        pesoAdultos += peso
        cantidadAdultos += 1
    else:
        pesoAncianos += peso
        cantidadAncianos += 1


#  aca se aclara si cantidad de niños es 0 el promedio  va hacer 0
promedioNinos = pesoNinos / cantidadNinos if cantidadNinos > 0 else 0    
promedioJovenes = pesoJovenes / cantidadJovenes if cantidadJovenes > 0 else 0
promedioAdultos = pesoAdultos / cantidadAdultos if cantidadAdultos > 0 else 0
promedioAncianos = pesoAncianos / cantidadAncianos if cantidadAncianos > 0 else 0

# se imprime o se muestra el total de personas ingresadas el pomedio 
print("Promedio de peso de niños:", promedioNinos)
print("Promedio de peso de jóvenes:", promedioJovenes)
print("Promedio de peso de adultos:", promedioAdultos)
print("Promedio de peso de ancianos:", promedioAncianos)

