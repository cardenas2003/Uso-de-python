import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de ejemplo
data = {
    'Horas estudiadas': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'Puntuación en el examen': [50, 60, 65, 70, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 98],
    'Nivel de motivación': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Establecer un estilo atractivo para el gráfico
sns.set(style="whitegrid")

# Configurar el gráfico
plt.figure(figsize=(10, 6))

# Crear el gráfico de dispersión
scatter = plt.scatter(df['Horas estudiadas'], df['Puntuación en el examen'], 
                      s=df['Nivel de motivación']*10,  # Tamaño de los puntos proporcional al nivel de motivación
                      c=df['Nivel de motivación'],  # Color de los puntos según el nivel de motivación
                      cmap='viridis',  # Mapa de colores
                      alpha=0.7,  # Transparencia de los puntos
                      edgecolors='w',  # Color de los bordes de los puntos
                      linewidth=0.5)

# Mejorar la presentación
plt.title('Relación entre Horas Estudiadas y Puntuación en el Examen', fontsize=16)
plt.xlabel('Horas Estudiadas', fontsize=12)
plt.ylabel('Puntuación en el Examen', fontsize=12)

# Añadir barra de color para el nivel de motivación
plt.colorbar(scatter, label='Nivel de Motivación')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
