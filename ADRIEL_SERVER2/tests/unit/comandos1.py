#import mysql.connector
import conexao_mysql 

conexao = conexao_mysql.conexao()
cursor = conexao.cursor()

if conexao is not None:
    print('Conexão bem-sucedida!')


comando_idx_titulo = '''ALTER TABLE livros ADD INDEX idx_titulo (titulo);
'''
comando_add_disponivel = '''ALTER TABLE livros ADD disponivel BOOLEAN DEFAULT TRUE;'''

# Definir todos os valores da coluna 'disponivel' como 1 (TRUE)
comando_definir_disponivel = '''UPDATE livros SET disponivel = 1;'''
ver_livros = '''SELECT * FROM livros;'''

consulta_colunas = '''SHOW COLUMNS FROM emprestimos;'''

def show_colunas():
    cursor.execute(consulta_colunas)
    colunas = [coluna[0] for coluna in cursor.fetchall()]
    return colunas

def executar_comando(comando):
    cursor.execute(comando)
    resultados = cursor.fetchall()
    return resultados

comando_drop_emprestimos = '''DROP TABLE emprestimos;'''
comando_mod_tit = "ALTER TABLE livros MODIFY COLUMN titulo VARCHAR(100) NOT NULL;"
comando_dropar_INDEX = "DROP INDEX idx_titulo ON livros;"

cursor.execute(comando_mod_tit)
cursor.execute(comando_dropar_INDEX)
#cursor.execute()
cursor.close()
conexao.close()