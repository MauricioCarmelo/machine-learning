# Mauricio Carmelo (2019)

import csv
import numpy as np


def loadCSV(filepath):
	""" method which loads the information from a .csv file
		INPUT
			filepath - relative path to the .csv file
		OUTPUT
			sheet - dictionary structure referencing an attribute to all values in a single column
			attributes - name of column attribute
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


sheet, attributes, instances = loadCSV('input.csv')

print 'Loaded sheet within a dictionary:'
for key in sheet.keys():
	print sheet[key]