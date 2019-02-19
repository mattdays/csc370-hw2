import math, random, gp
from sklearn.metrics import mean_squared_error


class Tree:
	OPS_1 = ["x", "+", "-", "*", "/"]
	OPS_2 = ["x", "x2", "x3", "+", "-", "*", "/"]
	OPS_3 = ["x", "+", "-", "*", "/", "e", "sin", "log"]

	OPS_VARS = ["x", "x2", "x3"]
	OPS_UNARY = ["e", "sin", "log"]
	OPS_BINARY = ["+", "-", "*", "/"]

	def __init__(self, ops, data, original=None, maxDepth=None, growMode=None):
		if original:

			self.root = Tree.Node(original.root.value)
			Tree.clone(self.root, original.root.left, original.root.right)
			# self.fitness = self.calcFitness(data, ops)
			# self.fitness = gp.fitness(self, ops, data)

		else:

			self.root = Tree.Node(random.choice(Tree.OPS_BINARY))
			Tree.populate(self.root, ops, maxDepth, growMode)
			# self.fitness = self.calcFitness(data, ops)
			# self.fitness = gp.fitness(self, ops, data)


	@staticmethod
	def clone(node, left=None, right=None):
		if left:

			node.left = Tree.Node(left.value)
			Tree.clone(node.left, left.left, left.right)

		if right:

			node.right = Tree.Node(right.value)
			Tree.clone(node.right, right.left, right.right)

	def calcFitness(self, data, mode):
		# print("fitness")
		dataYs = []
		ourYs = []

		if (mode == 1):
			for row in range(len(data)):
				dataYs.append(data[row][1])
				ourYs.append(self.evaluate_tree(self.root, data[row][0]))
			return mean_squared_error(dataYs, ourYs)
		else:
			return -1
			# 	yVal = tree.evaluate_tree(row[0])
			# 	yVals.append(yVal)
			# yVals = numpy.array(yVals)

			# diff = numpy.array(20000)

			# numpy.subtract(data[:,1], yVals, diff)

			# numpy.square(diff, diff)

			# numpy.mean(diff)


			# diff = (numpy.square(numpy.subtract(data[:,1],yVals))).mean()
			
			# print(diff)
		# return diff


