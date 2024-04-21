from flask import Flask 
from flask_cors import CORS

from . import db
from .routes import livro_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_prefixed_env()

    db.init_app(app)
    app.register_blueprint(livro_routes)

    app.debug = True

    return app