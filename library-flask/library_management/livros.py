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

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return render_template('table.html', data=rows)


@livro_routes.post('/api/adicionar_livro')
def add_livro():
    conn = None
    cursor = None
    try:
        dados_formulario = request.json
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        titulo = dados_formulario['titulo']
        autor = dados_formulario['autor']
        genero = dados_formulario['genero']
        cursor.execute(
            "INSERT INTO livros (titulo,autor,genero) VALUES (%s, %s, %s)",
            (titulo, autor, genero)
        )
        conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print(f"Erro ao adicionar o livro: {e}")
        return jsonify(success=False, error=str(e)), 400  # Retorno de erro com status 400
    finally:
        if cursor is not None:
            cursor.close()


@livro_routes.get('/api/search_livro')
def search():
    conn = None
    cursor = None
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        # Captura o valor de 'nome_livro' do request.args
        nome_livro = request.args.get('nome_livro')

        # Verifica se 'nome_livro' está vazio ou None
        if not nome_livro:
            cursor.execute('SELECT * FROM livros')
        else:
            cursor.execute('SELECT * FROM livros WHERE titulo LIKE %s', ("%" + nome_livro + "%",))

        # Obtém os resultados da consulta
        livro = cursor.fetchall()

        # Depuração: imprime o resultado da consulta
        print(f"Resultado da pesquisa: {livro}")
        cursor.close()
        # Retorna os dados para o template
        return render_template('search.html', data=livro)

    except Exception as e:
        print(f"Erro ao buscar o livro: {e}")

    finally:
        if cursor:
            cursor.close()

@livro_routes.put('/api/update_livro/<int:id_livro>')
def update_livro(id_livro):
    conn = None
    cursor = None
    try:
        conn = get_db()
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
        return jsonify(success=True)
    except Exception as e:
        print(f"Erro ao atualizar o livro: {e}")
        return jsonify(success=False, error=str(e)), 400
    finally:
        cursor.close()

@livro_routes.delete('/api/delete_livro')
def delete():
    conn = None
    cursor = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        data = request.json
        id_deletado = data['id_deletado']
        cursor.execute('DELETE FROM livros WHERE id_livro = %s', (id_deletado,))
        conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print(f"Erro ao deletar o livro: {e}")
        return jsonify(success=False, error=str(e)), 400
    finally:
        cursor.close()

@livro_routes.get('/api/gerar_relatorio')
def gerar_relatorio():
    conn = None
    cursor = None
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM livros')
        livros = cursor.fetchall()
        return jsonify(livros)
    except Exception as e:
        print(f"Erro ao gerar o relatório: {e}")
        return jsonify(success=False, error=str(e)), 400
    finally:
        cursor.close()