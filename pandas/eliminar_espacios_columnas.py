import pandas as pd

# Paso 1: Leer el archivo de Excel
archivo_excel = 'INFOABIERTAS.xlsx'  # Reemplaza 'tu_archivo.xlsx' con el nombre de tu archivo
df = pd.read_excel(archivo_excel)

# Paso 2: Verificar nombres de columnas antes de la modificación (opcional)
print("Nombres de columnas antes:")
print(df.columns)

# Paso 3: Eliminar espacios en los nombres de las columnas
df.columns = df.columns.str.replace(' ', '')

# Paso 4: Verificar nombres de columnas después de la modificación (opcional)
print("Nombres de columnas después:")
print(df.columns)

# Paso 5: Renombrar la columna "columna S"
df = df.rename(columns={"Cumple/NoCumple": "CumpleNoCumple"})

# Paso 5: Renombrar la columna "columna AL"
df = df.rename(columns={"AltasTramites": "AltasTramites"})

# Paso 5: Renombrar la columna "columna AW"
df = df.rename(columns={"GESTIO/NOGESTIO": "GESTIONOGESTIO"})

# Paso 5: Renombrar la columna "columna BT"
df = df.rename(columns={"Silver/Bronce": "SilverBronce"})

# Paso 5: Renombrar la columna "columna BO"
df = df.rename(columns={"T.Facturación": "TFacturación"})

# Paso 5: Renombrar la columna "columna AP"
df = df.rename(columns={"DELTA+EQUIPOS": "DELTAEQUIPOS"})

# Paso 5: Renombrar la columna "columna AQ"
df = df.rename(columns={"DELTA+EQUIPOSLB": "DELTAEQUIPOSLB"})

# Paso 5: Renombrar la columna "columna bh"
df = df.rename(columns={"+/-": "MasoMenos"})

df = df.rename(columns={"Nombre_Mes": "NombreMes"})

# Paso 6: Guardar el archivo de Excel con los nuevos nombres de las columnas
df.to_excel('tu_archivo_sin_espacios.xlsx', index=False)  # Reemplaza 'tu_archivo_sin_espacios.xlsx' si quieres un nombre diferente
