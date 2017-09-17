# Proyecto 1 - Programación II LCC250 2017 - Marengo Juan Pablo - Morengo Rodrigo

import unittest, builtins, sys
from unittest import mock

# Import the code
sys.path.append('src/main')
from tuttiFrutti import *

#####################################################
#						TEST						#
#####################################################

class TestAll(unittest.TestCase):
	@mock.patch('builtins.input', side_effect = ['11', '-9', 'Hola', '3'])
	def test_askForPlayers (self, input):
		assert askForPlayers(5) == 3

	@mock.patch('builtins.input', side_effect = ['Juan', 'Pablo', 'Pablo', 'Rodrigo'])
	def test_askForPlayersNames (self, input):
		assert askForPlayersNames(3) == ['Juan', 'Pablo', 'Rodrigo']

	def test_calculateRoundPoints (self):
		assert calculateRoundPoints('a', {'Juan': ('aa', 'ab', 'ac'), 'Carlos': ('ad', 'ae', 'f'), 'Marta': ('g', 'ae', 'h')}) == {'Juan': 30, 'Carlos': 15, 'Marta': 5}
		assert calculateRoundPoints('a', {'Juan': ('b', 'c'), 'Carlos': ('b', 'f')}) == {'Juan': 0, 'Carlos': 0}
		assert calculateRoundPoints('a', {'Juan': (), 'Carlos': ()}) == {'Juan': 0, 'Carlos': 0}

	def test_calculateTotalScores (self):
		assert calculateTotalScores({'Juan': 20, 'Carlos': 15}, {'Juan': 0, 'Carlos': 10}) == {'Juan': 20, 'Carlos': 25}

	def test_getWinners (self):
		assert getWinners({}) == []
		assert getWinners({'Juan': 10, 'Carlos': 15, 'Marta': 5}) == [('Carlos', 15)]
		assert getWinners({'Juan': 20, 'Carlos': 20, 'Marta': 5}).sort() == [('Juan', 20), ('Carlos', 20)].sort()

	def test_initScoreboard (self):
		assert initScoreboard([]) == {}
		assert initScoreboard(['Juan', 'Carlos']) == {'Juan': 0, 'Carlos': 0}

	def test_isRepeated (self):
		obj = {'Juan': ('a', 'b', 'c'), 'Carlos': ('d', 'e', 'f'), 'Marta': ('g', 'e', 'h')}

		assert not isRepeated('Carlos', obj, 0)
		assert isRepeated('Carlos', obj, 1)

	def test_isThereAWinner (self):
		assert isThereAWinner({'Juan': 10, 'Carlos': 15}, 15)
		assert isThereAWinner({'Juan': 10, 'Carlos': 18}, 15)
		assert not isThereAWinner({'Juan': 10, 'Carlos': 15}, 20)

	def test_randomValue (self):
		assert randomValue([4, 'Pepe', 2.5]) in [4, 'Pepe', 2.5]
		assert randomValue(['Marta']) == 'Marta'
		assert randomValue([]) is None

	@mock.patch('builtins.input', side_effect = ['Anastasia', 'rojo', 'carlos', 'Azul'])
	def test_startRound (self, input):
		assert startRound('a', ['Juan', 'Pablo'], ['Nombre', 'Color']) == {'Juan': ('Anastasia', 'rojo'), 'Pablo': ('carlos', 'Azul')}

if __name__ == '__main__':
	unittest.main()