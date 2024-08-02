import pandas as pd

df = pd.read_excel(r'C:\RepositorioPMO\pandas\tu_archivo_sin_espacios.xlsx', engine='openpyxl')
json_data = df.to_json(orient='records')

with open(r'C:C:\RepositorioPMO\pandas\tu_archivo_sin_espacios.json', 'w') as json_file:
    json_file.write(json_data)
    

    