from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instância do SQLAlchemy inicializada aqui (infraestrutura)
db = SQLAlchemy()

def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object or 'app.config.Config')

    # Inicializa o banco de dados
    db.init_app(app)

    # Cria as tabelas se não existirem
    with app.app_context():
        db.create_all()

    from app.blueprints import register_blueprints
    register_blueprints(app)

    return app
