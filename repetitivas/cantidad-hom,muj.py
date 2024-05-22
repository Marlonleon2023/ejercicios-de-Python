"""Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
total de n personas"""
hombres=0
mujeres=0
while True:
    #se solicita ala persona ingresada su genero 
    genero=input("ingresa tu genero (m) o (f) para terminar ingresa -->salir : ")   
    
    if genero.lower()=="salir":   # se establece una condicion para salir
        break
    # se ingresan las condiciones  y se guardan en una variable
    elif genero.lower()=="m":
        hombres+=1
    elif genero.lower()=="f":
        mujeres+=1
        # se suman todos los entudiantes 
    totalEstudent=hombres+mujeres
    
    # se imprime o se muestra  el resultado 
print("total de estudiantes ingresaron",totalEstudent)
print("ingresaron hombres",hombres)
print("ingresaro mujeres",mujeres)