import random

rangeMax = 10
rangeMin = -10
maxIterations = 10000
maxILSit = 100


def objectiveFunction(solution):
    score = 0
    for e in solution:
        score += e ** 2
    return score


def vecindario(solution):
    '''
    max = -1
    min = 99999
    for e in solution:
        max = e if e > max else max
        min = e if e < min else min
    '''
    vector = solution[:]
    index = random.randint(0, len(vector) - 1)
    vector[index] = random.randint(rangeMin, rangeMax)
    return vector


def perturbacion(solution):
    vector = solution[:]
    index = random.randint(0, len(vector) - 1)
    index2 = index
    while index2 == index:
        index2 = random.randint(0, len(vector) - 1)
    vector[index] = random.randint(rangeMin, rangeMax)
    vector[index2] = random.randint(rangeMin, rangeMax)
    return vector


def CreateSolution(n):
    return [random.randint(rangeMin, rangeMax) for i in range(n)]


if __name__ == '__main__':
    initialSolution = CreateSolution(5)
    tempSolution = initialSolution[:]
    vBest = objectiveFunction(initialSolution)

    itLocal = 0
    itILS = 0

    while itILS < maxILSit:

        while itLocal < maxIterations and vBest != 0:
            tempSolution = vecindario(tempSolution)
            vTempSolution = objectiveFunction(tempSolution)

            if vTempSolution < vBest:
                vBest = vTempSolution
                tempSolution = tempSolution[:]

            #print(f'\t\tIteracion {itLocal} S = {tempSolution}\t con vo = {vTempSolution}')
            itLocal += 1

        tempSolution = perturbacion(tempSolution)
        vTempSolution = objectiveFunction(tempSolution)
        if vTempSolution < vBest:
            vBest = vTempSolution
            tempSolution = tempSolution[:]
        print(f'IteracionILS {itILS} S = {tempSolution}\t con vo = {vTempSolution}')
        itILS += 1
