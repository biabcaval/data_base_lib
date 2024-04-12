import mysql.connector
import conexao_mysql 

conexao = conexao_mysql.conexao()
cursor = conexao.cursor()

comando_tabela_emprestimos = '''
CREATE TABLE emprestimos (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    aluno VARCHAR(100) NOT NULL,
    id_livro INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE NOT NULL,
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro)  
);

'''

def criar_tabela_emprestimos():
    try:
        cursor.execute(comando_tabela_emprestimos)
        conexao.commit()
        print('Tabela emprestimos criada com sucesso!')
    except mysql.connector.Error as err:
        if err.errno == 1050:
            print('Tabela emprestimos já existe')
        else:
            print(f'Erro ao criar a tabela emprestimos: {err}')


criar_tabela_emprestimos()

cursor.close()
conexao.close()