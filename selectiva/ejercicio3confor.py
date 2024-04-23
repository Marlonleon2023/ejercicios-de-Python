
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

#Para cada estudiante de 1 a 10:
for i in range(10):
    # Leer la calificación del estudiante
    calificacion = float(input(f"Ingrese la calificación del estudiante {i+1}: "))
    if calificacion < 50:
        contador1 += 1
    elif calificacion < 70:
        contador2 += 1
    elif calificacion < 80:
        contador3 += 1
    else:
        contador4 += 1


print("Cantidad de estudiantes con calificaciones:")
print("Menores a 50: ", contador1)
print("Entre 50 y 69: ", contador2)
print("Entre 70 y 79: ", contador3)
print("80 o más: ", contador4)
