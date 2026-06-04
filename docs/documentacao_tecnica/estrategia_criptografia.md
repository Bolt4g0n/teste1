# Estratégia de Criptografia e Justificativas Técnicas
**Projeto:** meu_site (Django)  
**Requisitos atendidos:** 3.7 e 3.8

---

## 1. Visão Geral da Estratégia

O projeto adota uma estratégia de segurança em camadas, aplicando criptografia em três frentes distintas:

1. **Senhas de usuários** — hash com PBKDF2-SHA256
2. **Comunicação** — HTTPS com TLS via certificado local (desenvolvimento)
3. **Chaves e segredos** — isolamento via variáveis de ambiente (.env)

---

## 2. Criptografia de Senhas (Requisito 1.1, 3.4, 3.5)

### Algoritmo utilizado: PBKDF2-SHA256

O Django utiliza por padrão o algoritmo **PBKDF2 com SHA-256** para armazenar senhas.

### Como funciona:
- A senha do usuário **nunca é armazenada em texto puro**
- O Django gera um **salt aleatório único** por usuário (requisito 1.3)
- O salt + senha são processados pelo PBKDF2-SHA256
- Somente o **hash resultante + salt** são salvos no banco (requisito 1.4)

### Formato armazenado no banco:
```
pbkdf2_sha256$<iterações>$<salt>$<hash>
```

### Justificativa técnica:
| Característica | Detalhe |
|---|---|
| Algoritmo | PBKDF2-SHA256 |
| Iterações padrão | 720.000 (Django 5.x) |
| Salt | Gerado aleatoriamente por usuário |
| Resistência a brute force | Alto custo computacional por design |
| Padrão reconhecido | NIST SP 800-132, OWASP recomendado |

O PBKDF2 foi escolhido por ser o algoritmo padrão e auditado do Django, amplamente aceito por organizações de segurança como NIST e OWASP. Ele é propositalmente lento, o que dificulta ataques de força bruta e dicionário.

---

## 3. Comunicação Segura — TLS/HTTPS (Requisitos 3.1, 3.2, 3.3)

### Estratégia adotada:

Em **desenvolvimento**, o servidor é executado com HTTPS local usando o `django-extensions` com `runserver_plus` e certificado autoassinado gerado pelo `pyOpenSSL`:

```bash
python manage.py runserver_plus --cert-file cert.crt
```

Isso gera os arquivos `cert.crt` e `cert.key`, ativando TLS localmente.

### Configurações no settings.py:
```python
SECURE_SSL_REDIRECT = False          # Desativado apenas em dev local
SESSION_COOKIE_SECURE = True         # Cookie de sessão só via HTTPS
CSRF_COOKIE_SECURE = True            # Cookie CSRF só via HTTPS
SECURE_HSTS_SECONDS = 0              # Ativar em produção: 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

### Justificativa técnica:
| Configuração | Motivo |
|---|---|
| `SESSION_COOKIE_SECURE` | Impede que cookies de sessão sejam transmitidos em HTTP puro, evitando roubo de sessão |
| `CSRF_COOKIE_SECURE` | Protege contra ataques CSRF em canais não criptografados |
| `SECURE_HSTS_*` | Instrui o navegador a sempre usar HTTPS, bloqueando downgrades |
| `SECURE_CONTENT_TYPE_NOSNIFF` | Evita que o navegador interprete arquivos com tipo MIME incorreto |

Em **produção**, `SECURE_SSL_REDIRECT = True` seria ativado para forçar HTTPS em todas as requisições.

---

## 4. Proteção de Chaves Criptográficas (Requisito 3.6)

### Estratégia adotada: variáveis de ambiente via `.env`

A `SECRET_KEY` do Django — usada para assinar sessões, tokens CSRF e tokens de recuperação de senha — **não está no código-fonte**. Ela é carregada a partir de um arquivo `.env` local:

```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
```

```bash
# .env (não enviado ao GitHub)
SECRET_KEY=django-insecure-...
```

### Justificativa técnica:
- O arquivo `.env` é listado no `.gitignore`, evitando exposição no repositório
- Cada ambiente (dev, staging, produção) pode ter sua própria chave
- Segue o padrão **12-Factor App** para configuração de aplicações
- Impede que a chave apareça em logs, histórico de commits ou ferramentas de CI/CD

---

## 5. Tokens de Recuperação de Senha (Requisitos 2.2, 2.3, 2.4, 2.5)

### Algoritmo utilizado: HMAC-SHA256

O Django gera tokens de recuperação de senha usando **HMAC-SHA256** baseado na `SECRET_KEY` do projeto.

### Como funciona:
1. Usuário solicita recuperação → Django gera token único
2. Token é assinado com HMAC-SHA256 usando a SECRET_KEY
3. Link enviado contém: `uid` (ID do usuário em base64) + `token`
4. Ao clicar no link, o Django valida a assinatura e a expiração
5. Após uso, o token é **automaticamente invalidado** (requisito 2.4)
6. Tokens expirados retornam tela de erro adequada (requisito 2.5)

### Configuração de expiração:
```python
PASSWORD_RESET_TIMEOUT = 259200  # 3 dias em segundos
```

### Justificativa técnica:
| Característica | Detalhe |
|---|---|
| Algoritmo | HMAC-SHA256 |
| Base | SECRET_KEY do projeto |
| Expiração | 3 dias (259.200 segundos) |
| Uso único | Invalidado automaticamente após uso |
| Resistência a falsificação | Impossível sem a SECRET_KEY |

---

## 6. Resumo das Escolhas Técnicas

| Componente | Algoritmo/Mecanismo | Justificativa |
|---|---|---|
| Senhas | PBKDF2-SHA256 | Padrão Django, NIST/OWASP aprovado, resistente a brute force |
| Salt de senha | Aleatório por usuário | Impede ataques de rainbow table |
| Tokens de reset | HMAC-SHA256 | Assinatura criptográfica, uso único, com expiração |
| Comunicação | TLS/HTTPS | Criptografia em trânsito, padrão da indústria |
| Chaves secretas | Variável de ambiente (.env) | Isolamento de segredos, padrão 12-Factor App |
| Cookies | Secure + HttpOnly | Protegidos contra interceptação e XSS |

---
