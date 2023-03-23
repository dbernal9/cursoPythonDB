"""
Torneo de Starcraft 2
Registrar jugadores con Nombre, Email, Puntos ganados, Raza (terran, zerg, protoss)
Estado (activo/inactivo), contador de partidas
"""

from enum import Enum
import random


##########################################################################################
# ABSTRACIONES DEL JUGADOR
##########################################################################################
class Estado(Enum):
    ACTIVO = 1
    INACTIVO = 2

class Raza(Enum):
    TERRAN = 1
    ZERG = 2
    PROTOSS = 3
class Jugador:
    def __init__(self, nombre: str, apellido: str, mail: str, estado: Estado, raza: Raza):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__raza = raza
        self.__mail = mail
        self.__estado = estado
        self.__partidas = 0
        self.__puntos = 0

    def obtener_estado(self):
        return self.__estado
    def obtener_partidas(self):
        return self.__partidas
    def obtener_puntos(self):
        return self.__puntos
    def actualizar_partidas(self):
        self.__partidas += 1
    def actualizar_partidas(self, estado: str, resultado: str):
        self.__estado = "INACTIVO"
        self.__partidas += 1
        if resultado == "win":
            self.__puntos += 3
        else:
            self.__puntos += 1

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"(Nombre: {self.__nombre}, Apellido: {self.__apellido}, " \
               f"Email: {self.__mail}, Estado: {self.__estado}, Raza: {self.__raza}, " \
               f"Partidas jugadas: {self.__partidas})"

##########################################################################################
# ACCIONES DEL SISTEMA
##########################################################################################
def imprimir_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")
def salir():
    print("Cerrando...")
    exit(0)
def alta():
    #numberOfPlayers = int(input("Cuántos jugadores desea agregar?"))
    #if numberOfPlayers % 2 == 0:
        imprimir_header("ALTA JUGADOR")
        nombre = input("Nombre? ")
        apellido = input("Apellido? ")
        mail = input("Mail? ")
        estado = "ACTIVO"
        raza = input("Raza? TERRAN | ZERG | PROTOSS ")
        jugador = Jugador(nombre, apellido, mail, Estado[estado], Raza[raza])
        JUGADORES.append(jugador)
        print(f"Jugador registrado: {jugador}")
   # else:
        #print("El número de jugadores debe ser par")

def buscar_jugador():
    partidaslst =[]
    estadoslst = []
    found_pair = False
    if len(JUGADORES) % 2 == 0:
        for jugador in JUGADORES:
            partidaslst.append(jugador.obtener_partidas())
            estadoslst.append(jugador.obtener_estado())
    else:
        print("No se puede generar partida con un numero de participantes impar")
    for index,(stat,part) in enumerate(zip(partidaslst,estadoslst)):
        if stat == "Estado.ACTIVO" and partidaslst.count(part) == 2 and not found_pair:
            indices = [i for i, x in enumerate(partidaslst) if x == b]
            if index in indices:
                indices.remove(index)
            print("Partida generada")
            found_pair = True

def generar_partida():
    buscar_jugador()
    """imprimir_header("Generando Partida")
    for index, jugador in enumerate(JUGADORES):
        if jugador.obtener_estado() == Estado["ACTIVO"]:
            print({f"{index}) {jugador}"})"""




##########################################################################################
# CONTROL PRINCIPAL
##########################################################################################
JUGADORES = []

MENU = {
    "alta": alta,
    "partida": generar_partida,
    #"mostrar resultados": mostrar_todos,
    "salir":salir,
}

OPTIONS = ' | '.join(MENU.keys())

while True:
    action = input(f"Que accion deases realizar? {OPTIONS}\n")
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Accion not soportada: {action}")