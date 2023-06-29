# Programa con diferentes tipos de variables y entrada del usuario

# Pedir al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Pedir al usuario que ingrese la cantidad de productos
cantidad_productos = int(input("Ingrese la cantidad de productos: "))

# Pedir al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Variables de tipo boolean
es_mayor_de_edad = edad >= 18
es_productos_disponibles = cantidad_productos > 0

# Variables de tipo string
mensaje_saludo = "Hola, " + nombre + "!"

# Imprimir valores de las variables
print("Edad:", edad)
print("Cantidad de productos:", cantidad_productos)
print("¿Es mayor de edad?", es_mayor_de_edad)
print("¿Hay productos disponibles?", es_productos_disponibles)
print("Mensaje de saludo:", mensaje_saludo)
