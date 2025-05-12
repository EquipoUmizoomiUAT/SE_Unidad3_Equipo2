import RunEvolution

if __name__ == '__main__':
    populationSize = 1000  # N Max 10k - Bigger get slower
    mutationChance = 0.75  # T Apparently more mutation is worse
    generationAttempts = 10000  # G
    numberOfParents = populationSize // 2
    if numberOfParents % 2 == 1:
        numberOfParents += 1
    bestSolution = RunEvolution.StartGenetic(populationSize, mutationChance, generationAttempts, numberOfParents)
    print("Best Solution:")
    print(bestSolution)