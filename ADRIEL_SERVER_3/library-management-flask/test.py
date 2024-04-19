import mysql.connector

def conexao():
    try:
        conexao = mysql.connector.connect(
            host='0.tcp.sa.ngrok.io',
            user='root',
            password='39*72p16lf',
            database='biblioteca',
            port=12185,
            ssl_disabled=True
        )
        return conexao
    except mysql.connector.Error as error:
        print(f'Erro ao conectar ao MySQL: {error}')
        return None

#Testando a conexão
conn = conexao()
if conn is not None:
    print('Conexão bem-sucedida!')
    conn.close()
else:
    print('Falha na conexão.')