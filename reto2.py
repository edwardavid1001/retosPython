# Programa de operaciones básicas con elección del usuario

# Función para realizar la suma
def suma(a, b):
    return a + b

# Función para realizar la resta
def resta(a, b):
    return a - b

# Función para realizar la multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar la división
def division(a, b):
    return a / b

# Pedir al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Mostrar opciones de operaciones al usuario
print("Seleccione la operación que desea realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Leer la elección del usuario
opcion = int(input("Ingrese el número de la operación que desea realizar: "))

# Realizar la operación correspondiente según la elección del usuario
if opcion == 1:
    resultado = suma(numero1, numero2)
    operacion = "Suma"
elif opcion == 2:
    resultado = resta(numero1, numero2)
    operacion = "Resta"
elif opcion == 3:
    resultado = multiplicacion(numero1, numero2)
    operacion = "Multiplicación"
elif opcion == 4:
    resultado = division(numero1, numero2)
    operacion = "División"
else:
    print("Opción inválida. Por favor, ingrese un número válido de operación.")
    exit()

# Imprimir el resultado
print(operacion + ":", resultado)
