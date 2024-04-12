import mysql.connector
from flask import Flask, render_template, jsonify, request
import logging

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'#'0.tcp.sa.ngrok.io' 
#app.config['MYSQL_PORT'] =  14107
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =  "senharoot!26" #'39*72p16lf'
app.config['MYSQL_DB'] = "banco_p1" #'biblioteca'
app.config['JSON_AS_ASCII'] = False

conexao = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB'],
    #port=app.config['MYSQL_PORT'],
    ssl_disabled=True
)

cursor = conexao.cursor(dictionary=True, buffered=True)


@app.route('/')


def exibir():
    
    # print("Conexão com o banco de dados realizada com sucesso!")
    cursor.execute("SELECT * FROM livros")
    rows = cursor.fetchall()
    
    return render_template('table.html', data=rows)
        
@app.route('/api/search', methods=['GET'])

def search():
    try:
        nome_livro = request.args.get('nome_livro')
        if nome_livro!="":
            cursor.execute(cursor.execute('SELECT * FROM livros WHERE titulo LIKE %s', ("%" + nome_livro + "%",)))
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

@app.route('/api/delete', methods=['DELETE'])


# TA FUNCIONANDO 

def delete():
    try:
        data = request.json
        id_deletado = data['id_deletado']
        cursor.execute('DELETE FROM livros WHERE id_livro = %s', (id_deletado,))
        conexao.commit()
        return jsonify(success=True)
    except mysql.connector.Error as err:
        print(f"Erro ao deletar o livro: {err}")
        return jsonify(success=False, error=str(err))

# TA FUNCIONANDO

@app.route('/api/update/<int:id_livro>', methods=['POST'])
def update_livro(id_livro):
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

        
        # Retornar uma resposta de sucesso
        return jsonify({'success': True, 'message': 'Livro atualizado com sucesso'})
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar o livro: {err}")
        # Retornar uma resposta de erro
        return jsonify({'success': False, 'message': 'Erro ao atualizar o livro'})


# TA FUNCIONANDO 
    
@app.route('/api/adicionar_livro', methods=['POST'])
def adicionar_livro():
    if request.method != 'POST':
        return jsonify({'success': False, 'message': 'Método não permitido'}), 405  # Método não permitido

    try:
        titulo = request.json['titulo']
        autor = request.json['autor']
        genero = request.json['genero']

        cursor.execute("SELECT * FROM livros WHERE titulo = %s", (titulo,))
        livro_existente = cursor.fetchone()

        if livro_existente:

            return jsonify({'success': False, 'message': 'Livro já cadastrado'}), 409  # Conflito

        cursor.execute("INSERT INTO livros (titulo, autor, genero) VALUES (%s, %s, %s)", (titulo, autor, genero))

        return jsonify({'success': True, 'message': 'Livro cadastrado com sucesso'}), 201  # Criado
    except mysql.connector.Error as err:
        print(f"Erro ao adicionar o livro: {err}")
        return jsonify({'success': False, 'message': 'Erro interno do servidor'}), 500  # Erro interno do servidor





        
@app.route('/api/gerar_relatorio', methods=['GET'])
def gerar_relatorio():
    cursor  =  conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    return jsonify(livros)

if __name__ == '__main__':
    app.run(debug=True)
