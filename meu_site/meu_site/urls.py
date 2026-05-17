"""
URL configuration for meu_site project.
"""
from django.contrib import admin
from django.urls import path
from core import views  #  '.' para 'core' para apontar para a pasta certa!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testar/', views.testar_seguranca, name='testar_seguranca'),
]