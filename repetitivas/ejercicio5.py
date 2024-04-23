"""Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
de todo el grupo. """

# conjunto de  calificaciones 20 estudiantes 
# algoritmo calcule el pormedio y calificacion mas alta y baja de todo el grupo 

sumaCalificaciones = 0
cantidadCalificaciones = 0
calificacionMasAlta = float("-inf")   #a calificacion mas alta comience a aumentear desde el menor numero siempre sia la mas alta
calificacionMasBaja = float("inf")   #la calificacion mas baja siempre va hacer menor numero que la mayor

# Solicitar las calificaciones al usuario y calcular la suma, así como la calificación más alta y más baja
for x in range(1,20):  # Iterar sobre 20 alumnos
    calificacion = int(input("Ingresa tu calificación: ")) # se solicita ingresar las calificaciones 
    sumaCalificaciones += calificacion  # calificacion pasa a acumular en suma clalificaciones
    cantidadCalificaciones += 1        # lo que hace es cantida calificaciones vallan aumentado pase al contador
    if calificacion > calificacionMasAlta:   # aca  se ponen la condiciones de las nostas 
        calificacionMasAlta = calificacion
    if calificacion < calificacionMasBaja:
        calificacionMasBaja = calificacion

# Calcular el promedio
promedio = sumaCalificaciones / cantidadCalificaciones

# Imprimir resultados
print("Promedio:", promedio)
print("Calificación más alta:", calificacionMasAlta)
print("Calificación más baja:", calificacionMasBaja)




    
    


