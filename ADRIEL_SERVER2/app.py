import mysql.connector
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_USER'] = os.getenv('DB_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DB'] = "biblioteca"
app.config['JSON_AS_ASCII'] = False

conexao = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB'],
    port= os.getenv('DB_PORT'),
    ssl_disabled=True
)

# Mantenha a conexão aberta e reabra o cursor conforme necessário

@app.route('/')
def exibir():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    rows = cursor.fetchall()
    cursor.close()  # Feche o cursor após a execução da consulta
    return render_template('table.html', data=rows)

@app.route('/api/search', methods=['GET'])
def search():
    cursor = conexao.cursor()
    try:
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
        
    except mysql.connector.Error as err:
        print(f"Erro ao buscar o livro: {err}")
    cursor.close()

@app.route('/api/delete', methods=['DELETE'])
def delete():
    cursor = conexao.cursor()
    try:
        data = request.json
        id_deletado = data['id_deletado']
        cursor.execute('DELETE FROM livros WHERE id_livro = %s', (id_deletado,))
        
        
        return jsonify(success=True)
    except mysql.connector.Error as err:
        print(f"Erro ao deletar o livro: {err}")
        #return jsonify(success=False, error=str(err))
    conexao.commit()
    cursor.close()


@app.route('/api/update/<int:id_livro>', methods=['PUT'])
def update_livro(id_livro):
    cursor = conexao.cursor()
    app.logger.info(request.form)
    autor = request.form['autor']
    titulo = request.form['titulo']
    genero = request.form['genero']

    try:
        cursor.execute(
            "UPDATE livros SET autor = %s, titulo = %s, genero = %s WHERE id_livro = %s",
            (autor, titulo, genero, id_livro)
        )

        conexao.commit()
        cursor.close()
        return jsonify({'success': True, 'message': 'Livro atualizado com sucesso'})
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar o livro: {err}")
        return jsonify({'success': False, 'message': 'Erro ao atualizar o livro'})


@app.route('/api/adicionar_livro', methods=['POST'])
def adicionar_livro():
    cursor = conexao.cursor()
    if request.method != 'POST':
        return jsonify({'success': False, 'message': 'Método não permitido'}), 405

    try:
        titulo = request.json['titulo']
        autor = request.json['autor']
        genero = request.json['genero']

        cursor.execute("SELECT * FROM livros WHERE titulo = %s", (titulo,))
        livro_existente = cursor.fetchone()

        if livro_existente:
            return jsonify({'success': False, 'message': 'Livro já cadastrado'}), 409

        cursor.execute("INSERT INTO livros (titulo, autor, genero) VALUES (%s, %s, %s)", (titulo, autor, genero))
        conexao.commit()
        cursor.close()

        return jsonify({'success': True, 'message': 'Livro cadastrado com sucesso'}), 201
    
    except mysql.connector.Error as err:
        print(f"Erro ao adicionar o livro: {err}")
        return jsonify({'success': False, 'message': 'Erro interno do servidor'}), 500
    

@app.route('/api/gerar_relatorio', methods=['GET'])
def gerar_relatorio():
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    cursor.close()
    return jsonify(livros)

if __name__ == '__main__':
    app.run(debug=True)
