from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            return redirect('home')
        else:
            # Se errar a senha (ou se o Axes bloquear), envia uma mensagem de erro
            messages.error(request, "Usuário ou senha inválidos. Verifique suas credenciais.")
    else:
        # Se for apenas um GET (usuário acessando a página), exibe o formulário vazio
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


# O decorator garante que apenas usuários autenticados acessem esta View
@login_required(login_url='/login/')
def home(request):
    return render(request, 'core/home.html')


# Função que destrói a sessão do usuário e limpa os cookies de acesso
def fazer_logout(request):
    logout(request)
    return redirect('tela_login')