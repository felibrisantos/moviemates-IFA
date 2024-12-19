# MovieMates

MovieMates é uma aplicação web para reserva de ingressos de cinema. Os usuários podem visualizar filmes em cartaz, selecionar horários de exibição, reservar assentos e gerenciar suas reservas.

# Acesso ao Site

[MovieMates](https://moviemates1.vercel.app)

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/felibrisantos/moviemates-IFA.git
    cd moviemates
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações e colete os arquivos estáticos:
    ```sh
    python manage.py migrate
    python manage.py collectstatic --noinput
    ```

5. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

## Descrição dos Diretórios

- **accounts/**: Contém a lógica de autenticação e gerenciamento de usuários.
- **booking/**: Contém a lógica de reserva de ingressos.
- **movieticket/**: Configurações principais do projeto Django.
- **staff/**: Contém a lógica de administração e gerenciamento de filmes e exibições.
- **static/**: Arquivos estáticos como CSS, JavaScript e imagens.
- **staticfiles/**: Arquivos estáticos coletados.
- **templates/**: Templates HTML para renderização das páginas.

## Scripts

- **build_files.sh**: Script para instalação de dependências, execução de migrações e coleta de arquivos estáticos.

## Deploy

O projeto está configurado para deploy no Vercel. O arquivo `vercel.json` contém as configurações necessárias.
