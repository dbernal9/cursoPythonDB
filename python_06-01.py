"""
Escribe un script que dado la edad de una persona y su altura pueda determinar si la misma puede o no
subirse en la montaña rusa “Push-Pull”, dado que se debe ser mayor a 14 años y tener una altura no menor de 1,62.
El script debe ser capaz de informar si puede o no subirse y en el caso de que no,
porque razon (Si por edad, por tamaño u ambas)
"""


edad = 14
altura = 1.62

if edad < 14 and altura < 1.62:
    print("Hiiijoles carnal, tas muy chavo y chaparro pa este juego")
elif edad < 14:
    print("Hiiijoles carnal, tas muy chavo pa este juego")
elif altura < 1.62:
    print("Hiiijoles carnal, tas muy chaparro pa este juego")
else:
    print("Camara carnal, trepate, nomas agarrate bien")