📌 Descrição
Este é um sistema web desenvolvido com Django (Python) para gerenciar contatos. Ele permite que usuários cadastrem-se, façam login e adicionem contatos com nome, e-mail, telefone, descrição e uma imagem opcional.

O projeto foi criado como parte de um curso, reforçando habilidades em desenvolvimento backend, autenticação de usuários e manipulação de dados.

🔗 Demo online: https://luisotaviodias.pythonanywhere.com

🚀 Funcionalidades:

- Cadastro e login de usuários
- CRUD completo para contatos (criação, edição e exclusão)
- Upload de imagem opcional para contatos
- Interface intuitiva para gerenciamento de dados
- Proteção de dados dos usuários

🛠️ Tecnologias utilizadas:

- Django (framework backend)
- Python (linguagem de programação)
- SQLite/MySQL (banco de dados)
- HTML, CSS (interface básica)

⚙️ Como executar o projeto localmente
📌 Pré-requisitos:
- Python 3.8+ instalado
- Banco de dados SQLite ou MySQL configurado
- Virtualenv (opcional, mas recomendado)

📌 Passo a passo
1️⃣ Clone o repositório

```bash
git clone https://github.com/luis-otavio-ias/projeto-agenda.git
cd projeto-agenda
```

2️⃣ Crie um ambiente virtual e instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ Configure o banco de dados

No arquivo settings.py configure o banco de dados em DATABASES.

Se for usar SQLite, ele já estará configurado.

Se for usar MySQL:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "database_name",
        "USER": "seu_user",
        "PASSWORD": "sua_senha",	
        "HOST": "localhost", # Host padrão
        "PORT": "3306", # Porta padrão do MySQL
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

4️⃣ Aplique as migrações

```bash
python manage.py migrate
```

5️⃣ Crie um superusuário para acessar o painel administrativo

```
python manage.py createsuperuser
```

6️⃣ Inicie o servidor local

```
python manage.py runserver
```
Agora, acesse http://127.0.0.1:8000/ no navegador. 🚀

📝 Contribuição
Se quiser contribuir, fique à vontade para abrir issues ou enviar um pull request!

📄 Licença
Este projeto está sob a licença MIT.
