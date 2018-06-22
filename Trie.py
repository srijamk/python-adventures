class Node:
	global NUMBER_OF_CHARACTERS = 26
	def __init__(self):
		self.children = [None] * NUMBER_OF_CHARACTERS
		self.size = 0

	def getCharIndex(char):
		return char - 'a'

	def getNode(self, c):
		return self.children[getCharIndex(c))

	def setNode(self, node, c):
		self.children[getCharIndex(c)] = node

	def add(self, string):
		add(string, 0)

	def add(self, string, index):
		if index == len(string):
			return
		currentChar = string[index]
		child = getNode(currentChar)
		if child == None:	# Creates new node if child doesn't exist
			child = Node()
			setNode(currentChar, child)
		child.add(s, index + 1)		# Recursive

	def findCount(self, string, index):
		if index == len(string):
			return self.size
		child = getNode(string[index])
		if child == None:
			return 0


		
	
