# PyBlog

PyBlog é um pequeno blog desenvolvido em Python utilizando o framework Django. Este projeto foi criado para
estudar e praticar o desenvolvimento web com Django.

## Tecnologias Utilizadas

- Python 3.12
- Django 5.0.7
- SQLite3 (banco de dados padrão do Django)

## Recomendações

- Python 3.12
- Pip (gerenciador de pacotes do Python)
- Venv (modulo para ambientes virtuais do Python)
- Python-dotenv (uso de variáveis de ambiente)

## Instalação

1. Clone o repositório:
    ```bash
    git clone git@github.com:Gustavo-Gadelha/PyBlog.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd PyBlog
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - Windows:
        ```bash
        venv\Scripts\activate
        ```
    - Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
6. Crie o arquivo `.env` e adicione as variáveis de ambiente:
    ```plaintext
    SECRET_KEY=[your_secret_key]
    DEBUG=True
    ```
7. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
8. Crie um superusuário para acessar o admin do Django:
    ```bash
    python manage.py createsuperuser
    ```
9. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Uso

- Acesse o blog em `http://127.0.0.1:8000/`.
- Acesse o painel de administração em `http://127.0.0.1:8000/admin/`.

## Testes

Para rodar os testes, siga os passos abaixo:

1. Instale as dependências para testes:
    ```bash
    pip install -r tests/requirements.txt
    ```
2. Rode os testes com relatório de cobertura:
    ```bash
    pytest --cov=./ --cov-report html
    ```

3. Abra o arquivo `index.html`, no diretório `htmlcov`, no seu navegador para ver o relatório de cobertura.

## Contribuição

Sinta-se à vontade para contribuir com o projeto. Para isso, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma nova branch:
    ```bash
    git checkout -b minha-feature
    ```
3. Faça as alterações necessárias e commit:
    ```bash
    git commit -m 'Minha nova feature'
    ```
4. Envie para o repositório remoto:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
