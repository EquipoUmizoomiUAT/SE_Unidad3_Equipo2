import random
import random as rnd

# rnd.seed(5)
xMin = -10
xMax = 10


def NeighborSolution(solution):
    vector = solution[:]
    index = rnd.randint(0, len(solution) - 1)
    newValue = rnd.randint(xMin, xMax)
    vector[index] = newValue
    return vector


def ObjectiveFunction(solution):
    vo = sum([i ** 2 for i in solution])
    return vo


def CreateRandomSolution(n):
    v = [rnd.randint(xMin, xMax) for i in range(n)]
    return v


def Perturbation(solution):
    newVector = []
    for e in solution:
        newElement = e + random.randint(xMin, xMax)
        newElement = xMin if newElement < xMin else newElement
        newElement = xMax if newElement > xMax else newElement
        newVector.append(newElement)
    return newVector


if __name__ == "__main__":
    print("Inicia algoritmo:")
    tempSolution = CreateRandomSolution(5)  # S0
    print("solucion temporal: ", tempSolution)
    bestSolution = tempSolution[:]  # copia de los valores
    bestVO = ObjectiveFunction(bestSolution)
    print("solucion vo inicial: ", bestVO)

    maxIT_ILS = 100  # iterated local search = ils
    it_ILS = 0

    maxIT_LS = 10000
    it_LS = 0

    while it_ILS < maxIT_ILS:  # busqueda local iterada

        while it_LS < maxIT_LS:  # busqueda local
            tempSolution = NeighborSolution(tempSolution)
            tempVO = ObjectiveFunction(tempSolution)

            if tempVO < bestVO:
                bestVO = tempVO
                bestSolution = tempSolution[:]
                print("nueva best solucion: ", tempSolution, end="    ")
                print("vo: ", tempVO)

            # print("it", end="   ")
            # print("solucion: ", solucion_temporal, end="    ")
            # print("vo: ", vo_temporal)
            it_LS += 1

        tempSolution = Perturbation(tempSolution)
        tempVO = ObjectiveFunction(tempSolution)
        if tempVO < bestVO:
            bestVO = tempVO
            bestSolution = tempSolution[:]
            print("nueva best solucion: ", tempSolution, end="    ")
            print("vo: ", tempVO)
        it_ILS += 1

    print("mejor solucion: ", bestSolution)
    print("mejor vo: ", bestVO)

    # soft and hard constrainst
