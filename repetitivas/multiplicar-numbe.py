"""Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:
(1*2*3*4*5…)."""

numero = 1    # se inicia el contador

for i in range(1, 21):          # se crea un blucle for y se establece el rango desead
    numero *= i                  # se multiplica numero por i

# Imprimimos el resultado
print(f"El multiplicacion de los primeros 20 números naturales es: {numero}")

