class Node:
	def __init__(self, num_value):
		self.left_child = None
		self.right_child = None
		self.num_value = num_value
		self.parent = None

	def has_children(self):
		return self.left_child != None and self.right_child != None

	def has_only_left_child(self):
		return self.left_child != None and self.right_child == None

	def has_only_right_child(self):
		return self.right_child != None and self.left_child == None

	def print_children(self):
		if self.left_child == None:
			print("Left Child: None")
		else:
			print("Left Child: ", self.left_child.num_value)
		if self.right_child == None:
			print("Right Child: None")
		else:		
			print("Right Child: ", self.right_child.num_value)

class BinarySearchTree:
	def __init__(self):
		self.head = None
		self.num_nodes = 0
		self.depth = 0

	def swap(self, node, nextNode):
		node_parent = node.parent
		node_left_child = node.left_child
		node_right_child = node.right_child
		
		node.parent = nextNode.parent
		node.left_child = nextNode.left_child
		node.right_child = nextNode.right_child		

		nextNode.parent = node_parent
		nextNode.left_child = node_parent.left_child
		nextNode.right_child = node_parent.right_child

	def insert(self, node):
		self.insertf(node, self.head)

	def insertf(self, node, currentNode):
		if self.head == None:
			self.head = node
			return
		if node.num_value < currentNode.num_value and currentNode.left_child == None:
			currentNode.left_child = node
			node.parent = currentNode
			return
		if node.num_value >= currentNode.num_value and currentNode.right_child == None:
			currentNode.right_child = node
			node.parent = currentNode
			return

		
		if node.num_value < currentNode.num_value:
			self.insertf(node, currentNode.left_child)
		if node.num_value >= currentNode.num_value:
			self.insertf(node, currentNode.right_child)

	def remove(self, node):
		if not node.has_children():
			if node.parent.left_child == node:
				node.parent.left_child = None
			else:
				node.parent.right_child = None

		if node.has_only_left_child():
			if node.parent.left_child == node:
				node.parent.left_child = node.left_child
			else:
				node.parent.right_child = node.left_child
			return

		elif node.has_only_right_child():
			if node.parent.left_child == node:
				node.parent.left_child = node.right_child
			else:
				node.parent.right_child = node.right_child
			return

		else:
			self.swap(node, node.left_child)
			self.remove(node)

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
six = Node(6)
ten = Node(10)
twenty = Node(20)

B = BinarySearchTree()
B.insert(six)
B.insert(two)
B.insert(twenty)
B.insert(ten)
B.insert(one)
B.insert(four)
print(B.head.num_value)
six.print_children()
B.remove(twenty)
six.print_children()












