📁 Trabalho/ (Sua pasta principal)
│
├── 📁 venv/                 -> Ambiente virtual (9 mil arquivos. NÃO mexa, NÃO envie pro GitHub)
├── 📄 requirements.txt      -> Lista de bibliotecas (Gere com: pip freeze > requirements.txt)
│
└── 📁 meu_site/             -> RAIZ DO PROJETO DJANGO (Onde você roda os comandos)
    │
    ├── 📄 .env              -> Guarda a chave AES (Segurança: não envie pro GitHub/Professor)
    ├── 📄 manage.py         -> O "motor" do Django. (Nunca editamos este arquivo)
    ├── 📄 utils.py          -> Nosso motor de criptografia Fernet/AES.
    ├── 📄 db.sqlite3        -> Banco de dados padrão (É gerado automaticamente).
    │
    ├── 📁 meu_site/         -> PASTA DE CONFIGURAÇÕES GERAIS
    │   ├── 📄 settings.py   -> Configurações (HTTPS, Banco de dados, Apps instalados)
    │   ├── 📄 urls.py       -> O "GPS" do site (As rotas /admin e /testar)
    │   ├── 📄 asgi.py       -> (Para servidor em produção, não mexe agora)
    │   └── 📄 wsgi.py       -> (Para servidor em produção, não mexe agora)
    │
    └── 📁 core/             -> SUA APLICAÇÃO (Onde a mágica acontece)
        ├── 📄 views.py      -> A inteligência (Pega o dado, chama o utils.py e manda pra tela)
        ├── 📄 models.py     -> Estrutura do Banco de Dados (Ex: Tabela de Usuários LGPD)
        │
        └── 📁 templates/    -> FRONT-END (Você precisa criar esta pasta!)
            └── 📄 index.html -> O visual do site (HTML com a tabela de dados)
