import sys
import os

from datetime import date, timedelta
import random

# Adicionar o caminho do diretório superior ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import get_db
# Obtém a conexão com o banco de dados
conn = get_db()

id_emprestimo = (random.randint(10000, 99999))
matricula = 202403031
id_livro = 21


args =(id_emprestimo,matricula,id_livro,0)
with conn.cursor() as cursor:
    result_args = cursor.callproc('realizar_emprestimo', args)
    conn.commit()
    msg = result_args[3]
    print(msg)