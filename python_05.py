"""1. Pide al usuario dos variables a = 12 y b = 34, crea funciones que permitan calcular la suma, resta,
multiplicación y división, como también el valor del módulo de b entre a"""

def suma(numA: int, numB: int):
    return (numA+numB)
def resta(numA: int, numB: int):
    return numA-numB
def multip(numA: int, numB: int):
    return numA*numB
def divi(numA: int, numB: int):
    return numA/numB
def modulo(numA: int, numB: int):
    return numA%numB

numero_a = 12
numero_b = 34

print("La suma de tus numeros es ", suma(numero_a,numero_b))
print("La resta de tus numeros es ", resta(numero_a,numero_b))
print("La multiplicacion de tus numeros es ", multip(numero_a,numero_b))
print("La division de tus numeros es ", divi(numero_a,numero_b))
print("El modulo de tus numeros es ", modulo(numero_a,numero_b))

########################################################################################################################
"""2. Crea un método que permita convertir cualquier numero entero y a flotante"""
def int2float(num: int):
    return float(num)

numero_entero = int(input("Dame un numero entero: "))
print("Tu numero en float se ve asi: ", int2float(numero_entero))


########################################################################################################################
"""Extra: Define una función para convertir de grados Celsius a Fahrenheit, 
pide al usuario que ingrese la temperatura en Celsius e imprima la conversión."""
def celcius2fahrenheit(temperature):
    t = temperature*(9/5)+32
    return t
Temperatura = int(input("Ingresa los grados Celcius a convertir: "))
print("Esta es la temperatura en Fahrenheit: ", celcius2fahrenheit(Temperatura))


########################################################################################################################
"""Escribe una función llamada "es_par" que tome un número entero como parámetro y devuelva True si el 
número es par o False si el número es impar.
Luego, escribe un programa que pida al usuario que introduzca un número entero y 
utilice la función "es_par" para determinar si el número es par o impar. Imprime en pantalla un 
mensaje indicando si el número es par o impar."""


def es_par(num):
    return num%2

numero_nuevo = int(input("Dame un numero para ver si es par o no: "))
if (es_par(numero_nuevo)==0):
    print("Tu número es par")
else:
    print("Tu número es impar")

