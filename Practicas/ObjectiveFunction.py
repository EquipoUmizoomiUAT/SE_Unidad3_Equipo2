import ServiceSatisfacion as SatisfactionC
import EnergySatisfacion as EnergyC
import GlobalConfig as Config
import copy

class ObjectiveFunction:

    alpha = None
    beta = None
    config = None
    solution = None


    def __init__(self):
        alpha, beta = Config.GetSatisfactionWeights()
        config = Config.GetGlobalConfig()


    def CalculateSatisfaction(self, solution):
        self.solution = copy.deepcopy(solution)
        satisfaction = SatisfactionC.Satisfaction(self.config)
        energy = EnergyC.Energy(self.config)

        satisfactionValue = satisfaction.GetUserSatisfaction(self.solution)
        print(f'Satisfacción Servicios: {satisfactionValue}')

        energyGain = energy.GetEnergyConsumptionGain(self.solution)
        print(f'Satisfacción Energia: {energyGain}')

        solutionScore = satisfactionValue * self.alpha + energyGain * self.beta

        print(f'Puntaje de la solucion: {solutionScore}')