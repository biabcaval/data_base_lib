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

auth_routes = Blueprint('auth_routes', __name__, static_folder='static', template_folder='templates')
conn = get_db()


def create_view_aluno(matricula):
    cursor = conn.cursor()
    query_ViewAlunos = 'CREATE VIEW aluno_{} AS SELECT * FROM alunos WHERE matricula = %s'.format(matricula)
    cursor.execute(query_ViewAlunos, (matricula,))

    query_ViewEmprestimos = 'CREATE VIEW emprestimos_{} AS SELECT * FROM emprestimos WHERE id_aluno = %s'.format(matricula)
    cursor.execute(query_ViewEmprestimos, (matricula,))

    conn.commit()
    cursor.close()

##mostrar a pagina de login
@auth_routes.get('/')
def exibir_login(): 
    return render_template('tela_login.html')

@auth_routes.route('/', methods=['POST'])
def login():
    matricula = request.form.get('matricula')
    senha = request.form.get('senha')
    type_user = request.form.get('type_user')

    if type_user == 'Adm':
        cursor = conn.cursor(dictionary=True)

        query = 'SELECT * FROM admin WHERE matricula = %s AND senha = %s'
        cursor.execute(query, (matricula, senha))
        admin = cursor.fetchone()

        if admin:
            session['matricula'] = matricula
            return redirect(url_for('admin_routes.exibir_tela_admin'))
    else:     
        # Verifica se os campos de matrícula e senha foram enviados
        if matricula and senha:
            cursor = conn.cursor(dictionary=True)

            query = 'SELECT * FROM alunos WHERE matricula = %s AND senha = %s'
            cursor.execute(query, (matricula, senha))
            aluno = cursor.fetchone()

            if aluno:
                session['matricula'] = matricula
                create_view_aluno(matricula)
                return redirect(url_for('alunos.exibir_tela_aluno'))

        else:
            flash('Matrícula ou senha inválidos')
            return render_template('tela_login.html')

@auth_routes.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_routes.exibir_login'))

"""
<a href="{{ url_for('auth_routes.logout') }}">Logout</a>
"""



