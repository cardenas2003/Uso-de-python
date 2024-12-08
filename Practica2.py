import numpy as np

# 1. Crear un array de números del 1 al 10 y calcular la suma, media y valor máximo
array_1_10 = np.arange(1, 11)
suma = np.sum(array_1_10)
media = np.mean(array_1_10)
maximo = np.max(array_1_10)

print("Array del 1 al 10:", array_1_10)
print("Suma:", suma)
print("Media:", media)
print("Valor máximo:", maximo)

# 2. Crear un array de 3x4 lleno de ceros y cambiar su forma a 2x6
array_ceros = np.zeros((3, 4))
array_ceros_reshape = array_ceros.reshape((2, 6))

print("\nArray original de ceros (3x4):")
print(array_ceros)
print("\nArray cambiado a forma 2x6:")
print(array_ceros_reshape)

# 3. Generar una matriz aleatoria de 3x3 y calcular su transpuesta
matriz_aleatoria = np.random.rand(3, 3)
transpuesta = matriz_aleatoria.T

print("\nMatriz aleatoria 3x3:")
print(matriz_aleatoria)
print("\nTranspuesta de la matriz:")
print(transpuesta)

# 4. Concatenar dos arrays de NumPy y mostrar el resultado
array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([6, 7, 8, 9, 10])
array_concatenado = np.concatenate((array_a, array_b))

print("\nArray concatenado:")
print(array_concatenado)
