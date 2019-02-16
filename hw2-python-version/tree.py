import math, random

class Tree:
	OPS_1 = ["x", "+", "-", "*", "/"]
	OPS_2 = ["x", "x2", "x3", "+", "-", "*", "/"]
	OPS_3 = ["x", "+", "-", "*", "/", "e", "sin", "log"]

	OPS_VARS = ["x", "x2", "x3"]
	OPS_UNARY = ["e", "sin", "log"]
	OPS_BINARY = ["+", "-", "*", "/"]

	def __init__(self, ops, original=None):
		if original:

			self.root = Tree.Node(original.root.value)
			Tree.clone(self.root, original.root.left, original.root.right)

		else:

			self.root = Tree.Node(random.choice(Tree.OPS_BINARY))
			Tree.populate(self.root, ops, 0)

	@staticmethod
	def clone(node, left=None, right=None):
		if left:

			node.left = Tree.Node(left.value)
			Tree.clone(node.left, left.left, left.right)

		if right:

			node.right = Tree.Node(right.value)
			Tree.clone(node.right, right.left, right.right)

	@staticmethod
	def populate(node, ops, depth):

		# Proportion of constant nodes vs variables vs operations
		dist = [.25, .5]

		r = random.random()

		if r < dist[0] and node.value not in Tree.OPS_UNARY:
			if ops == 2:
				node.left = Tree.Node(random.uniform(-10, 10))
			else:
				node.left = Tree.Node(random.randint(-10, 10))
		
		elif r < dist[1]:
			if ops == 2:
				node.left = Tree.Node(random.choice(Tree.OPS_VARS))
			else:
				node.left = Tree.Node("x")

		elif depth < 8:
			if ops == 3 and random.random() < .5:
				node.left = Tree.Node(random.choice(Tree.OPS_UNARY))
			else:
				node.left = Tree.Node(random.choice(Tree.OPS_BINARY))
			Tree.populate(node.left, ops, depth + 1)

		else:
			if ops == 2:
				node.left = Tree.Node(random.uniform(-10, 10))
			else:
				node.left = Tree.Node(random.randint(-10, 10))

		if node.value not in Tree.OPS_UNARY:
			r = random.random()

			if r < dist[0]:
				if ops == 2:
					node.right = Tree.Node(random.uniform(-10, 10))
				else:
					node.right = Tree.Node(random.randint(-10, 10))

			elif r < dist[1]:
				if ops == 2:
					node.right = Tree.Node(random.choice(Tree.OPS_VARS))
				else:
					node.right = Tree.Node("x")

			elif depth < 8:
				if ops == 3 and random.random() < .5:
					node.right = Tree.Node(random.choice(Tree.OPS_UNARY))
				else:
					node.right = Tree.Node(random.choice(Tree.OPS_BINARY))
				Tree.populate(node.right, ops, depth + 1)

			else:
				if ops == 2:
					node.right = Tree.Node(random.uniform(-10, 10))
				else:
					node.right = Tree.Node(random.randint(-10, 10))

	def count(self):
		return Tree.count_node(self.root)

	@staticmethod
	def count_node(node):

		c = 1
		if node.left:
			c += Tree.count_node(node.left)
		if node.right:
			c += Tree.count_node(node.right)
		return c

	def random_parent(self):

		r = random.randint(2, self.count())
		parent, left, c, f = Tree.get_parent(self.root, r)
		return parent, left

	@staticmethod
	def get_parent(node, n, count=0):

		count += 1

		if count == n:
			return None, None, count, True

		if node.left:

			parent, left, count, found = Tree.get_parent(node.left, n, count)

			if found:

				if parent:
					return parent, left, count, found
				else:
					return node, True, count, found

		if node.right:

			parent, left, count, found = Tree.get_parent(node.right, n, count)

			if found:

				if parent:
					return parent, left, count, found
				else:
					return node, False, count, found

		return None, None, count, False

	def evaluate_tree(self, x, x2=None, x3=None):
		return float(Tree.evaluate(self.root, x, x2, x3))

	@staticmethod
	def evaluate(node, x, x2, x3):

		if node.value == "x":
			return x
		elif node.value == "x2":
			return x2
		elif node.value == "x3":
			return x3
		elif type(node.value) is int or type(node.value) is float:
			return node.value

		elif node.value == "+":
			return Tree.evaluate(node.left,x,x2,x3) + Tree.evaluate(node.right,x,x2,x3)
		elif node.value == "-":	
			return Tree.evaluate(node.left,x,x2,x3) - Tree.evaluate(node.right,x,x2,x3)
		elif node.value == "*":
			return Tree.evaluate(node.left,x,x2,x3) * Tree.evaluate(node.right,x,x2,x3)
		elif node.value == "/":
			# Catch div by 0?
			if (Tree.evaluate(node.right,x,x2,x3) == 0):
				return math.inf
			else:
				return Tree.evaluate(node.left,x,x2,x3) / float(Tree.evaluate(node.right,x,x2,x3))

	def __str__(self):


		return str(self.root)

	class Node:


		def __init__(self, v):


			self.value = v
			self.left = None
			self.right = None

		def __str__(self):

			if self.value == "x" or self.value == "x2" or self.value == "x3":
				return self.value
			elif type(self.value) is int or type(self.value) is float:
				return str(round(self.value, 2))

			elif self.value == "+" or self.value == "-" or self.value == "*" or self.value == "/":
				return "(" + str(self.left) + " " + self.value + " " + str(self.right) + ")"
