from django.contrib import admin
from django.urls import path
from core.views import tela_login # Importe a sua view aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', tela_login, name='login'), # Esta é a nova rota!
]