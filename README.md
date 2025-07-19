# Cyber Incident Log

Sistema simples para registrar e gerenciar incidentes de segurança da informação, desenvolvido em Python com banco de dados MySQL.

## Funcionalidades

- Inserir novos incidentes com tipo, data, IP de origem, status e descrição.  
- Listar todos os incidentes registrados.  
- Conexão assíncrona com banco MySQL usando aiomysql.  
- Interface de terminal interativa.

## Tecnologias utilizadas

- Python 3.8+  
- aiomysql  
- MySQL (XAMPP)  
- Git e GitHub para versionamento

## Como rodar o projeto

1. Clone o repositório:
   ```bash
    git clone https://github.com/jgafarias/cyber-incident-log.git

2. Instale as dependências:  
   ```bash
    pip install -r requirements.txt

3. Configure o banco de dados MySQL (XAMPP):  
- Abra o painel do XAMPP e inicie o serviço MySQL.  
- Acesse o phpMyAdmin (geralmente em http://localhost/phpmyadmin).  
- Crie um banco de dados novo (ex: `cybersec_db`).  
- Importe o arquivo `db.sql` do seu projeto para criar as tabelas necessárias.  
- Crie um arquivo .env na raiz do projeto com as variáveis:  
   ```python
    DB_HOST=localhost  
    DB_USER=seu_usuario  
    DB_PASSWORD=sua_senha  
    DB_NAME=nome_da_sua_db

4. Execute o programa:  
   ```python
    python main.py

## Estrutura do projeto

   ```bash
    app/  
    ├── db/                   # Configuração do banco de dados  
    ├── services/             # Lógica de negócios (inserir, listar, atualizar incidentes)  
    ├── tests/                # Testes para inserir dados no banco
    ├── utils/                # Utilitários, como exportação de dados e limpar o terminal  
    main.py                  # Arquivo principal para rodar o app  
    db.sql                   # Script para criar banco e tabelas  
    .gitignore               # Arquivos ignorados pelo git  
    README.md                # Este arquivo
```

## Contato

João Gabriel Araújo Farias  
GitHub: [github.com/jgafarias/](https://github.com/jgafarias/)  
LinkedIn: [linkedin.com/in/jgafarias/  ](https://www.linkedin.com/in/jgafarias/)
