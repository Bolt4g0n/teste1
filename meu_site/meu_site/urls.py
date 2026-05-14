"""
URL configuration for meu_site project.
"""
from django.contrib import admin
from django.urls import path
from . import views  # Importa o arquivo views.py que está na mesma pasta

urlpatterns = [
    # O painel administrativo padrão do Django
    path('admin/', admin.site.urls),
    
    #rota de teste para criptografia
    path('testar/', views.testar_seguranca, name='testar_seguranca'),
]