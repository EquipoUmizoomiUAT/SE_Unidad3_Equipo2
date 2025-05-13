import pandas as pd

# Función para filtrar una serie numérica usando el rango intercuartílico (IQR)
# y luego devolver la mediana de los valores que no son outliers
def filterIQR_Median(series):
    Q1 = series.quantile(0.25)  # Primer cuartil (25%)
    Q3 = series.quantile(0.75)  # Tercer cuartil (75%)
    IQR = Q3 - Q1               # Rango intercuartílico

    # Filtramos valores dentro de [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
    filter = (series >= (Q1 - 1.5 * IQR)) & (series <= (Q3 + 1.5 * IQR))
    return series[filter].median()  # Retornamos la mediana de los valores filtrados

# Función principal para procesar el CSV original y crear un resume por heurística y conjunto VA
def processCSV_IQR(input_csv='heuristicResults.csv', output_csv='heuristicSummary_IQR.csv'):
    # Leemos el archivo CSV generado previamente por el script original
    df = pd.read_csv(input_csv)

    # Lista donde se almacenará el resume final
    resume = []

    # Agrupamos por nombre de la heurística y por número de conjunto VA (VA_Set)
    grouped = df.groupby(['Heurística', 'VA_Set'])

    # Recorremos cada grupo
    for (heuristica, va_set), grupo in grouped:
        # Calculamos la mediana IQR de las 30 ejecuciones de satisfacción para este grupo
        satisfaccion_iqr = filterIQR_Median(grupo['Satisfacción'])

        # Obtenemos los valores VA y VO del primer registro del grupo
        # (se asume que no cambian entre las 30 ejecuciones del mismo VA_Set)
        va_temp = grupo['VA_Temp'].iloc[0]
        vo_temp = grupo['VO_Temp'].iloc[0]
        va_hum = grupo['VA_Hum'].iloc[0]
        vo_hum = grupo['VO_Hum'].iloc[0]
        va_noise = grupo['VA_Noise'].iloc[0]
        vo_noise = grupo['VO_Noise'].iloc[0]
        va_light = grupo['VA_Light'].iloc[0]
        vo_light = grupo['VO_Luz'].iloc[0]

        # Añadimos los datos procesados al resume
        resume.append([
            heuristica,
            va_temp, vo_temp,
            va_hum, vo_hum,
            va_noise, vo_noise,
            va_light, vo_light,
            satisfaccion_iqr
        ])

    # Definimos los nombres de las columnas del nuevo DataFrame resume
    columnas = [
        "Heurística",
        "VA_Temp", "VO_Temp",
        "VA_Hum", "VO_Hum",
        "VA_Noise", "VO_Noise",
        "VA_Light", "VO_Luz",
        "Satisfacción"
    ]

    # Creamos el DataFrame final con los resultados resumidos
    df_resumen = pd.DataFrame(resume, columns=columnas)

    # Guardamos el DataFrame como un nuevo archivo CSV
    df_resumen.to_csv(output_csv, index=False)

    # Mostramos el nombre del archivo guardado y el resume generado
    print("Archivo guardado como:", output_csv)
    print(df_resumen)

# Punto de entrada del script
if __name__ == "__main__":
    processCSV_IQR()
