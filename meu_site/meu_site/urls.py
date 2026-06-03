from django.urls import path
from core import views

urlpatterns = [
    # Rota raiz (Home Page) protegida
    path('', views.home, name='home'),
    
    # Rota do formulário de autenticação
    path('login/', views.tela_login, name='tela_login'),
    
    # Rota para destruição de sessão
    path('logout/', views.fazer_logout, name='logout'),
]