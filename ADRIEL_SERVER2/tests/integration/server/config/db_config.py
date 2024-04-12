#from app import app
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os
from flask import Flask

app = Flask(__name__)

load_dotenv()

def get_mysql_connection():
    try:
        connection = connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None



