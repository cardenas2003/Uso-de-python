import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de ejemplo
data = {
    'Puntuación': [50, 60, 65, 70, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 98, 99, 100, 102, 103, 105],
    'Nivel de motivación': ['Baja', 'Media', 'Media', 'Alta', 'Alta', 'Media', 'Media', 'Alta', 'Alta', 'Baja', 
                            'Alta', 'Alta', 'Media', 'Alta', 'Alta', 'Media', 'Alta', 'Media', 'Baja', 'Alta']
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Establecer un estilo atractivo para el gráfico
sns.set(style="whitegrid")

# Configurar el gráfico
plt.figure(figsize=(10, 6))

# Crear los histogramas separados por el nivel de motivación
sns.histplot(data=df, x="Puntuación", hue="Nivel de motivación", multiple="dodge", kde=False, bins=10, palette="Set2")

# Mejorar la presentación
plt.title('Distribución de las Puntuaciones según el Nivel de Motivación', fontsize=16)
plt.xlabel('Puntuación en el Examen', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
