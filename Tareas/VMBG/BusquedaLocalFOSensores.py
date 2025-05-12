import copy  # Used for creating deep copies of dictionaries
import random  # Used for generating random numbers
from TrabajoClase import EnergyConsumptionClase as Energy  # Custom class for calculating energy consumption
from TrabajoClase import SatisfactionClase as Satisfaction  # Custom class for calculating user satisfaction

maxIterations = 1000  # Maximum number of iterations for the optimization loop

# Configuration dictionary for environmental parameters
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

alpha = 0.75  # Weight for satisfaction in the objective function
beta = 0.25  # Weight for energy gain in the objective function

# Instantiate Energy and Satisfaction classes using the configuration
energy = Energy.Energy(config)
satisfaction = Satisfaction.Satisfaction(config)


def ObjectiveFunction(solution):
    """
    Calculates the objective function score based on energy gain and user satisfaction.

    Args:
        solution (dict): The current solution (environmental parameter settings).

    Returns:
        float: The total objective function score.
    """
    energyGain = energy.GetEnergyConsumptionGain(solution)  # Calculate energy gain
    satisfactionValue = satisfaction.GetUserSatisfaction(solution)  # Calculate user satisfaction
    totalScore = satisfactionValue * alpha + beta * energyGain  # Combine satisfaction and energy gain with weights
    return totalScore


def NeighborSolution(solution):
    """
    Generates a neighboring solution by randomly changing one parameter.

    Args:
        solution (dict): The current solution.

    Returns:
        dict: The neighboring solution.
    """
    service = random.choice(list(solution.keys()))  # Randomly choose a service (parameter) to modify
    minimum, maximum = config[service]['range']  # Get the range of allowed values for the chosen service
    newPrediction = random.uniform(minimum, maximum)  # Generate a new random value within the range
    solution[service]['OptValue'] = newPrediction  # Update the solution with the new value
    return solution


def CreateSolution():
    """
    Creates an initial random solution.

    Returns:
        dict: The initial solution.
    """
    solution = {
        'temp': {
            'IsMaximization': False,  # Temperature should be minimized
            'RealValue': 15,  # Current real temperature value
            'OptValue': random.uniform(config['temp']['range'][0], config['temp']['range'][1]),  # Randomly initialize optimal temperature
        },
        'humidity': {
            'IsMaximization': False,  # Humidity should be minimized
            'RealValue': 70,  # Current real humidity value
            'OptValue': random.uniform(config['humidity']['range'][0], config['humidity']['range'][1]),  # Randomly initialize optimal humidity
        },
        'noise': {
            'IsMaximization': False,  # Noise level should be minimized
            'RealValue': 82,  # Current real noise level value
            'OptValue': random.uniform(config['noise']['range'][0], config['noise']['range'][1]),  # Randomly initialize optimal noise level
        },
        'light': {
            'IsMaximization': True,  # Light intensity should be maximized
            'RealValue': 132,  # Current real light intensity value
            'OptValue': random.uniform(config['light']['range'][0], config['light']['range'][1]),  # Randomly initialize optimal light intensity
        }
    }
    return solution


if __name__ == '__main__':
    initialSolution = CreateSolution()  # Create an initial random solution
    sBest = copy.deepcopy(initialSolution)  # Initialize the best solution with the initial solution
    vBest = ObjectiveFunction(initialSolution)  # Calculate the objective function value of the initial solution
    newSolution = copy.deepcopy(initialSolution)

    iterations = 0  # Initialize iteration counter

    # Main optimization loop
    while iterations < maxIterations and vBest != 1:  # Continue until max iterations or perfect score is reached
        newSolution = NeighborSolution(copy.deepcopy(newSolution))  # Generate a neighboring solution
        vNewSolution = ObjectiveFunction(newSolution)  # Calculate the objective function value of the new solution

        # Update the best solution if the new solution is better
        if vNewSolution > vBest:
            vBest = vNewSolution
            sBest = copy.deepcopy(newSolution)

            # Print the current iteration's best solution and score
            print(f"Iteration {iterations}:")
            for service, values in sBest.items():
                print(f"  {service}: OptValue = {values['OptValue']}")
            print(f"  Objective Function Score: {vBest}\n")

        iterations += 1  # Increment iteration counter

    # Print the final best solution and score
    print(f"Final Iteration: {iterations}:")
    for service, values in sBest.items():
        print(f"  {service}: OptValue = {values['OptValue']}")
    print(f" Best Objective Function Score: {vBest}\n")