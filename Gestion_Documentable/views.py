import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings  # Importa settings desde Django
import os  # Importa el módulo os para manipulación de archivos

BASE_DIR = settings.BASE_DIR  # Obtiene BASE_DIR desde las configuraciones de Django

def index(request):            
    return render(request, 'index.html')

@csrf_exempt
def upload_excel(request):
    if request.method == 'POST' and request.FILES.get('file'):
        excel_file = request.FILES['file']
        
        try:
            # Leer el archivo de Excel
            df = pd.read_excel(excel_file, engine='openpyxl')
            
            # Eliminar espacios en los nombres de las columnas
            df.columns = df.columns.str.replace(' ', '')
            
            # Convertir el DataFrame a JSON
            json_data = df.to_json(orient='records')
            
            # Guardar el JSON en un archivo temporal en el servidor
            temp_dir = os.path.join(BASE_DIR, 'temp')
            os.makedirs(temp_dir, exist_ok=True)
            temp_file = os.path.join(temp_dir, 'data.json')
            with open(temp_file, 'w') as f:
                f.write(json_data)
            
            # Preparar la respuesta para descargar el archivo JSON
            response = HttpResponse(open(temp_file, 'rb'), content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="data.json"'
            return response
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return render(request, 'index.html')
