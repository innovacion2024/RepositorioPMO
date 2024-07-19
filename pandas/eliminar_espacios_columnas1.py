import pandas as pd

# Leer el archivo de Excel
archivo_excel = 'Facturacion.xlsx'  # Reemplaza 'tu_archivo.xlsx' con el nombre de tu archivo
df = pd.read_excel(archivo_excel)

# Verificar nombres de columnas antes de la modificación (opcional)
print("Nombres de columnas antes:")
print(df.columns)

# Eliminar espacios en los nombres de las columnas
df.columns = df.columns.str.replace(' ', '')

# Verificar nombres de columnas después de la modificación (opcional)
print("Nombres de columnas después:")
print(df.columns)

# Guardar el archivo de Excel con los nuevos nombres de las columnas
df.to_excel('tu_archivo_sin_espacios.xlsx', index=False)  # Reemplaza 'tu_archivo_sin_espacios.xlsx' si quieres un nombre diferente