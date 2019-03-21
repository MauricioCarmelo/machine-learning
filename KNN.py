# # Mauricio Carmelo (2019)


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


def getBiggestIndexOfIndex(distances, indexes, k):
	"""
		INPUT
			distances - list where all distances are stored during runtime
		OUTPUT
			biggest - index of the biggest element within 'indexes' list
	"""
	biggest = 0 # first element of 'indexes' list
	for i in range(0, k):
		if distances[indexes[i]] > distances[indexes[biggest]]:
			biggest = i
	return biggest


def getIndexOfKsmallests(distances, k):
	"""
		INPUT
			distances
			k
		OUTPUT
			indexes - indexes that references the k smallest elements within 'distances' list
	"""

	indexes = [] # indexes of smallest number within 'distances' array
	
	for i in range(0, k):
		indexes.append(i)

	biggest = getBiggestIndexOfIndex(distances, indexes, k) # index of biggest number in results
	for i in range(k, len(distances)):
		if distances[i] < distances[indexes[biggest]]:
			indexes.remove(indexes[biggest]) # remove by value
			indexes.append(i) # insert index of smaller element in results
			biggest = getBiggestIndexOfIndex(distances, indexes, k)
	
	return indexes

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

def KNN(filepath, point, k):

	"""
		KNN algoritm
		INPUT
			filepath
			point
			k
		OUTPUT
			answer - result of KNN guess
	"""

	sheet, attributes, instances = loadCSV(filepath)
	#determine the values to be calculated to prepare instances_int
	to_be_calc = dicionaryExtractor(sheet, 'tempoEspera', 'tempo', 'tem')
	to_be_calc = np.array(to_be_calc)
	
	# calculate manhattan distances
	distances = []
	for p in to_be_calc.T:
		distances.append(manhattanDistance(point, p))

	kSmallests = getIndexOfKsmallests(distances, k)

	print kSmallests

	for n in kSmallests:
		print dicionarySpecificExtractor(sheet, n, 'id')	


k = 3
point = [0, 0, 0]
KNN('input.csv', point, k)




