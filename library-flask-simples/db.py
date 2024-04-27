
import mysql.connector


#Conectando ao Banco de Dados
def get_db():
    db = mysql.connector.connect(
            host='localhost',#'0.tcp.sa.ngrok.io',
            user='root',
            password= "senharoot!26",#'39*72p16lf', 
            database=  "banco_p1", #'biblioteca',
            #port=18446,
            ssl_disabled=True)  
    
    if db.is_connected():
        print(f"Conectado ao banco de dados biblioteca")

    return db

print(get_db())