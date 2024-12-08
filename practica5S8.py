import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de ejemplo
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'SUV': [120, 130, 135, 140, 150, 160, 170, 180, 175, 185, 190, 200],
    'Sedan': [100, 90, 95, 110, 120, 130, 140, 145, 150, 160, 170, 180],
    'Hatchback': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Establecer un estilo atractivo para el gráfico
sns.set(style="whitegrid")

# Configurar el gráfico
plt.figure(figsize=(10, 6))

# Graficar las ventas de cada tipo de vehículo
plt.plot(df['Mes'], df['SUV'], label='SUV', marker='o', linestyle='-', color='b', linewidth=2)
plt.plot(df['Mes'], df['Sedan'], label='Sedan', marker='o', linestyle='-', color='g', linewidth=2)
plt.plot(df['Mes'], df['Hatchback'], label='Hatchback', marker='o', linestyle='-', color='r', linewidth=2)

# Mejorar la presentación
plt.title('Ventas Mensuales de Vehículos Durante el Año', fontsize=16)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ventas', fontsize=12)
plt.xticks(rotation=45)  # Rotar las etiquetas de los meses
plt.legend(title='Tipos de Vehículo')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
