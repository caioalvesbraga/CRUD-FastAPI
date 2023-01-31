# QuadrinhosAPI com FastAPI

Este projeto tem o objetivo de aprofundar os meus conhecimentos no uso do framework python FastAPI. A aplicação consiste numa API onde é possível realizar operações
CRUD (Create, Read, Update e Delete) com a finalidade de fazer a organização dos quadrinhos que você possui e salvar em um banco de dados.

## ✔️ Técnicas e tecnologias utilizadas

As técnicas e tecnologias utilizadas pra isso são:

- Banco de dados SQLite3
- FastAPI
- Linguagem Python
- Orientação a Objetos e seus principais conceitos - como associações simples, classes e heranças.
- ORM (Mapeamento Objeto-Relacioanal)
- SQLAlchemy

## 📁 Acesso ao projeto

Você pode [acessar o código fonte do projeto inicial](https://github.com/caioalvesbraga/CRUD-FastAPI) ou [baixá-lo](https://github.com/caioalvesbraga/CRUD-FastAPI/archive/refs/heads/main.zip).

## 🛠️ Abrir e rodar o projeto

Após baixar o projeto, você pode deve criar uma máquina virtual e importar os packages necessários para rodar a aplicação: 
**"pip install fastapi uvicorn[standard] sqlalchemy"**

Logo depois, é só digitar o comando "uvicorn main:app --reload", e a aplicação estará pronta para ser testada através do Postman/Insomnia ou através da documentação Swagger gerada automaticamente com o framework FastAPI.
