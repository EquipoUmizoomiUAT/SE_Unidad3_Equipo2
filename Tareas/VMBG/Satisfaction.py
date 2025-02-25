def GetSatisfaction(Vmin, Vmax, Vo, isMaximization):
    result = (Vmax - Vo) / (Vmax - Vmin)
    if isMaximization:
        result = 1 - result
    return result


def GetInputVector():
    inputVector = input("Ingresa el vector solucion T/H/R/IL\n").strip().split(',')

    if len(inputVector) != 4:
        exit("Vector Invalido")
    try:
        for i in range(len(inputVector)):
            inputVector[i] = int(inputVector[i])
    except ValueError:
        exit("Valores invalidos")

    return inputVector


if __name__ == '__main__':
    ranges = [
        16,     # TMin
        21,     # TMax
        40,     # HMin
        60,     # HMax
        0,      # NMin
        60,     # NMax
        100,    # LMin
        300     # LMax
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

    while True:
        solutions = GetInputVector()

        satisfaction = []

        i = 0
        for j in range(len(weights)):
            satisfaction.append(GetSatisfaction(ranges[i], ranges[i + 1], solutions[j], maximization[j]))
            i += 2

        satisfaction = [satisfaction[i] * weights[i] for i in range(len(weights))]

        print(f'Satisfaccion Total = {sum(satisfaction)}\n')
