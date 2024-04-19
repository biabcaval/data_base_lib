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

livro_routes = Blueprint('livro_routes', __name__,static_folder='static', template_folder='templates')

@livro_routes.get('/')
def exibir():
    conn = None
    cursor = None
    query = "SELECT * FROM livros"
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        return render_template('table.html', data=rows)
    except Exception as e:
        print(f"Erro ao buscar o livro: {e}")
    finally:
        cursor.close()
        conn.close()

@livro_routes.post('/api/adicionar_livro')
def add_livro():
    conn = None
    cursor = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        autor = request.form['autor']
        titulo = request.form['titulo']
        genero = request.form['genero']
        cursor.execute(
            "INSERT INTO livros (autor, titulo, genero) VALUES (%s, %s, %s)",
            (autor, titulo, genero)
        )
        conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print(f"Erro ao adicionar o livro: {e}")
    finally:
        cursor.close()
        conn.close()

@livro_routes.context_processor
def get_room_types():
    room_types = []
    return dict(room_types=room_types)

@livro_routes.get("/")
def index():
    bookings = []
    return render_template("list.html", bookings=bookings)

@livro_routes.post("/create")
def create_post():
    reference_number = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=10)
    )
    return redirect(url_for("livro_routes.index"))

