"""Desarrollar una aplicación de agenda: Crea una aplicación que permita al usuario agregar, 
editar y eliminar eventos en una agenda.
Puedes usar una base de datos para almacenar los datos de los eventos."""

from enum import Enum
print("Bievenido(@) a tu agenda , mira tus prioridades")

agenda=["correr","caminar","saltar","trabajar","limpiar","comer"]

print(agenda)  
class agendas(Enum):
        AGREGAR=1
        EDITAR=2
        ELIMINAR=3
        SALIR=4
while True:
    def mostrarMenu():
        print("1. Agregar elemento")
        print("2. Editar elemento")
        print("3. Eliminar elemento")
        print("4. Deseo Salir")
        opcion=input("Seleciona una opcion: ")
        if not opcion.isdigit():
            print("ingresa un valor valido un numero entero")
        return opcion

    opcion=mostrarMenu()

    #agregar en agenda
    if opcion==str(agendas.AGREGAR.value):
        agregar=input("que tarea quieres agregar : ")
        agenda.append(agregar)
        print(agenda)
    elif opcion==str(agendas.EDITAR.value):
        editar=input("que tarea quieres editar?: ")
        nuevoValor=input("Ingresa el nuevo valor: ")
        
        if editar in agenda:
            indice=agenda.index(editar)
            agenda[indice]=nuevoValor
            print(agenda)
        else:
            print(f"No se ha encontrado {editar} no se puede editar")
            
    elif opcion==str(agendas.ELIMINAR.value):
        eliminar=input("Que tarea deseas eliminar: ")
        if eliminar in agenda:
            agenda.remove(eliminar)
            print(agenda)
        
    elif opcion==str(agendas.SALIR.value):
        print("gracias por ingresar")
        break
print(agenda)