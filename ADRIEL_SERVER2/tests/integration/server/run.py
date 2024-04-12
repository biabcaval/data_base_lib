from flask import Flask
from .app.routes.livro_routes import livro_routes
from .app.routes.emprestimo_routes import emprestimo_routes

app = Flask(__name__)

# Registrar os blueprints
app.register_blueprint(livro_routes)
app.register_blueprint(emprestimo_routes)

if __name__ == '__main__':
    app.run(debug=True)
