import pandas as pd

df = pd.read_excel(r'C:\Users\indira.tapiab\Desktop\RepositorioPMO\pandas\tu_archivo_sin_espacios.xlsx', engine='openpyxl')
json_data = df.to_json(orient='records')

with open(r'C:C:\Users\indira.tapiab\Desktop\RepositorioPMO\pandas\tu_archivo_sin_espacios.json', 'w') as json_file:
    json_file.write(json_data)
    
    
    