# MODE dictates partialGrow or fullGrow
	@staticmethod
	def populate(node, ops, maxDepth, growMode):
		if (growMode == 0):
			Tree.partialGrow(node, ops, maxDepth)
		elif (growMode == 1):
			Tree.fullGrow(node, ops, maxDepth)

		# # Proportion of constant nodes vs variables vs operations
		# dist = [.25, .5]

		# r = random.random()

		# if r < dist[0] and node.value not in Tree.OPS_UNARY:
		# 	if ops == 2:
		# 		node.left = Tree.Node(random.uniform(-10, 10))
		# 	else:
		# 		node.left = Tree.Node(random.randint(-10, 10))
		
		# elif r < dist[1]:
		# 	if ops == 2:
		# 		node.left = Tree.Node(random.choice(Tree.OPS_VARS))
		# 	else:
		# 		node.left = Tree.Node("x")

		# elif depth < 8:
		# 	if ops == 3 and random.random() < .5:
		# 		node.left = Tree.Node(random.choice(Tree.OPS_UNARY))
		# 	else:
		# 		node.left = Tree.Node(random.choice(Tree.OPS_BINARY))
		# 	Tree.populate(node.left, ops, depth + 1)

		# else:
		# 	if ops == 2:
		# 		node.left = Tree.Node(random.uniform(-10, 10))
		# 	else:
		# 		node.left = Tree.Node(random.randint(-10, 10))

		# if node.value not in Tree.OPS_UNARY:
		# 	r = random.random()

		# 	if r < dist[0]:
		# 		if ops == 2:
		# 			node.right = Tree.Node(random.uniform(-10, 10))
		# 		else:
		# 			node.right = Tree.Node(random.randint(-10, 10))

		# 	elif r < dist[1]:
		# 		if ops == 2:
		# 			node.right = Tree.Node(random.choice(Tree.OPS_VARS))
		# 		else:
		# 			node.right = Tree.Node("x")

		# 	elif depth < 8:
		# 		if ops == 3 and random.random() < .5:
		# 			node.right = Tree.Node(random.choice(Tree.OPS_UNARY))
		# 		else:
		# 			node.right = Tree.Node(random.choice(Tree.OPS_BINARY))
		# 		Tree.populate(node.right, ops, depth + 1)

		# 	else:
		# 		if ops == 2:
		# 			node.right = Tree.Node(random.uniform(-10, 10))
		# 		else:
		# 			node.right = Tree.Node(random.randint(-10, 10))
	@staticmethod
	def partialGrow(node, ops, depth):
		if (node.value in Tree.OPS_BINARY):
			if (depth >= 1 and random.getrandbits(1) ):
				if (node.left == None):
					newLeft = Tree.Node(random.choice(Tree.OPS_BINARY))
					node.left = newLeft
					Tree.partialGrow(node.left, ops, depth - 1)
				if (node.right == None):
					newRight = Tree.Node(random.choice(Tree.OPS_BINARY))
					node.right = newRight
					Tree.partialGrow(node.right, ops, depth - 1)
			else:
				if (node.left == None):
					
					if (ops == 2):
						# Random chance of variable1, v2, v3, constant
						rand = random.randint(1,4)
						if (rand == 1):
							newVal = "x1"
						elif (rand == 2):
							newVal = "x2"
						elif (rand == 3):
							newVal = "x3"
						else:
							newVal = random.randrange(1,10)
					else:
						if (random.getrandbits(1)):
							newVal = random.randrange(1,10)
						else:
							newVal = "x"

					newLeft = Tree.Node(newVal)
					node.left = newLeft
					Tree.partialGrow(node.left, ops, depth - 1)
				if (node.right == None):

					if (ops == 2):
						# Random chance of variable1, v2, v3, constant
						rand = random.randint(1,4)
						if (rand == 1):
							newVal = "x1"
						elif (rand == 2):
							newVal = "x2"
						elif (rand == 3):
							newVal = "x3"
						else:
							newVal = random.randrange(1,10)
					else:
						if (random.getrandbits(1)):
							newVal = random.randrange(1,10)
						else:
							newVal = "x"

					newRight = Tree.Node(newVal)
					node.right = newRight
					Tree.partialGrow(node.right, ops, depth - 1)





		# if (depth > 0 and random.getrandbits(1)):
		# 	return Tree.Node(random.choice(Tree.OPS_BINARY), Tree.partialGrow(depth - 1), Tree.partialGrow(depth - 1))
		# else:
		# 	if (random.getrandbits(1)):
		# 		print("HERE")

		# 		return Tree.Node(0)
		# 	else: 
		# 		return Tree.Node(1)
        

		# if (depth > 0 and random.getrandbits(1)):
		# 	newVal = random.choice(Tree.OPS_BINARY)
		# 	pass
		# 	# return Tree(newVal, partialGrow(depth - 1), partialGrow(depth - 1))
		# else:
		# 	if (random.getrandbits(1)):
		# 		return Tree(random.randrange(1, 10))
		# 	else:
		# 		return Tree("x")

	@staticmethod
	def fullGrow(node, ops, depth):
		if (node.value in Tree.OPS_BINARY):
			if (depth >= 1):
				if (node.left == None):
					newLeft = Tree.Node(random.choice(Tree.OPS_BINARY))
					node.left = newLeft
					Tree.fullGrow(node.left, ops, depth - 1)
				if (node.right == None):
					newRight = Tree.Node(random.choice(Tree.OPS_BINARY))
					node.right = newRight
					Tree.fullGrow(node.right, ops, depth - 1)
			else:
				if (node.left == None):
					
					if (ops == 2):
						# Random chance of variable1, v2, v3, constant
						rand = random.randint(1,4)
						if (rand == 1):
							newVal = "x1"
						elif (rand == 2):
							newVal = "x2"
						elif (rand == 3):
							newVal = "x3"
						else:
							newVal = random.randrange(1,10)
					else:
						if (random.getrandbits(1)):
							newVal = random.randrange(1,10)
						else:
							newVal = "x"

					newLeft = Tree.Node(newVal)
					node.left = newLeft
					Tree.fullGrow(node.left, ops, depth - 1)
				if (node.right == None):

					if (ops == 2):
						# Random chance of variable1, v2, v3, constant
						rand = random.randint(1,4)
						if (rand == 1):
							newVal = "x1"
						elif (rand == 2):
							newVal = "x2"
						elif (rand == 3):
							newVal = "x3"
						else:
							newVal = random.randrange(1,10)
					else:
						if (random.getrandbits(1)):
							newVal = random.randrange(1,10)
						else:
							newVal = "x"

					newRight = Tree.Node(newVal)
					node.right = newRight
					Tree.fullGrow(node.right, ops, depth - 1)
		# if (depth == 0):
		# 	if (ops == 2):
		# 		# Random chance of variable1, v2, v3, constant
		# 		rand = random.randint(1,4)
		# 		if (rand == 1):
		# 			newVal = "x1"
		# 		elif (rand == 2):
		# 			newVal = "x2"
		# 		elif (rand == 3):
		# 			newVal = "x3"
		# 		else:
		# 			newVal = random.randrange(1,10)
		# 	else:
		# 		if (random.getrandbits(1)):
		# 			newVal = random.randrange(1,10)
		# 		else:
		# 			newVal = "x"
		# 	print (newVal)
		# 	node = Tree.Node(newVal)
		# 	# node.left = None
		# 	# node.right = None
		# 	# return node
		# else:
		# 	node.left = Tree.Node(random.choice(Tree.OPS_BINARY))
		# 	Tree.fullGrow(node.left, ops, depth - 1)

		# 	node.right = Tree.Node(random.choice(Tree.OPS_BINARY))
		# 	Tree.fullGrow(node.right, ops, depth - 1)
		# # if (depth > 0):
		# # 	newVal = random.choice(Tree.OPS_BINARY)
		# # 	node.left = Tree.Node(newVal)
		# # 	Tree.fullGrow(node.left, ops, depth -1)
		# # 	# temp = Tree.Node(newVal)
		# # 	temp.left = Tree.fullGrow(temp, ops, depth - 1)
		# # 	temp.right = Tree.fullGrow(temp, ops, depth - 1)
		# # 	# return Tree(newVal, fullGrow(depth - 1), fullGrow(depth - 1))
		# # else:
		# # 	if (random.getrandbits(1)):
		# # 		return Tree(random.randrange(1, 10))
		# # 	else:
		# # 		return Tree("x")


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
	
	def getTreeHeight(self):
		return Tree.getNodeHeight(self.root)

	@staticmethod
	def getNodeHeight(node):
		if (node is None):
			return -1 
		return max(Tree.getTreeHeight(node.left), Tree.getTreeHeight(node.right)) + 1

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
		# print("eval Tree")
		# return float(Tree.evaluate(self.root, x, x2, x3))
		return Tree.evaluate(self.root, x, x2, x3)


	@staticmethod
	def evaluate(node, x, x2, x3):

		# print("eval Rec")
		if node is None:
			return 0
		
		if node.left is None and node.right is None:
			if node.value == "x":
				return x
			elif node.value == "x2":
				return x2
			elif node.value == "x3":
				return x3
			else:
				return node.value

		leftVal = Tree.evaluate(node.left,x,x2,x3)
		rightVal = Tree.evaluate(node.right,x,x2,x3)

		if node.value == "+":
			return leftVal + rightVal
		elif node.value == "-":
			return leftVal - rightVal
		elif node.value == "*":
			return leftVal * rightVal
		elif node.value == "/":
			# Catch div by 0?
			if (rightVal >= -0.001 and rightVal <= 0.001):
				return 1
			else:
				return leftVal / rightVal

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


			elif self.value == "e":
				return "e^" + str(self.left)
			elif self.value == "sin":
				return "sin(" + str(self.left) + ")"
			elif self.value == "log":
				return "log(" + str(self.left) + ")"