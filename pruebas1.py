import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Crear un DataFrame con nombres, profesión y países
data = {
    'Nombre': ['Ana', 'Luis', 'María', 'Pedro', 'Carla', 'Juan', 'Elena', 'Diego'],
    'Profesión': ['Ingeniero', 'Doctor', 'Arquitecto', 'Abogado', 'Diseñador', 'Profesor', 'Médico', 'Programador'],
    'País': ['España', 'México', 'Colombia', 'Argentina', 'Perú', 'Chile', 'Uruguay', 'Ecuador']
}
df_personas = pd.DataFrame(data)
print("DataFrame de personas:")
print(df_personas)

# 2. Cargar un archivo CSV y mostrar las primeras 5 filas
csv_file = 'Catalogo.csv'
try:
    df_csv = pd.read_csv(csv_file)
    print("\nPrimeras 5 filas del archivo CSV:")
    print(df_csv.head())
except FileNotFoundError:
    print("\nEl archivo CSV no se encontró.")

# 3. Generar un DataFrame con valores aleatorios y mostrar el resumen estadístico
df_random = pd.DataFrame(np.random.rand(100, 8), columns=[f'Columna_{i+1}' for i in range(8)])
print("\nResumen estadístico del DataFrame aleatorio:")
print(df_random.describe())

# 4. Generar un gráfico (opcional)
plt.figure(figsize=(10, 6))
df_random.mean().plot(kind='bar', color='skyblue')
plt.title('Media de cada columna del DataFrame aleatorio')
plt.xlabel('Columnas')
plt.ylabel('Media')
plt.show()
