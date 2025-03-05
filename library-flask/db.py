
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


#Conectando ao Banco de Dados
def get_db():
    db = mysql.connector.connect(
            host= os.getenv('DB_HOST'),
            user= os.getenv('DB_USER'),
            password= os.getenv('DB_PASSWORD'),
            database=  os.getenv('DB_NAME'),
            #port=18446,
            ssl_disabled=True)  
    
    if db.is_connected():
        print(f"Conectado ao banco de dados biblioteca")

    return db
