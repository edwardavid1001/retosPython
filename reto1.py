def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_a_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

eleccion = int(input("Ingrese 1 para Fahrenheit y 2 para Kelvin: "))
celsius = float(input("Ingresa los grados Celsius: "))

if eleccion == 1:
    fahrenheit = celsius_a_fahrenheit(celsius)
    print("Grados Fahrenheit:", fahrenheit)
elif eleccion == 2:
    kelvin = celsius_a_kelvin(celsius)
    print("Grados Kelvin:", kelvin)
else:
    print("Opción inválida. Por favor, ingrese 1 o 2.")
