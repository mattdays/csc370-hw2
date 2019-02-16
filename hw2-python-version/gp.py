
import sys, random, math, numpy

from tree import Tree

def howFit(tree, data):
	# for k,v in data.items():
	# 	ourVal = Tree.evaluate_tree(tree, k)
	# 	mse = numpy.mean()
	firstPoint = list(data.keys())[0]
	ourVal = Tree.evaluate_tree(tree, firstPoint)
	return (ourVal - firstPoint) ** 2

def crossover(pop, mode = 1):
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

	elif node.value in Tree.OPS_BINARY:
		replace = random.choice(Tree.OPS_BINARY)
		while replace == node.value:
			replace = random.choice(Tree.OPS_BINARY)
		node.value = replace