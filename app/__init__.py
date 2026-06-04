from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object or 'app.config.Config')

    db.init_app(app)
    Swagger(app)

    from app.blueprints import register_blueprints
    register_blueprints(app)  

    with app.app_context():
        db.create_all() 

    return app