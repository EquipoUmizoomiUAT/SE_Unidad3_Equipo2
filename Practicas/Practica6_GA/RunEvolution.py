from Practicas.Practica6_GA import BinaryTournament, PointCrossover, Selection, InitialPopulation
from Practicas import ObjectiveFunction
from tqdm import tqdm


def StartGenetic(populationSize, mutationChance, generationAttemps, parentNumber):
    populationVector = InitialPopulation.GetInitialPopulation(populationSize)
    scoresVector = []
    generation = 0
    score = -1
    lastScore = -2
    gensWOUpgrade = 0
    gensWOUpgradeLimit = 50
    OB = ObjectiveFunction.ObjectiveFunction()

    for generation in tqdm(range(generationAttemps), desc="Procesando Generaciones del Gentico..."):
        print(generation)
        scoresVector = [OB.CalculateSatisfaction(e)[0] for e in populationVector]
        parentsVector = BinaryTournament.SelectParents(populationVector, scoresVector, parentNumber)
        childrenVector, childrenScores = PointCrossover.PointCrossover(populationVector, mutationChance)
        populationVector.extend(childrenVector)
        scoresVector.extend(childrenScores)
        populationVector, scoresVector = Selection.Selection(populationVector, scoresVector, populationSize)
        score = max(scoresVector)
        if score == lastScore:
            gensWOUpgrade += 1
            if gensWOUpgrade >= gensWOUpgradeLimit:
                break
        else:
            gensWOUpgrade = 0
        lastScore = score

    bestIndex = scoresVector.index(score)
    return populationVector[bestIndex]


def StartGeneticP7(populationSize, mutationChance, generationAttemps, parentNumber, va):
    populationVector = InitialPopulation.GetInitialPopulationP7(populationSize ,va)
    scoresVector = []
    generation = 0
    score = -1
    lastScore = -2
    gensWOUpgrade = 0
    gensWOUpgradeLimit = 50
    OB = ObjectiveFunction.ObjectiveFunction()

    for generation in range(generationAttemps):
        scoresVector = [OB.CalculateSatisfaction(e)[0] for e in populationVector]
        parentsVector = BinaryTournament.SelectParents(populationVector, scoresVector, parentNumber)
        childrenVector, childrenScores = PointCrossover.PointCrossover(populationVector, mutationChance)
        populationVector.extend(childrenVector)
        scoresVector.extend(childrenScores)
        populationVector, scoresVector = Selection.Selection(populationVector, scoresVector, populationSize)
        score = max(scoresVector)
        if score == lastScore:
            gensWOUpgrade += 1
            if gensWOUpgrade >= gensWOUpgradeLimit:
                break
        else:
            gensWOUpgrade = 0
        lastScore = score

    bestIndex = scoresVector.index(score)
    return populationVector[bestIndex]
