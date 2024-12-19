#!/bin/bash

# Verifique se o pip3 está instalado, se não, instale-o
if ! command -v pip3 &> /dev/null
then
    echo "pip3 não encontrado, instalando..."
    apt-get update && apt-get install -y python3-pip
fi

# Instale as dependências do projeto
echo "Instalando dependências do projeto..."
pip3 install -r requirements.txt

# Execute as migrações e colete os arquivos estáticos
echo "Executando migrações e coletando arquivos estáticos..."
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput

echo "Build concluído com sucesso."
