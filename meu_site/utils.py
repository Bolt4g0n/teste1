import os
from cryptography.fernet import Fernet

# Requisito 3.6: Chave em variável de ambiente
ENCRYPTION_KEY = os.environ.get('APP_ENCRYPTION_KEY')

if not ENCRYPTION_KEY:
    # Para desenvolvimento, você pode gerar uma temporária, 
    # mas em produção DEVE vir do ambiente.
    raise ValueError("A variável APP_ENCRYPTION_KEY não foi configurada.")

cipher_suite = Fernet(ENCRYPTION_KEY.encode())

def criptografar_dado(texto):
    if not texto: return None
    return cipher_suite.encrypt(texto.encode('utf-8')).decode('utf-8')

def descriptografar_dado(dado_cripto):
    if not dado_cripto: return None
    return cipher_suite.decrypt(dado_cripto.encode('utf-8')).decode('utf-8')