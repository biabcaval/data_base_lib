from gerar_matricula import gerar_matricula 
import mysql.connector
import random
from dotenv import load_dotenv
import os
import sys
'''sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import get_db, close_db'''
#import string


load_dotenv()

# interessante para saber: criação de senha aleatória
#all_characters = string.ascii_letters + string.digits 
#password = ''.join(random.choices(all_characters, k=length))
#+ string.punctuation
conexao = mysql.connector.connect(
    host = os.getenv("FLASK_DB_HOST"),
    user = os.getenv("FLASK_DB_USER"),
    password = os.getenv("FLASK_DB_PASSWORD"),
    database = os.getenv("FLASK_DB_NAME"),
    port = os.getenv("FLASK_DB_PORT"),
    ssl_disabled=True

)


# Lista de tuplas com informações de nome, senha, email e telefone
dados_alunos = [
    ('João', 'joao123', 'joao@email.com', '123-456-7890'),
    ('Chuu', 'chuu456', 'chuu@email.com', '234-567-8901'),
    ('Kendall Roy', 'kendall789', 'kendall@email.com', '345-678-9012'),
    ('Finn', 'finn101112', 'finn@email.com', '456-789-0123'),
    ('Fiona Apple', 'fiona1234', 'fiona@email.com', '567-890-1234'),
    ('Bjork', 'bjork567', 'bjork@email.com', '678-901-2345'),
    ('Thom Yorke', 'thom12345', 'thom@email.com', '789-012-3456'),
    ('Isobel', 'isobel6789', 'isobel@email.com', '890-123-4567')
]



n = len(dados_alunos)

def alunos_no_bd(matricula, nome, email, senha, telefone):
    conn = conexao
    cursor = conn.cursor()
    query = "INSERT INTO alunos (matricula, nome, email, senha, telefone) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (matricula, nome, email, senha, telefone))
    conn.commit()
    cursor.close()


for i in range(n):
    nome = dados_alunos[i][0]
    ano = random.choice([2022,2023,2024])
    nivel = random.randint(1,3)
    matricula = gerar_matricula(ano,nivel)

    senha = dados_alunos[i][1]
    email = dados_alunos[i][2] 
    telefone = dados_alunos[i][3]
    alunos_no_bd(matricula, nome, email, senha, telefone)
    print(f"Aluno {nome} adicionado com sucesso!")



'''def drop_linhas():
    conn = conexao
    cursor = conn.cursor()
    query = "DELETE FROM alunos"
    cursor.execute(query)
    conn.commit()
    cursor.close()'''


conexao.close()
'''length = int(input("Length of password: "))
password = ''.join(random.choices(all_characters, k=length))
print(password)'''