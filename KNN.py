# Mauricio Carmelo (2019)

from enum import Enum
import csv
import numpy as np

class Classe(Enum):
	SAT = 'SAT'
	INS = 'INS'

def loadCSV(filepath):
	""" method which loads the information from a .csv file
		INPUT
			filepath - relative path to the .csv file
		OUTPUT
			sheet - dictionary structure referencing an attribute to all values in a single column
			attributes - names of columns
			instances - list of values of each row, which makes an instance
	"""
	with open(filepath) as csv_file:
		instances = []

		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				attributes = row
				line_count += 1
			else:
				instances.append(row)
				line_count += 1

	sheet = dict.fromkeys(attributes, {})
	instances = np.array(instances)	

	column = 0
	for item in attributes:
		sheet[item] = instances[:,column]
		column += 1

	return sheet, attributes, instances


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


def dicionarySpecificExtractor(dictionary, n, *args):
	"""
		returns the nth element from 'dictionary' for '*args'
	"""

	l = []
	for arg in args:
		l.append(dictionary[arg][n])
	return l

def dicionaryExtractor(dictionary, *args):
	l = []
	l_real = []
	for arg in args:
		l.append(dictionary[arg])
	for item in l:
		l_real.append(map(float, item))
	return l_real

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


# Test

point = [0.3, 0.7]
kTests = [1, 3, 5, 7] # different tests with different K numbers
results = KNN('input.csv', point, kTests)
print results