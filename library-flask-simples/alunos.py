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
    return render_template('tela_aluno.html')

@alunos_routes.route('/emprestimos', methods=['POST'])

def exibir_tela_emprest_aluno():
    return render_template('tela_aluno_emprest.html')