# Mauricio Carmelo (2019)

import csv
import numpy as np


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


def dicionaryExtractor(dictionary, *args):
	l = []
	l_real = []
	for arg in args:
		l.append(dictionary[arg])
	for item in l:
		l_real.append(map(float, item))
	return l_real

def dicionarySpecificExtractor(dictionary, n, *args):
	"""
		returns the nth element from 'dictionary' for '*args'
	"""

	l = []
	for arg in args:
		l.append(dictionary[arg][n])
	return l