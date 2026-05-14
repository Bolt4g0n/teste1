from django.http import HttpResponse
# Importa as funções do arquivo utils.py que criamos na raiz
from utils import criptografar_dado, descriptografar_dado 

def testar_seguranca(request):
    """
    Função de teste para validar a criptografia Fernet (AES).
    """
    texto_original = "Sua mensagem ultra secreta aqui"
    
    # Criptografando o dado
    dado_criptografado = criptografar_dado(texto_original)
    
    # Descriptografando para provar que funciona
    dado_revelado = descriptografar_dado(dado_criptografado)
    
    html = f"""
    <html>
        <body>
            <h2>Teste de Criptografia - Segurança da Informação</h2>
            <p><strong>Original:</strong> {texto_original}</p>
            <p><strong>Criptografado (Base64/AES):</strong> {dado_criptografado}</p>
            <hr>
            <p><strong>Descriptografado com sucesso:</strong> {dado_revelado}</p>
        </body>
    </html>
    """
    return HttpResponse(html)