from flask import Flask 
from flask_cors import CORS

from . import db
from .livros import livro_routes
from .emprestimos import emprestimo_routes
from .auth import auth_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_prefixed_env()

    db.init_app(app)
    app.register_blueprint(livro_routes, url_prefix='/livros')
    app.register_blueprint(emprestimo_routes, url_prefix='/emprestimos')
    app.register_blueprint(auth_routes, url_prefix='/login')

    app.debug = True

    return app