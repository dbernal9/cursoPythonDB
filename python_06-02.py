"""
Escribe un script que dado el día,mes y año de nacimiento de una persona determine lo siguiente:
    * Cuántos años tiene.
    * Si en lo que va del año ya cumplio o no.
    * Determinar a qué generación pertenece:
        - La generación silenciosa. Nacidos entre 1920 y 1939.
        - Los baby boomers. Nacidos entre 1940 y 1959.
        - Generación X. Nacidos entre 1960 y 1979.
        - Generación Y o millennials. Nacidos entre 1980 y 1989.
        - Generación Z. Nacidos entre 1990 en adelante.
Extra: Utilizar libreria de datetime para obtener mes y año.
"""
import datetime
año_actual = datetime.date.today().year
cumpleaños = input("Escribe tu fecha de nacimiento en este formato DD/MM/YYYY ")
dia = int(cumpleaños.split("/")[0])
mes = int(cumpleaños.split("/")[1])
año = int(cumpleaños.split("/")[2])

edad = año_actual - año
if mes <= datetime.date.today().month and dia <= datetime.date.today().day:
    print("Ya cumplio años")
else:
    print("Todavía le falta")

if año >= 1920 and año <= 1939:
    print("Eres de la generacion silenciosa")
elif año >= 1940 and año <= 1959:
    print("Eres de la baby boomer")
elif año >= 1960 and año <= 1979:
    print("Eres de la generacion x")
elif año >= 1980 and año <= 1989:
    print("Eres de la millenial")
elif año > 1990:
    print("Eres de la generacion z")

