from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def tela_login(request):
    # Se o usuário já estiver logado, manda ele direto para a home
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # O Django pega os dados digitados e tenta validar
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # Se a senha estiver certa, o login() cria a sessão criptografada
            user = form.get_user()
            login(request, user)
            return redirect('home') # Substitua 'home' pelo nome da sua tela principal
        else:
            # Se errar a senha (ou se o Axes bloquear), envia uma mensagem de erro
            messages.error(request, "Usuário ou senha inválidos. Verifique suas credenciais.")
    else:
        # Se for apenas um GET (usuário acessando a página), exibe o formulário vazio
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})