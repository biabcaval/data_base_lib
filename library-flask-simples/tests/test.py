from db import get_db
from datetime import date, timedelta

# Estabeleça a conexão com o banco de dados
conn = get_db()

id_emprestimo = 1015
matricula = 202202015
id_livro = 11
data_emprestimo = date.today()
data_prevista_devolucao = data_emprestimo + timedelta(days=7)

'''cursor = conn.cursor(dictionary=True)
query = 'INSERT INTO emprestimos (id_emprestimo, id_aluno, id_livro, data_emprestimo,data_prevista_devolucao) VALUES (%s, %s, %s, %s,%s)'

try:
    cursor.execute(query, (id_emprestimo, matricula, id_livro, data_emprestimo,data_prevista_devolucao))
    conn.commit()
    print('Empréstimo realizado com sucesso!')
except Exception as e:
    print('Erro ao realizar o empréstimo: ' + str(e))
finally:
    cursor.close()
    conn.commit()
    conn.close()'''

'''# Crie o cursor dentro do contexto da conexão
with conn.cursor() as cursor:
    # Chame o stored procedure
    cursor.callproc('realizar_emprestimo', (id_emprestimo, matricula, id_livro, data_emprestimo),'')
    print('Empréstimo realizado com sucesso!')

# Faça commit das alterações no banco de dados
conn.commit()'''
cursor = conn.cursor()

cursor.callproc("biblioteca.realizar_emprestimo", (id_emprestimo, matricula, id_livro, data_emprestimo,""))

# Obter a mensagem retornada pelo procedimento armazenado
cursor.execute("SELECT @mensagem")
mensagem_saida = cursor.fetchone()[0]
print("Mensagem de saída:", mensagem_saida)
# Commitar as mudanças no banco de dados
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()