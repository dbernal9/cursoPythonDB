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

class Jugador:
    def __init__(self, nombre: str, apellido: str, mail: str, estado: str, raza: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__raza = raza
        self.__mail = mail
        self.__estado = estado
        self.__partidas = 0
        self.__puntos = 0

    def obtener_nombre(self):
        return self.__nombre
    def obtener_apellido(self):
        return self.__apellido
    def obtener_raza(self):
        return self.__raza
    def obtener_estado(self):
        return self.__estado
    def obtener_partidas(self):
        return self.__partidas
    def obtener_puntos(self):
        return self.__puntos
    def actualizar_puntos(self, puntos: int):
        self.__puntos += puntos
    def actualizar_partidas(self):
        self.__partidas += 1
    def actualizar_estado(self):
        self.__estado = "Inactivo"

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
        estado = "Activo"
        raza = input("Raza? Terran | Zerg | Protoss ")
        jugador = Jugador(nombre, apellido, mail, estado, raza)
        JUGADORES.append(jugador)
        print(f"Jugador registrado: {jugador}")

   # else:
        #print("El número de jugadores debe ser par")

def jugar_partida(players: list, activos: list):
    jugadorespartida = players
    jugadoresactivos = activos

    if len(jugadoresactivos) < 2:
        return True
def obtener_ganador():
    print(f"{40 * '='} TORNEO FINALIZADO {40 * '='}")
    print(f"Lista de jugadores\n{JUGADORES}")
    for ganador in JUGADORES:
        if ganador.obtener_estado() == "Activo":
            print(f"Y el ganador es:\n{ganador.obtener_nombre()} {ganador.obtener_apellido()} "
                  f"Puntos: {ganador.obtener_puntos()}")

def generar_partida():
    import random
    #Buscando jugadores
    jugadoresactivos = []
    for jugador in JUGADORES:
        if jugador.obtener_estado() == "Activo":
            jugadoresactivos.append(jugador)
    # print("Jugadores activos")
    # print(jugadoresactivos)
    for i in range(len(JUGADORES) + 1):
        foundpair = False
        while not foundpair:
            jugadorespartida = random.sample(jugadoresactivos, 2)
            if jugadorespartida[0].obtener_partidas() == jugadorespartida[1].obtener_partidas():
                foundpair = True
        print(f"{40 * '='} Partida generada {40 * '='}")
        randomwin = random.randint(0, 1)

        if randomwin == 0:
            jugadorespartida[0].actualizar_partidas()  # Ganó jugador 1, sumar partida
            jugadorespartida[0].actualizar_puntos(3)  # Ganó jugador 1, sumar 3 puntos
            jugadorespartida[1].actualizar_partidas()  # Perdió jugador 2, sumar partida
            jugadorespartida[1].actualizar_puntos(1)  # Perdió jugador 2, sumar 1 punto
            jugadorespartida[1].actualizar_estado()  # Perdió jugador 2, cambiar a inactivo
            for index, j in enumerate(jugadoresactivos):
                if jugadoresactivos[index] == jugadorespartida[1]:
                    print(f"Jugador eliminado :\n {jugadoresactivos.pop(index)}")

        else:
            jugadorespartida[1].actualizar_partidas()  # Ganó jugador 1, sumar partida
            jugadorespartida[1].actualizar_puntos(3)  # Ganó jugador 1, sumar 3 puntos
            jugadorespartida[0].actualizar_partidas()  # Perdió jugador 2, sumar partida
            jugadorespartida[0].actualizar_puntos(1)  # Perdió jugador 2, sumar 1 punto
            jugadorespartida[0].actualizar_estado()  # Perdió jugador 2, cambiar a inactivo
            for index, j in enumerate(jugadoresactivos):
                if jugadoresactivos[index] == jugadorespartida[0]:
                    print(f"Jugador eliminado :\n{jugadoresactivos.pop(index)}")
        if len(jugadoresactivos) < 2:
            print(f"{40 * '='} TORNEO FINALIZADO {40 * '='}")
            break
    obtener_ganador()
def mostrar_resultados():
    print(f"{40 * '='} RESULTADOS {40 * '='}")
    if len(JUGADORES) > 0:
        for index, jug in enumerate(JUGADORES):
            print(f"Jugador {index} {jug.obtener_nombre()} {jug.obtener_apellido()} Puntos: {jug.obtener_puntos()}")
    else:
        print("No hay jugadores registrados")



##########################################################################################
# CONTROL PRINCIPAL
##########################################################################################
JUGADORES = []

MENU = {
    "alta": alta,
    "partida": generar_partida,
    "resultados": mostrar_resultados,
    "salir": salir,
}

OPTIONS = ' | '.join(MENU.keys())

while True:
    action = input(f"Que accion deases realizar? {OPTIONS}\n")
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Accion not soportada: {action}")