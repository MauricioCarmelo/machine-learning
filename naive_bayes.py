import pandas as pd

class PosterioriMatrix:

	def __init__(self, datagram, target, values):
		self.datagram = datagram
		self.target = target
		self.X = values
		self.build_matrix()


	def build_matrix(self):
		self.matrix = {}

		# calculate frequencies
		for item in self.datagram[self.target].unique():
			
			dataset = self.datagram.loc[self.datagram[self.target] == item]
			
			print "item: " + str(item)
			print "dataset"
			print dataset

			for key, val in self.X.items():
				subset = dataset.loc[dataset[key] == val]
				print "key: " + str(key) + " val: " + str(val)	
				print "subset"
				print subset

				print len(dataset)
				print len(subset)

				prob = len(subset) / float(len(dataset))
				print prob
				print


class NaiveBayes:

	def loadDatagram(self, filepath):
		self.filepath = filepath
		self.datagram = pd.read_csv(self.filepath) # open datagram form CSV file

	def runAlgorithm(self, target_attribute, values):
		
#		apriori_props = get_apriori_probabilities()
		posteriori_matrix = PosterioriMatrix(self.datagram, target_attribute, values)




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
naive.runAlgorithm("prato", predictive_values)






