def GetSatisfaction(Vmin, Vmax, Vo, isMaximization):
    result = (Vmax - Vo) / (Vmax - Vmin)
    if isMaximization:
        result = 1 - result
    return result


def GetInputVector():
    inputVector = input("Ingresa el vector solucion T/H/R/IL\n")
    if inputVector == 'exit':
        exit('Program Terminated')
    else:
        inputVector = inputVector.strip().split(',')
    if len(inputVector) != 4:
        exit("Vector Invalido")
    try:
        print('Parseando vector...')
        for i in range(len(inputVector)):
            inputVector[i] = int(inputVector[i])
    except ValueError:
        exit("Valores invalidos")

    return inputVector


def GetMinimizationEnergyCost(cost, currentValue, desiredValue):
    return cost + cost * (currentValue - desiredValue) if currentValue >= desiredValue else 0


def GetMaximizationEnergyCost(cost, currentValue, desiredValue):
    return cost + cost * (desiredValue - currentValue) if currentValue <= desiredValue else 0


if __name__ == '__main__':
    alpha = 0.5
    beta = 0.5
    ranges = [
        16,   # TMin
        21,   # TMax
        40,   # HMin
        60,   # HMax
        0,    # NMin
        60,   # NMax
        100,  # LMin
        300   # LMax
    ]

    weights = [
        0.35,
        0.25,
        0.25,
        0.15
    ]

    maximization = [
        False,
        False,
        False,
        True
    ]

    costPerUnitOfChange = [
        25,
        30,
        50,
        5
    ]

    # solutions = GetInputVector()
    currentValues = [23, 65, 56, 98]
    solutions = [20, 55, 12, 252]

    satisfaction = []

    i = 0
    print("Calculando satisfaccion de servicios...")
    for j in range(len(weights)):
        satisfaction.append(GetSatisfaction(ranges[i], ranges[i + 1], solutions[j], maximization[j]))
        i += 2

    print("Calculando satisfaccion total...")
    satisfaction = [satisfaction[i] * weights[i] for i in range(len(weights))]

    print(f'Satisfaccion Total = {round(sum(satisfaction), 5)}\n')

    energyCosts = []
    gain = 0
    rangesIndex = 0
    for i in range(len(costPerUnitOfChange)):
        if maximization[i]:
            pass
            energyPredicted = GetMaximizationEnergyCost(costPerUnitOfChange[i], currentValues[i], solutions[i])
            energyMin = GetMaximizationEnergyCost(costPerUnitOfChange[i], currentValues[i], ranges[rangesIndex])
            energyMax = GetMaximizationEnergyCost(costPerUnitOfChange[i], currentValues[i], ranges[rangesIndex + 1])
        else:
            energyPredicted = GetMinimizationEnergyCost(costPerUnitOfChange[i], currentValues[i], solutions[i])
            energyMax = GetMinimizationEnergyCost(costPerUnitOfChange[i], currentValues[i], ranges[rangesIndex])
            energyMin = GetMinimizationEnergyCost(costPerUnitOfChange[i], currentValues[i], ranges[rangesIndex + 1])
        rangesIndex += 2
        energyCosts.append(round(1 - (energyMax - energyPredicted) / (energyMax - energyMin), 5))
        gain += energyCosts[i] * weights[i]
    print('Costos de Energia', energyCosts)
    print('Ganancia:', round(gain, 5))
    fo = round(sum(satisfaction) * alpha + gain * beta, 5)
    print('Fo:', fo)
