import pandas as pd
import numpy as np

# Crear el DataFrame con los datos de productos y precios
data = {
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Precio': [150, -25, 100, None]
}

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Paso 1: Validar que todos los precios sean mayores o iguales a cero y no nulos
def validar_precio(precio):
    return precio is not None and precio >= 0

df['Precio Valido'] = df['Precio'].apply(validar_precio)

# Paso 2: Mostrar los productos con precios inválidos
productos_invalidos = df[df['Precio Valido'] == False]
print("\nProductos con precios inválidos:\n", productos_invalidos)

# Resultado final
df_resultado = df
print("\nDataFrame Final:\n", df_resultado)
