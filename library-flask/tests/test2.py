import sys
import os

# Adicionar o caminho do diretório superior ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import get_db
from datetime import date, timedelta

# Obtém a conexão com o banco de dados
conn = get_db()

cursor = conn.cursor()
print('Cursor connected')

# Executar a primeira consulta para adicionar um livro
titulo = 'l1'
autor = 'a1'
genero = 'g1'
values = (titulo, autor, genero)

cursor.callproc("biblioteca.add_livro(%s,%s,%s,'p_mensagem')", values)

for result in cursor.stored_results():
    print(result.fetchall())
'''
cursor.execute("SELECT @p_mensagem as mensagem;")
resultado = cursor.fetchall()
mensagem = resultado if resultado else None
print("Mensagem da stored procedure:", mensagem)

conn.commit()
cursor.close()'''

# Agora você pode usar a variável mensagem conforme necessário
'''print("Mensagem após commit:", mensagem)'''