"""un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e
imprima:
• La cantidad de estudiantes que obtuvieron una calificación menor a 50.
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero
menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero
menor que 80.
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100."""

# 23 estudiantes exemane
# lea a cada estudiante 
califica50=0
califica5070=0
califica7080=0
califica80m=0
print("Para este examen se calificara de 1 a 100")  # mensaje de entrada sobre la calificacion
for i in range(0,23):
    
    ingresaCalificacion=int(input(f"ingresa tu calificacion estudiante {i+1}: "))  #se le pide al estudiante ingresar calificacion
    # condiciones sobre la nota que se ha sacado el estudiante
    if ingresaCalificacion<50:
        califica50+=1
    elif 50<= ingresaCalificacion <70:
        califica5070+=1
    elif 70<= ingresaCalificacion <80:
        califica7080+=1
    else:
        califica80m+=1
        
# se muestra el rago de  la calificacion que obtuvo
print("los estudiantes que sacaron calificacion menor a 50 son: ",califica50)
print("los estudiantes que sacaron calificacion mayor e igual a 50 y menor a 70 son: ",califica5070)
print("los estudiantes que sacaron calificacion mayor e igual a 70 y menor a 80 son: ",califica7080)
print("los estudiantes que sacaron calificacion mayor e igual a 80 son: ",califica80m)
            
