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
| Python 3 | Linguagem principal | 3.14.3 |
| Django | Framework web | 6.0.5 |
| Cryptography | Criptografia e segurança | 48.0.0 |
| Git/GitHub | Versionamento e colaboração | 2.54.0 |

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
├── docs/                                       #  Documentação técnico-científica do projeto
│   ├── atas_reuniao/                           #  Atas e alinhamentos da equipe
│   │   └── ata_18_05_2026.md                   #  Registro inicial de organização
│   │
│   ├── documentacao_tecnica/                   #  Documentação técnica do sistema
│   │   └── README.md                           #  Informações técnicas
│   │
│   ├── imagens/                                #  Diagramas, prints e materiais visuais
│   │   └── README.md                           #  Organização das imagens
│   │
│   ├── poster_cientifico/                      #  Desenvolvimento do pôster científico
│   │   └── README.md                           #  Estrutura do pôster
│   │
│   ├── referencias/                            #  Referências bibliográficas
│   │   ├── README.md                           #  Organização das referências
│   │   └── referencias.md                      #  Referências utilizadas
│   │
│   ├── resumo_cientifico/                      #  Desenvolvimento do resumo científico
│   │   ├── README.md                           #  Estrutura do resumo
│   │   └── resumo.md                           #  Desenvolvimento do resumo científico
│   │
│   └── README.md                               #  Organização geral da documentação
│
├── meu_site/
│   ├── __pycache__/                            #  Arquivos compilados automaticamente
│   │
│   ├── core/                                   #  Aplicação principal do sistema
│   │   ├── templates/                          #  Templates HTML da aplicação
│   │   │   └── cripto_teste.html               #  Interface de testes da criptografia
│   │   │
│   │   ├── models.py                           #  Modelagem do banco de dados
│   │   └── views.py                            #  Controle das requisições
│   │
│   ├── meu_site/                               #  Configurações globais do Django
│   │   ├── __pycache__/                        #  Cache interno do Python
│   │   │
│   │   ├── __init__.py                         #  Inicialização do pacote Python
│   │   ├── asgi.py                             #  Configuração ASGI
│   │   ├── settings.py                         #  Configurações do sistema
│   │   ├── urls.py                             #  Rotas e endpoints da aplicação
│   │   └── wsgi.py                             #  Configuração WSGI
│   │
│   ├── .gitignore                              #  Arquivos ignorados pelo Git
│   ├── db.sqlite3                              #  Banco de dados SQLite local
│   ├── manage.py                               #  Gerenciador principal do Django
│   ├── utils.py                                #  Funções auxiliares de criptografia
│   └── README.md                               #  Documentação principal do sistema
```
```

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
