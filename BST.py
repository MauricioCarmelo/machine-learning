# Mauricio Carmelo (2019)


class Node:
	def __init__(self, value=None):
		self.value = value
		self.left=None
		self.right=None

class BinarySearchTree:
	def __init__(self):
		self.root=None
		self.cur_node=None

	def insert(self, value):
		if self.root:
			self.insert_recursively(value, self.root)
		else:
			self.root = Node(value)

	def insert_recursively(self, value, cur_node):
		if value < cur_node.value:
			if cur_node.left == None:
				cur_node.left = Node(value)
			else:
				self.insert_recursively(value, cur_node.left)

		elif value > cur_node.value:
			if cur_node.right == None:
				cur_node.right = Node(value)
			else:
				self.insert_recursively(value, cur_node.right)

	def printTree(self):
		if self.root != None:
			self.printTree_recursively(self.root)

	def printTree_recursively(self, cur_node):
		if cur_node.left:
			self.printTree_recursively(cur_node.left)
		print cur_node.value
		if cur_node.right:
			self.printTree_recursively(cur_node.right)