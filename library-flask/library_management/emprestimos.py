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
