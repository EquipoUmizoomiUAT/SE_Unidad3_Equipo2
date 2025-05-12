class Satisfaction:
    # Class attributes to store preferences and the current solution
    preferences = None  # Stores the preferred ranges, weights, and costs for each service
    solution = None  # Stores the current optimal values and optimization goals for each service

    def __init__(self, config):
        """
        Initializes the Satisfaction class with the given preferences.

        Args:
            config (dict): A dictionary containing the preferred ranges, weights,
                                and change costs for each service.
        """
        self.preferences = config

    def SetSolution(self, newSolution):
        """
        Updates the current solution with a new solution.

        Args:
            newSolution (dict): A dictionary containing the new optimal values and
                                 optimization goals for each service.
        """
        self.solution = newSolution

    def GetMinSatisfaction(self, service):
        """
        Calculates the satisfaction score for a service that should be minimized.

        Args:
            service (str): The name of the service (e.g., 'temp', 'humidity').

        Returns:
            float: The satisfaction score, normalized within the preferred range and
                   weighted by the service's importance.
        """
        # Extract the maximum and minimum values from the preferred range
        vMax = self.preferences[service]['range'][1]
        vMin = self.preferences[service]['range'][0]
        # Extract the current optimal value from the solution
        vO = self.solution[service]['OptValue']
        # Calculate the normalized satisfaction score
        serviceSatisfaction = (vMax - vO) / (vMax - vMin)
        # Apply the service's weight to the satisfaction score
        serviceSatisfaction = serviceSatisfaction * (self.preferences[service]['weight'])
        # Round the result to 4 decimal places for readability
        return round(serviceSatisfaction, 5)

    def GetMaxSatisfaction(self, service):
        """
        Calculates the satisfaction score for a service that should be maximized.

        Args:
            service (str): The name of the service (e.g., 'temp', 'humidity').

        Returns:
            float: The satisfaction score, normalized within the preferred range and
                   weighted by the service's importance.
        """
        # Extract the maximum and minimum values from the preferred range
        vMax = self.preferences[service]['range'][1]
        vMin = self.preferences[service]['range'][0]
        # Extract the current optimal value from the solution
        vO = self.solution[service]['OptValue']
        # Calculate the normalized satisfaction score
        serviceSatisfaction = (vMax - vO) / (vMax - vMin)
        # Invert the satisfaction score for maximization (1 - satisfaction)
        serviceSatisfaction = 1 - serviceSatisfaction
        # Apply the service's weight to the satisfaction score
        serviceSatisfaction = serviceSatisfaction * (self.preferences[service]['weight'])
        # Round the result to 4 decimal places for readability
        return round(serviceSatisfaction, 4)

    def GetUserSatisfaction(self, newSolution):
        """
        Calculates the overall user satisfaction based on the new solution.

        Args:
            newSolution (dict): A dictionary containing the new optimal values and
                               optimization goals for each service.

        Returns:
            float: The total satisfaction score, which is the sum of individual
                   satisfaction scores for all services.
        """
        # Update the current solution with the new solution
        self.SetSolution(newSolution)
        # Calculate satisfaction scores for all services
        newSatisfaction = [
            self.GetMaxSatisfaction(service) if self.solution[service]['IsMaximization'] else
            self.GetMinSatisfaction(service) for service in self.solution.keys()
        ]
        # Sum all individual satisfaction scores to get the total satisfaction
        newSatisfaction = sum(newSatisfaction)
        return newSatisfaction