# Arquitetura do Sistema

## Visão Geral

O projeto foi desenvolvido utilizando o framework Django seguindo o padrão arquitetural MVT (Model-View-Template), promovendo separação de responsabilidades e organização modular da aplicação.

---

## Estrutura da Aplicação

### core/
Responsável pela lógica principal do sistema, renderização das páginas e comunicação entre interface e processamento.

### templates/
Contém os arquivos HTML responsáveis pela interface visual da aplicação.

### views.py
Gerencia as requisições HTTP e integra a interface com as funções de criptografia.

### models.py
Responsável pela modelagem e integração com o banco de dados SQLite.

### utils.py
Implementa funções auxiliares de criptografia utilizando a biblioteca Cryptography/Fernet.

### settings.py
Centraliza as configurações globais do Django, incluindo segurança, banco de dados e middleware.

---

## Arquitetura de Segurança

O sistema aplica segurança em múltiplas camadas:

- Criptografia simétrica com Fernet (AES-128)
- Armazenamento seguro de segredos via `.env`
- Hash seguro de senhas com PBKDF2-SHA256
- Cookies protegidos
- Comunicação HTTPS/TLS
- Proteção CSRF integrada do Django

---

## Banco de Dados

O projeto utiliza SQLite durante o desenvolvimento, permitindo simplicidade de configuração e integração nativa com Django.

---

## Fluxo Geral do Sistema

1. Usuário acessa a interface web
2. Requisições são processadas pelas views
3. O sistema executa operações criptográficas
4. Os dados são tratados e retornados ao usuário
5. Logs e autenticações são gerenciados pelo Django