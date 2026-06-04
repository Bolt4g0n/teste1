import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

# --- CONFIGURAÇÃO DE AUDITORIA (LOGS) ---
logger = logging.getLogger(__name__)
logging.basicConfig(filename='security.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


# --- VIEWS DE AUTENTICAÇÃO BÁSICA ---

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


def fazer_logout(request):
    logout(request)
    return redirect('tela_login')


# --- VIEWS RESTRITAS (DASHBOARD E GESTÃO) ---

@login_required(login_url='/login/')
def home(request):
    return render(request, 'core/home.html')


# --- VIEW LIVRE (CRIAÇÃO DE USUÁRIO) ---
# Tiramos o @login_required daqui de cima para permitir cadastro aberto!

def criar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Salva com hash PBKDF2 e Salt automaticamente
            messages.success(request, "Novo usuário criado com sucesso! Faça seu login.")
            return redirect('tela_login') # Agora redireciona para o login em vez da home
        else:
            messages.error(request, "Erro ao criar usuário. Verifique os dados.")
    else:
        form = UserCreationForm()

    return render(request, 'core/criar_usuario.html', {'form': form})


# --- VIEWS DE RECUPERAÇÃO DE SENHA (COM AUDITORIA) ---

class CustomPasswordResetView(PasswordResetView):
    template_name = 'core/password_reset_form.html'
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        logger.warning(f"AUDITORIA: Solicitação de recuperação de senha para o e-mail: {email}")
        return super().form_valid(form)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'core/password_reset_confirm.html'
    
    def form_valid(self, form):
        logger.warning("AUDITORIA: Recuperação de senha concluída com sucesso via Token.")
        return super().form_valid(form)