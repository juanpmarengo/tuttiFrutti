#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys, random

#####################################################
#					  METHODS						#
#####################################################

# Representamos cantidad de jugadores con numeros enteros
# askForPlayers : int -> int
# El parámetro es la cantidad máxima de jugadores admitidos (definida por reglamento, en nuestro caso es 5)
# y la función devuelve el valor elegido por el usuario, garantizando que es un entero y se encuentra entre 1 y el máximo.
# Ejemplos:
# entrada: 5, salida: número entero entre 1 y 5 (incluyendo a ambos)   		(ingresado por el usuario)
# entrada: 10, salida: número entero entre 1 y 10 (incluyendo a ambos) 		(ingresado por el usuario)
def askForPlayers (maxPlayers):
	clearScreen()

	maxPlayers = int(maxPlayers)

	while True:
		try:
			players = float(input('Ingrese la cantidad de jugadores (Máximo ' + str(maxPlayers) + '): '))

			if players < 1 or players > maxPlayers:
				print('¡Debe ingresar un número entre 1 y ' + str(maxPlayers) + '!')

			elif players != int(players):
				print('¡Debe ser un número entero!')

			else:
				return int(players)

		except Exception:
			print('¡No es un número!')

# Representamos cantidad de jugadores con numeros enteros, y nombres con strings
# askForPlayersNames : int -> (string list)
# El parámetro es la cantidad de jugadores a participar, y la función se encarga de pedir
# los nombres de todos los jugadores, devolviendo una lista conformada por dichos nombres.
# Ejemplos:
# entrada: 3, salida: ["nombre 1", "nombre 2", "nombre 3"]						  	 (nombres ingresados por el usuario)
# entrada: 5, salida: ["nombre 1", "nombre 2", "nombre 3", "nombre 4", "nombre 5"]	 (nombres ingresados por el usuario)
def askForPlayersNames (numPlayers):
	clearScreen()

	names = []

	while len(names) < numPlayers:
		valid = False

		while not valid:
			name = input('Ingrese el nombre del jugador ' + str(len(names) + 1) + ': ')

			if name in names:
				print('¡' + name + ' ya fue ingresado!')

			else:
				valid = True

		names.append(name)

	return names

# Representamos letras con strings, y cada jugador con sus respuestas mediante diccionarios cuyas claves son los nombres y los valores, sus respectivas respuestas.
# Luego, los jugadores con sus respectivas puntuaciónes son representados por otro diccionario, con los nombres como clave y el puntaje respectivo a cada uno como valores.
# calculateRoundPoints : string dict -> dict
# El primer argumento es la letra actualmente en juego, y el segundo son los jugadores con las palabras que han propuesto para cada categoría. La función se encarga de
# decidir cuántos puntos ha ganado cada jugador en la ronda actual.
# Ejemplo:
# entrada: ("a", {"j1":("alberto", "amarillo", "", "arvejas", "", "anana", "argentina") , "j2":("agustin", "amarillo", "avestruz", "avena", "", "arandano", "argentina")})
# salida: {"j1":40 , "j2":50}
def calculateRoundPoints (char, playersAnswers):
	playersPoints = {}

	for player in playersAnswers.keys():
		points = 0
		x = 0

		while x < len(playersAnswers[player]):
			if len(playersAnswers[player][x]) > 0 and playersAnswers[player][x][0].lower() == char.lower():
				if isRepeated(player, playersAnswers, x):
					points += 5

				else:
					points += 10

			x += 1

		playersPoints[player] = points

	return playersPoints

# Representamos a los jugadores y sus puntos para la ronda actual y para la partida entera con diccionarios (los nombres son las claves, y los puntos, los valores).
# Los nombres son strings y los puntos son números enteros.
# calculateTotalScores : dict dict -> dict
# El primer argumento es un diccionario que contiene a los jugadores con los puntos ganados en la ronda actual, y el segundo es un diccionario que representa la tabla de puntuaciones.
# La función suma a cada jugador el puntaje que ha ganado al finalizar la ronda actual.
# Ejemplo:
# entrada: ({"j1":40 , "j2":50}, {"j1":20 , "j2":55}) , salida: {"j1":60 , "j2":105}
def calculateTotalScores (roundPoints, scoreBoard):
	for player in scoreBoard.keys():
		scoreBoard[player] += roundPoints[player]

	return scoreBoard

