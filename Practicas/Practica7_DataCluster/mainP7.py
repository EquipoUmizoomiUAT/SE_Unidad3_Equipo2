import pandas as pd
from tqdm import tqdm
from Practicas.Practica2_LS import mainP2 as p2
from Practicas.Practica3_ILS import mainP3 as p3
from Practicas.Practica4_TS import mainP4 as p4
from Practicas.Practica5_SA import mainP5 as p5
from Practicas.Practica6_GA import mainP6 as p6


def RunHeuristic(vaVector, heuristicName, function, finalTable):
    for vaSet, vector in enumerate(tqdm(vaVector, desc=f"Procesando {heuristicName}...")):
        for execution in range(1, 31):
            VA_Temp, VA_Hum, VA_Noise, VA_Light = vector
            satisfaction, satisfactionS, satisfactionE, solution = function(vector)
            VO_Temp = solution['temp']['OptValue']
            VO_Hum = solution['humidity']['OptValue']
            VO_Noise = solution['noise']['OptValue']
            VO_Luz = solution['light']['OptValue']
            finalTable.append([
                vaSet, heuristicName, execution,
                VA_Temp, VO_Temp, VA_Hum, VO_Hum, VA_Noise, VO_Noise, VA_Light, VO_Luz,
                satisfaction, satisfactionS, satisfactionE
            ])


if __name__ == '__main__':
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')

    with open(file="../Practica1/output.csv", mode="r") as file:
        vaVector = []
        for line in file:
            line = line.strip()
            tempVector = line.split(',')
            newLine = []
            for e in tempVector:
                values = e.split('-')
                va = int(values[-1])
                newLine.append(va)
            vaVector.append(newLine)

    finalTable = []

    RunHeuristic(vaVector, "Busqueda Local", p2.runLS, finalTable)
    RunHeuristic(vaVector, "Busqueda Local Iterada", p3.runILS, finalTable)
    RunHeuristic(vaVector, "Busqueda Tabu", p4.runTS, finalTable)
    RunHeuristic(vaVector, "Recocido Simulado", p5.runSA, finalTable)
    RunHeuristic(vaVector, "Algoritmo Genético", p6.runGA, finalTable)

    columns = [
        "VA_Set", "Heurística", "Ejecución",
        "VA_Temp", "VO_Temp", "VA_Hum", "VO_Hum",
        "VA_Noise", "VO_Noise", "VA_Light", "VO_Luz",
        "Satisfacción", "Satisfacción_S", "Satisfacción_E"
    ]
    df = pd.DataFrame(finalTable, columns=columns)
    df.to_csv("heuristicResults.csv", index=False)
    print(df)
