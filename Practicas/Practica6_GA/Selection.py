def Selection(populationVector, scoresVector, populationSize):
    combined = list(zip(scoresVector, populationVector))

    combined.sort()
    combined = combined[:populationSize]

    scoresVector, populationVector = zip(*combined)

    return list(populationVector), list(scoresVector)