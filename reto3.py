# Cálculo del factorial utilizando un ciclo for

# Función para calcular el factorial
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Pedir al usuario que ingrese un número válido
while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            raise ValueError
        break
    except ValueError:
        print("¡Error! Ingrese un número entero positivo válido.")

# Calcular el factorial
factorial = calcular_factorial(numero)

# Imprimir el resultado
print("El factorial de", numero, "es:", factorial)
