import csv, sys, math, numpy, random, gp

from tree import Tree


OPS_1 = ["x", "+", "-", "*", "/"]

dataDict = dict()

errorDict = dict()

absoluteBest = math.inf
bestTree = None

def readData(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        try:
            lineCount = 0
            for row in reader:
                if (lineCount != 0):
                    dataDict[(float) (row[0])] = (float) (row[1])
                lineCount+=1
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


# should use ramped 1/2 & 1/2 with full and partial growth
def generatePopulation(popSize):
    startPop = []
    for i in range(popSize):
        newTree = Tree(OPS_1)
        startPop.append(newTree)
    return startPop
    # readData(file)

def selectTree(pop):
    global absoluteBest, bestTree

    k = random.randrange(2,10)
    tournament = []
    errors = []

    for i in range(k):
        toAdd = random.choice(pop)
        tournament.append(toAdd)
        fitness = gp.howFit(toAdd, dataDict)
        errors.append(fitness)

    localBest = errors.index(min(errors))
    localBestTree = tournament[localBest]

    if (localBest < absoluteBest):
        absoluteBest = localBest
        bestTree = localBestTree
    return localBestTree

def newPop(pop):
    newPop = []
    
    count = 0
    while (count < len(pop)):
        parent1 = selectTree(pop)
        parent2 = selectTree(pop)
        child1, child2 = gp.cross(parent1, parent2)
        newPop.append(child1)
        newPop.append(child2)
        count += 1
    gp.mutate(newPop, 0.2, 1)
    return newPop

def runExperiment(filename, numGenerations):
    global bestTree
    readData(filename)
    pop = generatePopulation(100)
    
    gens = 0
    while(gens < numGenerations):
        pop = newPop(pop)
        gens += 1
    
    print(bestTree)



def main():
    runExperiment("dataset1.csv", 50)

if __name__ == "__main__":
    main()