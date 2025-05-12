def Selection(populationVector, scoresVector, populationSize):
    # Combine score + solution pairs
    combined = list(zip(scoresVector, populationVector))

    # Sort by score, descending
    combined.sort(key=lambda x: x[0], reverse=True)

    # Keep the top-N based on score
    combined = combined[:populationSize]

    # Unzip back into two separate lists
    scoresVector, populationVector = zip(*combined)

    return list(populationVector), list(scoresVector)