# Representamos una tabla de puntuaciones con un diccionario, cuyas claves son los nombres de los jugadores (strings) y sus valores son los puntajes totales respectivos a cada jugador (números enteros)
# congratsWinner : dict -> None
# Esta función recibe como argumento la tabla de puntuaciones, y felicita al/los jugador/es con más puntos.
# Ejemplos:
# entrada: {"j1":200 , "j2":170 , "j3":90}, salida: (impresión por pantalla) 'El ganador es j1 con un puntaje de 200'
# entrada: {"j1":205 , "j2":205 , "j3":150}, salida: (impresión por pantalla) Los ganadores son j1, j2 con un puntaje de 205'
def congratsWinner (scoreBoard):
	winners = getWinners(scoreBoard)

	if len(winners) == 1:
		print('El ganador es ' + winners[0][0] + ' con un puntaje de ' + str(winners[0][1]))

	else:
		stringWinners = ''

		for (player, score) in winners:
			stringWinners += player + ', '

		stringWinners = stringWinners[:len(stringWinners) - 2]

		print ('Los ganadores son ' + stringWinners + ' con un puntaje de ' + str(winners[0][1]) + '.')

# Limpia la consola, sin importar el sistema (Windows o Linux)
def clearScreen ():
	os.system('cls' if os.name == 'nt' else 'clear')

# Representamos una tabla de puntuaciones con un diccionario, cuyas claves son los nombres de los jugadores (strings) y sus valores son los puntajes totales respectivos a cada jugador (números enteros).
# endGame : dict -> None
# Esta función se encarga de mostrar la pantalla de final de juego.
def endGame (scoreBoard):
	printScoreboard(scoreBoard)
	congratsWinner(scoreBoard)

# Representamos una tabla de puntuaciones con un diccionario, cuyas claves son los nombres de los jugadores (strings) y sus valores son los puntajes totales respectivos a cada jugador (números enteros)
# getWinners : dict -> (tuple list)
# El argumento de esta función es una tabla de puntuaciones, y lo que se encarga de hacer, es devolver una lista de el/los jugador/es con el mayor puntaje.
# Ejemplos:
# entrada: {"j1":200 , "j2":170 , "j3":90}, salida: [("j1", 200)]
# entrada: {"j1":205 , "j2":205 , "j3":150}, salida: [("j1", 205), ("j2", 205)]
def getWinners (scoreBoard):
	winners = []

	for player in scoreBoard.keys():
		if winners == [] or winners[0][1] == scoreBoard[player]:
			winners.append((player, scoreBoard[player]))

		elif winners[0][1] < scoreBoard[player]:
			winners = [(player, scoreBoard[player])]

	return winners

# Representamos una lista de jugadores por sus nombres y las categorías de palabras con listas de strings, puntajes con numeros, y un alfabeto con un string.
# initGame : (string list) number (string list) string -> None
# Esta función recibe la lista con los nombres de los jugadores, el puntaje que representa una victoria, las categorías a poner en juego y el alfabeto a usar, y da lugar
# al ciclo principal del juego, donde cada repeticion del while es una ronda de la partida.
def initGame (players, maxPoints, categories, alphabet):
	clearScreen()

	scoreBoard = initScoreboard(players)

	while True:
		actualChar = randomValue(alphabet)

		if actualChar is None:
			endGame(scoreBoard)
			return

		alphabet.remove(actualChar)

		roundAnswers	= startRound(actualChar, players, categories)
		roundPoints 	= calculateRoundPoints(actualChar, roundAnswers)
		scoreBoard 		= calculateTotalScores(roundPoints, scoreBoard)

		if isThereAWinner(scoreBoard, maxPoints):
			endGame(scoreBoard)
			return

