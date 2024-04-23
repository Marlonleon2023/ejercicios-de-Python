"""Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos"""

# contadores necesarios para el programa
sumaEdades=0
cantidadAlumnos=0
ingresoHombre=0
ingresoMujeres=0
sumaHombres=0
sumaMujeres=0
while True:  # bucle infinito permite el ingreso de las personas 
  try:  # evalua si al ingresar un caracter incorrecto vuelva intentarlo 
    ingresaGenero=input("Ingresa (m) para hombre y (f) para mujer para terminar(salir): ") # se solicita ingresar genero
    if ingresaGenero.lower()=='salir':   # condicion para salir del programa si se desea 
        break          # detiene el programa si la condicion se cumple 
    elif ingresaGenero != 'm' and ingresaGenero != 'f':   # se crea una condicion si genero es diferente 
        print("genero o letra invalido")     # arroja un mesaje de ser verdadera la condicion
        continue            # de ser asi vuel a  comenzar el programa para ingresar genero correcto 
    edadesPersonas=int(input("ingresa tu edad : "))    # se solicita ingresar edad 
    if edadesPersonas==0:                # se vuelve a poner una condicion si se desea salir
        break
    #se crea una condicion donde  se evalua el tipo de genero y se agrega al contador  
    if ingresaGenero=="m":
        sumaHombres+=edadesPersonas
        ingresoHombre+=1
        print("ingreso hombre")
    elif ingresaGenero=="f":
        sumaMujeres+=edadesPersonas
        ingresoMujeres+=1
        print("ingreso una mujer")
        
    sumaEdades+=edadesPersonas  # edadespersonas se pasa sumaedades 
    cantidadAlumnos+=1          # cada ves que ingrese una persona se suma a cantidad de personas 
  except ValueError:       #  se  arroja un mensaje   que hay un error 
      print("debes ingresar numero entero o (0)para salir")  
    
      
  # se crean unas condiciones para calcular el promedio de mujer , hommbre, personas 
   
if ingresoHombre>0:
    promedioHombre=sumaHombres/ingresoHombre 
    print("el promedio de los hombres es : ",promedioHombre) 
else:
    print("no se ingreso nada")
if ingresoMujeres>0:
    promedioMujeres=sumaMujeres/ingresoMujeres
    print("el promedio de la mujeres es : ",promedioMujeres)
else:
    print("no se ingreso nada")
        
if cantidadAlumnos>0:
    promedio=sumaEdades/cantidadAlumnos
    print("el total del promedio es: " , promedio)
else:
    print("no se ingreso nada")





    
    
    
