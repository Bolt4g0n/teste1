from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    # Rotas Principais
    path('', views.home, name='home'),
    path('login/', views.tela_login, name='tela_login'),
    path('logout/', views.fazer_logout, name='logout'),
    path('criar-usuario/', views.criar_usuario, name='criar_usuario'),

    # Rotas de Recuperação de Senha (Checklist Tópico 2)
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='password_reset'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), name='password_reset_complete'),
]