import pandas as pd
import numpy

class PosterioriMatrix:

	def __init__(self, datagram, target, values):
		self.datagram = datagram
		self.target = target
		self.X = values
		self.matrix = {}
		self.build_matrix()

	def build_matrix(self):
		
		# calculate frequencies
		for item in self.datagram[self.target].unique():
			
			dataset = self.datagram.loc[self.datagram[self.target] == item]
			probabilities = []

			for key, val in self.X.items():
				subset = dataset.loc[dataset[key] == val]
				prob = len(subset) / float(len(dataset))
				probabilities.append(prob)

			self.matrix[item] = probabilities

	def getMatrix(self):
		return self.matrix



class NaiveBayes:

	def loadDatagram(self, filepath):
		self.filepath = filepath
		self.datagram = pd.read_csv(self.filepath) # open datagram form CSV file

	def getAprioriProbabilities(self, target):
		d = {}
		for item in self.datagram[target].unique():
			dataset = self.datagram.loc[self.datagram[target] == item]
			d[item] = len(dataset) / float(len(self.datagram))
		return d

	def runAlgorithm(self, target_attribute, values):
		
		apriori_props = self.getAprioriProbabilities(target_attribute)
		posteriori_props = PosterioriMatrix(self.datagram, target_attribute, values).getMatrix()

		result = {}
		for key, val in apriori_props.items():
			""" calculate the probabily taking into consideration
				the a priori and posteriori probabilities """
			prob = val * numpy.prod(posteriori_props[key])
			result[key] = prob
		return result


""" X is a dictionary with the predictive attributes
	We want to find Y = f(X)
	Y = {y1, y2...yn}, where yi is the probabily of X belong to class i: P(yi|X)
	
"""
predictive_values = {
	"nuvens": "chuva",
	"temperatura": "frio",
	"umidade": "normal",
	"vento": "sim"
}

naive = NaiveBayes()
naive.loadDatagram("data/naive-bayes-preprocessed-instancies.csv")
result = naive.runAlgorithm("prato", predictive_values)
print result

