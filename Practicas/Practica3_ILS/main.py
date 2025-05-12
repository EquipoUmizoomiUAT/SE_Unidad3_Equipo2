import copy
import random
from .. import ObjectiveFunction, GlobalConfig

rangeMax = 10
rangeMin = -10
maxIterations = 1000
maxILSIterations = 1000
config = GlobalConfig.GetGlobalConfig()

# Generate a neighbor solution by randomly changing one parameter
def NeighborSolution(solution):
    """
    Creates a neighboring solution by randomly changing the optimal value of one service.
    """
    service = random.choice(list(solution.keys())) #Choose a random service (temp, humidity, etc.)
    minimum, maximum = config[service]['range'] #Get the range of the chosen service
    newPrediction = random.uniform(minimum, maximum) #Generate a new random value within the range
    solution[service]['OptValue'] = newPrediction #Update the optimal value in the solution
    return solution


# Perturb a solution by randomly changing all parameters
def Perturbation(solution):
    """
    Perturbs a solution by randomly changing the optimal value of all services.
    """
    for service in solution.keys(): #Loop through all services
        minimum, maximum = config[service]['range'] #Get the range of the service
        oldValue = solution[service]['OptValue'] #Get the old optimal value
        newValue = oldValue + random.uniform(-10, 10) #Generate a new value by adding a random offset
        if newValue > maximum: #Ensure the new value is within the range
            newValue = maximum
        if newValue < minimum:
            newValue = minimum
        solution[service]['OptValue'] = newValue #Update the optimal value in the solution
    return solution


# Create an initial solution with random optimal values
def CreateSolution():
    """
    Creates an initial solution with random optimal values for each service.
    """
    solution = {
        'temp': {
            'IsMaximization': False,  # Temperature should be minimized
            'RealValue': 15,  # Current real temperature value
            'OptValue': random.uniform(config['temp']['range'][0], config['temp']['range'][1]),  # Desired optimal temperature value
        },
        'humidity': {
            'IsMaximization': False,  # Humidity should be minimized
            'RealValue': 70,  # Current real humidity value
            'OptValue': random.uniform(config['humidity']['range'][0], config['humidity']['range'][1]),  # Desired optimal humidity value
        },
        'noise': {
            'IsMaximization': False,  # Noise level should be minimized
            'RealValue': 82,  # Current real noise level value
            'OptValue': random.uniform(config['noise']['range'][0], config['noise']['range'][1]),  # Desired optimal noise level value
        },
        'light': {
            'IsMaximization': True,  # Light intensity should be maximized
            'RealValue': 132,  # Current real light intensity value
            'OptValue': random.uniform(config['light']['range'][0], config['light']['range'][1]),  # Desired optimal light intensity value
        }
    }
    return solution



if __name__ == '__main__':
    initialSolution = CreateSolution()
    OB = ObjectiveFunction.ObjectiveFunction()

    tempSolution = copy.deepcopy(initialSolution)
    vBest = OB.CalculateSatisfaction(initialSolution)

    iterations = 0
    itILS = 0

    while itILS < maxILSIterations:
        while iterations < maxIterations and vBest != 0:
            tempSolution = NeighborSolution(copy.deepcopy(tempSolution))
            vTempSolution = OB.CalculateSatisfaction(tempSolution)
            if vTempSolution < vBest:
                vBest = vTempSolution
                tempSolution = copy.deepcopy(tempSolution)
            iterations += 1
    tempSolution = Perturbation(copy.deepcopy(tempSolution))
    vTempSolution = OB.CalculateSatisfaction(tempSolution)
    if vTempSolution < vBest:
        vBest = vTempSolution
        tempSolution = copy.deepcopy(tempSolution)

    print(f'Iteracion {iterations} Best = {tempSolution}\t con vo = {vTempSolution}')
    itILS += 1
