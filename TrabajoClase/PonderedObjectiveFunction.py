import SatisfactionClase as SatisfactionC
import EnergyConsumptionClase as EnergyC

if __name__ == '__main__':
    alpha = 0.2
    beta = 0.8

    # Static preferences: These values are not expected to change often
    config = {
        'temp': {
            'range': [18, 26],  # Preferred temperature range
            'weight': 0.25,  # Importance of temperature in the overall satisfaction
            'changeCost': 5,  # Cost of changing the temperature
        },
        'humidity': {
            'range': [40, 60],  # Preferred humidity range
            'weight': 0.25,  # Importance of humidity in the overall satisfaction
            'changeCost': 5,  # Cost of changing the humidity
        },
        'noise': {
            'range': [0, 60],  # Preferred noise level range
            'weight': 0.25,  # Importance of noise level in the overall satisfaction
            'changeCost': 5,  # Cost of changing the noise level
        },
        'light': {
            'range': [200, 500],  # Preferred light intensity range
            'weight': 0.25,  # Importance of light intensity in the overall satisfaction
            'changeCost': 5,  # Cost of changing the light intensity
        },
    }

    # Dynamic solution: These values are expected to change frequently
    solution = {
        'temp': {
            'IsMaximization': False,  # Temperature should be minimized
            'RealValue': 15,  # Current real temperature value
            'OptValue': 18,  # Desired optimal temperature value
        },
        'humidity': {
            'IsMaximization': False,  # Humidity should be minimized
            'RealValue': 70,  # Current real humidity value
            'OptValue': 40,  # Desired optimal humidity value
        },
        'noise': {
            'IsMaximization': False,  # Noise level should be minimized
            'RealValue': 82,  # Current real noise level value
            'OptValue': 0,  # Desired optimal noise level value
        },
        'light': {
            'IsMaximization': True,  # Light intensity should be maximized
            'RealValue': 132,  # Current real light intensity value
            'OptValue': 500,  # Desired optimal light intensity value
        }
    }

    satisfaction = SatisfactionC.Satisfaction(config)
    energy = EnergyC.Energy(config)

    satisfactionValue = satisfaction.GetUserSatisfaction(solution)
    print(f'Satisfaction: {satisfactionValue}')

    energyGain = energy.GetEnergyConsumptionGain(solution)
    print(f'Energy: {energyGain}')

    solutionScore = satisfactionValue * alpha + energyGain * beta

    print(f'Solution score: {solutionScore}')
