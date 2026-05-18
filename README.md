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

#  Funcionalidades Atuais

-  Criptografia Simétrica utilizando AES-128
-  Cifragem e decifragem de mensagens
-  Armazenamento seguro de chave utilizando `.env`
-  Interface web desenvolvida com Django
-  Estrutura modularizada do sistema
-  Organização de logs e segurança
-  Integração com banco de dados SQLite

---

#  Stack Tecnológica

| Tecnologia | Finalidade |
|---|---|
| Python 3 | Linguagem principal |
| Django | Framework web |
| Cryptography | Criptografia e segurança |
| SQLite3 | Banco de dados |
| Git/GitHub | Versionamento e colaboração |

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
TRABALHO/
├── docs/                    #  Documentação técnico-científica
│   └── README.md            #  Organização da documentação acadêmica
│
└── meu_site/
    ├── core/
    │   ├── templates/
    │   │   └── cripto_teste.html
    │   ├── models.py
    │   └── views.py
    │
    ├── meu_site/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── .env
    ├── .gitignore
    ├── db.sqlite3
    ├── manage.py
    ├── utils.py
    ├── venv/
    └── README.md
```

---

#  Equipe do Projeto

| Integrante | Responsabilidade |
|---|---|
| Vinicius Freitas | Autenticação, gestão de credenciais, auditoria e banco de dados |
| Gustavo Muzel | Recuperação de senha, criptografia e comunicação segura |
| Kaiky Sena Kroquevichy | Resumo científico, pôster científico e documentação técnico-científica |
| Carlos Eduardo | Arquitetura do projeto, front-end, endpoints e Scrum Master |

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
