"""un grupo de 10 estudiantes presentan un examen de algoritmia. 
Hacer un algoritmo que lea por cada estudiante la calificación obtenida. 
Al finalizar calcule e imprima:
• La cantidad de estudiantes que obtuvieron una calificación menor a 50. 
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80. 
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100."""

# 10 estudiantes
# calificacion obtenida

contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

#ingresar  calificaciones

calificacion1 = float(input("Ingrese la calificación del estudiante 1: "))
calificacion2 = float(input("Ingrese la calificación del estudiante 2: "))
calificacion3 = float(input("Ingrese la calificación del estudiante 3 : "))
calificacion4 = float(input("Ingrese la calificación del estudiante 4: "))
calificacion5 = float(input("Ingrese la calificación del estudiante 5 : "))
calificacion6 = float(input("Ingrese la calificación del estudiante 6 : "))
calificacion7 = float(input("Ingrese la calificación del estudiante 7: "))
calificacion8 = float(input("Ingrese la calificación del estudiante 8: "))
calificacion9 = float(input("Ingrese la calificación del estudiante 9 : "))
calificacion10 = float(input("Ingrese la calificación del estudiante 10: "))


if calificacion1 < 50:
    contador1 += 1
elif calificacion2 < 50:
    contador1 += 1
elif calificacion3 < 50:
    contador1 += 1
elif calificacion4 < 50:
    contador1 += 1
elif calificacion5 < 50:
    contador1 += 1
elif calificacion6 < 50:
    contador1 += 1
elif calificacion7 < 50:
    contador1 += 1
elif calificacion8 < 50:
    contador1 += 1
elif calificacion9 < 50:
    contador1 += 1
elif calificacion10 < 50:
    contador1 += 1
elif calificacion1 < 70 and calificacion1 >= 50:
    contador2 += 1
elif calificacion2 < 70 and calificacion2 >= 50:
    contador2 += 1
elif calificacion3 < 70 and calificacion3 >= 50:
    contador2 += 1
elif calificacion4 < 70 and calificacion4 >= 50:
    contador2 += 1
elif calificacion5 < 70 and calificacion5 >= 50:
    contador2 += 1
elif calificacion6 < 70 and calificacion6 >= 50:
    contador2 += 1
elif calificacion7 < 70 and calificacion7 >= 50:
    contador2 += 1
elif calificacion8 < 70 and calificacion8 >= 50:
    contador2 += 1
elif calificacion9 < 70 and calificacion9 >= 50:
    contador2 += 1
elif calificacion10 < 70 and calificacion10 >= 50:
    contador2 += 1
elif calificacion1 < 80 and calificacion1 >= 70:
    contador3 += 1
elif calificacion2 < 80 and calificacion2 >= 70:
    contador3 += 1
elif calificacion3 < 80 and calificacion3 >= 70:
    contador3 += 1
elif calificacion4 < 80 and calificacion4 >= 70:
    contador3 += 1
elif calificacion5 < 80 and calificacion5 >= 70:
    contador3 += 1
elif calificacion6 < 80 and calificacion6 >= 70:
    contador3 += 1
elif calificacion7 < 80 and calificacion7 >= 70:
    contador3 += 1
elif calificacion8 < 80 and calificacion8 >= 70:
    contador3 += 1
elif calificacion9 < 80 and calificacion9 >= 70:
    contador3 += 1
elif calificacion10 < 80 and calificacion10 >= 70:
    contador3 += 1
elif calificacion1 >= 80:
    contador4 += 1
elif calificacion2 >= 80:
    contador4 += 1
elif calificacion3 >= 80:
    contador4 += 1
elif calificacion4 >= 80:
    contador4 += 1
elif calificacion5 >= 80:
    contador4 += 1
elif calificacion6 >= 80:
    contador4 += 1
elif calificacion7 >= 80:
    contador4 += 1
elif calificacion8 >= 80:
    contador4 += 1
elif calificacion9 >= 80:
    contador4 += 1
elif calificacion10 >= 80:
    contador4 += 1


print("Cantidad de estudiantes con calificaciones:")
print("Menores a 50: ", contador1)
print("Entre 50 y 69: ", contador2)
print("Entre 70 y 79: ", contador3)
print("80 o más: ", contador4)
