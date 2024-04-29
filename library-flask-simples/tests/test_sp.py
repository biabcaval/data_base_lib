import sys
import os

from datetime import date, timedelta
import random

# Adicionar o caminho do diretório superior ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import get_db
# Obtém a conexão com o banco de dados
conn = get_db()

id_emprestimo = random.randint(1000, 9999)
id_livro = 54
matricula = 202202015
data_emprestimo = date.today()
data_prevista_devolucao = data_emprestimo + timedelta(days=7)

cursor = conn.cursor()

titulo = 'titulo'
autor = 'autor'
genero = 'genero'

cursor.callproc("biblioteca.add_livro", (titulo, autor, genero))
conn.commit()
cursor.close()
print('Livro adicionado com sucesso!')