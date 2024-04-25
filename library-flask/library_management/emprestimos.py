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