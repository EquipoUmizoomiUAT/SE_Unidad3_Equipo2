from Practicas.Practica6_GA import RunEvolution
from Practicas import ObjectiveFunction

OB = ObjectiveFunction.ObjectiveFunction

def runGA(VA):
    populationSize = 500  # N Max 10k - Bigger get slower
    mutationChance = 0.75  # T Apparently more mutation is worse
    generationAttempts = 500  # G
    numberOfParents = populationSize // 2
    if numberOfParents % 2 == 1:
        numberOfParents += 1
    bestSolution = RunEvolution.StartGeneticP7(populationSize, mutationChance, generationAttempts, numberOfParents)
    return OB.CalculateSatisfaction(bestSolution), bestSolution

if __name__ == '__main__':
    populationSize = 1000  # N Max 10k - Bigger get slower
    mutationChance = 0.75  # T Apparently more mutation is worse
    generationAttempts = 500  # G
    numberOfParents = populationSize // 2
    if numberOfParents % 2 == 1:
        numberOfParents += 1
    bestSolution = RunEvolution.StartGenetic(populationSize, mutationChance, generationAttempts, numberOfParents)
    print("Best Solution:")
    print(bestSolution)