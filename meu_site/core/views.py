from django.shortcuts import render
from utils import criptografar_dado, descriptografar_dado 

def testar_seguranca(request):
    """
    Camada de Controle (View): Processa a lógica criptográfica
    e renderiza o resultado no Template correspondente.
    """
    texto_original = "Sua mensagem ultra secreta aqui"
    
    # 1. Executa o motor de criptografia AES
    dado_criptografado = criptografar_dado(texto_original)
    
    # 2. Executa a descriptografia para validação do fluxo
    dado_revelado = descriptografar_dado(dado_criptografado)
    
    # 3. Monta o dicionário de dados (Contexto) que o HTML vai precisar
    contexto = {
        'texto_original': texto_original,
        'dado_criptografado': dado_criptografado,
        'dado_revelado': dado_revelado
    }
    
    # 4. Envia os dados puramente limpos para o Front-end
    return render(request, 'cripto_teste.html', contexto)