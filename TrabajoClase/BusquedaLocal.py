import random

rangeMax = 10
rangeMin = -10
maxIterations = 1000


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
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.randint(rangeMin, rangeMax)
    return solution


def CreateSolution(n):
    return [random.randint(rangeMin, rangeMax) for i in range(n)]


if __name__ == '__main__':
    initialSolution = CreateSolution(5)
    sBest = initialSolution[:]
    vBest = objectiveFunction(initialSolution)

    iterations = 0

    while iterations < maxIterations and vBest != 0:
        newSolution = vecindario(sBest[:])
        vNewSolution = objectiveFunction(newSolution)
        if vNewSolution < vBest:
            vBest = vNewSolution
            sBest = newSolution[:]
        print(f'Iteracion {iterations} Best = {sBest}\t con vo = {vBest}')
        iterations += 1
