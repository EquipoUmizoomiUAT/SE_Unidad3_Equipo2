import copy
import random
import EnergyConsumptionClase as Energy
import SatisfactionClase as Satisfaction

maxLocalSearchIterations = 1000
maxIteratedLocalSearchIterations = 100
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
alpha = 0.5
beta = 0.5
energy = Energy.Energy(config)
satisfaction = Satisfaction.Satisfaction(config)


def ObjectiveFunction(solution):
    energyGain = energy.GetEnergyConsumptionGain(solution)
    satisfactionValue = satisfaction.GetUserSatisfaction(solution)
    totalScore = satisfactionValue * alpha + beta * energyGain
    return totalScore


def NeighborSolution(solution):
    service = random.choice(list(solution.keys()))
    minimum, maximum = config[service]['range']
    newPrediction = random.randint(minimum, maximum)
    solution[service]['OptValue'] = newPrediction
    return solution


def Perturbation(solution):
    for service in solution.keys():
        minimum, maximum = config[service]['range']
        oldValue = solution[service]['OptValue']
        newValue = oldValue + random.randint(-10, 10)
        if newValue > maximum:
            newValue = maximum
        if newValue < minimum:
            newValue = minimum
        solution[service]['OptValue'] = newValue
    return solution


def CreateSolution():
    solution = {
        'temp': {
            'IsMaximization': False,  # Temperature should be minimized
            'RealValue': 15,  # Current real temperature value
            'OptValue': random.randint(config['temp']['range'][0], config['temp']['range'][1]),  # Desired optimal temperature value
        },
        'humidity': {
            'IsMaximization': False,  # Humidity should be minimized
            'RealValue': 70,  # Current real humidity value
            'OptValue': random.randint(config['humidity']['range'][0], config['humidity']['range'][1]),  # Desired optimal humidity value
        },
        'noise': {
            'IsMaximization': False,  # Noise level should be minimized
            'RealValue': 82,  # Current real noise level value
            'OptValue': random.randint(config['noise']['range'][0], config['noise']['range'][1]),  # Desired optimal noise level value
        },
        'light': {
            'IsMaximization': True,  # Light intensity should be maximized
            'RealValue': 132,  # Current real light intensity value
            'OptValue': random.randint(config['light']['range'][0], config['light']['range'][1]),  # Desired optimal light intensity value
        }
    }
    return solution


if __name__ == '__main__':
    initialSolution = CreateSolution()
    sBest = copy.deepcopy(initialSolution)
    vBest = ObjectiveFunction(initialSolution)

    localSearchIterations = 0
    iteratedLocalSearchIterations = 0


    while iteratedLocalSearchIterations < maxIteratedLocalSearchIterations:
        while localSearchIterations < maxLocalSearchIterations and vBest != 1:
            newSolution = NeighborSolution(copy.deepcopy(sBest))
            vNewSolution = ObjectiveFunction(newSolution)
            if vNewSolution > vBest:
                vBest = vNewSolution
                sBest = copy.deepcopy(newSolution)
            localSearchIterations += 1

        tempSolution = Perturbation(newSolution)
        vNewSolution = ObjectiveFunction(tempSolution)
        if vNewSolution > vBest:
            vBest = vNewSolution
            sBest = copy.deepcopy(newSolution)
        print(f"Iteration {localSearchIterations}:")
        for service, values in sBest.items():
            print(f"  {service}: OptValue = {values['OptValue']}")
        print(f"  Objective Function Score: {vBest}\n")
        iteratedLocalSearchIterations += 1
