from flask import Flask
from flask_cors import CORS
from auth import auth_routes
from alunos import alunos_routes


app = Flask(__name__)
CORS(app)

app.secret_key = 'meucu'
app.register_blueprint(auth_routes, url_prefix='/')
app.register_blueprint(alunos_routes, url_prefix='/alunos')

if __name__=="__main__":
    app.run(debug=True)