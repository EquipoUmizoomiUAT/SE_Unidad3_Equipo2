import random
from Practicas.Practica6_GA import Mutation
from Practicas import ObjectiveFunction

def PointCrossover(parentsVector, mutationChance):
    children = []
    childrenScores = []
    parentIndex = 0

    OB = ObjectiveFunction.ObjectiveFunction()

    while parentIndex < len(parentsVector):
        crossPoint = random.randint(0, len(parentsVector[0]) - 1)

        testo = parentsVector[parentIndex]

        parent1 = list(parentsVector[parentIndex].items())
        parent2 = list(parentsVector[parentIndex + 1].items())

        child1 = dict(parent1[:crossPoint] + parent2[crossPoint:])
        child2 = dict(parent2[:crossPoint] + parent1[crossPoint:])

        children.append(child1)
        children.append(child2)

        scoreChild1, *_ = OB.CalculateSatisfaction(child1)
        scoreChild2, *_ = OB.CalculateSatisfaction(child2)

        childrenScores.append(scoreChild1)
        childrenScores.append(scoreChild2)

        parentIndex += 2

    return children, childrenScores