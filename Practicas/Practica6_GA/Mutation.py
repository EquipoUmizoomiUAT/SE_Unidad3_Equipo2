import random
from Practicas import GlobalConfig

config = GlobalConfig.GetGlobalConfig()

def Mutate(child, mutationChance):
    for service in child.keys():
        if random.random() < mutationChance:
            child[service]['OptValue'] = random.uniform(config[service]['range'][0], config[service]['range'][1])
    return child