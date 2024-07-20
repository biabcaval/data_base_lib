import sys
import os

# Adicionar o caminho do diretório superior ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import get_db
from datetime import date, timedelta
import random

id_emprestimo = (random.randint(10000, 99999))
matricula = 202403031
id_livro = 20

values = (id_emprestimo,matricula,id_livro)

conn = get_db()
cursor = conn.cursor()
cursor.callproc('realizar_emprestimo',values)
conn.commit()
cursor.close()
print('Emprestimo realizado com sucesso!')
