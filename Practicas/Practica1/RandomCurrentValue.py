import random

ranges = {
    'temp': [18, 36],
    'humidity': [40, 100],
    'noise': [0, 65],
    'light': [0, 10000]
}

if __name__ == '__main__':
    lines = []
    for i in range(100):
        outputInfo = []
        for service in ranges:
            randomVA = random.randint(ranges[service][0], ranges[service][1])
            newString = f'{service}-{randomVA}'
            outputInfo.append(newString)
        lines.append(','.join(outputInfo))

    with open(file='output.csv', mode='w') as file:
        file.write('\n'.join(lines))