# Representamos jugadores por sus nombres con una lista de strings, y una tabla de puntuaciones con un diccionario.
# initScoreboard : (string list) -> dict
# El argumento de esta función es la lista de jugadores, a partir de la cual se encarga de crear la tabla de puntuaciones.
# Ejemplos:
# entrada: ["j1", "j2"], salida: {"j1":0 , "j2":0}
# entrada: ["pedro", "jose"], salida: {"pedro":0 , "jose":0}
def initScoreboard (players):
	scoreBoard = {}

	for player in players:
		scoreBoard[player] = 0

	return scoreBoard

# Representamos un jugador por su nombre con un string, las respuestas de los jugadores con un diccionario que contiene strings (las respuestas mismas) como valores, y un índice con un número.
# isRepeated : string dict number -> bool
# El primer argumento de esta función es un string con el nombre de un jugador, el segundo es un diccionario que contiene las respuestas de todos los jugadores, y el tercero es un índice.
# El trabajo de esta función es devolver verdadero si la respuesta del jugador dado, en el índice dado, es la misma que la de algún otro jugador en el mismo índice, y falso en caso contrario.
# Ejemplos:
# entrada: ("Carlos", {"Juan": ('a', 'b', 'c'), 'Carlos': ('d', 'e', 'f'), 'Marta': ('g', 'e', 'h')}, 0)
# salida: False
# entrada: ("Marta", {'Juan': ('a', 'b', 'c'), 'Carlos': ('d', 'e', 'f'), 'Marta': ('g', 'e', 'h')}, 1)
# salida: True
def isRepeated (player, playersAnswers, index):
	for otherPlayer in playersAnswers.keys():
		if player != otherPlayer and playersAnswers[player][index].lower() == playersAnswers[otherPlayer][index].lower():
			return True

	return False

# Representamos una tabla de puntuaciones con un diccionario, y puntajes con un número.
# isThereAWinner : dict number -> bool
# Esta función revisa si algún jugador ha superado el puntaje requerido para ganar, y devuelve verdadero en caso afirmativo, o falso en caso negativo.
# entrada: {"j1":200 , "j2":170 , "j3":90}, salida: True
# entrada: {"j1":50 , "j2":120 , "j3":10}, salida: False
def isThereAWinner (scoreBoard, maxPoints):
	for player in scoreBoard.keys():
		if scoreBoard[player] >= maxPoints:
			return True

	return False

# Representamos una tabla de puntuaciones con un diccionario.
# printScoreboard : dict -> None
# Esta función simplemente se encarga de imprimir la tabla de puntajes en la pantalla.
def printScoreboard (scoreBoard):
	clearScreen()
	print("Nombre - Puntaje")

	for player in scoreBoard.keys():
		print(player + ' ' + str(scoreBoard[player]))

# randomValue : (x list) -> x
# Devuelve un valor al azar dentro de una lista de valores si la lista no es vacía, y nada en caso contrario.
def randomValue (values):
	return values[random.randint(0, len(values) - 1)] if len(values) > 0 else None

# Representamos un caracter con un string, jugadores por sus nombres y las categorías a jugar con listas de strings.
# startRound : string (string list) (string list) -> dict
# Esta función se encarga de obtener las respuestas de los jugadores para la ronda del caracter en juego.
def startRound (char, players, categories):
	playersAnswers = {}

	for player in players:
		clearScreen()
		print('Turno de ' + player + '.')

		actualPlayerAnswers = []

		for category in categories:
			actualPlayerAnswers.append(input('Ingrese un/a ' + category + ' que comience con la letra ' + char + ': '))

		playersAnswers[player] = tuple(actualPlayerAnswers)

	return playersAnswers

#####################################################
#						MAIN						#
#####################################################

def main ():
	MAX_POINTS 	= 200
	MAX_PLAYERS = 5
	CATEGORIES  = ['Nombre', 'Color', 'Animal','Comida', 'Flor', 'Fruta', 'País']
	ALPHABET 	= list('abcdefghijklmnopqrstuvwxyz')
	
	numPlayers 	= askForPlayers(MAX_PLAYERS) if MAX_PLAYERS >= 2 else 1
	players 	= askForPlayersNames(numPlayers)

	initGame(players, MAX_POINTS, CATEGORIES, ALPHABET)

if __name__ == '__main__':
	main()