#!/bin/sh

# Inicializa o banco de dados
python3 todo_project/create_db.py

# Inicia a aplicação Flask
flask run --host=0.0.0.0 --reload