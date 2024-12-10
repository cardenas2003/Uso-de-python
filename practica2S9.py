import pandas as pd
import numpy as np

# Crear el DataFrame con los datos proporcionados
data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'María', 'Luis', 'Carla'],
    'Edad': [28, None, 40, 45, 38, 34],
    'Salario': ['3000', '4000', '4500', 'cuatro mil', '5000', '4000'],
    'Cargo': ['Analista', 'Gerente', 'Desarrollador', 'Gerente', 'Analista', None],
    'Fecha Ingreso': ['2021-01-15', '2020/03/12', '2022-07-01', '2021/12/01', None, '2020-03-12']
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

# Paso 4: Verificar que no haya valores faltantes en la columna 'Cargo'
faltantes_cargo = df['Cargo'].isnull().sum()
print("\nValores faltantes en la columna 'Cargo':", faltantes_cargo)

# Resultado final
df_resultado = df[['Nombre', 'Edad', 'Salario', 'Salario Numerico', 'Cargo', 'Fecha Ingreso Estandarizada']]
print("\nDataFrame Final:\n", df_resultado)
