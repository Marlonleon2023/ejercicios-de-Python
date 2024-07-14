"""GEstion de inventarios """

carros={'ford':"azul",
        'jeep':"roja",
        'honda':"amarilla"
        
        }

def agregar():
    carAgrega=input("que carro desea agregar: ")
    colorAgrega=input("ingresa el color del carro: ")
    carros.update({carAgrega:colorAgrega})
    mostrar()
    
def mostrar():
    if carros:
        print("Carros en el inventario:")
        for carro, color in carros.items():
            print(f"Carro: {carro}, Color: {color}")
    else:
        print("El inventario de carros está vacío.")
    
def actualizar():
    carActualiza=input("que carro deseas actualizar : ")
    colorCar=input("ingresar color de el carro: ")
    carros.update({carActualiza:colorCar})
    mostrar()
    
def eliminar():
    eliminaCar=input("que carro deseas eliminar: ")
    carros.pop(eliminaCar)
    mostrar()
    
while True:
    num=int(input("1.agregar\n 2.mostrar\n 3.actualizar\n 4.eliminar\n 5.salir\n "))

    match num:
        case 1:agregar()
        case 2:mostrar()
        case 3:actualizar()
        case 4:eliminar()
        case 5:
            print("saliendo del programa")
            break
        case _:print("opcion no valida")
    
