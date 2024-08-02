from django.urls import path
from django.contrib import admin 
from .views import index, upload_excel

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('upload', upload_excel, name='upload_excel'),
]
