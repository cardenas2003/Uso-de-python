import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de ventas (Ventas en unidades por ciudad y producto)
data = {
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E', 'Producto F', 'Producto G', 'Producto H'],
    'Bogotá': [250, 180, 200, 150, 220, 210, 190, 210],
    'Cali': [200, 220, 170, 180, 230, 240, 210, 220],
    'Bucaramanga': [210, 190, 210, 160, 210, 220, 180, 200]
}

# Crear un DataFrame a partir de los datos
df = pd.DataFrame(data)

# Establecer un estilo atractivo para el gráfico
sns.set(style="whitegrid")

# Configurar el gráfico
plt.figure(figsize=(10, 6))

# Graficar los datos: un gráfico de barras con hue por ciudad
df_melted = df.melt(id_vars=["Producto"], value_vars=["Bogotá", "Cali", "Bucaramanga"],
                    var_name="Ciudad", value_name="Ventas")

# Crear el gráfico de barras
sns.barplot(data=df_melted, x="Producto", y="Ventas", hue="Ciudad", palette="muted")

# Mejorar la presentación
plt.title('Ventas de Productos en Tres Ciudades', fontsize=16)
plt.xlabel('Productos', fontsize=12)
plt.ylabel('Ventas (Unidades)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Ciudad')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
