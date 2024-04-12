
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from mysql.connector import connect, Error
#from ...config.app import app
#from tables import Results
from config.db_config import get_mysql_connection, app
from flask import flash, render_template, jsonify, request, redirect, send_from_directory
from flask import Blueprint



livro_routes = Blueprint('livro_routes', __name__,static_folder='static', template_folder='templates')



@livro_routes.route('/livros',methods=['GET'])
def exibir():
    conn = None
    cursor = None
    query = "SELECT * FROM livros"
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return render_template('table.html', data=rows)
    except Exception as e:
        print(f"Erro ao buscar o livro: {e}")
    finally:
        cursor.close()
        conn.close()

@livro_routes.route('/api/adicionar_livro', methods=['POST'])
def add_livro():
    conn = None
    cursor = None
    try:
        conn = get_mysql_connection()
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

@livro_routes.route('/api/search_livro', methods=['GET'])
def search():
    conn = None
    cursor = None
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        nome_livro = request.args.get('nome_livro')
        if nome_livro:
            cursor.execute('SELECT * FROM livros WHERE titulo LIKE %s', ("%" + nome_livro + "%",))
            livro = cursor.fetchall()
            if livro:
                return render_template('search.html', data=livro)
            else:
                return render_template('search.html', data=[])
        else:
            cursor.execute('SELECT * FROM livros')
            livro = cursor.fetchall()
            return render_template('search.html', data=livro)
    except Exception as e:
        print(f"Erro ao buscar o livro: {e}")
    finally:
        cursor.close()
        conn.close()

@livro_routes.route('/api/delete_livro', methods=['DELETE'])
def delete():
    conn = None
    cursor = None
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        data = request.json
        id_deletado = data['id_deletado']
        cursor.execute('DELETE FROM livros WHERE id_livro = %s', (id_deletado,))
        conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print(f"Erro ao deletar o livro: {e}")
    finally:
        cursor.close()
        conn.close()

@livro_routes.route('/api/update_livro/<int:id_livro>', methods=['PUT'])
def update_livro(id_livro):
    conn = None
    cursor = None
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        autor = request.form['autor']
        titulo = request.form['titulo']
        genero = request.form['genero']
        cursor.execute(
            "UPDATE livros SET autor = %s, titulo = %s, genero = %s WHERE id_livro = %s",
            (autor, titulo, genero, id_livro)
        )
        conn.commit()
        print("Livro atualizado com sucesso")
        return redirect('/livros')
    except Exception as e:
        print(f"Erro ao atualizar o livro: {e}")
    finally:
        cursor.close()
        conn.close()

app.register_blueprint(livro_routes,url_prefix='/livros')


if __name__ == '__main__':
    app.run(debug=True)