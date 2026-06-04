def register_blueprints(app):
    from .figurinhas_handler import figurinha_blueprint
    app.register_blueprint(figurinha_blueprint)
