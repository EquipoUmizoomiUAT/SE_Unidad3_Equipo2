import random

rangeMax = 10
rangeMin = -10
maxIterations = 1000


def ObjectiveFunction(solution):
    score = 0
    for e in solution:
        score += e ** 2
    return score


def Vecindario(solution):
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
    config = {
        'temp': {
            'range': [18, 26],  # Preferred temperature range
            'weight': 0.25,  # Importance of temperature in the overall satisfaction
            'changeCost': 5,  # Cost of changing the temperature
        },
        'humidity': {
            'range': [40, 60],  # Preferred humidity range
            'weight': 0.25,  # Importance of humidity in the overall satisfaction
            'changeCost': 5,  # Cost of changing the humidity
        },
        'noise': {
            'range': [0, 60],  # Preferred noise level range
            'weight': 0.25,  # Importance of noise level in the overall satisfaction
            'changeCost': 5,  # Cost of changing the noise level
        },
        'light': {
            'range': [200, 500],  # Preferred light intensity range
            'weight': 0.25,  # Importance of light intensity in the overall satisfaction
            'changeCost': 5,  # Cost of changing the light intensity
        },
    }

    # Dynamic solution: These values are expected to change frequently
    initialSolution = {
        'temp': {
            'IsMaximization': False,  # Temperature should be minimized
            'RealValue': 15,  # Current real temperature value
            'OptValue': 23,  # Desired optimal temperature value
        },
        'humidity': {
            'IsMaximization': False,  # Humidity should be minimized
            'RealValue': 70,  # Current real humidity value
            'OptValue': 48,  # Desired optimal humidity value
        },
        'noise': {
            'IsMaximization': False,  # Noise level should be minimized
            'RealValue': 82,  # Current real noise level value
            'OptValue': 29,  # Desired optimal noise level value
        },
        'light': {
            'IsMaximization': True,  # Light intensity should be maximized
            'RealValue': 132,  # Current real light intensity value
            'OptValue': 357,  # Desired optimal light intensity value
        }
    }
    sBest = initialSolution[:]
    vBest = ObjectiveFunction(initialSolution)

    iterations = 0

    while iterations < maxIterations and vBest != 0:
        newSolution = Vecindario(sBest[:])
        vNewSolution = ObjectiveFunction(newSolution)
        if vNewSolution < vBest:
            vBest = vNewSolution
            sBest = newSolution[:]
        print(f'Iteracion {iterations} Best = {sBest}\t con vo = {vBest}')
        iterations += 1
