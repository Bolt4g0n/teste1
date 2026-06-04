# Requisitos de Segurança

## Visão Geral

O sistema foi desenvolvido aplicando princípios fundamentais de Segurança da Informação, garantindo confidencialidade, integridade e proteção dos dados processados pela aplicação.

---

# 1. Criptografia de Dados

O sistema utiliza criptografia simétrica baseada no algoritmo AES-128 através da biblioteca Fernet da framework Cryptography.

## Objetivos
- Garantir confidencialidade dos dados
- Impedir leitura não autorizada
- Proteger informações sensíveis

---

# 2. Proteção de Senhas

As senhas dos usuários são protegidas utilizando o algoritmo PBKDF2-SHA256 integrado ao Django.

## Características
- Hash seguro
- Salt aleatório por usuário
- Resistência a ataques de força bruta
- Compatibilidade com padrões OWASP

---

# 3. Comunicação Segura

A aplicação utiliza HTTPS/TLS para criptografia da comunicação entre cliente e servidor.

## Recursos aplicados
- TLS local em ambiente de desenvolvimento
- Cookies seguros
- Proteção CSRF
- HSTS habilitado para produção

---

# 4. Armazenamento Seguro de Segredos

As chaves sensíveis do sistema são armazenadas em variáveis de ambiente utilizando arquivo `.env`.

## Benefícios
- Evita exposição no GitHub
- Facilita separação de ambientes
- Segue padrão 12-Factor App

---

# 5. Segurança de Sessão

O sistema utiliza cookies protegidos para gerenciamento de sessão.

## Configurações aplicadas
- SESSION_COOKIE_SECURE
- CSRF_COOKIE_SECURE
- HttpOnly
- Proteção contra XSS

---

# 6. Recuperação de Senha

O sistema implementa recuperação segura de senha utilizando tokens assinados digitalmente via HMAC-SHA256.

## Características
- Token temporário
- Uso único
- Assinatura criptográfica
- Expiração automática

---

# 7. Proteção Contra Vulnerabilidades

O sistema adota proteções integradas do Django contra vulnerabilidades comuns.

## Proteções implementadas
- CSRF Protection
- XSS Protection
- Secure Cookies
- Validação de formulários
- Controle de sessão

---

# 8. Controle de Versionamento Seguro

O projeto utiliza Git/GitHub com exclusão de arquivos sensíveis através do `.gitignore`

## Arquivos protegidos
- `.env`
- arquivos temporários
- cache do Python
- ambiente virtual (`venv`)