# Mauricio Carmelo (2019)

from enum import Enum
import csv
import numpy as np
from loadCSV import loadCSV, dicionaryExtractor, dicionarySpecificExtractor

class Classe(Enum):
	SAT = 'SAT'
	INS = 'INS'

def manhattanDistance(point1, point2):
	"""
		INPUT
			point1
			point2
		OUTPUT
			distance - manhattan distance between point1 and point2			 - 

	"""
	distance = 0
	for xi, xj in zip(point1, point2):
		distance += abs(xi - xj)
	return distance

def KNN(filepath, point, kTests):

	"""
		KNN algoritm
		INPUT
			filepath
			point
			kTests - list with integer for values of k tests
		OUTPUT
			results - list of tuples for KNN for all k tests in kTests list
	"""

	sheet, attributes, instances = loadCSV(filepath)
	#determine the values to be calculated to prepare instances_int
	to_be_calc = dicionaryExtractor(sheet, 'tempoEspera', 'preco')
	to_be_calc = np.array(to_be_calc)
	
	# calculate manhattan distances
	distances = []
	for p in to_be_calc.T:
		distances.append(manhattanDistance(point, p))
	
	smallestDistances = np.argsort(distances)

	results = []

	for k in kTests:

		sat = 0
		ins = 0

		for n in range(0, k):
			classe = dicionarySpecificExtractor(sheet, smallestDistances[n], 'classe')
			classe = classe[0]
			if classe == 'SAT':
				sat += 1
			elif classe == 'INS':
				ins += 1

		if sat > ins:
			classe = 'SAT'
		elif ins > sat:
			classe = 'INS'
		else:
			classe = 'undetermined'

		results.append((k, classe))

	return results

point = [0.3, 0.7]
kTests = [1, 3, 5, 7] # different tests with different K numbers
results = KNN('input.csv', point, kTests)
print results