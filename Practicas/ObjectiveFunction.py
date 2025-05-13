from idlelib.debugobj_r import remote_object_tree_item

from Practicas import ServiceSatisfaction as SatisfactionC
from Practicas import EnergySatisfacion as EnergyC
from Practicas import GlobalConfig as Config
import copy

class ObjectiveFunction:

    alpha = None
    beta = None
    config = None
    solution = None


    def __init__(self):
        self.alpha, self.beta = Config.GetSatisfactionWeights()
        self.config = Config.GetGlobalConfig()


    def CalculateSatisfaction(self, solution):
        self.solution = copy.deepcopy(solution)
        satisfaction = SatisfactionC.Satisfaction(self.config)
        energy = EnergyC.Energy(self.config)

        serviceSatisfaction = satisfaction.GetUserSatisfaction(self.solution)

        energySatisfaction = energy.GetEnergyConsumptionGain(self.solution)

        solutionScore = serviceSatisfaction * self.alpha + energySatisfaction * self.beta

        return solutionScore, serviceSatisfaction, energySatisfaction