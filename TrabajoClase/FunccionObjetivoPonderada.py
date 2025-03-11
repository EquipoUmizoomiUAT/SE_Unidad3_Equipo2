class Satisfaction:
    preferences = None
    solution = None

    def __init__(self, preferences):
        self.preferences = preferences

    def SetSolution(self, solution):
        self.solution = solution

    def GetMinEnergyCost(self, service):
        pass

    def GetMaxEnergyCost(self, service):
        pass

    def GetMinSatisfaction(self, service):
        satisfaction = ((self.preferences[service][1] - self.solution[service]['Value']) /
                        (self.preferences[service][1] - self.preferences[service][0]))
        return round(satisfaction, 4)

    def GetMaxSatisfaction(self, service):
        satisfaction = 1 - ((self.preferences[service][1] - self.solution[service]['Value']) /
                            (self.preferences[service][1] - self.preferences[service][0]))
        return round(satisfaction, 4)

    def GetUserSatisfaction(self, solution):
        self.SetSolution(solution)
        satisfaction = [
            self.GetMinSatisfaction(service) if self.solution[service]['IsMaximization'] else
            self.GetMaxSatisfaction(service) for service in solution.keys()
        ]

        return satisfaction


if __name__ == "__main__":
    userPrefs = {
        'temp': [18, 26],
        'humidity': [40, 60],
        'noise': [0, 60],
        'light': [200, 500],
    }

    solutionTest = {
        'temp': {'IsMaximization': False, 'Value': 20},
        'humidity': {'IsMaximization': False, 'Value': 54},
        'noise': {'IsMaximization': False, 'Value': 34},
        'light': {'IsMaximization': True, 'Value': 395}
    }

    satisf = Satisfaction(userPrefs)
    userSatisf = satisf.GetUserSatisfaction(solutionTest)
    print(userSatisf)
