import numpy as np
import pandas as pd
from scipy import stats

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')

# Cargar el archivo con la satisfacción por heurística para cada instancia de VA
df = pd.read_csv("../Practica7_DataCluster/heuristicSummary_IQR.csv")

# Crear una ID única para cada combinación VA (opcional, puede usar índice también)
df['VA_ID'] = df[['VA_Temp', 'VA_Hum', 'VA_Noise', 'VA_Light']].astype(str).agg('-'.join, axis=1)

# Reorganizar el DataFrame para que las columnas sean las heurísticas y las filas las instancias VA
pivot_df = df.pivot(index='VA_ID', columns='Heurística', values='Satisfacción')

# Eliminar cualquier fila con valores faltantes (por si alguna heurística falló en alguna instancia)
pivot_df = pivot_df.dropna()

# Mostrar la tabla base
print("Datos pivot:")
print(pivot_df)

# Aplicar rankeo por fila (instancia de VA)
ranking = pivot_df.apply(stats.rankdata, axis=1)
print("\nColumnas Rankeadas (por fila):")
print(ranking)

# Calcular ranking promedio por heurística
ranking_promedio = ranking.mean()
print("\nRanking Promedio por Heurística:")
print(ranking_promedio)

# Aplicar prueba de Friedman
res = stats.friedmanchisquare(*[pivot_df[col] for col in pivot_df.columns])

print("\nResultado Prueba de Friedman:")
print(res)

#Ho = hipotesis nula...
# NO EXISTE DIFERENCIA ESTADISTICA ENTRE LAS MUESTRAS (GRUPOS)
#Ha = hipostesis alternativa
# EXISTE DIFERENCIA ESTADISTICA ENTRE LAS MUESTRAS (GRUPOS)

# Interpretar resultado
alpha = 0.05
if res.pvalue < alpha:
    print(f"\np-value = {res.pvalue:.4f} < {alpha} → Se rechaza H₀. Hay diferencia significativa entre heurísticas.")
else:
    print(f"\np-value = {res.pvalue:.4f} ≥ {alpha} → No se rechaza H₀. No hay diferencia significativa.")
