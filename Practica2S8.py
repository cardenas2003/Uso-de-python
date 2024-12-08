import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de ventas
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto'],
    'Papa (Cali)': [100, 150, 200, 250, 300, 400, 300, 150],
    'Cebolla (Bogotá)': [90, 120, 160, 200, 240, 100, 200, 150],
    'Tomate (Cartagena)': [80, 110, 150, 190, 230, 330, 350, 240]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Establecer un estilo atractivo para el gráfico
sns.set(style="whitegrid")

# Configurar el gráfico
plt.figure(figsize=(10, 6))

# Graficar los datos usando un gráfico de líneas
plt.plot(df['Mes'], df['Papa (Cali)'], label='Papa (Cali)', marker='o', linestyle='-', color='b', linewidth=2)
plt.plot(df['Mes'], df['Cebolla (Bogotá)'], label='Cebolla (Bogotá)', marker='o', linestyle='-', color='g', linewidth=2)
plt.plot(df['Mes'], df['Tomate (Cartagena)'], label='Tomate (Cartagena)', marker='o', linestyle='-', color='r', linewidth=2)

# Mejorar la presentación
plt.title('Evolución de las Ventas de Productos en 8 Meses', fontsize=16)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ventas (Unidades)', fontsize=12)
plt.xticks(rotation=45)  # Rotar las etiquetas de los meses
plt.legend(title='Productos')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
