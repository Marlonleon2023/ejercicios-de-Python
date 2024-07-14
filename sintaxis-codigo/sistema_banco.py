

cuenta=[]

def agregar():
    agrega=int(input("ingresa  el valor que deseas agregar: "))
    cuenta.append(agrega)
    mostrar()
    
def mostrar():
    for list in cuenta:
        print(sum(cuenta))
        
def abonar():
    abono=int(input("cantidad a abonar: "))
    cuenta.append(abono)
    mostrar()
    
def retirar():
    retiro=int(input("ingresa la cantidad a retirar: "))
    cuenta[0]-=retiro
    mostrar()

while True:
    num=int(input("ingresa 1 agregar 2 mostrar 3 abonar 4  retirar 5 salir: "))

    match num:
        case 1:agregar()
        case 2:mostrar()
        case 3:abonar()
        case 4:retirar()
        case 5:
            print("saliendo del programa...")
            break
        case _:print("opcion no valida")

    