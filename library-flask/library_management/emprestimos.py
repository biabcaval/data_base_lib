import random
import string

from flask import (
    abort,
    Blueprint, 
    redirect, 
    request, 
    render_template, 
    url_for,
    jsonify
)

from .db import get_db

emprestimo_routes = Blueprint('emprestimo_routes', __name__,static_folder='static', template_folder='templates')

@emprestimo_routes.get('/')
def exibir():
    conn = None
    cursor = None
    query = "SELECT * FROM emprestimos"

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return render_template('table.html', data=rows)



'''

fazer emprestimo
- verificar se o livro ta disponivel
- verificar se o aluno ja tem 2 livros emprestados
ou se ele tem 1 livro em atraso
-qnd eu pego um livro emprestado, na tabela livros o atributo 'disponivel' muda o valor para 0


ver emprestimos
devolver livro
-atualizar 'status' de emprestimo para 'em atraso'
e na tabela livros, mudar o valor de 'disponivel' para 1 para o livro q ta sendo devolvido


'''


@emprestimo_routes.post('/exibir_tela_emprest_aluno')
def exibir_tela_emprest_aluno():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    #usado para pegar com POST ao invés do GET e não deixar a informação visível na URL
    id_aluno = request.form.get('matricula')
    
    #consulta para obter os empréstimos do aluno
    query = "SELECT * FROM emprestimos WHERE id_aluno = ?"
    cursor.execute(query, (id_aluno,))
    emprestimos = cursor.fetchall()

    cursor.close()

    #renderize o template existente com os dados dos empréstimos
    return render_template('seu_template.html', emprestimos=emprestimos)



@emprestimo_routes.post('/devolver_livro')
def devolver_livro():
    #dados do empréstimo a ser devolvido
    id_emprestimo = request.form.get('id_emprestimo')

    #conexão com o banco
    conn = get_db()
    cursor = conn.cursor()

    #atualizar o status do empréstimo para 'devolvido'
    update_emprestimo_query = "UPDATE emprestimos SET status = 'devolvido', data_real_devolucao = %s WHERE id = %s"
    cursor.execute(update_emprestimo_query, (datetime.now().strftime('%Y-%m-%d'), id_emprestimo))
    conn.commit()

    #atualizar o status de disponibilidade do livro
    update_livro_query = "UPDATE livros SET disponivel = 1 WHERE id = (SELECT id_livro FROM emprestimos WHERE id = %s)"
    cursor.execute(update_livro_query, (id_emprestimo,))
    conn.commit()

    cursor.close()
    conn.close()

    #redirecionar o usuário para a página de empréstimos
    return redirect(url_for('emprestimo_routes.ver_emprestimos'))
