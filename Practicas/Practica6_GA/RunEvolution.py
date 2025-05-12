import BinaryTournament, PointCrossover, Selection, InitialPopulation
from Practicas import ObjectiveFunction

def StartGenetic(populationSize, mutationChance, generationAttemps, parentNumber):
    populationVector = InitialPopulation.GetInitialPopulation(populationSize)
    scoresVector = []
    generation = 0
    score = -1
    lastScore = -2
    gensWOUpgrade = 0
    gensWOUpgradeLimit = 20
    OB = ObjectiveFunction.ObjectiveFunction()

    for generation in range(generationAttemps):
        print(generation)
        scoresVector = [OB.CalculateSatisfaction(e) for e in populationVector]
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
