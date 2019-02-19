import csv, sys, math, numpy, random, gp

from tree import Tree


OPS_1 = ["x", "+", "-", "*", "/"]

dataDict = []#dict()

testDict = []#dict()

errorDict = dict()

absoluteBest = math.inf
bestTree = None

def readData(filename, mode):
    global dataDict

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        try:
            if (mode == 1):
                lineCount = 0
                for row in reader:
                    if (lineCount >= 1 and lineCount < 20001):
                        dataDict.append((float (row[0]), float (row[1])))
                        # dataDict[(float) (row[0])] = (float) (row[1])
                    elif (lineCount >= 20001 and lineCount <= 25001):
                        testDict.append((float (row[0]), float (row[1])))
                        # testDict[(float) (row[0])] = (float) (row[1])
                    lineCount+=1
            # print("Experiment Dataset: ", len(dataDict))
            # print("Test Dataset: ", len(testDict))
            # print(dataDict[0][0])
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    dataDict = numpy.array(dataDict)
    # print(dataDict[:,1])


# should use ramped 1/2 & 1/2 with full and partial growth
def generatePopulation(size, startRange, endRange, ops):
    startPop = []
    for i in range(startRange, endRange+1):
        for j in range(0, 50):
            test = Tree(ops,None, i, 0)
            startPop.append(test)

            test2 = Tree(ops, None, i, 1)
            startPop.append(test2)

            # Create tree with partialGrow(i)
            # Append that to start pop
            # Create tree with fullGrow(i)
            # Append that to startPop
        # newTree = Tree(OPS_1)
        # startPop.append(newTree)
    # print(startPop[0])
    # temp = gp.fitness(startPop[0],ops,dataDict)
    return startPop

def selectTree(pop, ops):
    # print("select")

    global absoluteBest, bestTree

    k = 20#random.randrange(2,10)
    tournament = []
    errors = []

    for i in range(k):
        toAdd = random.choice(pop)
        tournament.append(toAdd)
        fitness = gp.fitness(toAdd, ops, dataDict)
        errors.append(fitness)

    localBest = errors.index(min(errors))
    localBestTree = tournament[localBest]

    if (localBest < absoluteBest):
        absoluteBest = localBest
        bestTree = localBestTree
    # SHOULD WE WATCH OUT FOR 0????
    return localBestTree

def newPop(pop,ops):
    newPop = []
    
    count = 0
    while (count < len(pop)):
        # print("newPop")

        parent1 = selectTree(pop,ops)
        parent2 = selectTree(pop, ops)
        child1, child2 = gp.cross(parent1, parent2)
        newPop.append(child1)
        newPop.append(child2)
        count += 1
    gp.mutate(newPop, 0.2, 1)
    return newPop

def runExperiment(filename, numGenerations, ops):
    global bestTree
    readData(filename,1)
    pop =  generatePopulation(5,2,6,1)
    
    gens = 0
    while(gens < numGenerations):
        pop = newPop(pop, ops)
        gens += 1
    
    print(bestTree)



def main():
    runExperiment("dataset1.csv", 1, 1)
    # readData("dataset1.csv",1)
    # generatePopulation(500,2,6,1)
    # print(dataDict[0])
    # Tree(l,l,)
    # test = Tree(1,None, 2, 0)
    # Tree.populate(test, 1, 0, 1)
    # print(str(test))

if __name__ == "__main__":
    main()