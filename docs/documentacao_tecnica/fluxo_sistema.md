# Fluxo Geral do Sistema

## Fluxo de criptografia
1. Usuário envia texto
2. Sistema recebe requisição
3. Utilitário de criptografia processa os dados
4. Dados são criptografados com Fernet/AES
5. Resultado é exibido na interface

## Fluxo de autenticação
1. Usuário envia credenciais
2. Django aplica PBKDF2-SHA256
3. Sistema valida hash armazenado
4. Sessão segura é criada