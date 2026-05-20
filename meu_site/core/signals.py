import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

# Chama o logger configurado no settings.py
logger = logging.getLogger('core.seguranca')

# Função auxiliar para pegar o IP de quem está acessando
def get_client_ip(request):
    if not request: return '0.0.0.0'
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')
    return request.META.get('REMOTE_ADDR', '0.0.0.0')

@receiver(user_logged_in)
def registrar_login_sucesso(sender, user, request, **kwargs):
    ip = get_client_ip(request)
    logger.info(f"LOGIN BEM-SUCEDIDO: Usuário '{user.username}' acessou o sistema.", extra={'ip': ip})

@receiver(user_login_failed)
def registrar_login_falha(sender, credentials, request, **kwargs):
    ip = get_client_ip(request)
    username = credentials.get('username', 'Desconhecido')
    logger.warning(f"FALHA DE LOGIN: Tentativa negada para o usuário '{username}'.", extra={'ip': ip})

@receiver(user_logged_out)
def registrar_logout(sender, user, request, **kwargs):
    ip = get_client_ip(request)
    username = user.username if user else 'Anônimo'
    logger.info(f"LOGOUT: Usuário '{username}' encerrou a sessão.", extra={'ip': ip})