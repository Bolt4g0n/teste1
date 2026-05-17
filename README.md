## ✨ Resumo das Funcionalidades

* **Criptografia Simétrica (AES-128):** Utilização do algoritmo Fernet para cifrar (Plaintext para Base64) e decifrar dados com segurança de ponta a ponta na aplicação.

## 🛠️ Stack Tecnológica

* **Linguagem:** Python (3.14)
* **Framework Web:** Django (6.0.5)
* **Segurança e Criptografia:** Biblioteca `cryptography`
* **Banco de Dados:** 
* **Controle de Versão:** Git / GitHub

## 📁 Estrutura do Projeto

Abaixo está o mapa exato da arquitetura do projeto e a responsabilidade de cada diretório e arquivo:

```text
TRABALHO/
└── meu_site/
    ├── core/                   # 🧠 Aplicação Principal (Lógica de negócios e visualização)
    │   ├── __pycache__/        # ⚙️ Arquivos compilados em cache (Gerados automaticamente)
    │   ├── templates/          # 🎨 Diretório de Front-end
    │   │   └── cripto_teste.html # 📄 Interface visual onde o usuário vê a criptografia acontecer
    │   ├── models.py           # 📊 Definição das tabelas e estruturação do banco de dados
    │   └── views.py            # ⚙️ Camada de controle: processa requisições, chama o utils.py e envia ao HTML
    │
    ├── meu_site/               # 🛠️ Configurações Globais do Projeto Django
    │   ├── __pycache__/        # ⚙️ Arquivos compilados em cache (Gerados automaticamente)
    │   ├── __init__.py         # 📦 Arquivo em branco que sinaliza ao Python que isso é um pacote
    │   ├── asgi.py             # 🌐 Ponto de entrada para servidores web assíncronos
    │   ├── settings.py         # ⚙️ Coração do sistema: configurações de segurança, banco e apps instalados
    │   ├── urls.py             # 🗺️ "GPS" do site: mapeia links (ex: /testar/) para as suas views
    │   └── wsgi.py             # 🌐 Ponto de entrada para servidores web síncronos
    │
    ├── __pycache__/            # ⚙️ Arquivos compilados da raiz (Gerados automaticamente)
    ├── .env                    # 🔒 SEGURANÇA: Armazena a chave AES localmente (Nunca vai para o GitHub)
    ├── .gitignore              # 🛡️ Arquivo que instrui o Git a ignorar arquivos sensíveis (como o .env)
    ├── db.sqlite3              # 🗄️ Banco de dados local (desenvolvimento)
    ├── manage.py               # 🕹️ Ferramenta de linha de comando para interagir com o projeto
    ├── utils.py                # 🔐 Motor central de Criptografia Simétrica (Lógica independente)
    ├── venv/                   # 📦 Ambiente Virtual: guarda o Python e dependências de forma isolada
    └── README.md               # 📖 Documentação principal do projeto (este arquivo)