#  Sistema de Criptografia Simétrica com Django

Projeto acadêmico desenvolvido para a disciplina de Segurança da Informação, com foco na implementação de criptografia simétrica utilizando AES-128 através da biblioteca Fernet em uma aplicação web desenvolvida com Django.

---

# Objetivo do Projeto

O projeto tem como objetivo demonstrar conceitos fundamentais de segurança da informação aplicados em aplicações web modernas, incluindo:

- Criptografia de dados
- Proteção de credenciais
- Comunicação segura
- Auditoria e logs
- Recuperação de senha
- Segurança em banco de dados
- Arquitetura segura de aplicações web

---

# Funcionalidades Atuais
Criptografia Simétrica (AES-128/Fernet): Motor independente para cifragem e decifragem de dados sensíveis em repouso.

Autenticação e Sessões Seguras: Sistema de login com validação de credenciais (PBKDF2 + Salt nativos), controle de rotas protegidas e invalidação completa de sessão durante o logout.

Proteção contra Força Bruta (Rate Limit): Implementação de bloqueio automático de IP via django-axes para mitigar ataques automatizados de dicionário após múltiplas tentativas falhas.

Auditoria e Logs de Segurança: Sistema assíncrono via Signals que registra silenciosamente eventos críticos (acessos bem-sucedidos, tentativas negadas e logouts), capturando o IP e o carimbo de tempo no arquivo isolado security.log.

Isolamento de Segredos (Padrão 12-Factor App): Armazenamento de chaves críticas (APP_ENCRYPTION_KEY e SECRET_KEY) exclusivamente em variáveis de ambiente (.env), garantindo que não sejam expostas no código-fonte.

Estrutura de Repositório Blindada: Arquivo .gitignore configurado para impedir o vazamento de logs de segurança, bancos de dados locais e variáveis de ambiente para a nuvem.

Arquitetura MVT Modularizada: Separação clara de responsabilidades com lógica de criptografia em utils.py, ouvintes de eventos em signals.py e controle de requisições web através do framework Django.

---

#  Stack Tecnológica

| Tecnologia | Versão |
|---|---|
| Python 3 | 3.14.3 |
| Django | 6.0.5 |
| Cryptography | 48.0.0 |
| Git/GitHub | 2.54.0 |


---

#  Segurança Implementada

O sistema utiliza criptografia simétrica baseada no algoritmo AES-128 por meio da biblioteca Fernet, garantindo:

- Confidencialidade dos dados
- Integridade das informações
- Segurança no armazenamento de chaves
- Proteção contra exposição de credenciais

A chave criptográfica é armazenada localmente utilizando variáveis de ambiente (`.env`), evitando exposição no repositório GitHub.

---

# Estrutura do Projeto

```bash
📦 TRABALHO (Raiz do Projeto)
├── 📂 docs/                     # Documentação acadêmica e de engenharia do projeto
│   ├── 📂 atas_reuniao/         # Registros dos encontros, decisões e progresso da equipe
│   ├── 📂 documentacao_tecnica/ # Arquitetura e justificativas de segurança (Criptografia, LGPD, etc.)
│   ├── 📂 imagens/              # Diagramas e capturas de tela do sistema em funcionamento
│   ├── 📂 poster_cientifico/    # Material visual de apoio para a apresentação final
│   ├── 📂 referencias/          # Base teórica, artigos e normas (OWASP, NIST) utilizados
│   ├── 📂 resumo_cientifico/    # Abstract e visão geral acadêmica do projeto
│   └── 📄 README.md             # Guia de leitura exclusivo da pasta de documentação
│
├── 📂 meu_site/                 # Diretório principal do sistema web (Backend em Django)
│   ├── 📂 core/                 # Aplicativo central (Regras de negócio e interfaces)
│   │   ├── 📂 templates/core/   # Telas do sistema (Front-end em HTML)
│   │   │   └── 📄 login.html    # Interface de autenticação de usuários
│   │   ├── 📄 apps.py           # Configuração do app e gatilho de inicialização dos logs
│   │   ├── 📄 models.py         # Estrutura e tabelas do banco de dados
│   │   ├── 📄 signals.py        # "Espiões" invisíveis que registram logins, falhas e logouts
│   │   └── 📄 views.py          # Controladores que validam acessos e direcionam as telas
│   │
│   ├── 📂 meu_site/             # Painel de Controle global do framework Django
│   │   ├── 📄 __init__.py       # Arquivo em branco que indica que a pasta é um módulo Python
│   │   ├── 📄 asgi.py           # Configuração para comunicação de servidores assíncronos
│   │   ├── 📄 settings.py       # Configurações globais (Segurança, Banco, Sessões e HTTPS)
│   │   ├── 📄 urls.py           # Mapa central de rotas e links do site (ex: /login, /home)
│   │   └── 📄 wsgi.py           # Tradutor padrão para colocar o site no ar em servidores de produção
│   │
│   ├── 📄 .env                  # Guarda chaves secretas. 
│   ├── 📄 .gitignore            # Filtro de segurança: bloqueia o envio de senhas e logs para a nuvem
│   ├── 🗄️ db.sqlite3            # Banco de dados local (armazena os hashes PBKDF2 dos usuários)
│   ├── ⚙️ manage.py             # Ferramenta principal de terminal para executar comandos no servidor
│   ├── 📄 security.log          # Registro de auditoria isolado (quem logou, IPs, falhas)
│   └── 📄 utils.py              # Serviço independente de criptografia (Motor de cifragem AES/Fernet)
│
├── 📂 venv/                     # Ambiente virtual (isla as bibliotecas do projeto do resto do computador)
└── 📄 README.md                 # Manual principal com instruções de instalação, execução e tecnologias
```
```
---


🚀 Guia Rápido de Execução (Windows)
 
Siga os passos abaixo no seu terminal (PowerShell ou CMD) para rodar o projeto localmente:
 
1. Ative o ambiente virtual
 
Na pasta raiz do projeto, ative o isolamento das bibliotecas para que o Python reconheça as dependências:
 
.\venv\Scripts\activate
 
2. Acesse a pasta da aplicação
Navegue para dentro do diretório principal onde está o arquivo de gerenciamento do Django:
 
cd meu_site
 
3. Ligue o servidor local
Inicie a aplicação com o comando padrão:
 
python manage.py runserver
 
4. Acesse o sistema
 
Com o servidor rodando, abra o seu navegador e acesse a rota da nossa tela de autenticação:
 
👉 http://127.0.0.1:8000/login/
 
(Nota: Para encerrar o servidor no terminal quando terminar de testar, basta pressionar Ctrl + C).


---

#  Futuras Implementações

- Sistema completo de autenticação
- Logs avançados de auditoria
- Criptografia aplicada ao banco de dados
- Melhorias visuais na interface
- Sistema de recuperação de senha
- Endpoints protegidos
- Controle de acesso por usuário

---

#  Disciplina

Segurança da Informação

Projeto desenvolvido para fins acadêmicos.

# Colaboradores

KAIKY SENA KROQUEVICHY - 11231102733 
CARLOS EDUARDO LOURANÇO PEREIRA - 11231102525 
GUSTAVO MUZEL DE CARVALHO - 11231102563 
VINICIUS FREITAS DE SANTANA - 11231103599 
