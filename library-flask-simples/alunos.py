from db import get_db #importação da conexão
import random

from flask import (
    Flask,
    Blueprint,
    url_for,
    render_template, 
    request, 
    redirect, 
    flash,
    session)



alunos_routes = Blueprint('alunos_routes', __name__,static_folder='static', template_folder='templates')
conn = get_db()


@alunos_routes.route('/', methods=['POST'])
def exibir_tela_aluno():

    '''logica: toda vez q ele entrar na tela de aluno,
    ele vai checar se tem algum empréstimo em atraso para aplicar multa''' 
    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM alunos WHERE matricula = %s'
    matricula = session.get('matricula')
    cursor.execute(query, (matricula,))
    data = cursor.fetchone()

    cursor.callproc('apply_multa')

    conn.commit()
    cursor.close()
    return render_template('tela_aluno.html',data=data)

@alunos_routes.route('/emprestimos', methods=['POST'])
def exibir_tela_emprest_aluno():
    # cursor = conn.cursor(dictionary=True)
    # matricula = session.get('matricula')
    # query = 'SELECT * FROM emprestimos WHERE id_aluno = %s'
    # cursor.execute(query, (matricula,))
    # emprestimos = cursor.fetchall()
    # cursor.close()
    return render_template('tela_aluno_emprest.html')#data=emprestimos


@alunos_routes.route('/livros', methods=['POST'])
def exibir_tela_livros_aluno():
    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM livros'
    cursor.execute(query)
    livros = cursor.fetchall()
    cursor.close()
    return render_template('tela_aluno_livros.html',data=livros)


# aluno faz emprestimo na tabela de livros
@alunos_routes.route('/livros', methods=['POST'])
def fazer_emprestimo():
    cursor = conn.cursor(dictionary=True)
    id_emprestimo = random.randint(1000,9999)
    matricula = session.get('matricula')
    id_livro = request.form.get('id_livro')
    data_emprestimo = request.form.get('data_emprestimo')
    cursor.callproc('realizar_emprestimo', (id_emprestimo, matricula, id_livro, data_emprestimo))
    
    #se a data de emprestimo q eu colocar for antiga, já aplicamos a multa
    cursor.callproc('apply_multa')
    
    conn.commit()
    cursor.close()
    return redirect(url_for('alunos_routes.exibir_tela_livros_aluno'))




@alunos_routes.route('/livros', methods=['POST'])
def pesquisar_livro():
    cursor = conn.cursor(dictionary=True)
    livro = request.form.get('pesquisa')
    query = 'SELECT * FROM livros WHERE titulo LIKE %s'
    cursor.execute(query, ('%'+livro+'%',))
    livros = cursor.fetchall()
    cursor.close()
    return render_template('tela_aluno_search_livros.html', livros=livros)

@alunos_routes.route('/emprestimos', methods=['POST'])
def devolver_livro():
    cursor = conn.cursor(dictionary=True)
    id_emprestimo = request.form.get('id_emprestimo')
    cursor.callproc('devolver_livro', (id_emprestimo,))
    conn.commit()
    cursor.close()
    return redirect(url_for('alunos_routes.exibir_tela_emprest_aluno'))


@alunos_routes.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('auth_routes.exibir_login'))