"""Cree una lista vacía  denominada aprendices y edades, llénelas solicitando los datos por teclado."""


aprendices=[]
edades=[]
while True:
    aprendiz=input("ingresa tu nombre para terminar ingresa (salir): ")
    if aprendiz.lower()=="salir":
        break
    edad=int(input("ingresa tu edad: "))
    aprendices.append(aprendiz)
    edades.append(edad)
print("aprendices ingresados : ",aprendices)
print("edades de los aprendices ingresados: ",edades)
"""
Muestre el aprendiz con la mayor edad"""
aprendizMayor=""
edadMayor=0
for aprendiz,edad in zip(aprendices,edades):
    if edad>edadMayor:
        aprendizMayor=aprendiz
        edadMayor=edad
    
        
if aprendizMayor:
    print(f"El aprendiz con la mayor edad es {aprendizMayor}, con {edadMayor} años.")
else:
    print("No se han ingresado aprendices.")
    
"""Inserte el nombre de la instructora en la posición 1"""
aprendices.insert(1,"Sandra Milena")
print(aprendices)

"""Cuente cuantos aprendices tienen 18 años"""
mayores=0
for edad in edades:
    if edad==18:
        mayores+=1
print(f"el numero de aprendices que tienen 18 años {mayores}")

"""Agregue un aprendiz x al final de la lista"""

aprendices.append("julian")
print(aprendices)

"""Borre el nombre de la instructora de la lista"""
if "Sandra Milena" in aprendices:
    aprendices.remove("Sandra Milena")
    print("el nombre de la instructora se ha eliminado")
else:
    print("el nombre de la instructora no esta en la lista")
print(aprendices)



