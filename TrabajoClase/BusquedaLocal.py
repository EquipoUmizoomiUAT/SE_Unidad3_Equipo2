import random


def objectiveFunction(solution):
    score = 0
    for e in solution:
        score += e ** 2
    return score


def vecindario(solution, min, max):
    '''
    max = -1
    min = 99999
    for e in solution:
        max = e if e > max else max
        min = e if e < min else min
    '''
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.randint(min, max)
    return solution


if __name__ == '__main__':
    initialSolution = [3, 1, 2, 5, 4]
    xMin = -10
    xMax = 10
    sBest = initialSolution
    vBest = objectiveFunction(initialSolution)
    iterations = 0
    while iterations < 100 and vBest != 0:
        newSolution = vecindario(initialSolution[:], xMin, xMax)
        vNewSolution = objectiveFunction(newSolution)
        if vNewSolution < vBest:
            vBest = vNewSolution
            sBest = newSolution
        initialSolution = newSolution
        print(f'Solution = {initialSolution}')
        print(f'VBest = {vBest}')
        print(f'sBest = {sBest}')
        iterations += 1
