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

alunos_routes = Blueprint('aluno_routes', __name__,static_folder='static', template_folder='templates')

### PAGINA ALUNO

@alunos_routes.route('/exibir_tela_aluno', methods=['POST'])

def exibir_tela_aluno():
    return render_template('tela_aluno.html')

@alunos_routes.route('/exibir_tela_emprest_aluno', methods=['POST'])

def exibir_tela_emprest_aluno():
    return render_template('tela_aluno_emprest.html')
