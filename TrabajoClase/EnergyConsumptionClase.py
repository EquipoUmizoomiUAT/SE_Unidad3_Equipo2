def GetMinEnergyCost(cost, currentValue, desiredValue):
    """
    Calculates the energy cost when the current value is above the desired value.

    Args:
        cost (float): The base cost of changing the value.
        currentValue (float): The current value of the service.
        desiredValue (float): The desired value of the service.

    Returns:
        float: The total energy cost if the current value is above the desired value;
               otherwise, returns 0.
    """
    totalCost = cost + cost * (currentValue - desiredValue) if currentValue >= desiredValue else 0
    return totalCost


def GetMaxEnergyCost(cost, currentValue, desiredValue):
    """
    Calculates the energy cost when the current value is below the desired value.

    Args:
        cost (float): The base cost of changing the value.
        currentValue (float): The current value of the service.
        desiredValue (float): The desired value of the service.

    Returns:
        float: The total energy cost if the current value is below the desired value;
               otherwise, returns 0.
    """
    totalCost = cost + cost * (desiredValue - currentValue) if currentValue <= desiredValue else 0
    return totalCost


class Energy:
    # Class attributes to store preferences and the current solution
    preferences = None  # Stores the preferred ranges, weights, and costs for each service
    solution = None  # Stores the current real values, optimal values, and optimization goals for each service

    def __init__(self, preferences):
        """
        Initializes the Energy class with the given preferences.

        Args:
            preferences (dict): A dictionary containing the preferred ranges, weights,
                                and change costs for each service.
        """
        self.preferences = preferences

    def SetSolution(self, newSolution):
        """
        Updates the current solution with a new solution.

        Args:
            newSolution (dict): A dictionary containing the new real values, optimal values,
                               and optimization goals for each service.
        """
        self.solution = newSolution

    def GetEnergyConsumptionGain(self, newSolution):
        """
        Calculates the energy consumption satisfaction based on the new solution.

        Args:
            newSolution (dict): A dictionary containing the new real values, optimal values,
                                and optimization goals for each service.

        Returns:
            float: The total energy consumption satisfaction score, which is the sum of
                   individual energy consumption scores for all services, weighted by their importance.
        """
        # Update the current solution with the new solution
        self.SetSolution(newSolution)
        energyGain = 0  # Initialize the total energy gain/satisfaction score

        # Iterate over each service in the solution
        for service in self.solution.keys():
            # Extract the cost, real value, desired value, and range for the current service
            cost = self.preferences[service]['changeCost']
            realValue = self.solution[service]['RealValue']
            desiredValue = self.solution[service]['OptValue']
            minValue = self.preferences[service]['range'][0]
            maxValue = self.preferences[service]['range'][1]

            # Calculate energy costs based on whether the service should be maximized or minimized
            if self.solution[service]['IsMaximization']:
                # Calculate energy costs for maximization
                energyObjective = GetMaxEnergyCost(cost, realValue, desiredValue)
                energyMin = GetMaxEnergyCost(cost, realValue, minValue)
                energyMax = GetMaxEnergyCost(cost, realValue, maxValue)
            else:
                # Calculate energy costs for minimization
                energyObjective = GetMinEnergyCost(cost, realValue, desiredValue)
                energyMin = GetMinEnergyCost(cost, realValue, maxValue)
                energyMax = GetMinEnergyCost(cost, realValue, minValue)
            try:
                # Calculate the normalized energy consumption satisfaction score
                energyConsumption = round(1 - (energyMax - energyObjective) / (energyMax - energyMin), 5)
            except ZeroDivisionError:
                energyConsumption = 0

            # Apply the service's weight to the energy consumption score
            energyConsumption *= self.preferences[service]['weight']
            # Add the weighted score to the total energy gain
            energyGain += energyConsumption

        return energyGain

"""
if __name__ == "__main__":
    # Static preferences: These values are not expected to change often
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
    solution = {
        'temp': {
            'IsMaximization': False,  # Temperature should be minimized
            'RealValue': 15,  # Current real temperature value
            'OptValue': 18,  # Desired optimal temperature value
        },
        'humidity': {
            'IsMaximization': False,  # Humidity should be minimized
            'RealValue': 70,  # Current real humidity value
            'OptValue': 40,  # Desired optimal humidity value
        },
        'noise': {
            'IsMaximization': False,  # Noise level should be minimized
            'RealValue': 82,  # Current real noise level value
            'OptValue': 0,  # Desired optimal noise level value
        },
        'light': {
            'IsMaximization': True,  # Light intensity should be maximized
            'RealValue': 132,  # Current real light intensity value
            'OptValue': 500,  # Desired optimal light intensity value
        }
    }

    # Instantiate the Energy class with the static preferences
    satisfaction = Energy(config)
    # Calculate the energy consumption gain based on the dynamic solution
    energy_satisfaction = satisfaction.GetEnergyConsumptionGain(solution)
    # Print the total energy consumption gain
    print(f"Energy Consumption Gain: {energy_satisfaction}")
"""