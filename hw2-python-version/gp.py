
import sys, random, math, numpy

from tree import Tree

def fitness(tree, mode, data):
	# print("fitness")
	yVals = []
	if (mode == 1):
		for row in data:
			yVal = tree.evaluate_tree(row[0])
			yVals.append(yVal)
		yVals = numpy.array(yVals)

		# diff = numpy.array(20000)

		# numpy.subtract(data[:,1], yVals, diff)

		# numpy.square(diff, diff)

		# numpy.mean(diff)


		diff = (numpy.square(numpy.subtract(data[:,1],yVals))).mean()
		
		# print(diff)
	return diff
# # def howFit(tree, data):
# 	# If node count > max
# 	# If depth > max
# 	# Return Huge number


# 	# for k,v in data.items():
# 	# 	ourVal = Tree.evaluate_tree(tree, k)
# 	# 	mse = numpy.mean()
# 	firstPoint = list(data.keys())[0]
# 	ourVal = Tree.evaluate_tree(tree, firstPoint)
# 	return (ourVal - firstPoint) ** 2

# 	# Error is initialized to 0.000001 to avoid divide-by-zero errors (in the perfect case).
# 	error = 0.000001

# 	try:
# 		# Evaluate fitness based on Generator1.jar.
# 		if mode == 1:
# 			with open("data_test.txt", 'r') as inf:
# 				for i in range(int(ratio*total_data)):
# 					x, y = inf.next().split()
# 					error += math.fabs(tree.evaluate_tree(float(x)) - float(y))

# 		# Evaluate fitness based on data.txt.
# 		elif mode == 2:
# 			with open("data.txt", 'r') as inf:
# 				for i in range(int(ratio*total_data)):
# 					x, x2, x3, y = inf.next().split()
# 					error += math.fabs(tree.evaluate_tree(float(x), float(x2), float(x3)) - float(y))

# 		# Evaluate fitness based on Generator2.jar.
# 		elif mode == 3:
# 			with open("data2_copy.txt", 'r') as inf:
# 				for i in range(int(ratio*total_data)):
# 					x, y = inf.next().split()
# 					error += math.fabs(tree.evaluate_tree(float(x)) - float(y))

# 		else:
# 			raise ValueError("You dun fucked up good, foo!  Wrong mode in fitness")

# 	# If the tree causes a ValueError, it's no good.
# 	except (ValueError, ZeroDivisionError):
# 		return sys.maxint

# 	return error

def crossover(pop, mode = 1):
	# fit = []
	# orig = []
	# best = (None, float(math.inf))

	# for i, tree in enumerate(pop):

	# 	current = fitness(tree, mode)
	# 	if current < best[1]:
	# 		best = (tree, current)

	# 	orig.append(current)
	# 	fit.append(1.0 / current)

	# 	if i % 100 == 0:
	# 		print (i)

	# print ("Best tree: " + str(best[0]))
	# print ("Error: " + str(round(best[1])))

	# crosses = weighted_pick(fit, len(fit))
	# children = []

	# for i in xrange(0, len(crosses), 2):
	# 	#print "Crossing: " + str(crosses[i]) + " and " + str(crosses[i+1])
	# 	c1, c2 = combine(pop[crosses[i]], pop[crosses[i+1]])
	# 	#print "Result: " + str(c1) + " and " + str(c2)
	# 	children.append(c1)
	# 	children.append(c2)

	# return children
	pass

def selection(weights,n_picks):
	pass

def cross(first, second):

	first = Tree(0, first)
	second = Tree(0, second)

	parent1, left1 = first.random_parent()
	parent2, left2 = second.random_parent()

	if left1:
		temp = parent1.left

		if left2:
			parent1.left = parent2.left
			parent2.left = temp

		else:
			parent1.left = parent2.right
			parent2.right = temp
	else:
		temp = parent1.right

		if left2:
			parent1.right = parent2.left
			parent2.left = temp

		else:
			parent1.right = parent2.right
			parent2.right = temp

	return first, second

def mutate(pop, ratio, mode):
	for tree in pop:
		if random.random() < ratio:
			mutate_tree(tree, mode)

def mutate_tree(tree, mode):
	node, left = tree.random_parent()
	if left:
		node = node.left
	else:
		node = node.right
	mutate_node(node, mode)

def mutate_node(node, mode):
	if type(node.value) is int or node.value in Tree.OPS_VARS:

		if random.random() < 0.5:
			if mode == 2:
				node.value = random.uniform(-10, 10)
			else:
				node.value = random.randint(-10, 10)

		else:
			if mode == 2:
				node.value = random.choice(Tree.OPS_VARS)
			else:
				node.value = "x"

	elif node.value in Tree.OPS_UNARY:
		replace = random.choice(Tree.OPS_UNARY)
		while replace == node.value:
			replace = random.choice(Tree.OPS_UNARY)

		node.value = replace

	elif node.value in Tree.OPS_BINARY:
		replace = random.choice(Tree.OPS_BINARY)
		while replace == node.value:
			replace = random.choice(Tree.OPS_BINARY)
		node.value = replace