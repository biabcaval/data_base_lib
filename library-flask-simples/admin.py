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


admin_routes = Blueprint('admin_routes', __name__,static_folder='static', template_folder='templates')
conn = get_db()


#@admin_routes.route('/exibir_tela_admin', methods=['POST'])

@admin_routes.route('/', methods=['POST'])
def exibir_tela_aluno():

    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM livros'
    matricula = session.get('matricula')
    cursor.execute(query, (matricula,))