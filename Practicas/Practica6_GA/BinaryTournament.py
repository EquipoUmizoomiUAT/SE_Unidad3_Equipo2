import random

def SelectParents(populationVector, scoresVector, parentNumbers):
    parents = []
    for i in range(parentNumbers):
        parent1 = random.randint(0, len(populationVector) - 1)
        parent2 = random.randint(0, len(populationVector) - 1)

        while parent1 == parent2:
            parent2 = random.randint(0, len(populationVector) - 1)

        if scoresVector[parent1] > scoresVector[parent2]:
            parents.append(populationVector[parent1])
        else:
            parents.append(populationVector[parent2])

    return parents

