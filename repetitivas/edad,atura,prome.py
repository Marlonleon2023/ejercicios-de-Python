"""Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa
se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio
,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos
que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad
sea igual a 0."""

#  obtener los datos de los alumnos  🔥
# sexo , edad  y altura  🔥
# programa debe finalizar cuando se igrese en edad  0 🔥
# mostrar la cantidad de hombres , cantidad de mujeres , y altura promedio   🔥
#la cantidad de alumnos con altura mayor o igual a 1,70 cm  🔥
#la cantidad de alumnos altura menor o igual a 150 cm 🔥

# Contadores
mujeres=0
hombres=0
alturaP=0
totalAlumnos=0
mayores170=0
igualesoMenores150=0

while True:     # se Inicia el blucle
    # Se obtienen los datos de los alumnos 
  try:     # evaluea si cometiste un error e ingresaste un careacter invalido te pide que ingreses uno valido
    sexo=input("Ingresa tu tipo de sexo Hombre (m) y Mujer (f): ")   # se ingresa tipo sexo
    if sexo !='m' and sexo !='f':   # se pone la condicion para saber si es igual la letra o diferente 
        print("ingresaste sexo o palabra invalida")   # si es diferene imprime mensaje 
        continue     # si es diferente el (sexo) continue
    edad=int(input("Ingresa tu edad o (0) para terminar : "))    # pide  ingresar la edad    
    if edad==0:      # se ingresa condicion si es 0 para salir en edad
        print("gracias por el ingreso de tus datos ")
        break
    altura=float(input("ingresa tu altura: "))
    
    # condicionales para  saber cuantos hombres y mujeres hay
    if sexo=='m':
        hombres+=1
        print("Hombre")
    elif sexo=='f':
        print("Mujer")
        mujeres+=1
    else:
        print("letra o sexo invalido")
    #condicionales para saber la altura  que se ingresa si es la altura 170 o <= igual 150 se guardan en unos contadores
    if altura>=170:
        mayores170+=1
    elif altura<=150:
        igualesoMenores150+=1
    
    # los datos ingresados de altura pasan a contador llamado alturaP 
    alturaP+=altura  
    totalAlumnos+=1        #aca se cuentan cuantos alumnos hay
    
  except ValueError:    # dectecta el error y manda un mensaje 
      print("dijita un numero entero o ingresa (0) para terminar") 
    
    
#imprime el promedio de las alturas
promedio=alturaP/totalAlumnos 
# muestra los datos obtenidos 
print("hombres",hombres)
print("mujeres",mujeres)
print("el promedio de la altura es: ", promedio)
print("alumnos con una altura de 170cm",mayores170 )
print("alumnos menores o igual a 150cm ",igualesoMenores150 )
    
    
    