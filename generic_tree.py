# Mauricio Carmelo (2019)

class Node:
	def __init__(self, value=None):
		self.value = value
		self.childs=[]

class Tree:
	def __init__(self, value):
		self.root = Node (value)

	def insert(self, value, fatherValue):

		if self.root is None:
			self.root = Node(value)

		else:
			self.insert_recursively(value, fatherValue, self.root)

	def insert_recursively(self, value, fatherValue, cur_node):

		if cur_node.value == fatherValue:
			cur_node.childs.append( Node(value) )

		else:
			for child in cur_node.childs:
				self.insert_recursively(value, fatherValue, child)

	def printTree(self):
		if self.root != None:
			self.printTree_recursively(self.root)

	def printTree_recursively(self, cur_node):
		for child in cur_node.childs:
			self.printTree_recursively(child)
		print cur_node.value