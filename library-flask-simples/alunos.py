from db import get_db #importação da conexão
import random
from datetime import date


from flask import (
    Flask,
    Blueprint,
    url_for,
    render_template, 
    request, 
    redirect, 
    flash,
    session,
    jsonify)



alunos_routes = Blueprint('alunos_routes', __name__,static_folder='static', template_folder='templates')
conn = get_db()


@alunos_routes.route('/', methods=['GET'])
def exibir_tela_aluno():
 
    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM alunos WHERE matricula = %s'
    matricula = session.get('matricula')
    cursor.execute(query, (matricula,))
    data = cursor.fetchone()
    print(data)
    cursor.close()
    return render_template('tela_aluno.html',data=data)


@alunos_routes.route('/livros', methods=['GET'])
def exibir_tela_livros_aluno():
    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM livros'
    cursor.execute(query)
    livros = cursor.fetchall()
    cursor.close()
    return render_template('tela_aluno_livros.html',data=livros)

@alunos_routes.route('/emprestimos', methods=['GET'])
def exibir_tela_emprest_aluno():
    cursor = conn.cursor(dictionary=True)
    matricula = session.get('matricula')
    query = 'SELECT * FROM emprestimos WHERE id_aluno = %s'
    cursor.execute(query, (matricula,))
    emprestimos = cursor.fetchall()
    cursor.close()
    return render_template('tela_aluno_emprest.html',data=emprestimos)

# aluno faz emprestimo na tabela de livros
@alunos_routes.route('/livros/fazer_emprestimo', methods=['POST','GET'])
def fazer_emprestimo():
    if request.method == 'POST':
        print('entrou na rota de emprestimo')
        
        id_emprestimo = random.randint(10000,99999)
        matricula = session.get('matricula')
        data = request.get_json()
        id_livro = data.get('id_livro')

        #values = (id_emprestimo,matricula,id_livro)

        if id_livro:
            id_livro = int(id_livro)  # Convertendo para inteiro
            print('id livro:', id_livro)
            with conn.cursor(dictionary=True) as cursor:
                cursor.callproc('realizar_emprestimo', (id_emprestimo,matricula,id_livro))
                conn.commit()
            mensagem = 'Emprestimo realizado com sucesso!'
            
        else:
            mensagem ='Selecione um livro para realizar o emprestimo'
        return jsonify({'mensagem': mensagem})
    #flash('mds')
    #return redirect(url_for('alunos_routes.exibir_tela_livros_aluno'))

@alunos_routes.route('/emprestimos/devolver_livro', methods=['POST'])
def devolver_livro():
    data = request.get_json()
    id_emprestimo = data.get('id_emprestimo')
    id_livro = data.get('id_livro')
    with conn.cursor(dictionary=True) as cursor:
        cursor.callproc('devolucao', (id_emprestimo,id_livro))
        conn.commit()
        mensagem = 'Devolução realizada com sucesso!'
        return jsonify({'mensagem': mensagem})
    
    #return redirect(url_for('alunos_routes.exibir_tela_emprest_aluno'))


@alunos_routes.route('/livros/pesquisar_livro', methods=['POST'])
def pesquisar_livro():
    cursor = None
    cursor = conn.cursor(dictionary=True)
    livro = request.form.get('pesquisa')
    query = 'SELECT * FROM livros WHERE titulo LIKE %s'
    cursor.execute(query, ('%'+livro+'%',))
    livros = cursor.fetchall()
    cursor.close()
    return render_template('tela_aluno_search_livros.html', livros=livros)



@alunos_routes.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('auth_routes.exibir_login'))


