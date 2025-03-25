import copy
import random
import EnergyConsumptionClase as Energy
import SatisfactionClase as Satisfaction

# Configuration for environmental parameters (temperature, humidity, noise, light)
config = {
    'temp': {
        'range': [18, 26],  # Preferred temperature range
        'weight': 0.25,  # Importance of temperature in overall satisfaction
        'changeCost': 5,  # Cost of changing the temperature
    },
    'humidity': {
        'range': [40, 60],  # Preferred humidity range
        'weight': 0.25,  # Importance of humidity in overall satisfaction
        'changeCost': 5,  # Cost of changing the humidity
    },
    'noise': {
        'range': [0, 60],  # Preferred noise level range
        'weight': 0.25,  # Importance of noise level in overall satisfaction
        'changeCost': 5,  # Cost of changing the noise level
    },
    'light': {
        'range': [200, 500],  # Preferred light intensity range
        'weight': 0.25,  # Importance of light intensity in overall satisfaction
        'changeCost': 5,  # Cost of changing the light intensity
    },
}

# Weights for satisfaction and energy gain in the objective function
alpha = 0.75  # Weight for satisfaction
beta = 0.25   # Weight for energy gain

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