import random
import Mutation
from Practicas import ObjectiveFunction

def PointCrossover(parentsVector, mutationChance):
    children = []
    childrenScores = []
    parentIndex = 0

    OB = ObjectiveFunction.ObjectiveFunction()

    while parentIndex < len(parentsVector):
        crossPoint = random.randint(0, len(parentsVector[0]) - 1)

        parent1 = list(parentsVector[parentIndex])
        parent2 = list(parentsVector[parentIndex + 1])

        child1 = dict(parent1[:crossPoint] + parent2[crossPoint:])
        child2 = dict(parent2[:crossPoint] + parent1[crossPoint:])

        children.append(child1)
        children.append(child2)

        childrenScores.append(OB.CalculateSatisfaction(child1))
        childrenScores.append(OB.CalculateSatisfaction(child2))

        parentIndex += 2

    return children, childrenScores