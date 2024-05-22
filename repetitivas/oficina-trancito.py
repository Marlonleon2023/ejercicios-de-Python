"""La oficina de tránsito de Ibagué desea saber, de  n autos que entran a la ciudad
de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo
dígito de la placa de cada carro, se puede determinar el color de la calcomanía
utilizando la siguiente relación"""

# saber el numero de autos ingresa a ibague  🔥
# cuantos entran con calcomania de color por medio de su ultimo dijito 🔥
# dijito de la placa  definira el color de la calcomania 🔥

"Contadores "
azul=0
rojo=0
verde=0
amarillo=0
rosado=0
print("Bienvenidos ala ciudad de ibague")   # mensaje de bienvenida
while True:   # se crea un blucle true para ingresar los carros deseados  sin limitaciones de cantidad 
    
    ingresIbague=input("ingresa placa del carro ingresa (s) si deseas salir: ") # solicida ingresar numero de placa a ibague 
    # se establecen la condicion para salir y se pone un mensaje por haber ingresado a ibague
    if ingresIbague.lower()=='s':     
        print("gracias por ingresar a Ibague ")
        break
    
    try:        # desee  poner try por si encriben una letra , de la oportunidad de ingresar un numero y no se borre el progreso
        ultimoDigito=int(ingresIbague)%10   #  aca ingreso  pone con el resto a 10 para obtener el ultimo digito de la placa y se pasa el valor a ultimo digito
        print(ultimoDigito)  # se imprime el ultimo digito 
        
        #condiciones de los ultimos dijitos de las placas  y se guardan en un contador dependiento del numero
        if ultimoDigito==9 or ultimoDigito ==0:
            azul+=1
            print("a ingresa carro con calcomania azul")
        elif ultimoDigito==5 or ultimoDigito== 6:
            rojo+=1
            print("A ingresado un carro Con calcomania roja")
        elif ultimoDigito==7 or ultimoDigito== 8:
            verde+=1
            print("A ingresado un carro con calcomania verde ")
        elif ultimoDigito==1 or ultimoDigito== 2:
            amarillo+=1
            print("A ingresado un carro con calcomania amarillo ")
        elif ultimoDigito==3 or ultimoDigito== 4:
            rosado+=1
            print("A ingresado un carro con calcomania rosado ")
        else:
            print("no se encontro numero en nuestra base de datos")
            
    except ValueError:  #aca detecta el error y imprime un mensaje que debe ser un numero 
        print("error debes ingresar un numero entero o 's' para salir")
    
#se calcula el total de los carros ingresados 
totalcarrosIngresados=azul+verde+rojo+amarillo+rosado
print("total de carros ingresados a ibague",totalcarrosIngresados)
# se defines el numero de carros que ingresaron por el color de su calcomania
print("ingresaron",verde,"carros con calcomania de color verde")
print("ingresaron",rojo,"carros con calcomania de color rojo")
print("ingresaron",azul,"carros con calcomania de color azul")
print("ingresaron",amarillo,"carros con calcomania de color amarillo")
print("ingresaron",rosado,"carros con calcomania de color rosado")


