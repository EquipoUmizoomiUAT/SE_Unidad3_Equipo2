import math
import random as rnd

xMin = -10
xMax = 10


def CreateRandomSolution(n):
    v = [rnd.randint(xMin, xMax) for i in range(n)]
    return v


def NeighborSolution(solution):
    vector = solution[:]
    index = rnd.randint(0, len(solution) - 1)
    newValue = rnd.randint(xMin, xMax)
    vector[index] = newValue
    return vector


def ObjectiveFunction(solution):
    vo = sum([i ** 2 for i in solution])
    return vo


if __name__ == '__main__':
    initialSolution = CreateRandomSolution(5)
    bestSolution = initialSolution
    bestValue = ObjectiveFunction(bestSolution)
    temperature = 100
    umbral = 2
    maxIterations = 250
    alpha = 0.8
    iterations = 0
    while temperature > umbral:
        iterations += 1
        auxiliarSolution = bestSolution
        tempSolution = bestSolution
        tempValue = ObjectiveFunction(tempSolution)
        for k in range(maxIterations):
            auxiliarSolution = NeighborSolution(auxiliarSolution)
            objValue = ObjectiveFunction(auxiliarSolution)
            difference = objValue - tempValue
            if difference < 0:
                tempSolution = auxiliarSolution
                tempValue = objValue
            else:
                i = rnd.uniform(0, 1)
                if i < math.exp(difference / temperature):
                    tempSolution = auxiliarSolution
            temperature = temperature * alpha
        if tempValue < bestValue:
            bestSolution = tempSolution
            bestValue = tempValue

    print(f"T: {temperature}")
    print(f"Best Solution: {bestSolution}")
    print(f"Best Value: {bestValue}")
    print(f"Number of Iterations: {iterations}")