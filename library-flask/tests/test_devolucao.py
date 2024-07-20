import sys
import os

# Adicionar o caminho do diretório superior ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import get_db
from datetime import date, timedelta

id_emprestimo = 56253
id_livro = 20

conn = get_db()
cursor = conn.cursor()
cursor.callproc('devolucao', (id_emprestimo, id_livro))
conn.commit()
cursor.close()
print('Devolução realizada com sucesso!')