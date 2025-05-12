import copy
import random
from .. import EnergySatisfacion as Energy
from .. import ServiceSatisfacion as Satisfaction

# Define the maximum number of iterations for local search and iterated local search
maxLocalSearchIterations = 1000
maxIteratedLocalSearchIterations = 100

# Configuration for environmental parameters (temperature, humidity, noise, light)
config = {
    'temp': {
        'range': [18, 26],  # Preferred temperature range
        'weight': 0.70,  # Importance of temperature in overall satisfaction
        'changeCost': 5,  # Cost of changing the temperature
    },
    'humidity': {
        'range': [40, 60],  # Preferred humidity range
        'weight': 0.10,  # Importance of humidity in overall satisfaction
        'changeCost': 5,  # Cost of changing the humidity
    },
    'noise': {
        'range': [0, 60],  # Preferred noise level range
        'weight': 0.04,  # Importance of noise level in overall satisfaction
        'changeCost': 5,  # Cost of changing the noise level
    },
    'light': {
        'range': [200, 500],  # Preferred light intensity range
        'weight': 0.16,  # Importance of light intensity in overall satisfaction
        'changeCost': 5,  # Cost of changing the light intensity
    },
}

tabooLibrary = dict()
tabooTime = 2

# Weights for satisfaction and energy gain in the objective function
alpha = 0.60  # Weight for satisfaction
beta = 0.40   # Weight for energy gain

# Initialize energy consumption and satisfaction classes with the given configuration
energy = Energy.Energy(config)
satisfaction = Satisfaction.Satisfaction(config)

# Objective function to evaluate a solution
def ObjectiveFunction(solution):
    """
    Calculates the total score of a solution based on energy gain and user satisfaction.
    """
    energyGain = energy.GetEnergyConsumptionGain(solution) #Calculate Energy gain
    satisfactionValue = satisfaction.GetUserSatisfaction(solution) #Calculate user satisfaction
    totalScore = satisfactionValue * alpha + beta * energyGain #Combine satisfaction and energy gain
    return totalScore

# Generate a neighbor solution by randomly changing one parameter
def NeighborSolution(solution):
    """
    Creates a neighboring solution by randomly changing the optimal value of one service.
    """
    service = random.choice(list(solution.keys())) #Choose a random service (temp, humidity, etc.)
    while service in tabooLibrary:
        service = random.choice(list(solution.keys()))  # Choose a random service (temp, humidity, etc.)
    minimum, maximum = config[service]['range'] #Get the range of the chosen service
    newPrediction = random.uniform(minimum, maximum) #Generate a new random value within the range
    solution[service]['OptValue'] = newPrediction #Update the optimal value in the solution
    return solution, service

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

# Main execution block
if __name__ == '__main__':
    initialSolution = CreateSolution() #Create an initial random solution
    sBest = copy.deepcopy(initialSolution) #Copy the initial solution to the best solution
    vBest = ObjectiveFunction(initialSolution) #Calculate the objective function value of the initial solution
    newSolution = copy.deepcopy(initialSolution)
    localSearchIterations = 0
    iteratedLocalSearchIterations = 0

    # Main loop for iterated local search
    while iteratedLocalSearchIterations < maxIteratedLocalSearchIterations:
        # Local search loop
        while localSearchIterations < maxLocalSearchIterations and vBest != 1: #Continue local search until max iterations or optimal solution
            newSolution, updatedService = NeighborSolution(newSolution) #Generate a neighbor solution
            vNewSolution = ObjectiveFunction(newSolution) #Calculate the objective function value of the neighbor solution
            if vNewSolution > vBest: #If the neighbor solution is better, update the best solution
                tabooLibrary[updatedService] = tabooTime + 1
                vBest = vNewSolution
                sBest = copy.deepcopy(newSolution)
            tabooCopy = tabooLibrary.copy()
            for service, serviceTabooTime in tabooLibrary.items():
                serviceTabooTime -= 1
                if serviceTabooTime == 0:
                    del tabooCopy[service]
                else:
                    tabooCopy[service] = serviceTabooTime
            tabooLibrary = tabooCopy.copy()
            localSearchIterations += 1


        # Perturbation step
        newSolution = Perturbation(newSolution)
        vNewSolution = ObjectiveFunction(newSolution)
        if vNewSolution > vBest:
            vBest = vNewSolution
            sBest = copy.deepcopy(newSolution)

        # Print the current iteration's results
        print(f"Iteration {iteratedLocalSearchIterations}:")
        for service, values in sBest.items():
            print(f"  {service}: OptValue = {values['OptValue']}")
        print(f"  Objective Function Score: {vBest}\n")
        iteratedLocalSearchIterations += 1

    # Print the final results
    print(f"Final Iteration: {iteratedLocalSearchIterations}:")
    for service, values in sBest.items():
        print(f"  {service}: OptValue = {values['OptValue']}")
    print(f" Best Objective Function Score: {vBest}\n")