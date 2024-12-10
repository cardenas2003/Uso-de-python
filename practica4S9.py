from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# 1. Crear una cadena con datos sensibles (número de tarjeta)
numero_tarjeta = "1234-5678-9101-1121"

# 2. Generar una clave de encriptación de 256 bits
clave = os.urandom(32)  # 32 bytes = 256 bits
iv = os.urandom(16)  # Vector de inicialización (IV) de 16 bytes

# Función para encriptar datos
def encriptar_datos(datos, clave, iv):
    # Convertir los datos a bytes
    datos_bytes = datos.encode('utf-8')
    
    # Rellenar los datos para que sean múltiplos de 128 bits
    padder = padding.PKCS7(128).padder()
    datos_padded = padder.update(datos_bytes) + padder.finalize()
    
    # Crear el objeto Cipher con AES en modo CBC
    cipher = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    encriptador = cipher.encryptor()
    
    # Encriptar los datos
    datos_encriptados = encriptador.update(datos_padded) + encriptador.finalize()
    
    return datos_encriptados

# Función para desencriptar datos
def desencriptar_datos(datos_encriptados, clave, iv):
    # Crear el objeto Cipher con AES en modo CBC
    cipher = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    desencriptador = cipher.decryptor()
    
    # Desencriptar los datos
    datos_desencriptados = desencriptador.update(datos_encriptados) + desencriptador.finalize()
    
    # Eliminar el relleno
    unpadder = padding.PKCS7(128).unpadder()
    datos_desempaquetados = unpadder.update(datos_desencriptados) + unpadder.finalize()
    
    # Convertir a texto
    return datos_desempaquetados.decode('utf-8')

# 3. Encriptar el número de tarjeta
numero_tarjeta_encriptado = encriptar_datos(numero_tarjeta, clave, iv)
print(f"Datos encriptados: {numero_tarjeta_encriptado.hex()}")

# 4. Desencriptar los datos
numero_tarjeta_desencriptado = desencriptar_datos(numero_tarjeta_encriptado, clave, iv)
print(f"Datos desencriptados: {numero_tarjeta_desencriptado}")

