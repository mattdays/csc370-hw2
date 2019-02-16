import random
import math
import copy


class Tree(object):

    OPERATIONS = ["+", "-", "*", "/"]

    def __init__(self, value, left=None, right=None):
        # self.NODE_TYPE =
        self.value = value
        if (left and right):
            self.leftChild = left
            self.rightChild = right
        else:
            self.leftChild = None
            self.rightChild = None

    def __str__(self):
        if (type(self.value) is int or type(self.value) is float):
            return str(round(self.value, 2))
        elif (self.value == "x"):
            return self.value
        elif (self.value == "+" or self.value == "-" or self.value == "*" or self.value == "/"):
            return "(" + str(self.leftChild) + " " + self.value + " " + str(self.rightChild) + ")"
        else:
            return "CORNER CASE"

    def countNodes(self):
        stack = []
        stack.append(self)

        c = 0
        while (not stack):
            node = stack.pop()
            c += 1
            if (node.leftChild):
                stack.append(node.leftChild)
                stack.append(node.rightChild)
        return c

    def getRandomNode(self):
        r = random.randint(2, self.countNodes())
        parent, left, c, f = Tree.findNthNode(self, self, r)
        return parent, left

    def findNthNode(self, node, n, count=0):
        count += 1
        if (count == n):
            return None, None, count, True
        if (node.leftChild):
            parent, left, count, found = Tree.findNthNode(node.leftChild, n, count)
            if (found):
                if (parent):
                    return parent, left, count, found
                else:
                    return node, True, count, found
        if (node.rightChild):
            parent, left, count, found = Tree.findNthNode(node.rightChild, n, count)
            if (found):
                if (parent):
                    return parent, left, count, found
                else:
                    return node, False, count, found
        return None, None, count, False



def partialGrow(depth):
    if (depth > 0 and random.getrandbits(1)):
        newVal = random.choice(Tree.OPERATIONS)
        return Tree(newVal, partialGrow(depth - 1), partialGrow(depth - 1))
    else:
        if (random.getrandbits(1)):
            return Tree(random.randrange(1, 10))
        else:
            return Tree("x")


def fullGrow(depth):
    if (depth > 0):
        newVal = random.choice(Tree.OPERATIONS)
        return Tree(newVal, partialGrow(depth - 1), partialGrow(depth - 1))
    else:
        if (random.getrandbits(1)):
            return Tree(random.randrange(1, 10))
        else:
            return Tree("x")


def evaluate(tree, input):
    result = -1

    if (tree == None):
        result = 0
    else:
        if (type(tree.val) is str):
            if(tree.val == "x"):
                result = input
            else:
                operand1 = evaluate(tree.leftChild, input)
                operand2 = evaluate(tree.rightChild, input)
                result = compute(tree.value, operand1, operand2)
        else:
            result = tree.val
    return result


def compute(operator, operand1, operand2):
    if (operator == ("+")):
        result = operand1 + operand2 
    elif (operator == ("-")):
        result = operand1 - operand2
    elif (operator == ("*")):
        result = operand1 * operand2
    else:
        if (operand2 == 0):
            result = 0
        else:
            result = operand1 / operand2
    return result
