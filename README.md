# TechTrack: Gestão de Carreira e Wiki Tech
O TechTrack é uma plataforma de Gestão de Conhecimento Pessoal (PKM) e Carreira, desenvolvida para o Projeto Integrador I (PI-1) da UNIVESP. O objetivo é centralizar a documentação técnica do estudante e gerenciar a evolução de suas candidaturas através de "Snapshots" de competências.

## Instalação e Setup Inicial
Siga estes passos para configurar o ambiente em sua máquina local:

### 1. Clonar o Repositório
Use os comandos abaixo (lembre-se de trocar "seu-usuario" pelo seu nome no GitHub):

`git clone https://github.com/seu-usuario/techtrack.git`
e depois
`cd techtrack`

### 2. Ambiente Virtual (Venv)
Crie o ambiente isolado para evitar conflitos de bibliotecas:

Windows: `python -m venv venv` e depois `.\venv\Scripts\activate`

Mac/Linux: `python3 -m venv venv` e depois `source venv/bin/activate`

### 3. Instalar Dependências
`pip install -r requirements.txt`

### 4. Banco de Dados e Servidor
Prepare o banco de dados inicial e suba o site:

`python manage.py migrate` e depois `python manage.py runserver`

Acesse em seu navegador: http://127.0.0.1:8000/
