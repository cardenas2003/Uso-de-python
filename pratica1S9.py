import pandas as pd
import numpy as np

# Crear el DataFrame con los datos proporcionados
data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'María', 'Luis', 'Ana'],
    'Edad': [28, 34, None, 45, 38, 34],
    'Salario': ['3000', '4000', 'cinco mil', '4500', '4000', '5000'],
    'Fecha Ingreso': ['2021-01-15', '2020/03/12', '2022-07-01', '2021/12/01', '2021-05-20', '2020-03-12']
}

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Paso 1: Identificar y contar los valores faltantes en cada columna
valores_faltantes = df.isnull().sum()
print("Valores faltantes por columna:\n", valores_faltantes)

# Paso 2: Verificar el formato de la columna 'Salario' para asegurar que todos los valores sean numéricos
# Crear una función para verificar si un valor es numérico
def es_numerico(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Aplicar la validación a la columna 'Salario'
df['Salario Numerico'] = df['Salario'].apply(es_numerico)
print("\nValores no numéricos en la columna 'Salario':\n", df[df['Salario Numerico'] == False])

# Paso 3: Validar y estandarizar el formato de la columna 'Fecha Ingreso' a YYYY-MM-DD
# Intentar convertir las fechas al formato correcto
def estandarizar_fecha(fecha):
    try:
        return pd.to_datetime(fecha).strftime('%Y-%m-%d')
    except:
        return None

df['Fecha Ingreso Estandarizada'] = df['Fecha Ingreso'].apply(estandarizar_fecha)
print("\nFechas no válidas o estandarizadas:\n", df[['Fecha Ingreso', 'Fecha Ingreso Estandarizada']])

# Resultado final
df_resultado = df[['Nombre', 'Edad', 'Salario', 'Salario Numerico', 'Fecha Ingreso Estandarizada']]
print("\nDataFrame Final:\n", df_resultado)
