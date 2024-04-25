import random
import string

from flask import (
    abort,
    Blueprint, 
    redirect, 
    request, 
    render_template, 
    url_for,
    jsonify,
    session
)

from .db import get_db

auth_routes = Blueprint('auth_routes', __name__,static_folder='static', template_folder='templates')

#if bibliotecario ou aluno (n sei direito como vai rolar)


## função para criar a view do aluno
def create_view_aluno(matricula):
    conn = get_db()

    cursor = conn.cursor()
    query_ViewAlunos = 'CREATE VIEW aluno_{} AS SELECT * FROM alunos WHERE matricula = %s'.format(matricula)
    cursor.execute(query_ViewAlunos, (matricula,))

    query_ViewEmprestimos = 'CREATE VIEW emprestimos_{} AS SELECT * FROM emprestimos WHERE id_aluno = %s'.format(matricula)
    cursor.execute(query_ViewEmprestimos, (matricula,))

    conn.commit()
    cursor.close()


##mostrar a pagina de login
@auth_routes.get('/login')
def exibir_login(): 
    return render_template('tela_login.html')


@auth_routes.route('/login', methods=['GET'])
def login():
    matricula = request.args.get('matricula')
    senha = request.args.get('senha')

    #verifica se os campos de matrícula e senha foram preenchidos
    if matricula and senha:  
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        query = 'SELECT * FROM alunos WHERE matricula = %s AND senha = %s'
        cursor.execute(query, (matricula, senha))
        aluno = cursor.fetchone()

        if aluno:
            session['matricula'] = matricula
            return redirect(url_for('livro_routes.exibir'))

    #se os campos de matrícula e senha não forem preenchidos 
    #ou se a autenticação falhar, renderize o formulário de login
    return render_template('tela_login.html')

@auth_routes.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_routes.login'))
